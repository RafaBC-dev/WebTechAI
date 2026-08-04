# Lenguaje de lenguaje masivo se ejecuta localmente en un microcontrolador ESP32-S3

**Fecha:** 2026-08-04
**Categoría:** ia
**Tags:** llms, esp32, ia-local
**Título original:** 28.9M-parameter LLM runs locally on ESP32-S3 at 9 tokens/s

---

## Introducción

Un ingeniero ha logrado ejecutar un modelo de lenguaje de lenguaje de 28,9 millones de parámetros en un microcontrolador ESP32-S3, lo que permite generar texto de manera local sin necesidad de conexión a internet.

## ¿Qué es?

El proyecto 'esp32-ai' utiliza un modelo de lenguaje de lenguaje (LLM) entrenado en la tarea de generar historias cortas. El modelo tiene 28,9 millones de parámetros y es capaz de generar texto de manera local en el microcontrolador ESP32-S3.

## ¿Cómo funciona?

El modelo se ejecuta en la memoria flash del microcontrolador, que es lenta pero tiene una capacidad de almacenamiento grande. El ingeniero utilizó la técnica de per-capas de Google para cargar solo las capas necesarias en la memoria RAM, lo que permite una ejecución más eficiente.

## ¿Por qué importa?

Este proyecto es relevante porque muestra que es posible ejecutar modelos de lenguaje de lenguaje de gran complejidad en dispositivos embebidos, lo que abre nuevas posibilidades para aplicaciones como la generación de texto en tiempo real en dispositivos móviles o la creación de sistemas de recomendación en entornos de IoT.

## Consejo técnico

Si deseas experimentar con modelos de lenguaje de lenguaje en un microcontrolador ESP32-S3, puedes utilizar la biblioteca 'esp32-ai' y seguir los pasos del ingeniero para cargar y ejecutar el modelo en tu dispositivo.

```bash
npm install esp32-ai
```

---

**Fuente original:** [https://www.cnx-software.com/2026/08/03/28-9m-parameter-llm-runs-locally-on-esp32-s3-at-9-tokens-s/](https://www.cnx-software.com/2026/08/03/28-9m-parameter-llm-runs-locally-on-esp32-s3-at-9-tokens-s/)
