"""
Módulo para resumir noticias usando Groq (100% gratuito).
Groq free tier: 14.400 peticiones/día, sin tarjeta de crédito.

Instalación:  pip install groq python-dotenv
API key:      https://console.groq.com → API Keys → Create key
.env:         GROQ_API_KEY=gsk_...
"""

from groq import Groq
from dotenv import load_dotenv
import os, json, re, time

load_dotenv()

MODEL = "llama-3.1-8b-instant"


def _client() -> Groq:
    key = os.getenv("GROQ_API_KEY")
    if not key:
        raise ValueError(
            "Falta GROQ_API_KEY en el .env\n"
            "Consíguela gratis en: https://console.groq.com"
        )
    return Groq(api_key=key)


def summarize_with_gemini(text: str) -> dict:
    """
    Genera un resumen completo y útil de una noticia técnica.
    El objetivo es que el lector entienda perfectamente el tema
    sin necesidad de leer el artículo original.

    Returns dict con: titulo, intro, que_es, como_funciona, por_que_importa,
                      consejo, comando, tags
    """
    client = _client()

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
- tags: 3-5 términos técnicos cortos, en inglés si son jerga estándar del sector (ej: ROS2, SLAM, Docker, LLM)
- comando: solo si es realmente relevante y útil, no lo fuerces
- Todo el contenido debe ser suficientemente detallado para que el lector NO necesite ir a la fuente original para entender el tema
- Escribe en español neutro, claro y directo"""

    for intento in range(3):
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.4,
                max_tokens=1200,
            )

            raw = response.choices[0].message.content.strip()
            raw = re.sub(r'^```(?:json)?\s*', '', raw)
            raw = re.sub(r'\s*```$', '', raw)

            result = json.loads(raw)

            for key in ("titulo", "intro", "que_es", "como_funciona",
                        "por_que_importa", "consejo", "comando", "tags"):
                result.setdefault(key, "")

            if not isinstance(result["tags"], list):
                result["tags"] = []

            return result

        except json.JSONDecodeError:
            print("  ⚠️  JSON inválido, reintentando...")
            if intento == 2:
                raw_text = response.choices[0].message.content.strip()
                return {
                    "titulo": "", "intro": raw_text[:600],
                    "que_es": "", "como_funciona": "", "por_que_importa": "",
                    "consejo": "", "comando": "", "tags": []
                }
            time.sleep(2)
            continue

        except Exception as e:
            msg = str(e)
            if "429" in msg or "rate" in msg.lower():
                if intento < 2:
                    print(f"  ⏳ Rate limit. Esperando 30s...")
                    time.sleep(30)
                    continue
                return {"titulo": "", "intro": "", "que_es": "", "como_funciona": "",
                        "por_que_importa": "", "consejo": "", "comando": "", "tags": []}
            print(f"  ✗ Error Groq: {e}")
            raise

    return {"titulo": "", "intro": "", "que_es": "", "como_funciona": "",
            "por_que_importa": "", "consejo": "", "comando": "", "tags": []}
