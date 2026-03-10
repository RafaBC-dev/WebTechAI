"""
utils.py — Funciones auxiliares de TechPulse ES
================================================
Contiene cuatro grupos de funciones:
  1. Limpieza de HTML            → clean_html()
  2. Descarga del artículo completo → scrape_full_article()
  3. Categorización de noticias  → categorize_news(), get_relevance_score()
  4. Generación de slugs         → generate_slug(), generate_unique_slug()
"""

import re
import unicodedata
import requests
from bs4 import BeautifulSoup


# ══════════════════════════════════════════════════════════════════
# 1. LIMPIEZA DE HTML
# ══════════════════════════════════════════════════════════════════

def clean_html(html_content: str) -> str:
    """Convierte HTML en texto plano limpio eliminando etiquetas y ruido."""
    if not html_content:
        return ""
    soup = BeautifulSoup(html_content, 'html.parser')
    for tag in soup(["script", "style", "nav", "footer", "aside", "figure"]):
        tag.decompose()
    text = soup.get_text(separator='\n', strip=True)
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()


# ══════════════════════════════════════════════════════════════════
# 2. DESCARGA DEL ARTÍCULO COMPLETO
# ══════════════════════════════════════════════════════════════════

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

BLOCKED_DOMAINS = [
    'wired.com', 'bloomberg.com', 'ft.com',
    'wsj.com', 'nytimes.com', 'technologyreview.com'
]


def scrape_full_article(url: str, fallback_text: str = "", timeout: int = 15) -> str:
    """
    Descarga el artículo completo desde su URL original.
    Si falla por cualquier motivo devuelve fallback_text del RSS.
    Limita el texto a 3000 chars para no saturar el contexto de la IA.
    """
    if not url:
        return fallback_text
    for domain in BLOCKED_DOMAINS:
        if domain in url:
            return fallback_text
    try:
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
        resp.raise_for_status()
        content_type = resp.headers.get('content-type', '')
        if 'text/html' not in content_type:
            return fallback_text
        soup = BeautifulSoup(resp.text, 'html.parser')
        for tag in soup(['script', 'style', 'nav', 'header', 'footer',
                         'aside', 'form', 'iframe', 'noscript']):
            tag.decompose()
        body_text = ""
        for selector in CONTENT_SELECTORS:
            container = soup.select_one(selector)
            if container:
                text = container.get_text(separator='\n', strip=True)
                text = re.sub(r'\n{3,}', '\n\n', text)
                if len(text) > 300:
                    body_text = text
                    break
        if not body_text:
            paragraphs = soup.find_all('p')
            body_text = '\n'.join(
                p.get_text(strip=True) for p in paragraphs
                if len(p.get_text(strip=True)) > 60
            )
        if not body_text or len(body_text) < len(fallback_text or ""):
            return fallback_text
        return body_text[:3000].strip()
    except Exception:
        return fallback_text


# ══════════════════════════════════════════════════════════════════
# 3. CATEGORIZACIÓN Y RELEVANCIA
# ══════════════════════════════════════════════════════════════════

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
# para un sitio de tecnología/programación/makers
IRRELEVANT_KEYWORDS = [
    "dinosaur", "fossil", "paleontology", "celebrity", "sports",
    "football", "movie", "film", "music", "fashion", "cooking",
    "recipe", "travel", "tourism", "politics", "election",
    "stock market", "finance", "crypto", "nft", "covid",
    "health", "medical", "surgery", "climate", "weather"
]


def get_relevance_score(title: str, content: str) -> tuple[int, str]:
    """
    Calcula la puntuación de relevancia de un artículo y su categoría.

    Devuelve una tupla (score, categoria) donde:
    - score = 0 si contiene keywords irrelevantes
    - score = puntuación total de keywords técnicas encontradas
    - categoria = la categoría con mayor puntuación

    Un score bajo (< 3) indica que el artículo no es relevante
    para el sitio y debe descartarse.
    """
    text  = (title + " " + content).lower()
    title_lower = title.lower()

    # Primero comprobamos si hay keywords claramente irrelevantes en el título
    # Si el título menciona dinosaurios, deportes, etc. → descartamos directamente
    for kw in IRRELEVANT_KEYWORDS:
        if kw in title_lower:
            return 0, "irrelevante"

    # Calculamos puntuación por categoría
    scores = {cat: 0 for cat in CATEGORY_KEYWORDS}
    for cat, keywords in CATEGORY_KEYWORDS.items():
        for kw in keywords:
            if kw in text:
                # Keyword en título vale el doble que en el cuerpo
                scores[cat] += 2 if kw in title_lower else 1

    best_cat   = max(scores, key=scores.get)
    best_score = scores[best_cat]

    # Si ninguna categoría supera el mínimo, el artículo es irrelevante
    if best_score == 0:
        return 0, "irrelevante"

    return best_score, best_cat


def categorize_news(title: str, content: str) -> str:
    """
    Devuelve solo la categoría. Wrapper de get_relevance_score()
    para mantener compatibilidad con el código existente en main.py.
    """
    _, category = get_relevance_score(title, content)
    return category


# ══════════════════════════════════════════════════════════════════
# 4. GENERACIÓN DE SLUGS
# ══════════════════════════════════════════════════════════════════

def _remove_accents(text: str) -> str:
    """Elimina tildes y diacríticos conservando la letra base."""
    return ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    )


def generate_slug(text: str, max_length: int = 55) -> str:
    """Convierte un texto en slug URL-friendly."""
    slug = text.lower()
    slug = _remove_accents(slug)
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[\s_]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    slug = slug.strip('-')
    return slug[:max_length]


def generate_unique_slug(text: str, known_slugs: set, max_length: int = 55) -> str:
    """
    Genera un slug único añadiendo sufijo numérico si ya existe.
    Ejemplo: "articulo" → "articulo-2" → "articulo-3"...
    """
    base    = generate_slug(text, max_length)
    slug    = base
    counter = 2
    while slug in known_slugs:
        suffix = f"-{counter}"
        slug   = base[:max_length - len(suffix)] + suffix
        counter += 1
    return slug
