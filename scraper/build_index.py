#!/usr/bin/env python3
"""
build_index.py — Generador de archivos estáticos de TechPulse ES
=================================================================
Lee todos los archivos Markdown de docs/content/ y genera tres
archivos estáticos que el frontend y los buscadores necesitan:

  - docs/index.json   → array JSON consumido por app.js del frontend
  - docs/sitemap.xml  → mapa del sitio para Google y otros buscadores
  - docs/feed.xml     → feed RSS propio para lectores de noticias

Este script se ejecuta DESPUÉS de main.py (que genera los .md)
y ANTES de publicar el sitio en GitHub Pages.

Uso:
    cd scraper
    python build_index.py

La URL del sitio se lee desde config.json (clave "site_url").
"""

import os
import json
import re
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone

# BASE_DIR apunta a la raíz del proyecto (un nivel arriba de scraper/)
BASE_DIR   = Path(__file__).resolve().parent.parent
# OUTPUT_DIR es docs/ — donde se generan los archivos estáticos
OUTPUT_DIR = BASE_DIR / "docs"


# ── CONFIGURACIÓN ────────────────────────────────────────────────

def load_config() -> dict:
    """
    Carga la configuración del proyecto desde scraper/config.json.

    Por qué existe:
        La URL del sitio (site_url) es necesaria para construir los
        enlaces del sitemap.xml y feed.xml. Al leerla desde config.json
        en lugar de tenerla hardcodeada, el mismo código funciona en
        desarrollo local, staging y producción sin modificaciones.

    Returns:
        Diccionario con la configuración. Si config.json no existe,
        devuelve valores por defecto con URLs de ejemplo para que
        el script pueda ejecutarse sin configuración previa.
    """
    config_path = BASE_DIR / "scraper" / "config.json"
    if config_path.exists():
        with open(config_path, encoding="utf-8") as f:
            return json.load(f)
    # Valores por defecto cuando no hay config.json
    return {
        "site_url":  "https://RafaBC-dev.github.io/WebTechAI",
        "site_name": "TechPulse ES",
        "site_desc": "Tecnología, robótica e IA explicada en español"
    }


# ── EXTRACCIÓN DE METADATOS ──────────────────────────────────────

def extract_metadata(path: str) -> dict:
    """
    Extrae todos los metadatos de un archivo Markdown de artículo.

    Por qué existe:
        Los artículos se guardan como texto Markdown plano sin un sistema
        de frontmatter estándar. Esta función los parsea usando expresiones
        regulares para extraer los campos que el frontend necesita:
        título, categoría, fecha, slug, tags, preview y si tiene código.

    Campos extraídos y cómo:
        - title:       primera línea que empieza por "# " (encabezado H1)
        - category:    línea "**Categoría:** valor"
        - tags:        línea "**Tags:** tag1, tag2, tag3"
        - date:        prefijo del nombre de archivo (YYYY-MM-DD)
        - slug:        nombre de archivo sin el prefijo de fecha ni .md
        - preview:     primer párrafo de la sección "## Introducción"
                       recortado a 240 chars con corte en la última palabra
        - has_command: True si el Markdown contiene algún bloque de código (```)
        - file_path:   ruta relativa desde docs/ para que el frontend
                       pueda hacer fetch() del archivo directamente

    Args:
        path: ruta absoluta al archivo .md

    Returns:
        Diccionario con los metadatos del artículo. Si hay algún error
        leyendo el archivo, devuelve el diccionario con campos vacíos.
    """
    meta = {
        "title": "", "category": "", "date": "", "slug": "",
        "tags": [], "preview": "", "has_command": False, "file_path": ""
    }
    try:
        with open(path, encoding="utf-8") as f:
            content = f.read()

        # Título: primera línea con "# " (H1 de Markdown)
        m = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if m:
            meta["title"] = m.group(1).strip()

        # Categoría: línea con el formato **Categoría:** valor
        for field, key in [
            (r'\*\*Categoría:\*\*\s*(.+)', "category"),
        ]:
            m = re.search(field, content, re.MULTILINE)
            if m:
                meta[key] = m.group(1).strip()

        # Tags: línea "**Tags:** tag1, tag2" → lista de strings
        m = re.search(r'\*\*Tags:\*\*\s*(.+)', content, re.MULTILINE)
        if m:
            meta["tags"] = [t.strip() for t in m.group(1).split(",") if t.strip()]

        # Fecha y slug: se extraen del nombre del archivo "YYYY-MM-DD-slug.md"
        filename = os.path.basename(path)
        m = re.match(r'^(\d{4}-\d{2}-\d{2})-(.+)\.md$', filename)
        if m:
            meta["date"] = m.group(1)   # "2025-03-08"
            meta["slug"] = m.group(2)   # "nueva-version-ubuntu"

        # Si no encontramos categoría en el contenido, la inferimos del nombre de carpeta
        if not meta["category"]:
            meta["category"] = os.path.basename(os.path.dirname(path)).capitalize()

        # Preview: primer párrafo del bloque "## Introducción"
        # El patrón captura todo hasta el siguiente ## o --- o fin de archivo
        m = re.search(r'## Introducción\s*\n+([\s\S]+?)(?=\n##|\n---|$)', content)
        if m:
            preview = re.sub(r'\n+', ' ', m.group(1).strip())
            # Recortamos a 240 chars y terminamos en la última palabra completa
            if len(preview) > 240:
                preview = preview[:240].rsplit(' ', 1)[0] + "…"
            meta["preview"] = preview

        # has_command: True si el artículo tiene algún bloque de código
        meta["has_command"] = "```" in content

        # file_path: ruta relativa desde docs/ para que el frontend pueda
        # hacer fetch('content/ia/articulo.md') en lugar de la ruta absoluta.
        # También normalizamos las barras invertidas (Windows → web).
        rel_path = Path(path).relative_to(BASE_DIR / "docs")
        meta["file_path"] = str(rel_path).replace("\\", "/")

    except Exception as e:
        print(f"  ⚠️  Error en {path}: {e}")

    return meta


# ── INDEX.JSON ───────────────────────────────────────────────────

def build_index(news: list):
    """
    Genera docs/index.json con el array de todos los artículos.

    Por qué existe:
        El frontend (app.js) necesita un único fichero JSON con todos los
        artículos para implementar el filtrado, la búsqueda y la paginación
        sin necesidad de un servidor backend. index.json actúa como una
        "base de datos" estática consumida directamente por el navegador.

    Contenido: array JSON ordenado por fecha descendente (más reciente primero),
    donde cada elemento es el diccionario devuelto por extract_metadata().

    Args:
        news: lista de diccionarios de metadatos, ya ordenada por fecha
    """
    OUTPUT_DIR = BASE_DIR / "docs"
    with open(OUTPUT_DIR / "index.json", "w", encoding="utf-8") as f:
        # indent=2 para que sea legible por humanos; ensure_ascii=False para tildes
        json.dump(news, f, indent=2, ensure_ascii=False)
    print(f"✅ index.json   — {len(news)} artículos")


# ── SITEMAP.XML ──────────────────────────────────────────────────

def build_sitemap(news: list, site_url: str):
    """
    Genera docs/sitemap.xml para la indexación en buscadores.

    Por qué existe:
        Un sitemap.xml le dice a Google, Bing y otros buscadores qué páginas
        existen en el sitio, cuándo se actualizaron y su prioridad relativa.
        Sin sitemap, los buscadores tienen que descubrir las páginas por su cuenta
        siguiendo enlaces, lo que puede tardar semanas o dejarse páginas sin indexar.

    Estructura del XML:
        - Página principal (priority 1.0): la más importante
        - Página about (priority 0.6): informativa, menos prioritaria
        - Un <url> por artículo (priority 0.8): contenido principal del sitio

    Los artículos usan URLs del tipo:
        https://sitio.github.io/detail.html?file=content/ia/articulo.md

    Args:
        news:     lista de metadatos de artículos
        site_url: URL base del sitio (ej: "https://usuario.github.io/repo")
    """
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # Empezamos con las páginas estáticas del sitio
    urls = [
        f'  <url><loc>{site_url}/</loc><lastmod>{today}</lastmod><priority>1.0</priority></url>',
        f'  <url><loc>{site_url}/about.html</loc><lastmod>{today}</lastmod><priority>0.6</priority></url>',
    ]

    # Añadimos una entrada por cada artículo con su fecha de publicación
    for n in news:
        if not n.get("date") or not n.get("file_path"):
            continue  # saltamos artículos sin fecha o sin ruta (datos incompletos)
        loc = f'{site_url}/detail.html?file={n["file_path"]}'
        urls.append(
            f'  <url><loc>{loc}</loc>'
            f'<lastmod>{n["date"]}</lastmod>'
            f'<priority>0.8</priority></url>'
        )

    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls)
        + "\n</urlset>"
    )
    with open(OUTPUT_DIR / "sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap)
    print(f"✅ sitemap.xml  — {len(urls)} URLs")


# ── FEED.XML (RSS propio) ────────────────────────────────────────

def build_feed(news: list, site_url: str, site_name: str, site_desc: str):
    """
    Genera docs/feed.xml: el feed RSS propio del sitio TechPulse ES.

    Por qué existe:
        Permite que los lectores se suscriban al sitio usando lectores de RSS
        (Feedly, NewsBlur, etc.) y reciban las novedades automáticamente,
        sin tener que visitar manualmente la web.
        También es una señal positiva para algunos buscadores.

    Detalles del feed:
        - Incluye los últimos 30 artículos (más es inusual para RSS)
        - Cada <item> contiene: título, enlace, GUID, fecha, categoría y descripción
        - Los caracteres especiales se escapan con xml_escape() para evitar XML inválido
        - El elemento <atom:link> es obligatorio según el estándar RSS con Atom

    Args:
        news:      lista de metadatos de artículos (ya ordenada por fecha)
        site_url:  URL base del sitio
        site_name: nombre del sitio para el canal RSS
        site_desc: descripción del sitio para el canal RSS
    """
    pub_date = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")

    def xml_escape(text: str) -> str:
        """
        Escapa los caracteres especiales del XML para evitar XML malformado.
        Los tres caracteres reservados en XML son &, < y >.
        Deben reemplazarse por sus entidades: &amp; &lt; &gt;
        """
        return (text or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    items = []
    # Solo incluimos los 30 más recientes (el feed.entries[:max] es estándar en RSS)
    for n in news[:30]:
        if not n.get("title") or not n.get("date"):
            continue  # saltamos entradas incompletas
        link = f'{site_url}/detail.html?file={n.get("file_path", "")}'
        try:
            # Convertimos la fecha "YYYY-MM-DD" al formato RFC 2822 que exige el estándar RSS
            d = datetime.strptime(n["date"], "%Y-%m-%d").replace(tzinfo=timezone.utc)
            item_date = d.strftime("%a, %d %b %Y 08:00:00 +0000")
        except Exception:
            item_date = pub_date  # fallback: fecha de generación del feed

        items.append(f"""  <item>
    <title>{xml_escape(n['title'])}</title>
    <link>{link}</link>
    <guid isPermaLink="true">{link}</guid>
    <pubDate>{item_date}</pubDate>
    <category>{xml_escape(n.get('category', ''))}</category>
    <description>{xml_escape(n.get('preview', ''))}</description>
  </item>""")

    rss = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
  <title>{xml_escape(site_name)}</title>
  <link>{site_url}</link>
  <description>{xml_escape(site_desc)}</description>
  <language>es</language>
  <lastBuildDate>{pub_date}</lastBuildDate>
  <atom:link href="{site_url}/feed.xml" rel="self" type="application/rss+xml"/>
{chr(10).join(items)}
</channel>
</rss>"""

    with open(OUTPUT_DIR / "feed.xml", "w", encoding="utf-8") as f:
        f.write(rss)
    print(f"✅ feed.xml     — {len(items)} entradas")


# ── MAIN ─────────────────────────────────────────────────────────

def build_all():
    """
    Función principal que orquesta la generación de todos los archivos estáticos.

    Flujo:
        1. Carga la configuración (site_url, site_name, site_desc)
        2. Verifica que existe docs/content/ (debe haber artículos previos)
        3. Recorre todos los .md de docs/content/ y extrae sus metadatos
        4. Ordena los artículos por fecha descendente (más reciente = primero)
        5. Genera index.json, sitemap.xml y feed.xml
        6. Muestra un resumen por categoría y el total de artículos
    """
    config    = load_config()
    site_url  = config.get("site_url",  "https://tu-usuario.github.io/tu-repo")
    site_name = config.get("site_name", "TechPulse ES")
    site_desc = config.get("site_desc", "Tecnología, robótica e IA explicada en español")

    print("🔨 TechPulse ES — Generando archivos estáticos")
    print(f"   Site URL: {site_url}")
    print("=" * 60)

    content_dir = BASE_DIR / "docs" / "content"
    if not content_dir.exists():
        print("⚠️  Carpeta 'content' no encontrada. Ejecuta main.py primero.")
        return

    # Recorremos todos los .md recursivamente y extraemos metadatos
    news = []
    for md in content_dir.rglob("*.md"):
        meta = extract_metadata(str(md))
        if meta["title"]:  # descartamos archivos sin título (probablemente corruptos)
            news.append(meta)

    if not news:
        print("⚠️  No se encontraron artículos en content/")
        return

    # Ordenamos por fecha descendente: el artículo más reciente aparece primero en index.json
    news.sort(key=lambda x: x.get("date", ""), reverse=True)

    # Generamos los tres archivos estáticos
    build_index(news)
    build_sitemap(news, site_url)
    build_feed(news, site_url, site_name, site_desc)

    # Resumen final: artículos por categoría
    print(f"\n📂 Artículos por categoría:")
    cats = Counter(n["category"] for n in news)
    for cat, count in sorted(cats.items()):
        print(f"   {cat}: {count}")
    print(f"\n✅ Total: {len(news)} artículos")


if __name__ == "__main__":
    build_all()
