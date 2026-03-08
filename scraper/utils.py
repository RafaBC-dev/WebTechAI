"""
Funciones auxiliares para TechPulse ES.
"""

import re
import unicodedata
import requests
from bs4 import BeautifulSoup


# ── HTML CLEANING ────────────────────────────────────────────────

def clean_html(html_content: str) -> str:
    """Extrae texto plano limpio de HTML."""
    if not html_content:
        return ""
    soup = BeautifulSoup(html_content, 'html.parser')
    for tag in soup(["script", "style", "nav", "footer", "aside", "figure"]):
        tag.decompose()
    text = soup.get_text(separator='\n', strip=True)
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()


# ── FULL ARTICLE SCRAPING ────────────────────────────────────────

# Selectores CSS para extraer el cuerpo del artículo en webs conocidas
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

# Dominios que bloquean scraping o tienen contenido detrás de paywall
BLOCKED_DOMAINS = [
    'wired.com', 'bloomberg.com', 'ft.com',
    'wsj.com', 'nytimes.com', 'technologyreview.com'
]


def scrape_full_article(url: str, fallback_text: str = "", timeout: int = 15) -> str:
    """
    Intenta obtener el texto completo del artículo desde su URL.
    Si falla (paywall, bloqueo, timeout), devuelve fallback_text del RSS.

    Returns:
        Texto del artículo (hasta ~3000 chars) o fallback_text si no se pudo.
    """
    if not url:
        return fallback_text

    # No intentar con dominios bloqueados
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

        # Solo procesar HTML
        content_type = resp.headers.get('content-type', '')
        if 'text/html' not in content_type:
            return fallback_text

        soup = BeautifulSoup(resp.text, 'html.parser')

        # Eliminar elementos de ruido
        for tag in soup(['script', 'style', 'nav', 'header', 'footer',
                         'aside', 'form', 'iframe', 'noscript',
                         '[class*="sidebar"]', '[class*="related"]',
                         '[class*="comment"]', '[class*="newsletter"]',
                         '[class*="ad-"]', '[class*="share"]']):
            tag.decompose()

        # Buscar el contenedor principal del artículo
        body_text = ""
        for selector in CONTENT_SELECTORS:
            container = soup.select_one(selector)
            if container:
                text = container.get_text(separator='\n', strip=True)
                text = re.sub(r'\n{3,}', '\n\n', text)
                if len(text) > 300:   # descartar contenedores vacíos
                    body_text = text
                    break

        if not body_text:
            # Último recurso: párrafos del body
            paragraphs = soup.find_all('p')
            body_text  = '\n'.join(p.get_text(strip=True) for p in paragraphs if len(p.get_text(strip=True)) > 60)

        if not body_text or len(body_text) < len(fallback_text or ""):
            return fallback_text

        # Limitar a ~3000 caracteres para no saturar el contexto de la IA
        return body_text[:3000].strip()

    except Exception:
        # Cualquier fallo (timeout, 403, etc.) → usar el RSS como fallback
        return fallback_text


# ── CATEGORIZATION ───────────────────────────────────────────────

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
    """Determina la categoría más probable de una noticia."""
    text   = (title + " " + content).lower()
    scores = {cat: 0 for cat in CATEGORY_KEYWORDS}

    for cat, keywords in CATEGORY_KEYWORDS.items():
        for kw in keywords:
            if kw in text:
                # Más peso si la keyword está en el título
                scores[cat] += 2 if kw in title.lower() else 1

    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "robotica"


# ── SLUG GENERATION ──────────────────────────────────────────────

def _remove_accents(text: str) -> str:
    """Convierte caracteres acentuados a su equivalente ASCII."""
    return ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    )


def generate_slug(text: str, max_length: int = 55) -> str:
    """
    Genera un slug URL-friendly, eliminando acentos y caracteres especiales.
    Incluye suficiente longitud para minimizar colisiones.
    """
    slug = text.lower()
    slug = _remove_accents(slug)
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[\s_]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    slug = slug.strip('-')
    return slug[:max_length]


def generate_unique_slug(text: str, known_slugs: set, max_length: int = 55) -> str:
    """
    Genera un slug único. Si ya existe, añade un sufijo numérico (-2, -3...).
    Evita colisiones entre artículos con títulos similares.
    """
    base = generate_slug(text, max_length)
    slug = base
    counter = 2
    while slug in known_slugs:
        suffix = f"-{counter}"
        slug   = base[:max_length - len(suffix)] + suffix
        counter += 1
    return slug
