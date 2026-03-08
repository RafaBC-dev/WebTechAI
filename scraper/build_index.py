#!/usr/bin/env python3
"""
TechPulse ES — Generador de archivos estáticos.

Genera a partir de los Markdown en web/content/:
  - index.json   → consumido por el frontend (en web/)
  - sitemap.xml  → para indexación en buscadores (en web/)
  - feed.xml     → RSS propio para suscriptores (en web/)

La URL del sitio se lee desde config.json (clave "site_url").
"""

import os
import json
import re
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone

# Ajustar rutas relativas desde scraper/ hacia arriba
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "docs"


# ── CONFIGURACIÓN ────────────────────────────────────────────────

def load_config() -> dict:
    config_path = BASE_DIR / "scraper" / "config.json"
    if config_path.exists():
        with open(config_path, encoding="utf-8") as f:
            return json.load(f)
    return {
        "site_url":  "https://tu-usuario.github.io/tu-repo",
        "site_name": "TechPulse ES",
        "site_desc": "Tecnología, robótica e IA explicada en español"
    }


# ── EXTRACCIÓN DE METADATOS ──────────────────────────────────────

def extract_metadata(path: str) -> dict:
    """
    Extrae todos los metadatos de un archivo Markdown:
    título, categoría, fecha, slug, tags, preview y si tiene código.
    """
    meta = {
        "title": "", "category": "", "date": "", "slug": "",
        "tags": [], "preview": "", "has_command": False, "file_path": ""
    }
    try:
        with open(path, encoding="utf-8") as f:
            content = f.read()

        # Título (primera línea con #)
        m = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if m:
            meta["title"] = m.group(1).strip()

        # Campos de la cabecera
        for field, key in [
            (r'\*\*Categoría:\*\*\s*(.+)', "category"),
        ]:
            m = re.search(field, content, re.MULTILINE)
            if m:
                meta[key] = m.group(1).strip()

        # Tags
        m = re.search(r'\*\*Tags:\*\*\s*(.+)', content, re.MULTILINE)
        if m:
            meta["tags"] = [t.strip() for t in m.group(1).split(",") if t.strip()]

        # Fecha y slug desde el nombre de archivo
        filename = os.path.basename(path)
        m = re.match(r'^(\d{4}-\d{2}-\d{2})-(.+)\.md$', filename)
        if m:
            meta["date"] = m.group(1)
            meta["slug"] = m.group(2)

        # Categoría desde la carpeta si no se encontró en el contenido
        if not meta["category"]:
            meta["category"] = os.path.basename(os.path.dirname(path)).capitalize()

        # Preview: primer párrafo de la Introducción
        m = re.search(r'## Introducción\s*\n+([\s\S]+?)(?=\n##|\n---|$)', content)
        if m:
            preview = re.sub(r'\n+', ' ', m.group(1).strip())
            if len(preview) > 240:
                preview = preview[:240].rsplit(' ', 1)[0] + "…"
            meta["preview"] = preview

        meta["has_command"] = "```" in content
        # file_path debe ser relativo desde web/ para que el frontend pueda fetch() correctamente
        # path es algo como: /repo/web/content/ia/articulo.md
        # queremos: content/ia/articulo.md
        rel_path = Path(path).relative_to(BASE_DIR / "docs")
        meta["file_path"]   = str(rel_path).replace("\\", "/")

    except Exception as e:
        print(f"  ⚠️  Error en {path}: {e}")

    return meta


# ── INDEX.JSON ───────────────────────────────────────────────────

def build_index(news: list):
    OUTPUT_DIR = BASE_DIR / "docs"
    with open(OUTPUT_DIR / "index.json", "w", encoding="utf-8") as f:
        json.dump(news, f, indent=2, ensure_ascii=False)
    print(f"✅ index.json   — {len(news)} artículos")


# ── SITEMAP.XML ──────────────────────────────────────────────────

def build_sitemap(news: list, site_url: str):
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    urls  = [
        f'  <url><loc>{site_url}/</loc><lastmod>{today}</lastmod><priority>1.0</priority></url>',
        f'  <url><loc>{site_url}/about.html</loc><lastmod>{today}</lastmod><priority>0.6</priority></url>',
    ]
    for n in news:
        if not n.get("date") or not n.get("file_path"):
            continue
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
    pub_date = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")

    def xml_escape(text: str) -> str:
        return (text or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    items = []
    for n in news[:30]:
        if not n.get("title") or not n.get("date"):
            continue
        link = f'{site_url}/detail.html?file={n.get("file_path", "")}'
        try:
            d = datetime.strptime(n["date"], "%Y-%m-%d").replace(tzinfo=timezone.utc)
            item_date = d.strftime("%a, %d %b %Y 08:00:00 +0000")
        except Exception:
            item_date = pub_date

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

    news = []
    for md in content_dir.rglob("*.md"):
        meta = extract_metadata(str(md))
        if meta["title"]:
            news.append(meta)

    if not news:
        print("⚠️  No se encontraron artículos en content/")
        return

    # Ordenar por fecha descendente
    news.sort(key=lambda x: x.get("date", ""), reverse=True)

    build_index(news)
    build_sitemap(news, site_url)
    build_feed(news, site_url, site_name, site_desc)

    print(f"\n📂 Artículos por categoría:")
    cats = Counter(n["category"] for n in news)
    for cat, count in sorted(cats.items()):
        print(f"   {cat}: {count}")
    print(f"\n✅ Total: {len(news)} artículos")


if __name__ == "__main__":
    build_all()
