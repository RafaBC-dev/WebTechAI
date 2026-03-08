#!/usr/bin/env python3
"""
main.py — Orquestador principal de TechPulse ES
================================================
Este es el punto de entrada del scraper. Coordina todo el proceso
de captura y procesamiento de noticias tecnológicas desde feeds RSS.

Flujo completo de ejecución:
  1. Lee config.json (feeds a usar, límites por feed y por ejecución)
  2. Para cada feed RSS, obtiene las últimas N entradas
  3. Descarta duplicados comparando slugs con los archivos ya existentes
  4. Intenta obtener el artículo completo haciendo scraping de la URL original
  5. Envía el contenido a Groq (LLaMA 3.1) para generar un resumen en español
  6. Guarda el resultado como archivo Markdown en docs/content/<categoría>/
  7. Registra el resultado en run_log.txt para auditoría

Uso:
    cd scraper
    python main.py
"""

import sys
import re
import json
import time
import feedparser          # librería para parsear feeds RSS/Atom
import requests            # peticiones HTTP para descargar los feeds
from datetime import datetime
from pathlib import Path

# BASE_DIR apunta a la raíz del proyecto (un nivel arriba de scraper/)
BASE_DIR = Path(__file__).resolve().parent.parent

# Importamos las funciones de los módulos auxiliares del proyecto
from brain import summarize_with_groq
from utils import clean_html, categorize_news, generate_unique_slug, scrape_full_article

# Forzamos la codificación UTF-8 en stdout para que los emojis y tildes
# se muestren correctamente en Windows (donde el default puede ser cp1252)
try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass  # Python < 3.7 no tiene reconfigure(); ignoramos silenciosamente


# ── CONFIGURACIÓN ────────────────────────────────────────────────

def load_config() -> dict:
    """
    Carga la configuración del proyecto desde scraper/config.json.

    Por qué existe:
        Centralizar la configuración en un JSON externo permite
        modificar feeds, límites y parámetros del sitio sin tocar
        el código Python. También facilita despliegues automáticos
        (GitHub Actions) con diferentes configuraciones.

    Estructura esperada de config.json:
        {
          "max_per_feed": 3,        // máx artículos por feed por ejecución
          "max_per_run": 15,        // máx artículos totales por ejecución
          "site_url": "https://...", // URL base del sitio publicado
          "feeds": [                // lista de URLs de feeds RSS/Atom
            "https://hackaday.com/feed/",
            ...
          ]
        }

    Returns:
        Diccionario con la configuración. Si config.json no existe,
        devuelve valores por defecto para que el scraper funcione
        incluso sin archivo de configuración.
    """
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


# Categorías válidas del sitio. Deben coincidir con las de CATEGORY_KEYWORDS en utils.py
# y con las carpetas que espera el frontend en docs/content/.
CATEGORIES  = ["ia", "robotica", "linux", "embebidos", "diseño-3d"]

# Directorio donde se guardan los archivos Markdown de los artículos
CONTENT_DIR = BASE_DIR / "docs" / "content"

# Archivo de log acumulativo de todas las ejecuciones
LOG_FILE    = BASE_DIR / "run_log.txt"


# ── DIRECTORIOS ──────────────────────────────────────────────────

def ensure_directories():
    """
    Crea las carpetas de contenido si no existen.

    Por qué existe:
        En un repositorio limpio o en un CI/CD, las carpetas de content/
        pueden no existir todavía. Esta función las crea antes de intentar
        guardar cualquier archivo, evitando errores de "directorio no encontrado".

    Crea: docs/content/ia/, docs/content/robotica/, docs/content/linux/,
          docs/content/embebidos/, docs/content/diseño-3d/
    """
    for cat in CATEGORIES:
        (CONTENT_DIR / cat).mkdir(parents=True, exist_ok=True)


# ── DEDUPLICACIÓN ────────────────────────────────────────────────

def load_known_slugs() -> set:
    """
    Carga todos los slugs de artículos ya procesados escaneando docs/content/.

    Por qué existe:
        En cada ejecución del scraper debemos saber qué artículos ya fueron
        procesados para no volver a procesarlos (lo que desperdiciaría cuota
        de API y generaría duplicados en el sitio).

    Cómo funciona:
        Recorre recursivamente todos los archivos .md en docs/content/.
        El nombre de cada archivo tiene el formato: YYYY-MM-DD-<slug>.md
        Extrae el slug eliminando el prefijo de fecha con una expresión regular.

    Returns:
        Set de slugs ya existentes. Ejemplo: {"nueva-version-ubuntu", "ros2-nav2-released"}
    """
    slugs = set()
    for f in CONTENT_DIR.rglob("*.md"):
        # El patrón ^\d{4}-\d{2}-\d{2}- coincide con el prefijo de fecha (YYYY-MM-DD-)
        # re.sub() lo elimina y nos quedamos solo con el slug
        slug = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', f.stem)
        slugs.add(slug)
    return slugs


def is_known_url(url: str) -> bool:
    """
    Comprueba si una URL ya fue procesada buscándola en los archivos Markdown.

    Por qué existe:
        Es una segunda capa de deduplicación, más lenta pero más fiable.
        La deduplicación por slug puede fallar si dos artículos distintos
        generan el mismo slug. La URL de la fuente original es única,
        así que buscarla en el contenido de los .md es un método seguro.

    Cuándo se usa:
        Solo se invoca si la comprobación por slug no es suficiente.
        Es más lenta porque lee cada .md del disco.

    Args:
        url: URL del artículo que queremos verificar

    Returns:
        True si la URL ya aparece en algún .md existente, False si es nueva
    """
    if not url:
        return False
    for md_file in CONTENT_DIR.rglob("*.md"):
        try:
            content = md_file.read_text(encoding="utf-8")
            if url in content:
                return True
        except Exception:
            pass  # ignoramos archivos que no se puedan leer (permisos, encoding...)
    return False


# ── GUARDADO ─────────────────────────────────────────────────────

def save_news(category: str, result: dict, title_original: str,
              source_url: str, known_slugs: set) -> bool:
    """
    Guarda una noticia procesada como archivo Markdown en el directorio correcto.

    Por qué existe:
        Centraliza la lógica de escritura de archivos. Genera el nombre del
        archivo con fecha y slug, construye el contenido Markdown formateado
        y registra el slug para evitar duplicados en la misma ejecución.

    Formato del archivo generado:
        Ruta: docs/content/<categoría>/YYYY-MM-DD-<slug>.md
        Contenido: Markdown con frontmatter manual (campos en negrita)
                   y secciones H2 para cada parte del resumen.

    Args:
        category:       categoría asignada al artículo (ej: "linux")
        result:         diccionario devuelto por summarize_with_gemini()
        title_original: título del artículo en su idioma original
        source_url:     URL del artículo fuente para el enlace al final
        known_slugs:    set de slugs ya usados (se actualiza en esta función)

    Returns:
        True si el archivo se guardó correctamente.
        False si no había contenido útil (intro vacía) → artículo descartado.
    """
    # Si la IA no generó una introducción, el artículo no tiene contenido útil
    if not result.get("intro"):
        return False

    date_str = datetime.now().strftime("%Y-%m-%d")
    # Usamos el título en español generado por la IA; si no hay, usamos el original
    title_es = result.get("titulo", "").strip() or title_original

    # Generamos un slug único para este artículo, añadiendo sufijo si hay colisión
    slug = generate_unique_slug(title_es, known_slugs)

    # Preparamos el bloque de código bash si el artículo incluye un comando útil
    tags_str   = ", ".join(result.get("tags", []))
    comando    = result.get("comando", "").strip()
    comando_md = f"\n\n```bash\n{comando}\n```" if comando else ""

    # Construimos el contenido completo del archivo Markdown.
    # El formato con **Campo:** es el que el frontend (app.js) espera para parsear.
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

    # Registramos el slug para evitar duplicados en el resto de esta ejecución
    known_slugs.add(slug)
    print(f"  ✅ {filename}")
    print(f"     → {title_es[:70]}")
    return True


# ── PROCESADO DE FEEDS ───────────────────────────────────────────

def process_feed(feed_url: str, known_slugs: set,
                 saved_titles: list, max_per_feed: int, max_per_run: int) -> None:
    """
    Descarga un feed RSS y procesa cada entrada nueva que encuentre.

    Por qué existe:
        Encapsula toda la lógica de procesamiento de un solo feed RSS.
        Esto hace que main() sea más limpio y que los errores de un feed
        concreto no afecten al resto de feeds del ciclo principal.

    Pasos para cada entrada del feed:
        1. Comprueba el límite global de la ejecución (max_per_run).
        2. Genera el slug del título original y comprueba si ya existe.
        3. Extrae el texto del RSS (descripción o content) como fallback.
        4. Intenta descargar el artículo completo con scrape_full_article().
        5. Llama a la IA (summarize_with_gemini) para generar el resumen.
        6. Determina la categoría con categorize_news().
        7. Guarda el archivo .md con save_news().

    Args:
        feed_url:      URL del feed RSS a procesar
        known_slugs:   set de slugs ya existentes (se modifica in-place)
        saved_titles:  lista de títulos guardados en esta ejecución (para el log)
        max_per_feed:  máximo de artículos a procesar de este feed
        max_per_run:   máximo global de artículos en esta ejecución completa
    """
    print(f"\n📡 {feed_url}")
    try:
        # Descargamos el feed con requests (en lugar de feedparser directamente)
        # para poder enviar cabeceras de User-Agent y evitar bloqueos
        headers  = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(feed_url, headers=headers, timeout=30)
        response.raise_for_status()

        # feedparser convierte el XML del RSS en un objeto Python navegable
        feed = feedparser.parse(response.text)

        # feed.bozo es True si el XML del feed tiene errores de formato.
        # Si además no hay entradas, no podemos hacer nada con este feed.
        if feed.bozo and not feed.entries:
            print(f"  ⚠️  Error de parseo: {feed.bozo_exception}")
            return

        nuevas = 0
        # [:max_per_feed] limita cuántas entradas por feed procesamos
        for entry in feed.entries[:max_per_feed]:

            # Verificamos el límite global antes de cada artículo
            if len(saved_titles) >= max_per_run:
                print(f"  ⏹ Límite diario ({max_per_run}) alcanzado.")
                return

            title_original = entry.get("title", "Sin título").strip()
            source_url     = entry.get("link", "")

            # ── Deduplicación rápida por slug ──
            # Importamos aquí dentro para evitar circular imports al inicio del módulo
            from utils import generate_slug
            if generate_slug(title_original) in known_slugs:
                print(f"  ↩ Ya existe: {title_original[:65]}")
                continue

            # ── Contenido del RSS como fallback ──
            # Algunos feeds usan el campo 'content', otros usan 'description'.
            # Intentamos primero 'content' (más completo) y caemos a 'description'.
            rss_content = ""
            if hasattr(entry, 'content') and entry.content:
                rss_content = entry.content[0].get('value', '')
            else:
                rss_content = entry.get("description", "")
            rss_text = clean_html(rss_content)  # eliminamos etiquetas HTML del RSS

            # ── Scraping del artículo completo ──
            # Intentamos obtener más texto que el que da el RSS para mejorar el resumen
            print(f"  🌐 Descargando artículo completo...")
            full_text = scrape_full_article(source_url, fallback_text=rss_text)

            # Informamos si obtuvimos el artículo completo o solo el resumen del RSS
            source_quality = "completo" if len(full_text) > len(rss_text) + 200 else "RSS"
            print(f"  📄 Contenido: {len(full_text)} chars (fuente: {source_quality})")

            # Limitamos el texto a 2500 chars para no exceder el contexto del modelo
            text_for_ai = f"Título: {title_original}\n\nContenido: {full_text[:2500]}"

            # ── Llamada a la IA ──
            print(f"  🤖 {title_original[:65]}...")
            result = summarize_with_groq(text_for_ai)

            # Si la IA no generó contenido, descartamos este artículo
            if not result.get("intro"):
                print(f"  ✗ Sin contenido generado, omitiendo.")
                continue

            # Determinamos la categoría y guardamos el archivo Markdown
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
    Escribe un registro de la ejecución al final de run_log.txt.

    Por qué existe:
        Permite auditar qué artículos se procesaron en cada ejecución,
        especialmente útil cuando el scraper corre de forma automática
        (GitHub Actions) y no hay una terminal abierta para leer la salida.

    Formato del log (se acumula, no se sobreescribe):
        [2025-03-08 12:30:00] Nuevos: 5
          + Título artículo 1
          + Título artículo 2
          ✗ Error en feed X: message

    Args:
        saved_titles: lista de títulos de artículos guardados exitosamente
        errors:       lista de mensajes de error ocurridos durante la ejecución
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

    # Modo "a" (append) para acumular logs de distintas ejecuciones
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line)


# ── MAIN ─────────────────────────────────────────────────────────

def main():
    """
    Función principal que orquesta todo el proceso de captura de noticias.

    Flujo:
        1. Carga la configuración desde config.json
        2. Crea los directorios de contenido si no existen
        3. Carga los slugs existentes para deduplicar
        4. Itera por cada feed RSS y procesa sus entradas nuevas
        5. Escribe el log de la ejecución
        6. Muestra un resumen en consola
    """
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
        # Si ya alcanzamos el límite global, no procesamos más feeds
        if len(saved_titles) >= max_per_run:
            print("\n⏹ Límite diario alcanzado.")
            break
        try:
            process_feed(url, known_slugs, saved_titles, max_per_feed, max_per_run)
        except Exception as e:
            # Un error en un feed no debe detener el resto de feeds
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
