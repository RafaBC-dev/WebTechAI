#!/usr/bin/env python3
"""
main.py — Orquestador principal del scraper de TechPulse ES
============================================================
Flujo de ejecución:
  1. Lee config.json (feeds, límites, score mínimo de relevancia)
  2. Carga slugs ya procesados para evitar duplicados
  3. Para cada feed RSS descarga las últimas entradas
  4. Filtra duplicados por slug
  5. Comprueba relevancia — descarta artículos off-topic (dinosaurios, deportes...)
  6. Hace scraping del artículo completo
  7. Llama a Groq/LLaMA para generar el resumen en español
  8. Guarda el Markdown en docs/content/<categoría>/
  9. Escribe el log de la ejecución en run_log.txt
"""

import sys
import re
import json
import time
import feedparser
import requests
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

from brain import summarize_with_groq
from utils import (clean_html, categorize_news, get_relevance_score,
                   generate_unique_slug, scrape_full_article, generate_slug)

try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass


# ── CONFIGURACIÓN ────────────────────────────────────────────────

def load_config() -> dict:
    """Lee config.json desde scraper/. Si no existe usa valores por defecto."""
    config_path = BASE_DIR / "scraper" / "config.json"
    if not config_path.exists():
        print("⚠️  config.json no encontrado. Usando valores por defecto.")
        return {
            "max_per_feed": 3,
            "max_per_run":  15,
            "min_relevance_score": 3,
            "feeds": ["https://hackaday.com/feed/"]
        }
    with open(config_path, encoding="utf-8") as f:
        return json.load(f)


CATEGORIES  = ["ia", "robotica", "linux", "embebidos", "diseño-3d"]
CONTENT_DIR = BASE_DIR / "docs" / "content"
LOG_FILE    = BASE_DIR / "run_log.txt"


# ── DIRECTORIOS ──────────────────────────────────────────────────

def ensure_directories():
    """Crea las carpetas de cada categoría si no existen."""
    for cat in CATEGORIES:
        (CONTENT_DIR / cat).mkdir(parents=True, exist_ok=True)


# ── DEDUPLICACIÓN ────────────────────────────────────────────────

def load_known_slugs() -> set:
    """
    Escanea docs/content/ y extrae los slugs de todos los .md existentes.
    Permite comprobar en O(1) si un artículo ya fue procesado.
    """
    slugs = set()
    for f in CONTENT_DIR.rglob("*.md"):
        slug = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', f.stem)
        slugs.add(slug)
    return slugs


# ── GUARDADO ─────────────────────────────────────────────────────

def save_news(category: str, result: dict, title_original: str,
              source_url: str, known_slugs: set) -> bool:
    """
    Guarda el resumen generado como archivo Markdown.
    Formato: docs/content/<categoría>/YYYY-MM-DD-<slug>.md
    Devuelve True si se guardó, False si no había contenido.
    """
    if not result.get("intro"):
        return False

    date_str   = datetime.now().strftime("%Y-%m-%d")
    title_es   = result.get("titulo", "").strip() or title_original
    slug       = generate_unique_slug(title_es, known_slugs)
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
    print(f"  ✅ [{category}] {filename}")
    print(f"     → {title_es[:70]}")
    return True


# ── PROCESADO DE FEEDS ───────────────────────────────────────────

def process_feed(feed_url: str, known_slugs: set, saved_titles: list,
                 max_per_feed: int, max_per_run: int,
                 min_score: int = 3) -> None:
    """
    Procesa un feed RSS completo:
      1. Descarga y parsea el feed
      2. Para cada entrada: deduplica → comprueba relevancia → scraping → IA → guarda
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

            if len(saved_titles) >= max_per_run:
                print(f"  ⏹ Límite diario ({max_per_run}) alcanzado.")
                return

            title_original = entry.get("title", "Sin título").strip()
            source_url     = entry.get("link", "")

            # ── Deduplicación por slug ──
            if generate_slug(title_original) in known_slugs:
                print(f"  ↩ Ya existe: {title_original[:65]}")
                continue

            # ── Contenido RSS como fallback ──
            rss_content = ""
            if hasattr(entry, 'content') and entry.content:
                rss_content = entry.content[0].get('value', '')
            else:
                rss_content = entry.get("description", "")
            rss_text = clean_html(rss_content)

            # ── Filtro de relevancia ANTES de gastar cuota de Groq ──
            # Comprobamos con el título y el texto RSS (más rápido que scrapear)
            score, category = get_relevance_score(title_original, rss_text)
            if score < min_score:
                print(f"  ⏭ Irrelevante (score={score}): {title_original[:65]}")
                continue

            # ── Scraping del artículo completo ──
            print(f"  🌐 Descargando artículo...")
            full_text      = scrape_full_article(source_url, fallback_text=rss_text)
            source_quality = "completo" if len(full_text) > len(rss_text) + 200 else "RSS"
            print(f"  📄 {len(full_text)} chars ({source_quality}) | score={score} | {category}")

            text_for_ai = f"Título: {title_original}\n\nContenido: {full_text[:2500]}"

            # ── Llamada a la IA ──
            print(f"  🤖 {title_original[:65]}...")
            result = summarize_with_groq(text_for_ai)

            if not result.get("intro"):
                print(f"  ✗ Sin contenido generado, omitiendo.")
                continue

            if save_news(category, result, title_original, source_url, known_slugs):
                saved_titles.append(title_original)
                nuevas += 1

        print(f"  → {nuevas} nuevas de este feed.")

    except Exception as e:
        print(f"  ✗ Error procesando feed: {e}")


# ── LOGGING ──────────────────────────────────────────────────────

def write_log(saved_titles: list, errors: list):
    """Añade una entrada al log acumulativo run_log.txt."""
    now  = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"\n[{now}] Nuevos: {len(saved_titles)}"
    for t in saved_titles:
        line += f"\n  + {t[:80]}"
    for e in errors:
        line += f"\n  ✗ {e}"
    line += "\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line)


# ── MAIN ─────────────────────────────────────────────────────────

def main():
    config       = load_config()
    feeds        = config.get("feeds", [])
    max_per_feed = config.get("max_per_feed", 3)
    max_per_run  = config.get("max_per_run", 15)
    min_score    = config.get("min_relevance_score", 3)

    print("🚀 TechPulse ES — Captura de noticias")
    print(f"   Feeds: {len(feeds)} | Máx/feed: {max_per_feed} | "
          f"Máx/ejecución: {max_per_run} | Score mínimo: {min_score}")
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
            process_feed(url, known_slugs, saved_titles,
                        max_per_feed, max_per_run, min_score)
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
