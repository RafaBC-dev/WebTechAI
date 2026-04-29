# Wipeout Clone en ESP32-S3: un juego clásico en un microcontrolador

**Fecha:** 2026-04-29
**Categoría:** embebidos
**Tags:** esp32, robotica, embebidos
**Título original:** Wipeout Clone Runs Native on ESP32-S3

---

## Introducción

Michael Biggins, un desarrollador experimentado, ha logrado crear un clone de Wipeout, un juego clásico de 1995, en un ESP32-S3. Este proyecto demuestra la capacidad del microcontrolador para ejecutar juegos 3D complejos.

## ¿Qué es?

Wipeout es un juego de carreras en 3D que originalmente se ejecutaba en la consola PlayStation. El proyecto de Michael Biggins consiste en crear un clone de este juego en un ESP32-S3, un microcontrolador con capacidad de procesamiento 32-bit y dos núcleos.

## ¿Cómo funciona?

El ESP32-S3 utiliza sus dos núcleos para ejecutar el juego, uno de ellos se encarga de la salida de video intercalada, mientras que el otro completa la segunda mitad de la imagen. El juego también utiliza 8 MB de PSRAM y 512 kB de video RAM para almacenar la información gráfica.

## ¿Por qué importa?

Este proyecto importa porque demuestra la capacidad del ESP32-S3 para ejecutar juegos 3D complejos, lo que puede abrir nuevas posibilidades para el desarrollo de juegos en microcontroladores. Además, el juego se ejecuta a 60 frames por segundo, lo que es más rápido que la versión original.

## Consejo técnico

Si deseas aprender más sobre la implementación de juegos 3D en microcontroladores, puedes investigar la biblioteca de desarrollo de ESP-IDF y su soporte para la renderización de gráficos.

---

**Fuente original:** [https://hackaday.com/2026/04/29/wipeout-clone-runs-native-on-esp32-s3/](https://hackaday.com/2026/04/29/wipeout-clone-runs-native-on-esp32-s3/)
