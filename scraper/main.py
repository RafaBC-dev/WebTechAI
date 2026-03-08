#!/usr/bin/env python3
"""
TechPulse ES — Captura y procesamiento de noticias tecnológicas.

Flujo:
  1. Lee config.json (feeds, límites, configuración del sitio)
  2. Para cada feed RSS, obtiene las últimas entradas
  3. Descarta duplicados comparando con los slugs ya indexados
  4. Intenta obtener el artículo completo haciendo scraping de la URL original
  5. Envía el contenido a Groq (LLaMA 3.1) para generar un resumen estructurado en español
  6. Guarda el resultado como archivo Markdown en web/content/<categoría>/
  7. Registra el resultado en run_log.txt
"""

import sys
import re
import json
import time
import feedparser
import requests
from datetime import datetime
from pathlib import Path

# Ajustar rutas relativas desde scraper/ hacia arriba y luego a web/
BASE_DIR = Path(__file__).resolve().parent.parent

from brain import summarize_with_gemini
from utils import clean_html, categorize_news, generate_unique_slug, scrape_full_article

try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass


# ── CONFIGURACIÓN ────────────────────────────────────────────────

def load_config() -> dict:
    config_path = BASE_DIR / "scraper" / "config.json"
    if not config_path.exists():
        print("⚠️  config.json no encontrado. Usando valores por defecto.")
        return {
            "max_per_feed": 3,
            "max_per_run":  15,
            "feeds": [
                "https://hackaday.com/feed/",
                "https://discourse.ros.org/latest.rss",
                "https://www.cnx-software.com/feed/"
            ]
        }
    with open(config_path, encoding="utf-8") as f:
        return json.load(f)


CATEGORIES  = ["ia", "robotica", "linux", "embebidos", "diseño-3d"]
CONTENT_DIR = BASE_DIR / "docs" / "content"
LOG_FILE    = BASE_DIR / "run_log.txt"


# ── DIRECTORIOS ──────────────────────────────────────────────────

def ensure_directories():
    for cat in CATEGORIES:
        (CONTENT_DIR / cat).mkdir(parents=True, exist_ok=True)


# ── DEDUPLICACIÓN ────────────────────────────────────────────────

def load_known_slugs() -> set:
    """
    Carga todos los slugs ya procesados escaneando content/.
    Se usa para evitar reprocesar artículos en ejecuciones sucesivas.
    """
    slugs = set()
    for f in CONTENT_DIR.rglob("*.md"):
        slug = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', f.stem)
        slugs.add(slug)
    return slugs


def is_known_url(url: str) -> bool:
    """
    Comprueba si una URL ya fue procesada buscándola en los archivos Markdown.
    Segunda capa de deduplicación (más lenta pero más fiable que solo el slug).
    """
    if not url:
        return False
    for md_file in CONTENT_DIR.rglob("*.md"):
        try:
            content = md_file.read_text(encoding="utf-8")
            if url in content:
                return True
        except Exception:
            pass
    return False


# ── GUARDADO ─────────────────────────────────────────────────────

def save_news(category: str, result: dict, title_original: str,
              source_url: str, known_slugs: set) -> bool:
    """
    Guarda una noticia procesada como archivo Markdown.

    Naming: content/<categoría>/YYYY-MM-DD-<slug>.md

    Returns:
        True si se guardó, False si era duplicado o no había contenido.
    """
    if not result.get("intro"):
        return False

    date_str = datetime.now().strftime("%Y-%m-%d")
    title_es = result.get("titulo", "").strip() or title_original

    # Slug único (con sufijo numérico si colisiona)
    slug = generate_unique_slug(title_es, known_slugs)

    tags_str   = ", ".join(result.get("tags", []))
    comando    = result.get("comando", "").strip()
    comando_md = f"\n\n```bash\n{comando}\n```" if comando else ""

    content = f"""# {title_es}

**Fecha:** {date_str}
**Categoría:** {category}
**Tags:** {tags_str}
**Título original:** {title_original}

---

## Introducción

{result.get('intro', '')}

## ¿Qué es?

{result.get('que_es', '')}

## ¿Cómo funciona?

{result.get('como_funciona', '')}

## ¿Por qué importa?

{result.get('por_que_importa', '')}

## Consejo técnico

{result.get('consejo', '')}{comando_md}

---

**Fuente original:** [{source_url}]({source_url})
"""

    filename  = f"{date_str}-{slug}.md"
    file_path = CONTENT_DIR / category / filename
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    known_slugs.add(slug)
    print(f"  ✅ {filename}")
    print(f"     → {title_es[:70]}")
    return True


# ── PROCESADO DE FEEDS ───────────────────────────────────────────

def process_feed(feed_url: str, known_slugs: set,
                 saved_titles: list, max_per_feed: int, max_per_run: int) -> None:
    """
    Descarga un feed RSS, filtra duplicados y procesa cada entrada nueva:
      1. Comprueba el slug del título original (rápido)
      2. Intenta scraping del artículo completo
      3. Llama a la IA para generar el resumen estructurado
      4. Guarda el Markdown
    """
    print(f"\n📡 {feed_url}")
    try:
        headers  = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(feed_url, headers=headers, timeout=30)
        response.raise_for_status()
        feed = feedparser.parse(response.text)

        if feed.bozo and not feed.entries:
            print(f"  ⚠️  Error de parseo: {feed.bozo_exception}")
            return

        nuevas = 0
        for entry in feed.entries[:max_per_feed]:

            # Límite global de la ejecución
            if len(saved_titles) >= max_per_run:
                print(f"  ⏹ Límite diario ({max_per_run}) alcanzado.")
                return

            title_original = entry.get("title", "Sin título").strip()
            source_url     = entry.get("link", "")

            # ── Deduplicación rápida por slug ──
            from utils import generate_slug
            if generate_slug(title_original) in known_slugs:
                print(f"  ↩ Ya existe: {title_original[:65]}")
                continue

            # ── Contenido del RSS como fallback ──
            rss_content = ""
            if hasattr(entry, 'content') and entry.content:
                rss_content = entry.content[0].get('value', '')
            else:
                rss_content = entry.get("description", "")
            rss_text = clean_html(rss_content)

            # ── Scraping del artículo completo ──
            print(f"  🌐 Descargando artículo completo...")
            full_text = scrape_full_article(source_url, fallback_text=rss_text)

            # Indicar si se obtuvo el artículo completo o solo el RSS
            source_quality = "completo" if len(full_text) > len(rss_text) + 200 else "RSS"
            print(f"  📄 Contenido: {len(full_text)} chars (fuente: {source_quality})")

            text_for_ai = f"Título: {title_original}\n\nContenido: {full_text[:2500]}"

            # ── Llamada a la IA ──
            print(f"  🤖 {title_original[:65]}...")
            result = summarize_with_gemini(text_for_ai)

            if not result.get("intro"):
                print(f"  ✗ Sin contenido generado, omitiendo.")
                continue

            category = categorize_news(title_original, full_text)
            if save_news(category, result, title_original, source_url, known_slugs):
                saved_titles.append(title_original)
                nuevas += 1

        print(f"  → {nuevas} nuevas de este feed.")

    except Exception as e:
        print(f"  ✗ Error procesando feed: {e}")


# ── LOGGING ──────────────────────────────────────────────────────

def write_log(saved_titles: list, errors: list):
    """
    Escribe un log de la ejecución en run_log.txt.
    Se acumula con ejecuciones anteriores (append).
    """
    now  = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"\n[{now}] Nuevos: {len(saved_titles)}"
    if saved_titles:
        for t in saved_titles:
            line += f"\n  + {t[:80]}"
    if errors:
        for e in errors:
            line += f"\n  ✗ {e}"
    line += "\n"

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line)


# ── MAIN ─────────────────────────────────────────────────────────

def main():
    config      = load_config()
    feeds       = config.get("feeds", [])
    max_per_feed = config.get("max_per_feed", 3)
    max_per_run  = config.get("max_per_run", 15)

    print("🚀 TechPulse ES — Captura de noticias")
    print(f"   Feeds: {len(feeds)} | Máx/feed: {max_per_feed} | Máx/ejecución: {max_per_run}")
    print("=" * 60)

    ensure_directories()

    known_slugs  = load_known_slugs()
    saved_titles = []
    errors       = []

    print(f"📂 {len(known_slugs)} artículos ya indexados\n")

    for url in feeds:
        if len(saved_titles) >= max_per_run:
            print("\n⏹ Límite diario alcanzado.")
            break
        try:
            process_feed(url, known_slugs, saved_titles, max_per_feed, max_per_run)
        except Exception as e:
            msg = f"Feed {url}: {e}"
            errors.append(msg)
            print(f"  ✗ {msg}")

    write_log(saved_titles, errors)

    print(f"\n{'='*60}")
    print(f"✅ Completado — {len(saved_titles)} artículos nuevos")
    if errors:
        print(f"⚠️  {len(errors)} errores (ver run_log.txt)")


if __name__ == "__main__":
    main()
