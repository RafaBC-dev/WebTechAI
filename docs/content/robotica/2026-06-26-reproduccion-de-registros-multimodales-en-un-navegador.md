# Reproducción de registros multimodales en un navegador

**Fecha:** 2026-06-26
**Categoría:** robotica
**Tags:** robotica, linux, codigo
**Título original:** Driveline: browser-based replay for MCAP/rosbag2 with synced video + signals

---

## Introducción

Un desarrollador ha creado una herramienta llamada Driveline para reproducir registros multimodales en un navegador web, lo que permite visualizar video y señales de manera sincronizada.

## ¿Qué es?

Driveline es una herramienta de código abierto que permite reproducir registros multimodales, como los generados por rosbag2/MCAP, en un navegador web. Puede reproducir video de alta definición (4K) junto con señales de manera sincronizada y precisa.

## ¿Cómo funciona?

La herramienta utiliza un core de Rust compilado a WASM que se ejecuta en el navegador, lo que significa que no se necesita un servidor para funcionar. Puede leer archivos MCAP con H.264 y reproducirlos de manera fluida.

## ¿Por qué importa?

Driveline es importante porque permite a los desarrolladores y investigadores reproducir y analizar registros multimodales de manera fácil y efectiva, lo que puede ser útil en aplicaciones como la robótica y la automatización.

## Consejo técnico

Si deseas reproducir registros multimodales en tu navegador, prueba Driveline y explora sus características, como la capacidad de leer ASAM MF4 y reproducir video y señales de manera sincronizada.

```bash
https://driveline.pages.dev
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/driveline-browser-based-replay-for-mcap-rosbag2-with-synced-video-signals/55702](https://discourse.openrobotics.org/t/driveline-browser-based-replay-for-mcap-rosbag2-with-synced-video-signals/55702)
