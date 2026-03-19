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

import json
import sys
import os
import time
import re
import feedparser
import requests
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from google.genai import types
from bs4 import BeautifulSoup

from utils import with_retries

from datetime import datetime, timezone

"""# Solo ejecutar los lunes (0 = lunes en Python)
if datetime.now(timezone.utc).weekday() != 0:
    print("No es lunes, saltando informes semanales.")
    exit(0)"""

# ── CONFIGURACIÓN ─────────────────────────────────────────────────────────────

# BASE_DIR apunta a la raíz del repositorio (igual que main.py)
BASE_DIR    = Path(__file__).resolve().parent.parent
REPORTS_DIR = BASE_DIR / "docs" / "reports"

# Modelo Gemini. gemini-2.5-flash .
GEMINI_MODEL = "gemini-2.5-flash"
MAX_OUTPUT_TOKENS = 8192
MAX_CONTEXT_CHARS = 12000

# Carga GEMINI_API_KEY desde .env
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
        "tema": "herramientas de agentes IA para developers",
        # RSS fiables sobre coding agents, editores IA y desarrollo asistido
        "feeds": [
            "https://simonwillison.net/atom/everything/",
            "https://github.blog/feed/",
            "https://code.visualstudio.com/feed.xml",
        ],
        # Solo procesar entradas que mencionen estas herramientas/conceptos
        "keywords": [
            "agent", "aider", "cursor", "copilot", "claude code",
            "windsurf", "codeium", "autonomous", "coding assistant",
            "continue", "antigravity", "devin", "replit", "llm",
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
    "llms": {
        "tema": "modelos de lenguaje grandes (LLMs), actualizaciones de modelos fundacionales",
        "feeds": [
            "https://huggingface.co/blog/feed.xml",
            "https://simonwillison.net/atom/everything/",
        ],
        "pages": [],
        "dynamic_pages": [
            "https://lmarena.ai/?leaderboard",
            "https://artificialanalysis.ai/models",
        ],
        "out": "../data/llms",
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

# Knowledge base fija sobre herramientas de agentes IA para coding.
# Se incluye siempre en el prompt de generate_agent_report() para garantizar
# que el informe sea útil incluso semanas con pocas novedades.
AGENT_KNOWLEDGE_BASE = """
Herramientas principales de agentes IA en 2025-2026:

- Claude Code: agente de terminal de Anthropic, opera sobre la base de código completa,
  muy potente para refactoring, debugging y proyectos grandes. Modelo Claude Sonnet/Opus.
  Precio: de pago (requiere cuenta Anthropic). Ideal para proyectos complejos.

- Aider: agente open source para terminal, integra git automáticamente al hacer cambios,
  compatible con múltiples LLMs (GPT-4, Claude, Gemini, Ollama). Gratuito.
  Ideal para devs que prefieren terminal y control total sobre el agente.

- Cursor: editor fork de VSCode con agente integrado, modo Composer para cambios masivos,
  soporte multi-archivo. Tiene capa gratuita y planes de pago (~$20/mes).
  Ideal para developers profesionales que quieren un IDE completo con IA.

- Windsurf (Codeium): editor con agente Cascade, capa gratuita generosa,
  buenas capacidades de contexto de proyecto. Alternativa a Cursor.
  Ideal para equipos y developers con presupuesto limitado.

- GitHub Copilot: extensión para VSCode, JetBrains y otros editores, de Microsoft.
  Ahora incluye modo agente. Plan individual $10/mes, incluido en GitHub Education.
  Ideal para developers ya integrados en el ecosistema GitHub/Microsoft.

- Continue: extensión open source para VSCode y JetBrains, conecta con LLMs locales
  (Ollama) o en la nube. Totalmente configurable. Gratuito.
  Ideal para devs que quieren privacidad o modelos locales.

- Antigravity (Google): editor con agentes IA de Google DeepMind, integración con
  modelos Gemini. En desarrollo activo.
"""


def fetch_feed_text_filtered(url: str, keywords: list,
                             max_entries: int = 10) -> str:
    """
    Variante de fetch_feed_text() que solo incluye entradas que mencionan
    al menos una de las keywords (comparación case-insensitive).

    Usada para la sección de agentes, donde queremos filtrar noticias genéricas
    de feeds amplios (como github.blog o simonwillison.net) y quedarnos solo
    con las relevantes para coding agents.

    Args:
        url:         URL del feed RSS/Atom.
        keywords:    Lista de palabras clave a buscar (case-insensitive).
        max_entries: Máximo de entradas a revisar antes del filtro.

    Returns:
        Texto markdown con las entradas filtradas. Cadena vacía si ninguna pasa.
    """
    headers = {"User-Agent": "Mozilla/5.0 TechPulseES-WeeklyReport/1.0"}
    try:
        resp = requests.get(url, headers=headers, timeout=20)
        resp.raise_for_status()
        feed = feedparser.parse(resp.text)
        if not feed.entries:
            print(f"  ⚠️  Sin entradas en {url}")
            return ""

        kw_lower = [k.lower() for k in keywords]
        texts = []
        skipped = 0

        for entry in feed.entries[:max_entries]:
            title = entry.get("title", "").strip()
            body  = ""
            if hasattr(entry, "content") and entry.content:
                body = entry.content[0].get("value", "")
            else:
                body = entry.get("description", "")
            body = BeautifulSoup(body, "html.parser").get_text(" ", strip=True)

            # Filtrar: el título O los primeros 300 chars del body deben contener la keyword
            searchable = (title + " " + body[:300]).lower()
            if not any(kw in searchable for kw in kw_lower):
                skipped += 1
                continue

            texts.append(f"### {title}\n{body[:600]}")

        if skipped:
            print(f"    (filtradas {skipped} entradas sin keywords relevantes)")

        return "\n\n".join(texts)

    except Exception as e:
        print(f"  ✗ Error en feed {url}: {e}")
        return ""


@with_retries(max_retries=3, delay=15)
def generate_agent_report(raw_text: str) -> str:
    """
    Genera la guía de referencia de herramientas de agentes IA.

    A diferencia del informe de benchmarks (datos numéricos) y del informe
    estándar (resumen de noticias), esta función produce una GUÍA ESTABLE de
    referencia que combina:
      1. Knowledge base fija (AGENT_KNOWLEDGE_BASE) — siempre actualizada
      2. Novedades de la semana scrapeadas de los feeds — opcionales

    El prompt indica explícitamente que si no hay novedades importantes,
    mantenga la guía de referencia sin cambios drásticos, evitando que
    un informe vacío sobreescriba contenido útil.

    Args:
        raw_text: Texto filtrado de los feeds sobre coding agents.

    Returns:
        String markdown con la guía completa.
    """
    prompt = f"""Eres un experto en herramientas de desarrollo asistido por IA y coding agents.

Tienes acceso a esta base de conocimiento sobre las principales herramientas disponibles:

{AGENT_KNOWLEDGE_BASE}

Además, estas son las novedades y noticias de esta semana sobre agentes IA para developers:

{raw_text[:MAX_CONTEXT_CHARS] if raw_text.strip() else "(No hay novedades destacadas esta semana)"}

Genera una guía de referencia completa en español con EXACTAMENTE estas secciones:

## Stacks de agentes recomendados ahora mismo
Incluye una tabla markdown comparativa con las herramientas principales:
| Herramienta | Tipo | Precio | Ideal para | Puntuación comunidad |
|-------------|------|--------|------------|---------------------|
(Rellena con los datos de la base de conocimiento y actualiza si hay novedades esta semana)

## Herramientas destacadas esta semana
(Si hay novedades, actualizaciones o lanzamientos importantes de los feeds, descríbelos aquí.
Si no hay novedades relevantes esta semana, escribe: "Sin cambios significativos esta semana.
 La guía de referencia se mantiene actualizada.")

## ¿Cuál elegir según tu caso?
Da recomendaciones concretas y directas para:
- **Si eres principiante**: ...
- **Si eres developer profesional**: ...
- **Si trabajas en equipo**: ...
- **Si quieres privacidad / modelos locales**: ...

## Recursos y documentación
Lista de enlaces oficiales de cada herramienta (máximo 8):
- [Nombre](url) — descripción en una línea

NORMAS:
- Escribe en español neutro y directo
- La tabla debe ser markdown válido con | pipes |
- No inventes datos que no tengas en la base de conocimiento o en los feeds
- Si no hay novedades esta semana, mantén la guía estable sin cambios drásticos
- Sé concreto: precios reales, nombres reales, ventajas reales"""

    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.35,
            max_output_tokens=MAX_OUTPUT_TOKENS,
        ),
    )
    time.sleep(35)
    return response.text.strip()

@with_retries(max_retries=3, delay=15)
def generate_report(tema: str, raw_text: str) -> str:
    """
    Genera informe markdown estándar para las secciones no-benchmark.
    Devuelve el texto markdown generado por Gemini.
    """
    prompt = f"""Eres un experto en {tema}.

Basándote en la siguiente información reciente obtenida de feeds y fuentes especializadas,
genera un informe semanal de referencia en español. El informe debe ser concreto,
actualizado y útil para un desarrollador que quiere saber el estado actual del tema.

INFORMACIÓN RECIENTE:
{raw_text[:MAX_CONTEXT_CHARS]}

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

    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.4,
            max_output_tokens=MAX_OUTPUT_TOKENS,
        ),
    )
    time.sleep(35)
    return response.text.strip()


@with_retries(max_retries=3, delay=15)
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

    semana_str = datetime.now().strftime("%d %b %Y").lstrip("0")

    prompt = f"""Eres un analista experto en benchmarks de LLMs. Tu trabajo es producir
análisis concretos y accionables, NO artículos genéricos.

INFORMACIÓN RECIENTE DE FUENTES ESPECIALIZADAS:
{raw_text[:MAX_CONTEXT_CHARS]}

⚠️ REGLA CRÍTICA: NO uses saltos de línea literales (Enters) dentro del campo "informe". Usa ESTRICTAMENTE la secuencia de escape "\\n" para separar párrafos. Escapa cualquier comilla doble interna con "\\\"".
Formato exacto:
{{
  "informe": "<TEXTO MARKDOWN AQUÍ>",
  "modelos": [ {{ "nombre": "...", "puntuacion": 85, "velocidad": "alta", "precio": "medio", "contexto": "128k", "destacado": false, "novedad": false }} ],
  "semana": "{semana_str}"
}}

EXIGENCIAS PARA el campo "informe" (OBLIGATORIAS, mínimo 400 palabras):

1. MENCIONA MODELOS ESPECÍFICOS: nombra cada modelo con su puntuación concreta
   (ej: "GPT-4o alcanza 87/100 en MMLU", "Claude 3.5 Sonnet: 85/100").
   No escribas solo "los modelos principales" sin nombres.

2. COMPARA VELOCIDAD Y PRECIO CON DATOS:
   Menciona tokens/segundo reales si los tienes, o al menos rangos de precio
   (ej: "GPT-4o: ~$5/M tokens input", "Gemini Flash: <$1/M tokens").
   No escribas "algunos son más rápidos" sin especificar cuáles ni cuánto.

3. RECOMENDACIONES POR CASO DE USO (sección obligatoria):
   Incluye párrafos concretos como:
   - "Para programación y debugging: usa [modelo] porque su ventana de
     contexto de [X]k tokens permite analizar proyectos completos y 
     su puntuación en HumanEval es [Y]."
   - "Para análisis de documentos largos: usa [modelo] porque..."
   - "Para uso local sin coste: usa [modelo] porque..."
   - "Para velocidad máxima en producción: usa [modelo] porque..."

4. MODELOS NUEVOS ESTA SEMANA: si alguno es novedad (novedad:true),
   dédica un párrafo explicando qué aporta respecto a los anteriores.

5. SECCIÓN OBLIGATORIA ## Recomendación de la semana:
   Un párrafo claro y directo: "Esta semana recomiendo [modelo] para [perfil]
   porque [razón concreta con datos]". Sin ambigüedades.

6. PROHIBIDO (será penalizado):
   - Frases sin datos: "el panorama evoluciona rápidamente", "la competencia
     es intensa", "hay avances significativos", "es un área en crecimiento"
   - Generalidades sin nombres: "los modelos de vanguardia", "las principales
     soluciones", "los líderes del mercado"
   - Cualquier conclusión no respaldada por datos del texto scrapeado

ESTRUCTURA EXACTA del campo "informe" (markdown dentro del JSON, usa \\n para saltos):
"## Estado actual\\n[3-4 frases con nombres y cifras reales]\\n\\n## Comparativa de modelos esta semana\\n[análisis modelo a modelo]\\n\\n## Mejor opción según tu caso de uso\\n[recomendaciones por perfil]\\n\\n## Novedades destacadas\\n[modelos nuevos; si no hay, una frase]\\n\\n## Recomendación de la semana\\n[el modelo a usar AHORA con justificación]\\n\\n## Recursos\\n[2-3 enlaces]"

REGLAS PARA modelos[]:
- Solo modelos mencionados explícitamente en el texto scrapeado
- puntuacion: 0-100 basado en benchmarks reales
- velocidad: exactamente \"alta\", \"media\" o \"baja\"
- precio: exactamente \"bajo\", \"medio\" o \"alto\"
- contexto: ventana real (\"8k\", \"128k\", \"200k\") o \"desconocido\"
- destacado: true solo para el modelo con mejor rendimiento overall
- novedad: true solo si fue lanzado o actualizado en los últimos 7 días
- Entre 3 y 8 modelos"""

    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    
    # 1. Definimos la estructura estricta que la API debe respetar
    schema_benchmarks = {
        "type": "OBJECT",
        "properties": {
            "informe": {"type": "STRING"},
            "modelos": {
                "type": "ARRAY",
                "items": {
                    "type": "OBJECT",
                    "properties": {
                        "nombre": {"type": "STRING"},
                        "puntuacion": {"type": "INTEGER"},
                        "velocidad": {"type": "STRING"},
                        "precio": {"type": "STRING"},
                        "contexto": {"type": "STRING"},
                        "destacado": {"type": "BOOLEAN"},
                        "novedad": {"type": "BOOLEAN"}
                    }
                }
            },
            "semana": {"type": "STRING"}
        },
        "required": ["informe", "modelos", "semana"]
    }

    # 2. Llamamos a la API forzando el formato
    response = client.models.generate_content(
        model=GEMINI_MODEL, # Nos aseguramos de que arriba cambiaste a "gemini-2.5-flash"
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.3,
            max_output_tokens=MAX_OUTPUT_TOKENS, # 🚀 Ampliado para que no se corte el texto
            response_mime_type="application/json",
            response_schema=schema_benchmarks # 🚀 Obliga al motor a cerrar el JSON
        ),
    )
    time.sleep(35)
    raw = response.text.strip()
    result = _json.loads(raw, strict=False)
    
    result.setdefault("informe", "")
    result.setdefault("modelos", [])
    result.setdefault("semana", semana_str)
    if not isinstance(result["modelos"], list):
        result["modelos"] = []
    return result


@with_retries(max_retries=3, delay=15)
def generate_llm_report(raw_text: str) -> list:
    """
    Genera el json listado de modelos LLM (docs/data/llms.json).
    """
    import json as _json

    prompt = f"""Eres un experto analizando y catalogando modelos de Inteligencia Artificial (LLMs).

INFORMACIÓN RECIENTE DE FUENTES ESPECIALIZADAS:
{raw_text[:MAX_CONTEXT_CHARS]}

Devuelve SOLO JSON válido. Para cada modelo incluye datos reales y actualizados.
mejor_para debe ser un array de strings.
novedad:true solo si el modelo salió esta semana.
destacado:true solo para el mejor modelo de cada empresa.

Genera una lista JSON con los 8-12 modelos más relevantes de esta semana siguiendo EXACTAMENTE esta estructura:
[
  {{
    "id": "claude-sonnet-4",
    "nombre": "Claude Sonnet 4.6",
    "empresa": "Anthropic",
    "logo_emoji": "🟠",
    "descripcion_corta": "",
    "que_es": "",
    "mejor_para": [],
    "no_usar_para": "",
    "contexto": "200k",
    "precio_input": "3$/M tokens",
    "precio_output": "15$/M tokens",
    "precio_tier": "medio",
    "velocidad": "alta",
    "disponible_en": ["API", "claude.ai"],
    "modelo_similar": "gpt-4o",
    "novedad": false,
    "destacado": false,
    "acceso_gratuito": false,
    "fecha_lanzamiento": "2025",
    "tags": []
  }}
]
"""

    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.3,
            max_output_tokens=MAX_OUTPUT_TOKENS,
            response_mime_type="application/json",
        ),
    )
    time.sleep(35)
    raw = response.text.strip()
    # Limpiar bloques ```json si los hay
    raw = re.sub(r'^```(?:json)?\s*', '', raw)
    raw = re.sub(r'\s*```$', '', raw)
    try:
        result = _json.loads(raw)
        if not isinstance(result, list):
            result = []
    except _json.JSONDecodeError as e:
        print(f"  ✗ Error parseando JSON de LLMs: {e}")
        print(f"  DEBUG raw (últimos 200 chars): {raw[-200:]}")  # añade esto
        result = []
    return result


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

        # Agregar texto de todos los feeds.
        # Para secciones con keywords (agentes) usamos el fetch filtrado que
        # descarta entradas sin relevancia antes de enviarlas a Groq.
        raw_parts = []
        keywords = cfg.get("keywords", [])
        for feed_url in cfg["feeds"]:
            print(f"  📡 Feed: {feed_url}")
            if keywords:
                text = fetch_feed_text_filtered(feed_url, keywords)
            else:
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

            elif report_id == "agentes":
                # Agentes: guia de referencia con knowledge base fija
                report_md = generate_agent_report(raw_text)
                save_report(cfg["out"], report_md)

            elif report_id == "llms":
                # LLMs: array JSON para la página interactiva
                llms_data = generate_llm_report(raw_text)
                
                import json as _json
                json_path = REPORTS_DIR / f"{cfg['out']}.json"
                
                with open(json_path, "w", encoding="utf-8") as jf:
                    _json.dump(llms_data, jf, ensure_ascii=False, indent=2)
                print(f"  ✅ {json_path.relative_to(BASE_DIR)}")
                print(f"     → {len(llms_data)} modelos extraídos")

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
