#!/usr/bin/env python3
"""
weekly_report.py — Generador de informes semanales para TechPulse ES
=====================================================================
Genera un informe markdown actualizado por sección del sidebar:
  - Benchmarks de modelos IA      → docs/reports/benchmarks.md
  - Agentes y frameworks de IA    → docs/reports/agentes.md
  - Proyectos y tutoriales ESP32  → docs/reports/esp32.md
  - Librerías y herramientas Python → docs/reports/python.md

Cada informe se sobreescribe en cada ejecución (es información «viva»).

EJECUCIÓN:
  python scraper/weekly_report.py
  (o mediante GitHub Actions los lunes a las 08:00 UTC)

DEPENDENCIAS:
  pip install groq python-dotenv feedparser requests beautifulsoup4
"""

import sys
import os
import time
import re
import feedparser
import requests
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from bs4 import BeautifulSoup

# ── CONFIGURACIÓN ─────────────────────────────────────────────────────────────

# BASE_DIR apunta a la raíz del repositorio (igual que main.py)
BASE_DIR    = Path(__file__).resolve().parent.parent
REPORTS_DIR = BASE_DIR / "docs" / "reports"

# Modelo Groq (igual que brain.py)
MODEL = "llama-3.1-8b-instant"

# Carga GROQ_API_KEY desde .env
load_dotenv()

# UTF-8 en consola Windows
try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass


# ── DEFINICIÓN DE INFORMES ────────────────────────────────────────────────────

# Cada entrada define:
#   tema    → descripción para el prompt de Groq
#   feeds   → lista de URLs RSS a scrapear
#   pages   → lista de URLs HTML a scrapear directamente (sin RSS)
#   out     → nombre del archivo de salida (sin .md)
REPORTS = {
    "benchmarks": {
        "tema": "benchmarks y comparativas de modelos de inteligencia artificial",
        "feeds": [
            "https://huggingface.co/blog/feed.xml",
            "https://simonwillison.net/atom/everything/",
            "https://venturebeat.com/category/ai/feed/",
        ],
        "pages": [],          # páginas estáticas (sin JS)
        "dynamic_pages": [    # páginas que necesitan JS para cargar
            "https://artificialanalysis.ai/models",
            "https://lmarena.ai/?leaderboard",
        ],
        "out": "benchmarks",
    },
    "agentes": {
        "tema": "agentes de inteligencia artificial: frameworks de agentes (LangChain, "
                "LangGraph, AutoGen, CrewAI, Swarm), casos de uso reales, noticias sobre "
                "agentes autónomos, herramientas nuevas y tendencias en agentic AI",
        "feeds": [
            "https://simonwillison.net/atom/everything/",
            "https://huggingface.co/blog/feed.xml",
        ],
        "pages": [],
        "dynamic_pages": [],
        "out": "agentes",
    },
    "esp32": {
        "tema": "ESP32: tutoriales, proyectos, novedades de hardware y firmware, "
                "MicroPython en ESP32, ESP-IDF, ESP32-S3, ESP32-C3, conectividad WiFi/BLE, "
                "integración con sensores y actuadores",
        "feeds": [
            "https://randomnerdtutorials.com/feed/",
            "https://blog.adafruit.com/feed/",
        ],
        "pages": [],
        "dynamic_pages": [],
        "out": "esp32",
    },
    "python": {
        "tema": "Python: librerías nuevas, actualizaciones de paquetes PyPI, tutoriales "
                "prácticos, herramientas para desarrolladores, buenas prácticas, "
                "rendimiento, typing, async, testing y novedades del ecosistema",
        "feeds": [
            "https://realpython.com/atom.xml",
            "https://pypi.org/rss/updates.xml",
        ],
        "pages": [],
        "dynamic_pages": [],
        "out": "python",
    },
}


# ── SCRAPING ──────────────────────────────────────────────────────────────────

def fetch_feed_text(url: str, max_entries: int = 6) -> str:
    """
    Descarga un feed RSS/Atom y extrae el texto de las últimas entradas.

    Por qué max_entries=6:
        Buscamos un balance entre contexto suficiente para el LLM y no
        superar el límite de tokens del modelo (1200 en brain.py pero
        aquí usamos 2000 para los informes).

    Args:
        url:         URL del feed RSS o Atom.
        max_entries: Número máximo de entradas a extraer.

    Returns:
        Texto concatenado de títulos + descripciones de las entradas.
    """
    headers = {"User-Agent": "Mozilla/5.0 TechPulseES-WeeklyReport/1.0"}
    try:
        resp = requests.get(url, headers=headers, timeout=20)
        resp.raise_for_status()
        feed = feedparser.parse(resp.text)
        if not feed.entries:
            print(f"  ⚠️  Sin entradas en {url}")
            return ""

        texts = []
        for entry in feed.entries[:max_entries]:
            title = entry.get("title", "").strip()
            # Preferimos content (Atom) sobre description (RSS 2.0)
            body = ""
            if hasattr(entry, "content") and entry.content:
                body = entry.content[0].get("value", "")
            else:
                body = entry.get("description", "")
            # Limpiar HTML con BeautifulSoup
            body = BeautifulSoup(body, "html.parser").get_text(" ", strip=True)
            # Limitar cada entrada para no saturar el contexto
            texts.append(f"### {title}\n{body[:600]}")

        return "\n\n".join(texts)

    except Exception as e:
        print(f"  ✗ Error en feed {url}: {e}")
        return ""


def fetch_dynamic_page(url: str, wait_seconds: int = 3, max_chars: int = 4000) -> str:
    """
    Descarga una página que requiere JavaScript usando Playwright (Chromium headless).

    A diferencia de fetch_page_text(), esta función lanza un navegador real que
    ejecuta el JS de la página antes de extraer el texto, lo que permite obtener
    contenido de tablas, clasificaciones y datos que se renderizan dinámicamente
    (artificialanalysis.ai/models, chat.lmsys.org, etc.).

    Por qué sync_playwright en lugar de async:
        weekly_report.py usa un flujo síncrono simple; usar asyncio añadiría
        complejidad innecesaria. sync_playwright es el wrapper síncrono oficial.

    Args:
        url:          URL de la página a cargar.
        wait_seconds: Segundos a esperar tras el load event para que el JS termine.
        max_chars:    Límite de caracteres del texto extraído.

    Returns:
        Texto visible de la página, truncado a max_chars. Cadena vacía si falla.
    """
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print(f"  ⚠️  Playwright no instalado. Ejecuta: pip install playwright && playwright install chromium")
        return ""

    try:
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=True)
            page    = browser.new_page()
            # Bloqueamos recursos pesados innecesarios para acelerar la carga
            page.route("**/*.{png,jpg,jpeg,gif,webp,svg,woff,woff2,mp4}",
                       lambda route: route.abort())
            page.goto(url, timeout=30_000, wait_until="domcontentloaded")
            # Esperamos a que el JS dinámico termine de poblar el DOM
            page.wait_for_timeout(wait_seconds * 1000)
            # Extraemos el texto visible del body (sin scripts ni estilos)
            text = page.evaluate("""
                () => {
                    const scripts = document.querySelectorAll('script, style, noscript');
                    scripts.forEach(el => el.remove());
                    return document.body?.innerText || '';
                }
            """)
            browser.close()

        # Limpiar líneas en blanco excesivas
        text = re.sub(r"\n{3,}", "\n\n", text.strip())
        return text[:max_chars]

    except Exception as e:
        print(f"  ✗ Error Playwright en {url}: {e}")
        return ""


def fetch_page_text(url: str, max_chars: int = 3000) -> str:
    """
    Descarga una página web y extrae su texto visible.

    Se usa para fuentes que no tienen feed RSS (ej: artificialanalysis.ai).

    Args:
        url:       URL de la página a descargar.
        max_chars: Límite de caracteres del texto extraído.

    Returns:
        Texto plano visible de la página, truncado a max_chars.
    """
    headers = {"User-Agent": "Mozilla/5.0 TechPulseES-WeeklyReport/1.0"}
    try:
        resp = requests.get(url, headers=headers, timeout=20)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        # Eliminar scripts, estilos y navegación
        for tag in soup(["script", "style", "nav", "footer", "header"]):
            tag.decompose()
        text = soup.get_text(" ", strip=True)
        # Colapsar espacios múltiples
        text = re.sub(r"\s{2,}", " ", text)
        return text[:max_chars]
    except Exception as e:
        print(f"  ✗ Error en página {url}: {e}")
        return ""


# ── GENERACIÓN DEL INFORME ────────────────────────────────────────────────────

def generate_report(tema: str, raw_text: str) -> str:
    """
    Genera informe markdown estándar para las secciones no-benchmark.
    Devuelve el texto markdown generado por Groq.
    """
    key = os.getenv("GROQ_API_KEY")
    if not key:
        raise ValueError("Falta GROQ_API_KEY en el .env")
    client = Groq(api_key=key)

    prompt = f"""Eres un experto en {tema}.

Basándote en la siguiente información reciente obtenida de feeds y fuentes especializadas,
genera un informe semanal de referencia en español. El informe debe ser concreto,
actualizado y útil para un desarrollador que quiere saber el estado actual del tema.

INFORMACIÓN RECIENTE:
{raw_text[:4000]}

Genera el informe con EXACTAMENTE estas secciones en markdown:

## Estado actual
(Resumen de dónde está el campo ahora mismo: tecnologías reales, herramientas maduras,
nivel de adopción. 3-5 frases.)

## Novedades destacadas esta semana
(Las noticias, lanzamientos o cambios más relevantes de la información anterior.
Lista de 3-5 puntos concretos con contexto.)

## Herramientas y recursos recomendados ahora mismo
(Las mejores opciones disponibles hoy para alguien que quiere trabajar en este área.
Sé específico: nombres, versiones si aplica, por qué son buenos ahora.)

## Recursos útiles
(Lista de 3-5 enlaces o referencias mencionados en la información, con una línea
explicando qué aporta cada uno. Formato: - [texto](url) — descripción)

Escribe en español neutro y directo. No uses frases genéricas. Sé concreto."""

    for intento in range(3):
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.4,
                max_tokens=2000,
            )
            return response.choices[0].message.content.strip()

        except Exception as e:
            msg = str(e)
            if "429" in msg or "rate" in msg.lower():
                if intento < 2:
                    print(f"  ⏳ Rate limit. Esperando 30s...")
                    time.sleep(30)
                    continue
                return "⚠️ No se pudo generar el informe por rate limit."
            print(f"  ✗ Error Groq: {e}")
            raise

    return "⚠️ No se pudo generar el informe."


def generate_benchmark_report(raw_text: str) -> dict:
    """
    Genera el informe de benchmarks en formato JSON+markdown dual.

    Groq devuelve un JSON con dos campos:
      - "informe":  markdown con análisis narrativo en español
      - "modelos":  lista de modelos con puntuación, velocidad, precio, contexto
      - "semana":   fecha del informe

    Args:
        raw_text: Texto scrapeado de feeds y páginas de benchmarks.

    Returns:
        dict con claves: informe (str), modelos (list), semana (str).
        Devuelve dict vacío si falla completamente.
    """
    import json as _json
    from datetime import datetime

    key = os.getenv("GROQ_API_KEY")
    if not key:
        raise ValueError("Falta GROQ_API_KEY en el .env")
    client = Groq(api_key=key)

    semana_str = datetime.now().strftime("%d %b %Y").lstrip("0")

    prompt = f"""Eres un analista experto en benchmarks y comparativas de modelos de IA.

Analiza la siguiente información reciente de fuentes especializadas y genera un informe
completo sobre el estado actual de los modelos de IA esta semana.

INFORMACIÓN RECIENTE:
{raw_text[:5000]}

Responde ÚNICAMENTE con JSON válido, sin bloques markdown, sin texto adicional.
El JSON debe tener este formato exacto:
{{
  "informe": "## Estado actual\n(3-5 frases sobre el panorama actual de modelos de IA)\n\n## Novedades esta semana\n(lista de 3-5 novedades concretas de los feeds, con nombres reales)\n\n## Análisis de rendimiento\n(análisis de velocidad, precio y calidad de los modelos mencionados)\n\n## Recursos útiles\n(lista de 2-4 enlaces concretos de las fuentes scrapeadas)",
  "modelos": [
    {{
      "nombre": "Nombre del modelo (ej: GPT-4o, Claude 3.5, Gemini 1.5 Pro)",
      "puntuacion": 85,
      "velocidad": "alta",
      "precio": "medio",
      "contexto": "128k",
      "destacado": false,
      "novedad": false
    }}
  ],
  "semana": "{semana_str}"
}}

REGLAS PARA modelos[]:
- Incluye SOLO modelos mencionados explícitamente en el texto scrapeado
- puntuacion: número 0-100 basado en resultados de benchmarks mencionados
- velocidad: exactamente "alta", "media" o "baja"
- precio: exactamente "bajo", "medio" o "alto"
- contexto: tamaño de ventana de contexto (ej: "8k", "128k", "200k") o "desconocido"
- destacado: true solo para el modelo con mejor rendimiento overall esta semana
- novedad: true solo si fue lanzado o actualizado en los últimos 7 días
- Incluye entre 3 y 8 modelos. Si no hay suficientes datos, incluye solo los que tengas
- Si no hay datos de benchmarks en el texto, devuelve modelos: []

REGLAS PARA informe:
- Escribe en español neutro, concreto y útil para desarrolladores
- Menciona nombres reales de modelos y benchmarks de las fuentes
- No inventes datos que no estén en el texto scrapeado"""

    for intento in range(3):
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
                max_tokens=2500,
            )
            raw = response.choices[0].message.content.strip()
            # Limpiar bloques ```json si los hay
            raw = re.sub(r'^```(?:json)?\s*', '', raw)
            raw = re.sub(r'\s*```$', '', raw)
            result = _json.loads(raw)
            # Garantías mínimas de estructura
            result.setdefault("informe", "")
            result.setdefault("modelos", [])
            result.setdefault("semana", semana_str)
            if not isinstance(result["modelos"], list):
                result["modelos"] = []
            return result

        except _json.JSONDecodeError:
            print(f"  ⚠️  JSON inválido en intento {intento+1}, reintentando...")
            if intento == 2:
                return {"informe": "⚠️ Error al generar el informe.",
                        "modelos": [], "semana": semana_str}
            time.sleep(3)
            continue

        except Exception as e:
            msg = str(e)
            if "429" in msg or "rate" in msg.lower():
                if intento < 2:
                    print(f"  ⏳ Rate limit. Esperando 30s...")
                    time.sleep(30)
                    continue
                return {"informe": "⚠️ Rate limit.", "modelos": [], "semana": semana_str}
            print(f"  ✗ Error Groq: {e}")
            raise

    return {"informe": "", "modelos": [], "semana": semana_str}


# ── ESCRITURA ─────────────────────────────────────────────────────────────────

def save_report(name: str, content: str) -> None:
    """
    Escribe el informe en docs/reports/<name>.md sobreescribiendo el anterior.

    Por qué sobreescribir y no versionar:
        Los informes son información «viva» de referencia (estado actual),
        no histórica. El usuario espera ver siempre la versión más fresca.
        El historial queda en Git si el repositorio está bajo control de versiones.

    Args:
        name:    Nombre del informe sin extensión (ej: "benchmarks").
        content: Texto markdown del informe generado por Groq.
    """
    from datetime import datetime
    date_str = datetime.now().strftime("%Y-%m-%d")
    out_path = REPORTS_DIR / f"{name}.md"

    full_content = f"<!-- Generado automáticamente el {date_str} —  NO editar a mano -->\n\n{content}\n"

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(full_content)

    print(f"  ✅ {out_path.relative_to(BASE_DIR)}")


# ── MAIN ──────────────────────────────────────────────────────────────────────

def main():
    """
    Orquesta la generación de todos los informes semanales.

    Flujo por informe:
      1. Scrapear feeds RSS → texto
      2. Scrapear páginas HTML → texto
      3. Concatenar todo el texto
      4. Llamar a Groq para generar el informe markdown
      5. Escribir el .md en docs/reports/
    """
    print("📊 TechPulse ES — Generador de informes semanales")
    print("=" * 55)

    # Crear carpeta de informes si no existe
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    print(f"📂 Directorio: {REPORTS_DIR.relative_to(BASE_DIR)}\n")

    for report_id, cfg in REPORTS.items():
        print(f"\n─── {report_id.upper()} ───")

        # Agregar texto de todos los feeds
        raw_parts = []
        for feed_url in cfg["feeds"]:
            print(f"  📡 Feed: {feed_url}")
            text = fetch_feed_text(feed_url)
            if text:
                raw_parts.append(text)

        # Agregar texto de páginas web estáticas
        for page_url in cfg.get("pages", []):
            print(f"  🌐 Página estática: {page_url}")
            text = fetch_page_text(page_url)
            if text:
                raw_parts.append(text)

        # Agregar páginas JavaScript dinámicas (Playwright)
        for dyn_url in cfg.get("dynamic_pages", []):
            print(f"  🖥️  Página dinámica (JS): {dyn_url}")
            text = fetch_dynamic_page(dyn_url)
            if text:
                raw_parts.append(f"[Fuente dinámica: {dyn_url}]\n{text}")

        if not raw_parts:
            print("  ⚠️  Sin contenido scrapeado, omitiendo.")
            continue

        raw_text = "\n\n---\n\n".join(raw_parts)
        print(f"  📝 {len(raw_text)} chars de contexto")

        # Generar informe con Groq
        print(f"  🤖 Generando informe...")
        try:
            if report_id == "benchmarks":
                # Benchmarks: genera JSON dual (informe + modelos)
                bench_data = generate_benchmark_report(raw_text)

                # Guardar .md con el campo "informe"
                save_report(cfg["out"], bench_data.get("informe", ""))

                # Guardar .json con el objeto completo
                import json as _json
                json_path = REPORTS_DIR / "benchmarks.json"
                with open(json_path, "w", encoding="utf-8") as jf:
                    _json.dump(bench_data, jf, ensure_ascii=False, indent=2)
                print(f"  ✅ {json_path.relative_to(BASE_DIR)}")
                print(f"     → {len(bench_data.get('modelos', []))} modelos extraídos")
            else:
                # El resto de secciones: markdown estándar
                report_md = generate_report(cfg["tema"], raw_text)
                save_report(cfg["out"], report_md)

        except Exception as e:
            print(f"  ✗ Error generando informe: {e}")
            continue

    print(f"\n{'=' * 55}")
    print("✅ Informes semanales completados")


if __name__ == "__main__":
    main()
