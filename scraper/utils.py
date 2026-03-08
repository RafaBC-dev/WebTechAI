"""
utils.py — Funciones auxiliares de TechPulse ES
================================================
Este archivo reúne todas las herramientas de soporte que usan distintos
módulos del proyecto. Está separado de main.py para que el código sea
más ordenado, reutilizable y fácil de probar por separado.

Contiene cuatro grupos de funciones:
  1. Limpieza de HTML            → clean_html()
  2. Descarga del artículo completo → scrape_full_article()
  3. Categorización de noticias  → categorize_news()
  4. Generación de slugs         → generate_slug(), generate_unique_slug()
"""

import re           # expresiones regulares: buscar y reemplazar patrones en texto
import unicodedata  # manejo de caracteres Unicode (tildes, ñ, etc.)
import requests     # librería para hacer peticiones HTTP (descargar páginas web)
from bs4 import BeautifulSoup  # librería para leer y navegar HTML


# ══════════════════════════════════════════════════════════════════
# 1. LIMPIEZA DE HTML
# ══════════════════════════════════════════════════════════════════

def clean_html(html_content: str) -> str:
    """
    Convierte HTML en texto plano limpio y legible.

    Por qué existe:
        Los feeds RSS devuelven el contenido con etiquetas HTML (<p>, <div>,
        <script>...). La IA no necesita esas etiquetas, necesita texto plano.
        Esta función hace esa conversión.

    Cómo funciona paso a paso:
        1. Si la cadena está vacía, devuelve "" de inmediato (caso borde).
        2. Parsea el HTML con BeautifulSoup, que lo convierte en un árbol
           navegable de nodos (como un DOM en el navegador).
        3. Elimina etiquetas que no aportan contenido útil al artículo:
           <script>, <style>, <nav>, <footer>, <aside>, <figure>.
           .decompose() las borra completamente del árbol.
        4. Extrae el texto plano con get_text(). El separador '\\n' pone
           salto de línea entre bloques; strip=True recorta espacios.
        5. Normaliza saltos de línea: tres o más seguidos → solo dos.
        6. Normaliza espacios: múltiples espacios → uno solo.

    Args:
        html_content: cadena de texto que puede contener etiquetas HTML

    Returns:
        Texto plano limpio, sin etiquetas HTML
    """
    # Si no hay contenido, devolvemos cadena vacía directamente
    if not html_content:
        return ""

    # Parseamos el HTML — BeautifulSoup lo convierte en un árbol navegable
    soup = BeautifulSoup(html_content, 'html.parser')

    # Eliminamos etiquetas que no aportan contenido útil al artículo.
    # .decompose() las borra completamente del árbol HTML.
    for tag in soup(["script", "style", "nav", "footer", "aside", "figure"]):
        tag.decompose()

    # Extraemos todo el texto del HTML limpio.
    # separator='\n' pone salto de línea entre bloques de texto.
    # strip=True elimina espacios al inicio y final de cada fragmento.
    text = soup.get_text(separator='\n', strip=True)

    # Reducimos 3 o más líneas en blanco seguidas a solo 2.
    # El patrón r'\n{3,}' significa "3 o más saltos de línea seguidos".
    text = re.sub(r'\n{3,}', '\n\n', text)

    # Reducimos múltiples espacios o tabulaciones a un solo espacio.
    text = re.sub(r'[ \t]+', ' ', text)

    return text.strip()


# ══════════════════════════════════════════════════════════════════
# 2. DESCARGA DEL ARTÍCULO COMPLETO
# ══════════════════════════════════════════════════════════════════

# Lista de selectores CSS para encontrar el cuerpo del artículo.
# Los probamos en orden: si el primero no funciona, probamos el siguiente.
# 'article' es el más específico y fiable; 'main' es el último recurso.
CONTENT_SELECTORS = [
    'article',                      # etiqueta HTML semántica para artículos
    '[class*="article-body"]',      # cualquier clase que contenga "article-body"
    '[class*="entry-content"]',     # común en blogs WordPress
    '[class*="post-content"]',      # también común en WordPress
    '[class*="article-content"]',   # variante usada en medios digitales
    '[class*="story-body"]',        # común en periódicos online
    '[class*="content-body"]',      # variante genérica
    'main',                         # elemento HTML principal (último recurso)
]

# Dominios que bloquean scraping o tienen contenido detrás de paywall.
# Con estos no intentamos descargar el artículo — usamos directamente
# el texto del RSS como fallback para no perder tiempo ni recibir errores.
BLOCKED_DOMAINS = [
    'wired.com', 'bloomberg.com', 'ft.com',
    'wsj.com', 'nytimes.com', 'technologyreview.com'
]


def scrape_full_article(url: str, fallback_text: str = "", timeout: int = 15) -> str:
    """
    Intenta descargar el artículo completo desde su URL original.

    Por qué existe:
        Los feeds RSS solo incluyen un resumen corto (150-300 caracteres).
        Cuanto más texto tenga la IA, mejor y más rico será el resumen generado.
        Esta función obtiene el texto completo haciendo una petición HTTP
        directa a la web original del artículo.

    Estrategia de descarga (en orden):
        1. Si el dominio está en la lista negra → devuelve fallback directamente.
        2. Realiza una petición GET simulando un navegador real (User-Agent).
        3. Verifica que la respuesta es HTML (no un PDF, imagen, etc.).
        4. Elimina ruido del HTML: menús, publicidad, comentarios, sidebars…
        5. Recorre CONTENT_SELECTORS buscando el contenedor principal del artículo.
        6. Si ningún selector funciona, recoge todos los párrafos <p> largos.
        7. Si el texto obtenido es menor que el fallback, devuelve el fallback.
        8. Devuelve hasta 3000 caracteres (límite de contexto para la IA).

    Args:
        url:           dirección web del artículo original
        fallback_text: texto del RSS, se usa si el scraping falla o da poco texto
        timeout:       segundos máximos de espera para la petición HTTP

    Returns:
        Texto del artículo (máx. 3000 chars) o fallback_text si el scraping falló
    """
    # Si no hay URL, no podemos hacer nada
    if not url:
        return fallback_text

    # Comprobamos la lista negra — si el dominio está bloqueado, salimos ya
    for domain in BLOCKED_DOMAINS:
        if domain in url:
            return fallback_text

    try:
        # Cabeceras HTTP que simulan un navegador real.
        # Muchas webs bloquean peticiones que no parecen venir de un navegador.
        # User-Agent es como nos "presentamos" al servidor web.
        headers = {
            'User-Agent': (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/120.0.0.0 Safari/537.36'
            ),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
        }

        # Petición HTTP GET (igual que cuando el navegador carga una página).
        # raise_for_status() lanza una excepción si el servidor devuelve 404, 403, etc.
        resp = requests.get(url, headers=headers, timeout=timeout)
        resp.raise_for_status()

        # Verificamos que la respuesta es HTML y no un PDF, imagen, etc.
        # Algunos artículos enlazan directamente a ficheros binarios.
        content_type = resp.headers.get('content-type', '')
        if 'text/html' not in content_type:
            return fallback_text

        # Parseamos el HTML descargado para poder navegarlo
        soup = BeautifulSoup(resp.text, 'html.parser')

        # Eliminamos ruido: publicidad, menús, formularios, redes sociales…
        # Esto mejora la calidad del texto extraído porque evita que mezclemos
        # el contenido del artículo con elementos de la interfaz de la página.
        for tag in soup(['script', 'style', 'nav', 'header', 'footer',
                         'aside', 'form', 'iframe', 'noscript',
                         '[class*="sidebar"]', '[class*="related"]',
                         '[class*="comment"]', '[class*="newsletter"]',
                         '[class*="ad-"]', '[class*="share"]']):
            tag.decompose()

        # Probamos cada selector CSS en orden hasta encontrar contenido válido.
        # El enfoque "cascada de selectores" nos permite adaptarnos a distintos
        # CMS y diseños web sin necesidad de reglas por dominio.
        body_text = ""
        for selector in CONTENT_SELECTORS:
            # select_one() devuelve el PRIMER elemento que coincide con el selector
            container = soup.select_one(selector)
            if container:
                text = container.get_text(separator='\n', strip=True)
                text = re.sub(r'\n{3,}', '\n\n', text)
                # Solo aceptamos el contenedor si tiene suficiente texto (>300 chars)
                # para evitar coger menús o sidebars que están vacíos o son muy cortos
                if len(text) > 300:
                    body_text = text
                    break  # encontramos contenido válido, dejamos de buscar

        if not body_text:
            # Último recurso: recogemos todos los párrafos <p> de la página.
            # Solo los que tienen más de 60 caracteres para descartar
            # elementos cortos como etiquetas, fechas o pies de foto.
            paragraphs = soup.find_all('p')
            body_text = '\n'.join(
                p.get_text(strip=True)
                for p in paragraphs
                if len(p.get_text(strip=True)) > 60
            )

        # Si el scraping obtuvo menos texto que el fallback, usamos el fallback.
        # No tiene sentido devolver menos información de la que ya teníamos en el RSS.
        if not body_text or len(body_text) < len(fallback_text or ""):
            return fallback_text

        # Limitamos a 3000 chars para no saturar la ventana de contexto de la IA.
        # Más texto no mejora el resumen pero sí consume más tokens (y cuota de API).
        return body_text[:3000].strip()

    except Exception:
        # Capturamos CUALQUIER error (timeout, 403 forbidden, SSL, red caída…)
        # y devolvemos el fallback silenciosamente.
        # No queremos que un artículo inaccesible rompa toda la ejecución.
        return fallback_text


# ══════════════════════════════════════════════════════════════════
# 3. CATEGORIZACIÓN DE NOTICIAS
# ══════════════════════════════════════════════════════════════════

# Diccionario que mapea cada categoría con sus palabras clave en inglés.
# Usamos inglés porque las noticias originales de los RSS están en inglés.
# Cuantas más keywords tenga cada categoría, más precisa es la clasificación.
# Las palabras clave se diseñan para ser distintivas y poco ambiguas entre sí.
CATEGORY_KEYWORDS = {
    "ia": [
        "ai", "artificial intelligence", "machine learning", "deep learning",
        "neural network", "llm", "gpt", "gemini", "chatbot", "nlp",
        "computer vision", "inference", "model", "training", "dataset",
        "transformer", "diffusion", "generative", "reinforcement learning"
    ],
    "robotica": [
        "robot", "ros", "ros2", "gazebo", "navigation", "slam",
        "manipulator", "arm", "autonomous", "mobile robot", "drone",
        "actuator", "servo", "kinematics", "path planning", "lidar",
        "behavior tree", "humanoid", "legged"
    ],
    "linux": [
        "linux", "kernel", "ubuntu", "debian", "fedora", "arch",
        "bash", "shell", "systemd", "docker", "container", "podman",
        "terminal", "cli", "open source", "gnu", "distro", "package",
        "wayland", "x11", "driver", "filesystem"
    ],
    "embebidos": [
        "embedded", "microcontroller", "arduino", "esp32", "stm32",
        "fpga", "circuit", "sensor", "pcb", "firmware", "rtos",
        "bare metal", "i2c", "spi", "uart", "gpio", "mcu",
        "raspberry pi", "micropython", "zephyr", "freertos"
    ],
    "diseño-3d": [
        "3d print", "3d printing", "cad", "cnc", "stl", "openscad",
        "fusion 360", "slicer", "filament", "resin", "fdm", "sla",
        "prusa", "bambu", "ender", "gcode", "mesh", "solidworks"
    ]
}


def categorize_news(title: str, content: str) -> str:
    """
    Determina la categoría más probable de una noticia por conteo de keywords.

    Por qué existe:
        Los feeds RSS no siempre vienen organizados por tema. Esta función
        asigna automáticamente cada artículo a una de las 5 categorías del sitio
        analizando el texto, sin depender de metadatos externos.

    Cómo funciona paso a paso:
        1. Concatena título y contenido en un solo texto en minúsculas.
        2. Inicializa un marcador en 0 para cada categoría.
        3. Para cada categoría, recorre sus keywords y suma puntos:
             - Si la keyword aparece en el TÍTULO → +2 puntos
               (el título es la señal más fuerte del tema central)
             - Si aparece solo en el cuerpo → +1 punto
        4. Selecciona la categoría con mayor puntuación total.
        5. Si la puntuación máxima es 0 (ninguna keyword hizo match),
           devuelve "robotica" como categoría por defecto.

    Ejemplo real:
        Título: "New ROS2 Navigation Stack Released"
        → "ros2" en título: +2 puntos a 'robotica'
        → "navigation" en título: +2 puntos a 'robotica'
        → Resultado: 'robotica' con 4 puntos (gana)

    Args:
        title:   título original de la noticia (en inglés)
        content: cuerpo del artículo (en inglés)

    Returns:
        Nombre de la categoría ganadora (ej: "robotica", "linux", "ia"…)
        Si ninguna keyword hace match, devuelve "robotica" como fallback.
    """
    # Combinamos título y contenido en un solo texto en minúsculas para buscar
    text = (title + " " + content).lower()

    # Inicializamos el marcador a 0 para cada categoría
    scores = {cat: 0 for cat in CATEGORY_KEYWORDS}

    # Recorremos cada categoría y sumamos puntos por cada keyword encontrada
    for cat, keywords in CATEGORY_KEYWORDS.items():
        for kw in keywords:
            if kw in text:
                # Keyword en título = 2 puntos porque el título resume el tema principal;
                # solo en el cuerpo = 1 punto porque puede ser una mención secundaria
                scores[cat] += 2 if kw in title.lower() else 1

    # max() con key=scores.get devuelve la categoría con mayor puntuación acumulada
    best = max(scores, key=scores.get)

    # Si el ganador tiene 0 puntos, ninguna keyword hizo match en ninguna categoría.
    # Usamos "robotica" como fallback porque es la categoría más amplia del sitio.
    return best if scores[best] > 0 else "robotica"


# ══════════════════════════════════════════════════════════════════
# 4. GENERACIÓN DE SLUGS
# ══════════════════════════════════════════════════════════════════
# Un "slug" es la versión URL-friendly de un texto.
# Ejemplo: "¿Qué es ROS2?" → "que-es-ros2"
# Se usa para nombrar los archivos .md de cada artículo de forma
# que sean compatibles con cualquier sistema operativo y navegador web.

def _remove_accents(text: str) -> str:
    """
    Elimina tildes y diacríticos de un texto, conservando la letra base.

    Por qué existe:
        Los nombres de archivo y las URLs no deberían tener tildes ni ñ,
        ya que pueden causar problemas de compatibilidad entre sistemas
        Windows/Linux/macOS y en algunos navegadores o servidores web.

    Cómo funciona:
        NFD (Normalization Form Decomposed) descompone cada carácter acentuado
        en su letra base + el acento como carácter separado codificado en Unicode.
        Ejemplo: 'é' se descompone en 'e' + (acento agudo U+0301)
        Luego filtramos los acentos, que tienen categoría Unicode 'Mn'
        (Mark, Nonspacing = marcas que no ocupan espacio tipográfico propio).

    Args:
        text: texto con posibles acentos (ej: "robótica", "diseño")

    Returns:
        Texto sin acentos (ej: "robotica", "diseno")
    """
    return ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'  # descartamos las marcas de acento (Nonspacing Mark)
    )


def generate_slug(text: str, max_length: int = 55) -> str:
    """
    Convierte cualquier texto en un slug válido para URLs y nombres de archivo.

    Por qué existe:
        Los títulos de los artículos contienen caracteres especiales, tildes,
        mayúsculas y espacios que no son válidos en nombres de archivo o URLs.
        Esta función produce una versión "limpia" usable directamente.

    Transformación completa (ejemplo):
        "¿Qué es ROS2 Navigation?" → "que-es-ros2-navigation"

    Pasos que aplica en orden:
        1. Convierte todo a minúsculas
        2. Elimina acentos con _remove_accents()
        3. Elimina caracteres especiales (¿, !, @, #, etc.)
           Solo conserva letras, números, espacios y guiones
        4. Convierte espacios y guiones bajos en guiones normales
        5. Elimina guiones duplicados consecutivos
        6. Elimina guiones al inicio y al final del resultado
        7. Recorta a max_length caracteres

    Args:
        text:       texto a convertir (normalmente el título en español)
        max_length: longitud máxima del slug resultante (55 chars por defecto)

    Returns:
        Slug URL-friendly (ej: "nueva-version-ubuntu-con-kernel-6-8")
    """
    slug = text.lower()
    slug = _remove_accents(slug)
    # \w en Python equivale a [a-zA-Z0-9_]; eliminamos todo lo demás salvo espacios y guiones
    slug = re.sub(r'[^\w\s-]', '', slug)
    # Convertimos espacios y guiones bajos en guiones normales (estándar web)
    slug = re.sub(r'[\s_]+', '-', slug)
    # Colapsamos guiones múltiples consecutivos en uno solo
    slug = re.sub(r'-+', '-', slug)
    # Eliminamos guiones al inicio y al final del slug
    slug = slug.strip('-')
    return slug[:max_length]


def generate_unique_slug(text: str, known_slugs: set, max_length: int = 55) -> str:
    """
    Genera un slug garantizando que no colisione con slugs ya existentes.

    Por qué existe:
        Si dos artículos tienen títulos muy parecidos pueden generar el mismo slug,
        y el segundo archivo sobreescribiría al primero en el sistema de archivos.
        Esta función evita ese problema añadiendo un sufijo numérico cuando hay
        colisión, de forma similar a como Windows nombra "archivo (2).txt".

    Cómo funciona:
        1. Genera el slug base con generate_slug().
        2. Comprueba si ese slug ya existe en known_slugs.
        3. Si hay colisión, añade "-2" al slug y vuelve a comprobar.
        4. Incrementa el contador hasta encontrar un slug libre.
        5. Recorta el base para que base+sufijo no supere max_length.

    Ejemplo de colisiones resueltas:
        Artículo 1: "Python 3.12 Released" → "python-3-12-released"    ✓
        Artículo 2: "Python 3.12 Released" → "python-3-12-released-2"  ✓
        Artículo 3: "Python 3.12 Released" → "python-3-12-released-3"  ✓

    Args:
        text:         texto del que generar el slug (normalmente el título del artículo)
        known_slugs:  set() con todos los slugs ya usados en esta ejecución
        max_length:   longitud máxima del slug resultante

    Returns:
        Slug único que NO existe en known_slugs; el caller debe añadirlo al set.
    """
    # Generamos el slug base a partir del texto recibido
    base = generate_slug(text, max_length)
    slug = base
    counter = 2  # empezamos en 2 para que el sufijo sea "-2", "-3", etc.

    # Seguimos incrementando hasta encontrar un slug no ocupado
    while slug in known_slugs:
        suffix = f"-{counter}"
        # Recortamos el base para que base+sufijo no supere max_length en total
        slug = base[:max_length - len(suffix)] + suffix
        counter += 1

    return slug