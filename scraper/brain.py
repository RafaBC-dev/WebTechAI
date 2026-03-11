"""
brain.py — Motor de inteligencia artificial de TechPulse ES
===========================================================
Envía el texto de cada noticia a un LLM (Groq/LLaMA 3.1) y
devuelve un resumen estructurado en español con 8 secciones.

Proveedor: Groq — 14.400 peticiones/día gratis, sin tarjeta.
Instalación: pip install groq python-dotenv
API key:     https://console.groq.com → API Keys → Create key
.env:        GROQ_API_KEY=gsk_...
"""

from groq import Groq
from dotenv import load_dotenv
import os, json, re, time
from utils import with_retries

# Carga las variables del fichero .env para que os.getenv() funcione
load_dotenv()

# Modelo elegido: rápido, alta cuota gratuita, suficiente calidad
MODEL = "llama-3.1-8b-instant"


def _client() -> Groq:
    """
    Crea una instancia autenticada del cliente Groq.

    Por qué existe separada:
        Centraliza la autenticación y lanza un mensaje claro
        si falta la API key, en lugar de un error críptico posterior.

    Returns:
        Instancia de Groq lista para peticiones

    Raises:
        ValueError: si GROQ_API_KEY no está en el .env
    """
    key = os.getenv("GROQ_API_KEY")
    if not key:
        raise ValueError(
            "Falta GROQ_API_KEY en el .env\n"
            "Consíguela gratis en: https://console.groq.com"
        )
    return Groq(api_key=key)


@with_retries(max_retries=3, delay=30)
def summarize_with_groq(text: str) -> dict:
    """
    Genera un resumen estructurado de una noticia técnica usando Groq/LLaMA.

    Por qué existe:
        Los artículos en inglés se destilan en 8 secciones en español,
        listas para renderizar directamente en el frontend del sitio.

    Cómo funciona paso a paso:
        1. Obtiene el cliente Groq autenticado.
        2. Construye un prompt que inyecta el texto del artículo y define
           la estructura JSON esperada con reglas de estilo.
        3. Llama a la API con temperatura 0.4 (respuestas precisas, no creativas).
        4. Limpia posibles bloques markdown (```json ... ```) del resultado.
        5. Parsea el JSON y rellena campos faltantes con setdefault().
        6. Reintenta hasta 3 veces en caso de JSON inválido.
        7. Espera 30s y reintenta si hay rate limit (error 429).

    Args:
        text: "Título: <título>\\n\\nContenido: <cuerpo>" en inglés

    Returns:
        dict con claves: titulo, intro, que_es, como_funciona,
        por_que_importa, consejo, comando (str), tags (list).
        Devuelve campos vacíos si la llamada falla completamente.
    """
    client = _client()

    # Prompt detallado: define el rol, la estructura JSON y las reglas de estilo.
    # temperature=0.4 → respuestas consistentes, poco aleatorias.
    prompt = f"""Eres un divulgador técnico experto en robótica, Linux, IA y sistemas embebidos.
Tu misión es explicar esta noticia de forma que cualquier persona interesada en tecnología
la entienda completamente después de leer tu resumen, sin necesidad de ir a la fuente original.

Escribe como un periodista técnico, no como un asistente. Sé concreto, útil y claro.
Responde ÚNICAMENTE con JSON válido, sin bloques markdown, sin texto adicional.

Noticia:
{text}

Devuelve exactamente este JSON (todos los campos en español salvo comando y tags):
{{
  "titulo": "Título atractivo en español que resume bien el tema (máx. 12 palabras)",
  "intro": "Párrafo de 2-3 frases que enganche al lector: qué ha pasado o qué existe, y por qué es relevante ahora mismo. Sin tecnicismos innecesarios.",
  "que_es": "Explicación clara de QUÉ ES o en qué consiste este proyecto, tecnología o noticia. 3-5 frases. Explica los conceptos clave para que alguien sin conocimiento previo lo entienda.",
  "como_funciona": "Explicación de CÓMO FUNCIONA o cómo se ha construido/implementado. 3-5 frases técnicas pero comprensibles. Si hay pasos, arquitectura o componentes importantes, menciónalos.",
  "por_que_importa": "Por qué esto importa: aplicaciones reales, problemas que resuelve, o qué cambia respecto a lo que había antes. 2-4 frases concretas.",
  "consejo": "Un consejo técnico REALMENTE ÚTIL y accionable relacionado con el tema. Algo que el lector pueda aplicar, investigar o probar. No genérico: que sea específico al tema de la noticia. 2-3 frases.",
  "comando": "Si aplica: un comando, fragmento de código, configuración o herramienta concreta que el lector pueda usar. Vacío si no aplica naturalmente.",
  "tags": ["tag1", "tag2", "tag3"]
}}

Reglas:
- tags: elige MÁXIMO 3 tags de esta lista EXACTA (usa el valor exacto, en minúsculas con guiones):
    IA y modelos:       llms | agentes | ia-local | benchmarks
    Microcontroladores: esp32 | arduino | raspberry-pi
    Software y Linux:   python | librerias | herramientas
  Solo usa tags de esa lista. Si ninguno encaja, devuelve lista vacía [].
- comando: solo si es realmente relevante y útil, no lo fuerces
- Todo el contenido debe ser suficientemente detallado para que el lector NO necesite ir a la fuente original
- Escribe en español neutro, claro y directo"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_tokens=1200,
    )

    raw = response.choices[0].message.content.strip()
    # El modelo a veces envuelve el JSON en bloques ```json ... ```; los eliminamos
    raw = re.sub(r'^```(?:json)?\s*', '', raw)
    raw = re.sub(r'\s*```$', '', raw)

    result = json.loads(raw)

    # setdefault() añade la clave solo si NO existe, preservando el valor del modelo
    for key in ("titulo", "intro", "que_es", "como_funciona",
                "por_que_importa", "consejo", "comando", "tags"):
        result.setdefault(key, "")

    # Garantizamos que tags sea siempre una lista, nunca una cadena
    if not isinstance(result["tags"], list):
        result["tags"] = []

    return result
