# Lámpara de Música Inteligente con LEDs y Microfono

**Fecha:** 2026-07-16
**Categoría:** embebidos
**Tags:** robotica, microcontroladores, diseño-3d
**Título original:** WLED HiveLight – Audioreactive Mood Lamp #3DPrinting #3DThursday

---

## Introducción

Adafruit presenta una lámpara de música inteligente que cambia de color y brillo en función de la música que se escucha. Esta lámpara es una creación de miqu y utiliza tecnología de vanguardia para crear un ambiente inmersivo.

## ¿Qué es?

La lámpara de música inteligente, llamada HiveLight, es un proyecto de robótica que utiliza un microcontrolador ESP32, una cinta de LEDs WS2812b, un microfono I2S y un sensor de toque. Esto le permite cambiar de color y brillo en función de la música que se escucha y responder a los toques del usuario.

## ¿Cómo funciona?

La lámpara utiliza un software llamado WLED AudioReactive para procesar la señal de audio y controlar la cinta de LEDs. El microcontrolador ESP32 se encarga de leer la señal de audio del microfono y enviarla al software, que a su vez envía la señal de control a la cinta de LEDs. El sensor de toque permite al usuario interactuar con la lámpara y cambiar su comportamiento.

## ¿Por qué importa?

Esta lámpara de música inteligente puede ser utilizada en cualquier espacio para crear un ambiente inmersivo y relajante. Puede ser utilizada en salas de música, salas de cine, o incluso en habitaciones de estar. Además, puede ser personalizada para adaptarse a las preferencias del usuario.

## Consejo técnico

Si deseas crear una lámpara de música inteligente similar, puedes descargar el software WLED AudioReactive y utilizarlo con un microcontrolador ESP32 y una cinta de LEDs WS2812b. Asegúrate de configurar correctamente los pines GPIO y la señal de audio para que la lámpara funcione correctamente.

```bash
wled -c /dev/ttyUSB0 -d 16 -a 12 -i 32/25/33
```

---

**Fuente original:** [https://blog.adafruit.com/2026/07/16/wled-hivelight-audioreactive-mood-lamp-3dprinting-3dthursday/](https://blog.adafruit.com/2026/07/16/wled-hivelight-audioreactive-mood-lamp-3dprinting-3dthursday/)
