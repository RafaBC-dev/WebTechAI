# TechPulse ES

> Curador automático de noticias tecnológicas en español, generadas y resumidas por IA.

Monitoriza más de 10 fuentes internacionales de referencia, extrae el contenido completo de cada artículo, lo resume en español con estructura clara y lo publica como web estática. Completamente gratuito, sin publicidad y sin servidor.

---

## Índice

1. [Concepto y filosofía](#1-concepto-y-filosofía)
2. [Stack tecnológico](#2-stack-tecnológico)
3. [Estructura del proyecto](#3-estructura-del-proyecto)
4. [Flujo de datos completo](#4-flujo-de-datos-completo)
5. [Archivos del backend](#5-archivos-del-backend)
6. [Archivos del frontend](#6-archivos-del-frontend)
7. [Configuración](#7-configuración)
8. [Puesta en marcha local](#8-puesta-en-marcha-local)
9. [Despliegue en GitHub Pages](#9-despliegue-en-github-pages)
10. [Automatización diaria](#10-automatización-diaria)
11. [Limitaciones conocidas](#11-limitaciones-conocidas)
12. [Posibles mejoras futuras](#12-posibles-mejoras-futuras)

---

## 1. Concepto y filosofía

El objetivo de TechPulse ES es actuar de **intermediario inteligente** entre las fuentes de noticias técnicas internacionales (principalmente en inglés) y el lector hispanohablante interesado en tecnología.

La propuesta de valor es concreta:
- El lector llega, lee el resumen en español y **entiende completamente** el tema sin necesidad de ir a la fuente original.
- Si quiere profundizar, el enlace al artículo original siempre está disponible al final.
- No hay publicidad, no hay tracking, no hay paywalls.

Cada artículo generado tiene **cuatro secciones fijas**: introducción, qué es, cómo funciona y por qué importa, más un consejo técnico práctico y, cuando aplica, un ejemplo de código o comando.

---

## 2. Stack tecnológico

| Componente     | Tecnología                          | Coste (limitaciones)        |
--------------------------------------------------------------------------------------
| IA / resúmenes | Groq API + LLaMA 3.1 8B             | **Gratis** (14.400 req/día) |
| Hosting        | GitHub Pages                        | **Gratis**                  |
| Automatización | GitHub Actions                      | **Gratis** (2.000 min/mes)  |
| Scraping       | Python + feedparser + BeautifulSoup | **Gratis**                  |
| Frontend       | HTML + CSS + JavaScript vanilla     | **Gratis**                  |
--------------------------------------------------------------------------------------
**Coste total de operación: 0 €/mes.**

---

## 3. Estructura del proyecto

```
techpulse-es/
│
├── 📄 config.json          → Configuración central (URL, feeds, límites)
├── 📄 requirements.txt     → Dependencias Python
├── 📄 run_log.txt          → Log acumulativo de ejecuciones (auto-generado)
│
├── 🐍 main.py              → Orquestador principal del scraper
├── 🐍 brain.py             → Módulo de IA (Groq / LLaMA 3.1)
├── 🐍 utils.py             → Herramientas: scraping, slugs, categorización, limpieza HTML
├── 🐍 build_index.py       → Generador de index.json, sitemap.xml y feed.xml
│
├── 🌐 index.html           → Página principal con grid de artículos
├── 🌐 detail.html          → Página de detalle de cada artículo
├── 🌐 about.html           → Página "Sobre el proyecto"
├── 🎨 styles.css           → Sistema de diseño completo (dark/light mode)
├── ⚡ app.js               → Lógica frontend: filtros, búsqueda, paginación, meta tags
│
├── 📁 content/             → Artículos generados (Markdown, ignorado en .gitignore local)
│   ├── ia/
│   ├── robotica/
│   ├── linux/
│   ├── embebidos/
│   └── diseño-3d/
│
├── 📄 index.json           → Índice de artículos (auto-generado por build_index.py)
├── 📄 sitemap.xml          → Sitemap para buscadores (auto-generado)
├── 📄 feed.xml             → Feed RSS propio (auto-generado)
│
└── 📁 .github/
    └── workflows/
        └── scraper.yml     → GitHub Actions: ejecución diaria automática
```

---

## 4. Flujo de datos completo

```
┌─────────────────────────────────────────────────────────┐
│                     EJECUCIÓN DIARIA                    │
│                  (GitHub Actions / local)               │
└─────────────────────────────────────────────────────────┘
                           │
                    1. main.py
                           │
              ┌────────────▼────────────┐
              │    Lee config.json      │
              │  (feeds, límites, URL)  │
              └────────────┬────────────┘
                           │
              ┌────────────▼────────────┐
              │  Carga slugs conocidos  │
              │    (deduplicación)      │
              └────────────┬────────────┘
                           │
                  Para cada feed RSS:
                           │
              ┌────────────▼────────────┐
              │   feedparser.parse()    │
              │   (últimas N entradas)  │
              └────────────┬────────────┘
                           │
              ┌────────────▼────────────┐
              │  ¿Slug ya conocido?     │──── SÍ → skip
              └────────────┬────────────┘
                          NO
                           │
              ┌────────────▼────────────┐
              │  scrape_full_article()  │
              │  Intenta obtener texto  │
              │  completo del artículo  │
              │  Fallback: texto RSS    │
              └────────────┬────────────┘
                           │
              ┌────────────▼────────────┐
              │  summarize_with_gemini()│
              │  (brain.py → Groq API)  │
              │  Devuelve JSON con:     │
              │  titulo, intro, que_es, │
              │  como_funciona,         │
              │  por_que_importa,       │
              │  consejo, comando, tags │
              └────────────┬────────────┘
                           │
              ┌────────────▼────────────┐
              │  categorize_news()      │
              │  (keywords matching)    │
              └────────────┬────────────┘
                           │
              ┌────────────▼────────────┐
              │  Guarda .md en          │
              │  content/<cat>/         │
              │  YYYY-MM-DD-slug.md     │
              └────────────┬────────────┘
                           │
                    2. build_index.py
                           │
              ┌────────────▼────────────┐
              │  Escanea content/**/*.md│
              │  Extrae metadatos       │
              │  Genera:                │
              │  • index.json           │
              │  • sitemap.xml          │
              │  • feed.xml             │
              └────────────┬────────────┘
                           │
                    3. GitHub Pages
                           │
              ┌────────────▼────────────┐
              │  Sirve archivos         │
              │  estáticos al navegador │
              │  app.js carga index.json│
              │  y renderiza la web     │
              └─────────────────────────┘
```

---

## 5. Archivos del backend

### `config.json`
Configuración central del proyecto. **Es el único archivo que hay que editar antes de desplegar.**

```json
{
  "site_url":     "https://tu-usuario.github.io/tu-repo",
  "site_name":    "TechPulse ES",
  "site_desc":    "Tecnología, robótica e IA explicada en español",
  "max_per_feed": 3,
  "max_per_run":  15,
  "feeds": [ ... ]
}
```

- `site_url`     → URL pública del sitio. Se usa en sitemap.xml, feed.xml y about.html.
- `max_per_feed` → Máximo de artículos a procesar por feed en cada ejecución.
- `max_per_run`  → Límite global de artículos nuevos por ejecución (evita saturar la cuota de Groq).

---

### `main.py` — Orquestador principal

**Función `main()`**
Punto de entrada. Carga config, inicializa directorios, carga slugs conocidos y llama a `process_feed()` para cada URL.

**Función `process_feed(feed_url, known_slugs, saved_titles, ...)`**
Descarga y parsea el feed RSS con `feedparser`. Para cada entrada:
1. Comprueba deduplicación por slug (rápido, O(1)).
2. Llama a `scrape_full_article()` para obtener el artículo completo.
3. Llama a `summarize_with_gemini()` para generar el resumen.
4. Llama a `save_news()` para guardar el Markdown.

**Función `save_news(category, result, title_original, source_url, known_slugs)`**
Construye el archivo Markdown con el formato estándar y lo guarda en `content/<categoría>/YYYY-MM-DD-<slug>.md`.

Formato del Markdown generado:
```markdown
# Título en español

**Fecha:** 2026-03-08
**Categoría:** robotica
**Tags:** ROS2, SLAM, Navigation
**Título original:** Original English Title

---

## Introducción
## ¿Qué es?
## ¿Cómo funciona?
## ¿Por qué importa?
## Consejo técnico

---

**Fuente original:** [https://...]( https://...)
```

**Función `load_known_slugs()`**
Escanea recursivamente `content/` y extrae el slug de cada nombre de archivo (`YYYY-MM-DD-<slug>.md`). Devuelve un `set` para búsquedas O(1).

**Función `write_log(saved_titles, errors)`**
Añade una línea al archivo `run_log.txt` con la fecha, los artículos nuevos y los errores. Se acumula con ejecuciones anteriores.

---

### `brain.py` — Módulo de IA

**Función `summarize_with_gemini(text)`**
(Nombre mantenido por compatibilidad histórica; usa Groq, no Gemini.)

Envía el texto a LLaMA 3.1 8B a través de la API de Groq con un prompt que exige respuesta en JSON. El prompt instruye al modelo a comportarse como un divulgador técnico, no como un asistente genérico.

Campos del JSON devuelto:

| Campo             | Descripción                                                  |
------------------------------------------------------------------------------------
| `titulo`          | Título en español (≤12 palabras)                             |
| `intro`           | Párrafo de enganche (qué ha pasado y por qué importa)        |
| `que_es`          | Explicación del concepto para alguien sin conocimiento previo|
| `como_funciona`   | Parte técnica: arquitectura, componentes, pasos              |
| `por_que_importa` | Aplicaciones reales, qué cambia respecto a lo anterior       |
| `consejo`         | Consejo técnico accionable y específico al tema              |
| `comando`         | Ejemplo de código/comando (vacío si no aplica)               |
| `tags`            | Lista de 3-5 términos técnicos                               |
------------------------------------------------------------------------------------

Gestión de errores:
- `JSONDecodeError` → guarda el texto plano como `intro` y continúa.
- Error 429 (rate limit) → espera 30s y reintenta hasta 3 veces.
- Otros errores → propaga la excepción para que `main.py` la registre en el log.

---

### `utils.py` — Herramientas auxiliares

**Función `scrape_full_article(url, fallback_text, timeout)`**
Intenta obtener el texto completo del artículo haciendo una petición HTTP a la URL original. Usa una lista de selectores CSS ordenados por especificidad (`article`, `[class*="entry-content"]`, `main`...) para encontrar el contenedor principal del artículo.

- Si el dominio está en `BLOCKED_DOMAINS` (paywalls conocidos), devuelve directamente el `fallback_text`.
- Si el scraping devuelve menos texto que el fallback, usa el fallback.
- Limita el texto a 3.000 caracteres para no saturar el contexto de la IA.

**Función `clean_html(html_content)`**
Elimina scripts, estilos y elementos de ruido del HTML con BeautifulSoup. Devuelve texto plano normalizado.

**Función `categorize_news(title, content)`**
Compara el texto contra listas de keywords por categoría. Pondera más las keywords encontradas en el título (×2) que en el cuerpo (×1). Devuelve la categoría con mayor puntuación.

Categorías disponibles: `ia`, `robotica`, `linux`, `embebidos`, `diseño-3d`.

**Función `generate_unique_slug(text, known_slugs, max_length)`**
Genera un slug URL-friendly eliminando acentos (normalización Unicode NFD), caracteres especiales y espacios. Si el slug ya existe en `known_slugs`, añade un sufijo numérico (`-2`, `-3`...) para evitar colisiones.

---

### `build_index.py` — Generador de estáticos

**Función `build_all()`**
Punto de entrada. Escanea `content/` recursivamente, extrae metadatos de cada `.md` y llama a los tres generadores.

**Función `extract_metadata(path)`**
Parsea un archivo Markdown con expresiones regulares para extraer: título, categoría, tags, fecha, slug, preview (primer párrafo de la Introducción) y si contiene bloques de código.

**Función `build_index(news)`**
Genera `index.json`: array JSON ordenado por fecha descendente con todos los metadatos. Es el archivo que consume el frontend.

**Función `build_sitemap(news, site_url)`**
Genera `sitemap.xml` con una `<url>` por artículo más las páginas estáticas (index, about). Los buscadores como Google lo usan para indexar el contenido.

**Función `build_feed(news, site_url, site_name, site_desc)`**
Genera `feed.xml`: RSS 2.0 estándar con las últimas 30 entradas. Permite a los lectores de RSS (Feedly, NetNewsWire, etc.) suscribirse al sitio.

---

## 6. Archivos del frontend

### `index.html` + `app.js` + `styles.css`

**Página principal.** Carga `index.json` con `fetch()` y renderiza dinámicamente el grid de tarjetas. No requiere servidor, funciona como HTML estático.

Funcionalidades implementadas:
- **Filtro por categoría** → pills clickables que filtran el array en memoria.
- **Buscador** → filtra en tiempo real por título, categoría, tags y preview.
- **Paginación** → muestra 12 artículos y un botón "Ver más" que carga 12 más.
- **Modo claro/oscuro** → toggle en la cabecera, persiste en `localStorage`.
- **Nav sincronizado** → los links de la cabecera y las pills de filtro están sincronizados entre sí.

### `detail.html`

**Página de detalle.** Lee el parámetro `?file=` de la URL, hace `fetch()` del archivo Markdown correspondiente y lo parsea con expresiones regulares para extraer cada sección.

Funcionalidades:
- **Meta tags dinámicos** → `og:title`, `og:description`, `twitter:card` se actualizan con el contenido del artículo para que las previews en redes sociales sean correctas.
- **Artículos relacionados** → busca en `index.json` artículos de la misma categoría o con tags comunes y los muestra al final.
- **Enlace a fuente original** → siempre visible al final con el texto "Ver fuente original ↗".

### `about.html`

Página informativa sobre el proyecto. Explica el funcionamiento, las fuentes monitorizadas y cómo suscribirse por RSS. Tiene un botón para copiar la URL del feed al portapapeles.

### `styles.css`

Sistema de diseño completo con variables CSS para dark/light mode.

Tipografía:
- `Syne` (titulares y badges) → geométrica y técnica
- `Fraunces` (cuerpo de texto) → legible y editorial
- `JetBrains Mono` (código, fechas, etiquetas) → monoespaciada

Colores por categoría:
| Categoría | Color |
|---|---|
| IA | Violeta `#a78bfa` |
| Robótica | Azul cielo `#38bdf8` |
| Linux | Verde `#34d399` |
| Embebidos | Naranja `#fb923c` |
| Diseño 3D | Rosa `#f472b6` |

---

## 7. Configuración

### Variables de entorno necesarias

Crea un archivo `.env` en la raíz del proyecto:

```env
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxx
```

Consigue la key gratis (sin tarjeta de crédito) en [console.groq.com](https://console.groq.com).

### `config.json` — ajustes recomendados antes de desplegar

```json
{
  "site_url": "https://TU-USUARIO.github.io/TU-REPO",
  "max_per_feed": 3,
  "max_per_run": 15
}
```

> ⚠️ `site_url` es el único campo crítico antes del despliegue. Un valor incorrecto rompe el sitemap, el feed RSS y la página about.

---

## 8. Puesta en marcha local

```bash
# 1. Clonar o descargar el proyecto
cd techpulse-es

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Crear el archivo .env
echo "GROQ_API_KEY=gsk_tu_clave_aqui" > .env

# 4. Editar config.json (feeds, límites)
# (opcional en local, necesario antes de desplegar)

# 5. Ejecutar el scraper
python main.py

# 6. Generar archivos estáticos
python build_index.py

# 7. Abrir la web en local
# Abre index.html directamente en el navegador
# O usa un servidor local para evitar errores de CORS:
python -m http.server 8000
# → http://localhost:8000
```

---

## 9. Despliegue en GitHub Pages

```bash
# 1. Crear repositorio en GitHub (puede ser público o privado)

# 2. Subir todos los archivos
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/TU-USUARIO/TU-REPO.git
git push -u origin main

# 3. Activar GitHub Pages
# GitHub → Settings → Pages → Source: Deploy from branch → main → / (root)

# 4. Añadir la API key como secreto
# GitHub → Settings → Secrets and variables → Actions → New repository secret
# Name: GROQ_API_KEY
# Value: gsk_tu_clave_aqui

# 5. Actualizar site_url en config.json
# "site_url": "https://TU-USUARIO.github.io/TU-REPO"
# Hacer commit y push

# La web estará disponible en:
# https://TU-USUARIO.github.io/TU-REPO
```

---

## 10. Automatización diaria

El archivo `.github/workflows/scraper.yml` configura GitHub Actions para ejecutar el scraper automáticamente cada día a las 7:00 UTC (9:00 hora España en invierno).

**Pasos del workflow:**
1. Checkout del repositorio
2. Instalar Python 3.11 y dependencias (con caché)
3. Ejecutar `main.py` (con `GROQ_API_KEY` del secret)
4. Ejecutar `build_index.py`
5. Commit y push automático de los archivos nuevos
6. Si falla, abre una Issue en el repositorio automáticamente

**Ejecución manual:**
En GitHub → Actions → "Scraper diario de noticias" → "Run workflow".

**Límites de GitHub Actions en el plan gratuito:**
- 2.000 minutos/mes para repositorios públicos: ilimitado.
- 2.000 minutos/mes para repositorios privados: el scraper tarda ~3 minutos/día = ~90 min/mes, bien dentro del límite.

---

## 11. Limitaciones conocidas

| Limitación                                                  | Impacto                                                  | Estado                        |
----------------------------------------------------------------------------------------------------------------------------------------------------------
| Algunos feeds solo dan resumen corto (no artículo completo) | Resumen de IA menos detallado                            | Mitigado con scraping directo |
| Groq free tier: 14.400 req/día, 30 req/min                  | No es problema con los límites actuales                  | Controlado                    |
| Discourse ROS es un foro, no un blog de noticias            | Algunos posts son preguntas de soporte                   | Asumido                       |
| Webs con paywall (Bloomberg, WSJ...) no son scrapiables     | No se incluyen en los feeds                              | Excluidas explícitamente      |
| Slugs de artículos en otro idioma pueden ser largos         | Nombres de archivo largos pero válidos                   | Limitado a 55 chars           |
| Sin búsqueda en el contenido completo (solo metadata)       | Búsquedas muy específicas pueden no encontrar resultados | Mejora futura                 |
----------------------------------------------------------------------------------------------------------------------------------------------------------

---

## 12. Posibles mejoras futuras

- **Búsqueda en contenido completo** → indexar el texto de los `.md` en el frontend con [Lunr.js](https://lunrjs.com/) o similar.
- **Imagen de portada automática** → generar o buscar una imagen representativa por artículo para las OG cards.
- **Panel de estadísticas** → página con gráficas de artículos por categoría, tendencias de tags, fuentes más activas.
- **Newsletter por email** → integrar [Mailchimp](https://mailchimp.com/) o [Buttondown](https://buttondown.email/) (gratuito hasta 100 suscriptores) para enviar resumen semanal.
- **Más idiomas** → el prompt de Groq se puede adaptar para generar en cualquier idioma.
- **Valoración de artículos** → botones de like/dislike con [Supabase](https://supabase.com/) (gratuito) para saber qué contenido gusta más.
- **Detección de duplicados semánticos** → usar embeddings para detectar artículos sobre el mismo tema aunque tengan títulos diferentes.

---

*Generado automáticamente · TechPulse ES*
