"""
utils.py — Funciones auxiliares de TechPulse ES
================================================
Contiene cuatro grupos de funciones:
  1. Limpieza de HTML            → clean_html()
  2. Descarga del artículo completo → scrape_full_article()
  3. Categorización de noticias  → categorize_news(), get_relevance_score()
  4. Generación de slugs         → generate_slug(), generate_unique_slug()

Este módulo actúa como caja de herramientas del scraper; todas las funciones
son puras o casi-puras (sin efectos secundarios persistentes) para que sean
fáciles de probar y reutilizar.
"""

import re
import unicodedata
import requests
import time
from functools import wraps
from bs4 import BeautifulSoup


# ══════════════════════════════════════════════════════════════════
# 1. LIMPIEZA DE HTML
# ══════════════════════════════════════════════════════════════════

def clean_html(html_content: str) -> str:
    """
    Convierte una cadena de HTML en texto plano limpio y legible.

    POR QUÉ EXISTE:
        Los feeds RSS suelen incluir HTML en su campo <description> o <content>.
        Antes de pasar el texto a la IA o al sistema de relevancia, necesitamos
        texto sin etiquetas, sin scripts y sin whitespace excesivo.

    CÓMO FUNCIONA PASO A PASO:
        1. Si la cadena está vacía, devuelve "" inmediatamente (cortocircuito).
        2. Parsea el HTML con BeautifulSoup usando el parser nativo de Python.
        3. Elimina por completo las etiquetas ruidosas:
              <script>  → código JavaScript ejecutable (sin valor textual)
              <style>   → reglas CSS
              <nav>     → menú de navegación del sitio
              <footer>  → pie de página con enlaces genéricos
              <aside>   → barras laterales o publicidad
              <figure>  → imágenes / capturas que no aportan texto útil
        4. Extrae el texto plano usando get_text(), separando nodos con saltos
           de línea y eliminando espacios al inicio/fin de cada fragmento.
        5. Colapsa tres o más saltos de línea consecutivos a dos (un párrafo).
        6. Colapsa múltiples espacios/tabulaciones en uno solo.
        7. Devuelve el texto sin espacios en los extremos.

    PARÁMETROS:
        html_content (str): Cadena que puede contener HTML arbitrario.

    RETORNA:
        str: Texto plano limpio, listo para procesar.
    """
    # Cortocircuito: evita parsear una cadena vacía o None
    if not html_content:
        return ""

    # Parsear el HTML. 'html.parser' es el parser de la librería estándar
    # de Python; no requiere dependencias externas como lxml.
    soup = BeautifulSoup(html_content, 'html.parser')

    # Eliminar las etiquetas que solo añaden ruido al texto extraído.
    # .decompose() elimina el nodo y todo su contenido del árbol DOM.
    for tag in soup(["script", "style", "nav", "footer", "aside", "figure"]):
        tag.decompose()

    # Extraer texto plano; separator='\n' inserta un salto de línea
    # entre bloques de texto adyacentes (p, div, li, etc.).
    text = soup.get_text(separator='\n', strip=True)

    # Normalizar el número de saltos de línea (máximo dos = un párrafo vacío)
    text = re.sub(r'\n{3,}', '\n\n', text)

    # Normalizar espacios horizontales: reemplazar múltiples espacios/tabs por uno
    text = re.sub(r'[ \t]+', ' ', text)

    return text.strip()


# ══════════════════════════════════════════════════════════════════
# 2. DESCARGA DEL ARTÍCULO COMPLETO
# ══════════════════════════════════════════════════════════════════

# Lista de selectores CSS que apuntan al bloque principal de contenido
# en la mayoría de CMS (WordPress, Ghost, Medium, etc.).
# Se prueban en orden: el primero que devuelva texto suficiente gana.
CONTENT_SELECTORS = [
    'article',
    '[class*="article-body"]',
    '[class*="entry-content"]',
    '[class*="post-content"]',
    '[class*="article-content"]',
    '[class*="story-body"]',
    '[class*="content-body"]',
    'main',
]

# Dominios que bloquean scrapers o están detrás de paywall.
# En lugar de intentar y fallar, devolvemos directamente el texto RSS.
BLOCKED_DOMAINS = [
    'wired.com', 'bloomberg.com', 'ft.com',
    'wsj.com', 'nytimes.com', 'technologyreview.com'
]


def scrape_full_article(url: str, fallback_text: str = "", timeout: int = 15) -> str:
    """
    Descarga el artículo completo desde su URL original y devuelve su texto.

    POR QUÉ EXISTE:
        Los feeds RSS solo incluyen un extracto corto (200-300 palabras) del
        artículo. Si pasamos únicamente ese extracto a la IA, el resumen queda
        muy pobre. Esta función descarga la página completa para obtener el
        texto íntegro del artículo y mejorar la calidad del resumen generado.

    POLÍTICA DE FALLBACK:
        Si cualquier paso falla (timeout, bloqueo, error HTTP, contenido no HTML,
        texto extraído más corto que el RSS…) la función devuelve fallback_text
        sin lanzar excepciones, garantizando que el flujo principal nunca se rompe.

    LÍMITE DE LONGITUD:
        El texto se recorta a 3 000 caracteres para no saturar la ventana de
        contexto del modelo de IA (Groq/LLaMA). Para artículos técnicos largos,
        3 000 caracteres suelen cubrir la introducción y las secciones clave.

    CÓMO FUNCIONA PASO A PASO:
        1. Si url está vacía → devuelve fallback_text.
        2. Si el dominio está en BLOCKED_DOMAINS → devuelve fallback_text.
        3. Realiza GET con cabeceras de navegador real para evitar bloqueos
           básicos de "User-Agent: python-requests".
        4. Comprueba que la respuesta sea text/html; si es PDF, JSON, etc.
           → devuelve fallback_text.
        5. Parsea el HTML y elimina elementos de UI (scripts, nav, footer…).
        6. Itera CONTENT_SELECTORS buscando el bloque de contenido principal.
           Si alguno devuelve más de 300 chars → lo usa y sale del bucle.
        7. Si ningún selector funcionó, une todos los <p> con más de 60 chars.
        8. Si el texto extraído es más corto que el fallback → devuelve fallback.
        9. Devuelve los primeros 3 000 caracteres del texto.

    PARÁMETROS:
        url           (str): URL del artículo original.
        fallback_text (str): Texto del RSS que se devuelve si algo falla.
        timeout       (int): Segundos máximos para la petición HTTP.

    RETORNA:
        str: Texto del artículo (hasta 3 000 chars) o fallback_text.
    """
    # Paso 1: URL vacía → no hay nada que descargar
    if not url:
        return fallback_text

    # Paso 2: Dominios bloqueados / paywall → no malgastamos tiempo
    for domain in BLOCKED_DOMAINS:
        if domain in url:
            return fallback_text

    try:
        # Paso 3: Cabeceras que imitan a Chrome en Windows para evitar bloqueos
        # básicos basados en User-Agent. Muchos servidores rechazan "python-requests".
        headers = {
            'User-Agent': (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/120.0.0.0 Safari/537.36'
            ),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
        }
        resp = requests.get(url, headers=headers, timeout=timeout)
        # Lanza excepción si el servidor devuelve 4xx o 5xx
        resp.raise_for_status()

        # Paso 4: Verificar que la respuesta es HTML y no otro tipo de recurso
        content_type = resp.headers.get('content-type', '')
        if 'text/html' not in content_type:
            return fallback_text

        # Paso 5: Parsear y limpiar el HTML de elementos de interfaz
        soup = BeautifulSoup(resp.text, 'html.parser')
        for tag in soup(['script', 'style', 'nav', 'header', 'footer',
                         'aside', 'form', 'iframe', 'noscript']):
            tag.decompose()

        # Paso 6: Buscar el contenedor de artículo con los selectores conocidos
        body_text = ""
        for selector in CONTENT_SELECTORS:
            container = soup.select_one(selector)
            if container:
                text = container.get_text(separator='\n', strip=True)
                # Normalizar saltos de línea excesivos
                text = re.sub(r'\n{3,}', '\n\n', text)
                # Solo aceptamos el contenedor si tiene texto sustancial (> 300 chars)
                if len(text) > 300:
                    body_text = text
                    break  # Primer selector válido → salimos

        # Paso 7: Último recurso — unir todos los párrafos <p> con texto real
        if not body_text:
            paragraphs = soup.find_all('p')
            body_text = '\n'.join(
                p.get_text(strip=True) for p in paragraphs
                if len(p.get_text(strip=True)) > 60  # Ignorar párrafos de 1 línea
            )

        # Paso 8: Si el texto raspado es más corto que el RSS, preferimos el RSS
        if not body_text or len(body_text) < len(fallback_text or ""):
            return fallback_text

        # Paso 9: Recortar a 3 000 chars para no saturar el contexto de la IA
        return body_text[:3000].strip()

    except Exception:
        # Cualquier error (timeout, conexión rechazada, etc.) → fallback silencioso
        return fallback_text


# ══════════════════════════════════════════════════════════════════
# 3. CATEGORIZACIÓN Y RELEVANCIA
# ══════════════════════════════════════════════════════════════════

# Diccionario de palabras clave por categoría temática del sitio.
# La clave es el slug de la categoría (coincide con el nombre de la carpeta
# en docs/content/); el valor es la lista de términos técnicos asociados.
# Las keywords se comparan en minúsculas contra el texto completo del artículo.
CATEGORY_KEYWORDS = {
    "ia": [
        "ai", "artificial intelligence", "machine learning", "deep learning",
        "neural network", "llm", "gpt", "gemini", "chatbot", "nlp",
        "computer vision", "inference", "model", "training", "dataset",
        "transformer", "diffusion", "generative", "reinforcement learning",
        "agent", "rag", "fine-tuning", "embedding", "ollama", "hugging face",
        "benchmark", "claude", "mistral", "llama", "openai", "stable diffusion"
    ],
    "robotica": [
        "robot", "ros", "ros2", "gazebo", "navigation", "slam",
        "manipulator", "arm", "autonomous", "mobile robot", "drone",
        "actuator", "servo", "kinematics", "path planning", "lidar",
        "behavior tree", "humanoid", "legged", "quadruped"
    ],
    "linux": [
        "linux", "kernel", "ubuntu", "debian", "fedora", "arch",
        "bash", "shell", "systemd", "docker", "container", "podman",
        "terminal", "cli", "open source", "gnu", "distro", "package",
        "wayland", "x11", "driver", "filesystem", "python", "programming",
        "developer", "software", "open-source", "git", "devops"
    ],
    "embebidos": [
        "embedded", "microcontroller", "arduino", "esp32", "stm32",
        "fpga", "circuit", "sensor", "pcb", "firmware", "rtos",
        "bare metal", "i2c", "spi", "uart", "gpio", "mcu",
        "raspberry pi", "micropython", "zephyr", "freertos",
        "esp8266", "pico", "teensy", "attiny", "iot", "internet of things",
        "maker", "diy electronics", "breadboard", "soldering"
    ],
    "diseño-3d": [
        "3d print", "3d printing", "cad", "cnc", "stl", "openscad",
        "fusion 360", "slicer", "filament", "resin", "fdm", "sla",
        "prusa", "bambu", "ender", "gcode", "mesh", "solidworks"
    ]
}

# Keywords que indican que el artículo es claramente irrelevante
# para un sitio de tecnología/programación/makers.
# Se comprueban SOLO en el título (no en el cuerpo) para minimizar
# falsos positivos: un artículo técnico puede mencionar "política" de
# forma secundaria, pero raramente tendrá esa palabra en el título.
IRRELEVANT_KEYWORDS = [
    "dinosaur", "fossil", "paleontology", "celebrity", "sports",
    "football", "movie", "film", "music", "fashion", "cooking",
    "recipe", "travel", "tourism", "politics", "election",
    "stock market", "finance", "crypto", "nft", "covid",
    "health", "medical", "surgery", "climate", "weather"
]


def get_relevance_score(title: str, content: str) -> tuple[int, str]:
    """
    Calcula la puntuación de relevancia de un artículo y determina su categoría.

    POR QUÉ EXISTE:
        Los feeds RSS recogen muchas noticias de tecnología en sentido amplio
        (finanzas, política tech, entretenimiento...) que no encajan en el
        enfoque de TechPulse ES. Esta función actúa como portero: solo deja
        pasar los artículos con contenido técnico claro y los clasifica en
        la categoría más apropiada, sin necesitar la IA ni coste adicional.

    SISTEMA DE PUNTUACIÓN:
        - Cada keyword encontrada en el cuerpo del texto suma 1 punto.
        - Cada keyword encontrada en el TÍTULO suma 2 puntos (el doble),
          porque el título es la señal más fuerte de la temática del artículo.
        - Si el título contiene alguna keyword irrelevante → score 0 directo.
        - Si ninguna categoría supera 0 puntos → score 0.
        - Un score < 3 en main.py provoca que el artículo sea descartado.

    CÓMO FUNCIONA PASO A PASO:
        1. Concatenar título + contenido en minúsculas (texto completo).
        2. Convertir el título a minúsculas por separado (para comparación rápida).
        3. Recorrer IRRELEVANT_KEYWORDS: si alguna aparece en el título → (0, "irrelevante").
        4. Inicializar un dict de puntuaciones {categoría: 0} para cada categoría.
        5. Para cada categoría y cada keyword:
              - Si la keyword está en el texto completo, sumar al score de esa categoría.
              - Si encima está en el título, sumar 1 extra (total +2 vs +1).
        6. Identificar la categoría con mayor puntuación (best_cat).
        7. Si best_score == 0 → ninguna categoría reconoce el artículo → (0, "irrelevante").
        8. Devolver (best_score, best_cat).

    PARÁMETROS:
        title   (str): Título original del artículo (puede ser en inglés).
        content (str): Texto del artículo o extracto RSS ya limpio (clean_html).

    RETORNA:
        tuple[int, str]: (puntuación, nombre_de_categoría).
                         Ejemplo: (7, "ia") o (0, "irrelevante").
    """
    # Paso 1: texto completo en minúsculas para búsquedas case-insensitive
    text  = (title + " " + content).lower()
    # Paso 2: título en minúsculas (lo usaremos para el bono de puntuación)
    title_lower = title.lower()

    # Paso 3: filtro rápido de irrelevancia basado en el título
    # Si el título menciona dinosaurios, deportes, cine, etc. → descartamos directamente
    for kw in IRRELEVANT_KEYWORDS:
        if kw in title_lower:
            return 0, "irrelevante"

    # Paso 4: inicializar puntuaciones a cero para cada categoría
    scores = {cat: 0 for cat in CATEGORY_KEYWORDS}

    # Paso 5: calcular puntuación por categoría
    for cat, keywords in CATEGORY_KEYWORDS.items():
        for kw in keywords:
            if kw in text:
                # Keyword en título vale el doble que en el cuerpo
                scores[cat] += 2 if kw in title_lower else 1

    # Paso 6: encontrar la categoría ganadora (mayor puntuación)
    best_cat   = max(scores, key=scores.get)
    best_score = scores[best_cat]

    # Paso 7: si ninguna categoría tiene puntuación, el artículo es irrelevante
    if best_score == 0:
        return 0, "irrelevante"

    # Paso 8: devolver la puntuación y la categoría ganadora
    return best_score, best_cat


def categorize_news(title: str, content: str) -> str:
    """
    Devuelve únicamente la categoría de un artículo como cadena de texto.

    POR QUÉ EXISTE:
        Es un wrapper de conveniencia sobre get_relevance_score() que descarta
        la puntuación numérica. Mantiene compatibilidad retroactiva con llamadas
        en main.py y otros módulos que solo necesitan saber la categoría, no el
        score exacto.

    CÓMO FUNCIONA:
        Llama a get_relevance_score() y desempaqueta solo el segundo elemento
        de la tupla usando la sintaxis de "ignorar con _".

    PARÁMETROS:
        title   (str): Título del artículo.
        content (str): Cuerpo del artículo o extracto RSS.

    RETORNA:
        str: Nombre de la categoría (p.ej. "ia", "linux") o "irrelevante".
    """
    # Desempaquetamos la tupla: ignoramos la puntuación (_) y usamos la categoría
    _, category = get_relevance_score(title, content)
    return category


# ══════════════════════════════════════════════════════════════════
# 4. GENERACIÓN DE SLUGS
# ══════════════════════════════════════════════════════════════════

def _remove_accents(text: str) -> str:
    """
    Elimina tildes y diacríticos de una cadena conservando la letra base.

    POR QUÉ EXISTE:
        Los slugs de URL deben contener solo caracteres ASCII estándar.
        "Comunicación" → "comunicacion", "über" → "uber", etc.
        Es una función privada (prefijo _) auxiliar de generate_slug().

    CÓMO FUNCIONA:
        1. Descompone el texto en forma NFD (Normalization Form D):
           cada carácter con tilde se separa en letra base + marca diacrítica.
           Ejemplo: 'é' → 'e' + '́' (combining acute accent, Unicode U+0301).
        2. Filtra los caracteres cuya categoría Unicode sea 'Mn'
           (Mark, Nonspacing), que son precisamente los diacríticos.
        3. Recompone la cadena resultante sin tildes.

    PARÁMETROS:
        text (str): Cadena de texto con posibles caracteres acentuados.

    RETORNA:
        str: La misma cadena sin diacríticos.
    """
    return ''.join(
        # 'Mn' = Mark, Nonspacing (tilde, diéresis, cedilla, etc.)
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    )


def generate_slug(text: str, max_length: int = 55) -> str:
    """
    Convierte un texto arbitrario en un slug apto para URLs.

    POR QUÉ EXISTE:
        Los nombres de archivo de los artículos y los identificadores únicos
        del sistema usan slugs (cadenas cortas, solo ASCII, sin espacios) para
        garantizar compatibilidad con todos los sistemas de archivos y servidores
        web sin necesidad de codificación porcentual en las URLs.

    CÓMO FUNCIONA PASO A PASO:
        1. Convertir a minúsculas: "Machine Learning" → "machine learning".
        2. Quitar tildes con _remove_accents(): "IA española" → "ia espanola".
        3. Eliminar cualquier carácter que no sea letra, dígito, espacio o guión:
           signos de puntuación, emojis, comillas, etc.
        4. Reemplazar espacios y guiones bajos por guiones: "ia espanola" → "ia-espanola".
        5. Colapsar guiones consecutivos en uno solo: "ia--espanola" → "ia-espanola".
        6. Recortar guiones al inicio y al final del slug.
        7. Truncar al máximo de caracteres indicado (por defecto 55).

    PARÁMETROS:
        text       (str): Texto original (normalmente el título del artículo).
        max_length (int): Longitud máxima del slug resultante (default: 55).

    RETORNA:
        str: Slug URL-friendly. Ejemplo: "que-es-el-machine-learning-en-2024".
    """
    # Paso 1: minúsculas
    slug = text.lower()
    # Paso 2: quitar acentos y diacríticos
    slug = _remove_accents(slug)
    # Paso 3: eliminar caracteres no permitidos en slugs
    slug = re.sub(r'[^\w\s-]', '', slug)
    # Paso 4: espacios y guiones bajos → guión
    slug = re.sub(r'[\s_]+', '-', slug)
    # Paso 5: múltiples guiones → uno solo
    slug = re.sub(r'-+', '-', slug)
    # Paso 6: eliminar guiones al inicio y al final
    slug = slug.strip('-')
    # Paso 7: truncar a la longitud máxima
    return slug[:max_length]


def generate_unique_slug(text: str, known_slugs: set, max_length: int = 55) -> str:
    """
    Genera un slug único que no colisione con los slugs ya existentes.

    POR QUÉ EXISTE:
        Si dos artículos tienen títulos muy similares, generate_slug() podría
        producir el mismo slug para ambos, provocando que el segundo sobrescriba
        al primero en el sistema de archivos. Esta función añade un sufijo
        numérico incremental para garantizar la unicidad.

    CÓMO FUNCIONA PASO A PASO:
        1. Genera el slug base a partir del texto con generate_slug().
        2. Inicializa slug = base y counter = 2.
        3. Entra en un bucle: mientras slug ya exista en known_slugs…
              a. Calcula el sufijo: "-2", "-3", "-4", etc.
              b. Trunca el slug base para que base + sufijo no supere max_length.
              c. Incrementa counter.
        4. Cuando encuentra un slug libre, lo devuelve.
        5. El conjunto known_slugs se actualiza FUERA de esta función (en save_news)
           para que los slugs generados en la misma ejecución también se registren.

    EJEMPLO:
        known_slugs = {"articulo-sobre-ros2"}
        generate_unique_slug("Artículo sobre ROS2", known_slugs)
        # → "articulo-sobre-ros2-2"  (porque "articulo-sobre-ros2" ya existe)

    PARÁMETROS:
        text        (str): Texto original del que derivar el slug.
        known_slugs (set): Conjunto de slugs ya registrados (se consulta en O(1)).
        max_length  (int): Longitud máxima del slug resultante (default: 55).

    RETORNA:
        str: Slug único garantizado que no está en known_slugs.
    """
    # Paso 1: generar el slug candidato sin sufijo
    base    = generate_slug(text, max_length)
    slug    = base
    counter = 2  # El primer duplicado será "-2", luego "-3", etc.

    # Paso 3: bucle hasta encontrar un slug libre
    while slug in known_slugs:
        suffix = f"-{counter}"
        # Recortar el base para dejar espacio al sufijo sin exceder max_length
        slug   = base[:max_length - len(suffix)] + suffix
        counter += 1

    # Paso 4: devolver el slug único encontrado
    return slug

def with_retries(max_retries=3, delay=15, exceptions=(Exception,)):
    """
    Decorador genérico para reintentar una función si lanza excepciones.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for intento in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if intento == max_retries - 1:
                        raise e # Si es el último intento, lanza el error real
                    print(f"⚠️ Error en {func.__name__} (Intento {intento+1}/{max_retries}). Reintentando en {delay}s...")
                    time.sleep(delay)
        return wrapper
    return decorator
