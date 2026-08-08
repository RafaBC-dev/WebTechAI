# SPOKE: un controlador de toque con RP2040 para proyectos musicales

**Fecha:** 2026-08-08
**Categoría:** embebidos
**Tags:** robotica, microcontroladores, software-y-linux
**Título original:** SPOKE: An RP2040-powered touch controller

---

## Introducción

La compañía Pimoroni ha lanzado un dispositivo llamado SPOKE, que parece una discoteca de música de los años 90, pero en realidad es un controlador de toque con 27 pines GPIO que puede ser utilizado para proyectos musicales.

## ¿Qué es?

El SPOKE es un dispositivo circular con 27 pines de toque capacitivo, un microcontrolador RP2040, un puerto USB-C y un botón de reset. Puede ser utilizado como un controlador MIDI estándar, con cada pin de toque asignado a una nota diferente.

## ¿Cómo funciona?

El SPOKE utiliza el microcontrolador RP2040 para leer los pines de toque y enviar señales MIDI a un software de sincronización de audio. Puede ser programado utilizando CircuitPython y se puede conectar a un ordenador para utilizarlo como controlador MIDI.

## ¿Por qué importa?

El SPOKE importa porque ofrece una forma sencilla de crear proyectos musicales con toques capacitivos y puede ser utilizado para crear instrumentos musicales innovadores y divertidos.

## Consejo técnico

Para crear un proyecto musical con el SPOKE, puedes utilizar el software de sincronización de audio de Pimoroni y programar el dispositivo utilizando CircuitPython. Puedes también utilizar el SPOKE como un controlador MIDI para sincronizar audio con otros dispositivos.

```bash
`circuitpython --board spokemidi` para programar el SPOKE utilizando CircuitPython
```

---

**Fuente original:** [https://www.raspberrypi.com/news/spoke-an-rp2040-powered-touch-controller/](https://www.raspberrypi.com/news/spoke-an-rp2040-powered-touch-controller/)
