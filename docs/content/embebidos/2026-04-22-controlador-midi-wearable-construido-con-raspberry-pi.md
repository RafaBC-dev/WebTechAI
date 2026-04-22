# Controlador MIDI wearable construido con Raspberry Pi

**Fecha:** 2026-04-22
**Categoría:** embebidos
**Tags:** robotica, microcontroladores, software y linux
**Título original:** Wearable MIDI Controller Built With Raspberry Pi

---

## Introducción

Un equipo de desarrolladores ha creado un controlador MIDI wearable que permite controlar sintetizadores con la mano. Este dispositivo innovador utiliza sensores flexibles y botones táctiles para generar sonidos únicos.

## ¿Qué es?

El proyecto se llama DigitSynth y consiste en un controlador wearable que se ajusta a la mano. Utiliza sensores flexibles para controlar parámetros del sintetizador y botones táctiles para cambiar acordes.

## ¿Cómo funciona?

El corazón del proyecto es un Raspberry Pi 5 que se comunica con un ADC TI ADS1115 para leer los sensores flexibles y botones táctiles. El Pi también utiliza un TLC59711 PWM driver para controlar LEDs que proporcionan retroalimentación visual.

## ¿Por qué importa?

Este proyecto es relevante porque permite a los músicos interactuar de manera intuitiva con los sintetizadores, creando sonidos únicos y emocionantes. También muestra la potencia de la tecnología de sensores y controladores wearable.

## Consejo técnico

Si deseas crear un proyecto similar, considera utilizar la librería Python para el Raspberry Pi y el ADC TI ADS1115. También puedes investigar sobre el uso de sensores flexibles y botones táctiles en proyectos de música electrónica.

```bash
sudo apt-get install python-rpi.gpio
```

---

**Fuente original:** [https://hackaday.com/2026/04/21/wearable-midi-controller-built-with-raspberry-pi/](https://hackaday.com/2026/04/21/wearable-midi-controller-built-with-raspberry-pi/)
