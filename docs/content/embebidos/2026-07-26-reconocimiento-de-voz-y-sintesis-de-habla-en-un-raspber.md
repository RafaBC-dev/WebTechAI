# Reconocimiento de voz y síntesis de habla en un Raspberry Pi Pico 2

**Fecha:** 2026-07-26
**Categoría:** embebidos
**Tags:** robotica, microcontroladores, software-y-linux
**Título original:** Voice Recognition and Speech Synthesis on an RPi Pico 2

---

## Introducción

Pete Warden ha lanzado un proyecto para crear una interfaz de voz completa en un chip de solo 50 centavos. Aunque no ha alcanzado su objetivo, ha logrado un avance significativo. Utiliza un Raspberry Pi Pico 2, un microcontrolador con 520 KiB de RAM y 4 MiB de flash, junto con una tarjeta de sonido I2S y un amplificador de clase D.

## ¿Qué es?

Este proyecto consiste en implementar un sistema de reconocimiento de voz y síntesis de habla en un microcontrolador Raspberry Pi Pico 2. Esto significa que el sistema puede reconocer comandos de voz y convertir texto en habla sin necesidad de conexión a Internet ni acceso a una API en la nube.

## ¿Cómo funciona?

El proyecto utiliza una tarjeta de sonido I2S para capturar la voz y un amplificador de clase D para amplificar el sonido. Luego, utiliza una biblioteca de reconocimiento de voz para analizar la voz y determinar qué comandos se están ejecutando. Por último, utiliza una biblioteca de síntesis de habla para convertir el texto en habla.

## ¿Por qué importa?

Este proyecto es importante porque permite crear sistemas de voz autónomos que no requieren conexión a Internet ni acceso a una API en la nube. Esto puede ser útil en aplicaciones como la automatización de hogares, la asistencia para personas con discapacidad y la creación de sistemas de voz para dispositivos móviles.

## Consejo técnico

Si deseas probar este proyecto, puedes descargar el código de GitHub y utilizar la biblioteca de reconocimiento de voz y síntesis de habla para crear tu propio sistema de voz autónomo.

```bash
git clone https://github.com/petewarden/pi-pico-voice
```

---

**Fuente original:** [https://blog.adafruit.com/2026/07/25/voice-recognition-and-speech-synthesis-on-an-rpi-pico-2/](https://blog.adafruit.com/2026/07/25/voice-recognition-and-speech-synthesis-on-an-rpi-pico-2/)
