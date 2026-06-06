# Un microcontrolador diminuto emula un procesador vintage con sorprendente velocidad

**Fecha:** 2026-06-06
**Categoría:** embebidos
**Tags:** microcontroladores, embebidos, linux
**Título original:** An Unlikely Host For An 8080 Emulator

---

## Introducción

Un ingeniero ha logrado emular un procesador vintage de la década de 1970 en un microcontrolador diminuto, demostrando que la velocidad no siempre depende del poder de procesamiento.

## ¿Qué es?

El proyecto consiste en emular el procesador Intel 8080 en un ATtiny85, un microcontrolador con pocos pines y capacidad de procesamiento limitada. El objetivo es demostrar que es posible emular hardware vintage en dispositivos modernos con recursos limitados.

## ¿Cómo funciona?

La emulación se logra mediante la reducción de la conexión física a un bus SPI y la utilización de un Teensy para offloadar las funciones de soporte. El código de emulación está optimizado en C y cuenta con una caché de 128 bytes para acelerar el proceso.

## ¿Por qué importa?

Este proyecto importa porque demuestra la posibilidad de emular hardware vintage en dispositivos modernos con recursos limitados. Esto puede ser útil para proyectos de retroinformática y para entender cómo funcionaban los sistemas antiguos.

## Consejo técnico

Si deseas emular un procesador vintage en un microcontrolador, considera utilizar una caché para acelerar el proceso y reducir la carga en el procesador. Puedes investigar sobre la implementación de cachés en el ATtiny85 y cómo optimizar el código de emulación.

```bash
git clone https://github.com/tedfried/8080-emulator.git
```

---

**Fuente original:** [https://hackaday.com/2026/06/06/an-unlikely-host-for-an-8080-emulator/](https://hackaday.com/2026/06/06/an-unlikely-host-for-an-8080-emulator/)
