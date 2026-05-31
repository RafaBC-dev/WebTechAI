# Nueva biblioteca PCMFlow722 para voz en vivo HD en ESP32 con G.722

**Fecha:** 2026-05-31
**Categoría:** embebidos
**Tags:** robotica, microcontroladores, software y linux
**Título original:** PCMFlow722 library enables two-way real-time HD voice over ESP-NOW with G.722 audio codec

---

## Introducción

Una nueva biblioteca llamada PCMFlow722 permite transmitir voz en vivo de alta calidad en tiempo real entre dispositivos ESP32 con una tarjeta de sonido y un micrófono, convirtiéndolos en walkie-talkies.

## ¿Qué es?

La biblioteca PCMFlow722 es una implementación de un codec de audio G.722 para la biblioteca de audio ligera PCMFlow, que ya soporta audio sin compresión, MP3 y FLAC. Esta biblioteca permite transmitir voz en vivo de alta calidad en tiempo real entre dispositivos ESP32 con una tarjeta de sonido y un micrófono.

## ¿Cómo funciona?

La biblioteca PCMFlow722 implementa un codificador G.722 que comprime audio de 16 kHz en PCM en G.722, y un decodificador que hace lo contrario. Esto permite transmitir audio de alta calidad en tiempo real con un gasto de banda de 64 kbps, lo mismo que el codec G.711, pero con un ancho de banda de audio doble.

## ¿Por qué importa?

Esta biblioteca es importante porque permite transmitir voz en vivo de alta calidad en tiempo real entre dispositivos ESP32, lo que puede ser útil en aplicaciones como comunicación de emergencia, sistemas de vigilancia o incluso juegos en línea.

## Consejo técnico

Si deseas probar esta biblioteca en tu propio dispositivo ESP32, puedes utilizar el ejemplo de código EspNowTransceiver.ino que viene incluido en la documentación de la biblioteca.

```bash
EspNowTransceiver.ino
```

---

**Fuente original:** [https://www.cnx-software.com/2026/05/30/pcmflow722-library-enables-two-way-real-time-hd-voice-over-esp-now-with-g-722-audio-codec/](https://www.cnx-software.com/2026/05/30/pcmflow722-library-enables-two-way-real-time-hd-voice-over-esp-now-with-g-722-audio-codec/)
