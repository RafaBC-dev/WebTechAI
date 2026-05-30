# Nueva biblioteca para voz en vivo HD en ESP-NOW con G.722

**Fecha:** 2026-05-30
**Categoría:** embebidos
**Tags:** robotica, esp32, arduino, linux
**Título original:** PCMFlow722 library enables two-way real-time HD voice over ESP-NOW with G.722 audio codec

---

## Introducción

La biblioteca PCMFlow722 permite comunicaciones de voz en vivo de alta calidad en ESP-NOW, revolucionando la comunicación en dispositivos ESP32

## ¿Qué es?

La biblioteca PCMFlow722 es una herramienta desarrollada por Tanaka Masayuki que permite transmitir voz en vivo de alta calidad (HD voice) entre dispositivos ESP32 utilizando el protocolo ESP-NOW. Esta biblioteca se basa en el codec G.722, que es un estándar de audio de alta calidad que ofrece una banda de audio de 7 kHz a una tasa de muestreo de 16 kHz.

## ¿Cómo funciona?

La biblioteca PCMFlow722 funciona implementando un encoder G.722 que comprime la señal de audio de 16 kHz a G.722, y un decoder que hace el proceso inverso. Esto permite transmitir voz en vivo de alta calidad a través de ESP-NOW, que es un protocolo de comunicación de bajo consumo de energía y bajo ancho de banda.

## ¿Por qué importa?

La biblioteca PCMFlow722 es importante porque permite a los desarrolladores crear dispositivos que puedan comunicarse de manera de alta calidad en tiempo real, sin la necesidad de una conexión a Internet. Esto abre nuevas posibilidades para aplicaciones como la comunicación de voz en vivo en dispositivos de automatización, robots y sistemas de vigilancia.

## Consejo técnico

Si deseas probar la biblioteca PCMFlow722 en tu propio dispositivo ESP32, puedes utilizar el ejemplo de código EspNowTransceiver.ino, que es un transmisor y receptor de voz en vivo HD que se puede ejecutar en un solo dispositivo.

```bash
EspNowTransceiver.ino
```

---

**Fuente original:** [https://www.cnx-software.com/2026/05/30/pcmflow722-library-enables-two-way-real-time-hd-voice-over-esp-now-with-g-722-audio-codec/](https://www.cnx-software.com/2026/05/30/pcmflow722-library-enables-two-way-real-time-hd-voice-over-esp-now-with-g-722-audio-codec/)
