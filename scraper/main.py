#!/usr/bin/env python3
"""
main.py — Orquestador principal del scraper de TechPulse ES
============================================================
Este módulo es el punto de entrada del pipeline de captura de noticias.

FLUJO DE EJECUCIÓN COMPLETO:
  1. Lee config.json (feeds, límites, score mínimo de relevancia)
  2. Carga slugs ya procesados para evitar duplicados
  3. Para cada feed RSS descarga las últimas entradas
  4. Filtra duplicados por slug
  5. Comprueba relevancia — descarta artículos off-topic (dinosaurios, deportes...)
  6. Hace scraping del artículo completo desde la URL original
  7. Llama a Groq/LLaMA para generar el resumen en español
  8. Guarda el Markdown en docs/content/<categoría>/
  9. Escribe el log de la ejecución en run_log.txt

DEPENDENCIAS INTERNAS:
  - brain.py  → summarize_with_groq() — llama a la API de Groq
  - utils.py  → limpieza, categorización, slugs, scraping

EJECUCIÓN:
  python scraper/main.py
  (o mediante GitHub Actions en el flujo CI/CD del repositorio)
"""

import sys
import re
import json
import time
import feedparser
import requests
from datetime import datetime
from pathlib import Path

# BASE_DIR apunta a la raíz del repositorio (un nivel por encima de scraper/)
# Usando Path(__file__).resolve() nos aseguramos de que funcione en cualquier
# directorio desde el que se ejecute el script, no solo desde la raíz.
BASE_DIR = Path(__file__).resolve().parent.parent

# Importar las funciones de IA y de utilidades
from brain import summarize_with_groq
from utils import (clean_html, categorize_news, get_relevance_score,
                   generate_unique_slug, scrape_full_article, generate_slug)

# Reconfigurar la salida estándar a UTF-8 para que los emojis y caracteres
# especiales se muestren correctamente en Windows (donde el encoding por
# defecto de la consola puede ser cp1252 en lugar de utf-8).
try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    # Python < 3.7 no tiene reconfigure(); en ese caso ignoramos el error
    pass


# ── CONFIGURACIÓN ────────────────────────────────────────────────

def load_config() -> dict:
    """
    Lee el archivo de configuración config.json y devuelve su contenido.

    POR QUÉ EXISTE:
        Centralizar toda la configuración del scraper en un JSON externo
        permite cambiar feeds, límites o umbrales de relevancia sin tocar
        el código Python, facilitando la personalización y el despliegue.

    CÓMO FUNCIONA:
        1. Construye la ruta absoluta a scraper/config.json usando BASE_DIR.
        2. Si el archivo no existe, emite un warning y devuelve valores por
           defecto razonables para que el scraper pueda funcionar de emergencia.
        3. Si existe, abre el archivo con codificación UTF-8 y parsea el JSON.

    VALORES POR DEFECTO:
        - max_per_feed: 3       → máximo 3 entradas por feed RSS
        - max_per_run: 15       → máximo 15 artículos en total por ejecución
        - min_relevance_score: 3 → score mínimo para aceptar un artículo
        - feeds: [hackaday]     → un feed de ejemplo como fallback

    RETORNA:
        dict: Diccionario con la configuración completa del scraper.
    """
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


# Categorías temáticas del sitio. Deben coincidir exactamente con las
# claves de CATEGORY_KEYWORDS en utils.py y con los nombres de carpeta
# dentro de docs/content/.
CATEGORIES = list(load_config().get("categories", {}).keys())

# Directorio raíz donde se guardan los artículos generados como Markdown
CONTENT_DIR = BASE_DIR / "docs" / "content"

# Archivo de log acumulativo (se añade, nunca se sobreescribe)
LOG_FILE    = BASE_DIR / "run_log.txt"


# ── DIRECTORIOS ──────────────────────────────────────────────────

def ensure_directories():
    """
    Crea las carpetas de cada categoría dentro de docs/content/ si no existen.

    POR QUÉ EXISTE:
        La primera vez que se ejecuta el scraper en un repositorio nuevo, o
        si alguien borra las carpetas manualmente, los archivos .md no podrían
        guardarse. Esta función garantiza que la estructura de directorios existe
        antes de intentar escribir cualquier artículo.

    CÓMO FUNCIONA:
        Itera sobre la lista global CATEGORIES y crea cada subdirectorio con
        mkdir(parents=True, exist_ok=True), que:
        - Crea todos los directorios intermedios necesarios (parents=True).
        - No lanza error si la carpeta ya existe (exist_ok=True).
    """
    for cat in CATEGORIES:
        (CONTENT_DIR / cat).mkdir(parents=True, exist_ok=True)


# ── DEDUPLICACIÓN ────────────────────────────────────────────────

def load_known_slugs() -> set:
    """
    Escanea docs/content/ y extrae los slugs de todos los archivos .md existentes.

    POR QUÉ EXISTE:
        Sin este mecanismo, el scraper podría procesar el mismo artículo cada
        vez que se ejecuta (el feed RSS mantiene los artículos varios días),
        generando duplicados y desperdiciando cuota de la API de Groq.
        Al cargar los slugs al inicio, cada comprobación de duplicado es O(1)
        gracias al uso de un conjunto (set).

    CÓMO FUNCIONA PASO A PASO:
        1. Crea un conjunto vacío.
        2. Usa rglob("*.md") para encontrar recursivamente todos los .md en
           CONTENT_DIR, independientemente de en qué subcarpeta estén.
        3. Para cada archivo, extrae el slug eliminando el prefijo de fecha
           "YYYY-MM-DD-" del nombre (ej: "2024-01-15-que-es-ros2" → "que-es-ros2").
           Esto permite comparar slugs independientemente de la fecha de publicación.
        4. Añade el slug al conjunto.
        5. Devuelve el conjunto completo.

    RETORNA:
        set: Conjunto de slugs ya indexados. Ejemplo: {"que-es-ros2", "llama-3-review"}.
    """
    slugs = set()
    for f in CONTENT_DIR.rglob("*.md"):
        # Quitar el prefijo de fecha "YYYY-MM-DD-" con una regex
        slug = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', f.stem)
        slugs.add(slug)
    return slugs


# ── GUARDADO ─────────────────────────────────────────────────────

def save_news(category: str, result: dict, title_original: str,
              source_url: str, known_slugs: set) -> bool:
    """
    Guarda el resumen generado por la IA como un archivo Markdown estructurado.

    POR QUÉ EXISTE:
        Serializa la respuesta JSON de Groq/LLaMA en un formato Markdown
        estandarizado y legible, que el script build_index.py posterioremnete
        leerá para construir el índice del sitio web estático.

    FORMATO DEL ARCHIVO GENERADO:
        docs/content/<categoría>/YYYY-MM-DD-<slug>.md
        Contiene: título en español, fecha, categoría, tags, introducción,
        descripción técnica, relevancia, consejo y opcionalmente un bloque
        de código bash si la IA generó un comando.

    CÓMO FUNCIONA PASO A PASO:
        1. Comprueba que el resultado de la IA tiene al menos el campo "intro";
           si no, devuelve False (artículo sin contenido útil).
        2. Genera la fecha actual como "YYYY-MM-DD".
        3. Usa el título en español de la IA o, si no hay, el título original RSS.
        4. Genera un slug único con generate_unique_slug() para evitar colisiones.
        5. Formatea los tags como "tag1, tag2, tag3".
        6. Si la IA dio un comando bash, lo envuelve en un bloque ```bash.
        7. Construye el contenido Markdown completo con f-string multilínea.
        8. Calcula el nombre de archivo y la ruta completa.
        9. Escribe el archivo en disco con codificación UTF-8.
        10. Registra el nuevo slug en known_slugs para evitar duplicados
            en la misma ejecución (no solo en ejecuciones anteriores).
        11. Imprime el resultado por pantalla y devuelve True.

    PARÁMETROS:
        category       (str): Categoría temática ("ia", "linux", etc.).
        result         (dict): Respuesta JSON de summarize_with_groq().
        title_original (str): Título original del artículo en inglés (RSS).
        source_url     (str): URL de la fuente del artículo.
        known_slugs    (set): Conjunto de slugs ya usados (se MODIFICA in-place).

    RETORNA:
        bool: True si el artículo se guardó correctamente, False si no hay contenido.
    """
    # Paso 1: sin introducción no hay artículo válido
    if not result.get("intro"):
        return False

    # Paso 2: fecha actual para el prefijo del nombre de archivo
    date_str   = datetime.now().strftime("%Y-%m-%d")

    # Paso 3: usar el título en español de la IA; si vacío, mantener el original
    title_es   = result.get("titulo", "").strip() or title_original

    # Paso 4: generar slug único basado en el título en español
    slug       = generate_unique_slug(title_es, known_slugs)

    # Paso 5: convertir la lista de tags en una cadena separada por comas
    tags_str   = ", ".join(result.get("tags", []))

    # Paso 6: bloque de código bash opcional (si la IA generó un comando)
    comando    = result.get("comando", "").strip()
    comando_md = f"\n\n```bash\n{comando}\n```" if comando else ""

    # Paso 7: construir el contenido Markdown completo del artículo
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

    # Paso 8: calcular nombre de archivo y ruta completa
    filename  = f"{date_str}-{slug}.md"
    file_path = CONTENT_DIR / category / filename

    # Paso 9: escribir el archivo en disco
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    # Paso 10: registrar el slug para detectar duplicados en esta misma ejecución
    known_slugs.add(slug)

    # Paso 11: feedback visual en consola
    print(f"  ✅ [{category}] {filename}")
    print(f"     → {title_es[:70]}")
    return True


# ── PROCESADO DE FEEDS ───────────────────────────────────────────

def process_feed(feed_url: str, known_slugs: set, saved_titles: list,
                 max_per_feed: int, max_per_run: int,
                 min_score: int = 3) -> None:
    """
    Descarga y procesa un feed RSS completo, aplicando todo el pipeline.

    POR QUÉ EXISTE:
        Encapsula la lógica de procesamiento de un feed individual para que
        main() pueda iterar limpiamente sobre múltiples feeds sin duplicar
        código. También aísla los errores por feed: si un feed falla, los
        demás siguen procesándose.

    PIPELINE POR ENTRADA DEL FEED:
        1. Deduplicación por slug          → evita reprocesar artículos ya guardados.
        2. Filtro de relevancia (score)    → descarta off-topic SIN llamar a Groq.
        3. Scraping del artículo completo  → más texto = mejor resumen.
        4. Llamada a la IA (Groq/LLaMA)    → genera el resumen en español.
        5. Guardado del Markdown           → escribe el archivo en docs/content/.

    LÓGICA DE LÍMITES:
        - max_per_feed: máximo de entradas a procesar de ESTE feed.
        - max_per_run: máximo global de artículos guardados en toda la ejecución.
          Si se alcanza, la función retorna inmediatamente (también desde dentro).

    CÓMO FUNCIONA PASO A PASO:
        1. Descarga el feed RSS con requests (en lugar de dejar que feedparser
           haga el GET, para poder controlar el User-Agent y el timeout).
        2. Parsea el XML del feed con feedparser.parse().
        3. Si feedparser detecta un error grave y no hay entradas → retorna.
        4. Itera sobre las primeras max_per_feed entradas del feed.
        5. Comprueba el límite diario global antes de cada entrada.
        6. Extrae título y URL de la entrada.
        7. Comprueba si el slug ya existe → si es así, salta la entrada.
        8. Extrae el texto RSS (<content> o <description>) y lo limpia con clean_html().
        9. Llama a get_relevance_score() con título + texto RSS.
           Si score < min_score → descarta la entrada (no gasta cuota de Groq).
        10. Descarga el artículo completo con scrape_full_article().
        11. Prepara el texto para la IA: "Título: ...\n\nContenido: ..."
            Limita el contenido a 2 500 chars para no saturar el contexto.
        12. Llama a summarize_with_groq() y obtiene el dict con el resumen.
        13. Si no hay intro → salta (la IA no generó contenido válido).
        14. Guarda el artículo con save_news() y actualiza contadores.
        15. Al final, imprime cuántos artículos nuevos se obtuvieron de este feed.

    PARÁMETROS:
        feed_url     (str):  URL del feed RSS a procesar.
        known_slugs  (set):  Slugs ya existentes (se modifica in-place al guardar).
        saved_titles (list): Lista acumulativa de títulos guardados en esta ejecución.
        max_per_feed (int):  Límite de entradas a procesar de este feed.
        max_per_run  (int):  Límite global de artículos por ejecución.
        min_score    (int):  Score mínimo de relevancia para aceptar un artículo.

    RETORNA:
        None (los resultados se acumulan en saved_titles y known_slugs).
    """
    print(f"\n📡 {feed_url}")
    try:
        # Paso 1: descargar el XML del feed con User-Agent explícito.
        # Algunos servidores rechazan el User-Agent por defecto de feedparser.
        headers  = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(feed_url, headers=headers, timeout=30)
        response.raise_for_status()

        # Paso 2: parsear el XML con feedparser (formato Atom o RSS)
        feed = feedparser.parse(response.text)

        # Paso 3: si el feed está malformado Y no tiene entradas, abandonamos
        # feed.bozo = True cuando el XML tiene errores de parseo
        if feed.bozo and not feed.entries:
            print(f"  ⚠️  Error de parseo: {feed.bozo_exception}")
            return

        nuevas = 0  # Contador de artículos nuevos en este feed

        # Paso 4: iterar sobre las primeras max_per_feed entradas
        for entry in feed.entries[:max_per_feed]:

            # Paso 5: comprobar el límite global ANTES de procesar cada entrada
            if len(saved_titles) >= max_per_run:
                print(f"  ⏹ Límite diario ({max_per_run}) alcanzado.")
                return

            # Paso 6: extraer metadatos básicos de la entrada RSS
            title_original = entry.get("title", "Sin título").strip()
            source_url     = entry.get("link", "")

            # ── Paso 7: Deduplicación por slug ──
            # Comparamos con el slug del título original ANTES de scrapear.
            # Si ya existe un archivo con ese slug, saltamos sin descargar nada.
            if generate_slug(title_original) in known_slugs:
                print(f"  ↩ Ya existe: {title_original[:65]}")
                continue

            # ── Paso 8: Contenido RSS como texto de fallback ──
            # Los feeds RSS pueden incluir el HTML completo del artículo
            # en el campo <content> (Atom) o bien un extracto en <description>.
            rss_content = ""
            if hasattr(entry, 'content') and entry.content:
                # Formato Atom: campo "content" es una lista de dicts
                rss_content = entry.content[0].get('value', '')
            else:
                # Formato RSS 2.0: campo "description" como string HTML
                rss_content = entry.get("description", "")
            # Limpiar el HTML del RSS para obtener texto plano
            rss_text = clean_html(rss_content)

            # ── Paso 9: Filtro de relevancia ANTES de gastar cuota de Groq ──
            # Usamos el título + texto RSS (no el artículo completo) porque:
            # a) Es más rápido (ya lo tenemos, no hay que hacer HTTP)
            # b) Si el artículo es irrelevante, no vale la pena scrapear
            score, category = get_relevance_score(title_original, rss_text)
            if score < min_score:
                print(f"  ⏭ Irrelevante (score={score}): {title_original[:65]}")
                continue

            # ── Paso 10: Scraping del artículo completo ──
            # Solo llegamos aquí si el artículo pasó el filtro de relevancia.
            # scrape_full_article devuelve rss_text como fallback si falla.
            print(f"  🌐 Descargando artículo...")
            full_text      = scrape_full_article(source_url, fallback_text=rss_text)
            # Indicador de calidad: ¿conseguimos más texto que el RSS?
            source_quality = "completo" if len(full_text) > len(rss_text) + 200 else "RSS"
            print(f"  📄 {len(full_text)} chars ({source_quality}) | score={score} | {category}")

            # Paso 11: preparar el prompt para la IA (título + primeros 2500 chars)
            # El límite de 2500 chars deja margen para las instrucciones del
            # system prompt de brain.py dentro de la ventana de contexto del modelo.
            text_for_ai = f"Título: {title_original}\n\nContenido: {full_text[:2500]}"

            # ── Paso 12: Llamada a la IA ──
            print(f"  🤖 {title_original[:65]}...")
            result = summarize_with_groq(text_for_ai)

            # Paso 13: verificar que la IA generó contenido útil
            if not result.get("intro"):
                print(f"  ✗ Sin contenido generado, omitiendo.")
                continue

            # Paso 14: guardar el artículo y actualizar contadores
            if save_news(category, result, title_original, source_url, known_slugs):
                saved_titles.append(title_original)
                nuevas += 1

        # Paso 15: resumen del feed procesado
        print(f"  → {nuevas} nuevas de este feed.")

    except Exception as e:
        # Si falla la descarga del feed o cualquier paso crítico, logueamos
        # el error pero continuamos con el siguiente feed
        print(f"  ✗ Error procesando feed: {e}")


# ── LOGGING ──────────────────────────────────────────────────────

def write_log(saved_titles: list, errors: list):
    """
    Añade una entrada al archivo de log acumulativo run_log.txt.

    POR QUÉ EXISTE:
        Permite rastrear el historial de ejecuciones del scraper: cuántos
        artículos se guardaron, cuáles fueron y si hubo errores. Es útil para
        depuración y para auditar el comportamiento del scraper a lo largo del tiempo.
        El log es ACUMULATIVO (modo "a"), nunca se sobreescribe.

    CÓMO FUNCIONA:
        1. Obtiene el timestamp actual en formato "YYYY-MM-DD HH:MM:SS".
        2. Construye una cadena con la línea de resumen y los títulos guardados.
        3. Añade cualquier error registrado durante la ejecución.
        4. Abre LOG_FILE en modo "append" y escribe la cadena.

    FORMATO EN EL ARCHIVO:
        [2024-01-15 10:32:00] Nuevos: 3
          + Título del artículo 1
          + Título del artículo 2
          ✗ Feed https://...: Connection timeout

    PARÁMETROS:
        saved_titles (list): Lista de títulos de artículos guardados exitosamente.
        errors       (list): Lista de mensajes de error ocurridos durante la ejecución.
    """
    # Paso 1: timestamp de la ejecución actual
    now  = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Paso 2: construir la línea de log con todos los títulos guardados
    line = f"\n[{now}] Nuevos: {len(saved_titles)}"
    for t in saved_titles:
        line += f"\n  + {t[:80]}"  # Truncar títulos muy largos para legibilidad

    # Paso 3: añadir errores si los hubo
    for e in errors:
        line += f"\n  ✗ {e}"
    line += "\n"

    # Paso 4: añadir al final del archivo (modo "a" = append)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line)


# ── MAIN ─────────────────────────────────────────────────────────

def main():
    """
    Función principal: orquesta toda la ejecución del scraper.

    POR QUÉ EXISTE:
        Es el punto de entrada del script. Coordina la carga de configuración,
        la inicialización del estado, el procesamiento de cada feed y el
        registro final de resultados.

    CÓMO FUNCIONA PASO A PASO:
        1. Carga la configuración desde config.json con load_config().
        2. Extrae los parámetros necesarios: lista de feeds, límites y score mínimo.
        3. Imprime la cabecera informativa con los parámetros de esta ejecución.
        4. Crea los directorios de categorías si no existen (ensure_directories).
        5. Carga el conjunto de slugs ya indexados (load_known_slugs).
        6. Inicializa las listas de resultados: saved_titles y errors.
        7. Itera sobre cada feed de la configuración:
              a. Comprueba el límite global antes de procesar el feed.
              b. Llama a process_feed() capturando posibles excepciones.
              c. Registra errores globales en la lista errors.
        8. Escribe el log de la ejecución con write_log().
        9. Imprime el resumen final con el número de artículos guardados.
    """
    # Paso 1 y 2: cargar configuración y extraer parámetros
    config       = load_config()
    feeds        = config.get("feeds", [])
    max_per_feed = config.get("max_per_feed", 3)
    max_per_run  = config.get("max_per_run", 15)
    min_score    = config.get("min_relevance_score", 3)

    # Paso 3: cabecera informativa → visible en los logs de GitHub Actions
    print("🚀 TechPulse ES — Captura de noticias")
    print(f"   Feeds: {len(feeds)} | Máx/feed: {max_per_feed} | "
          f"Máx/ejecución: {max_per_run} | Score mínimo: {min_score}")
    print("=" * 60)

    # Paso 4: asegurar que existen las carpetas de destino
    ensure_directories()

    # Paso 5: cargar slugs conocidos para la deduplicación
    known_slugs  = load_known_slugs()

    # Paso 6: inicializar acumuladores de resultados
    saved_titles = []  # Títulos de artículos guardados en esta ejecución
    errors       = []  # Mensajes de error para el log

    print(f"📂 {len(known_slugs)} artículos ya indexados\n")

    # Paso 7: procesar cada feed de la lista
    for url in feeds:
        # Comprobar límite global antes de iniciar cada feed
        if len(saved_titles) >= max_per_run:
            print("\n⏹ Límite diario alcanzado.")
            break
        try:
            process_feed(url, known_slugs, saved_titles,
                        max_per_feed, max_per_run, min_score)
        except Exception as e:
            # Error no capturado dentro de process_feed → registrar y continuar
            msg = f"Feed {url}: {e}"
            errors.append(msg)
            print(f"  ✗ {msg}")

    # Paso 8: escribir el log de esta ejecución
    write_log(saved_titles, errors)

    # Paso 9: resumen final
    print(f"\n{'='*60}")
    print(f"✅ Completado — {len(saved_titles)} artículos nuevos")
    if errors:
        print(f"⚠️  {len(errors)} errores (ver run_log.txt)")


# Punto de entrada del script cuando se ejecuta directamente.
# El bloque if __name__ == "__main__" evita que main() se ejecute
# si este módulo es importado por otro script (por ejemplo, en tests).
if __name__ == "__main__":
    main()
