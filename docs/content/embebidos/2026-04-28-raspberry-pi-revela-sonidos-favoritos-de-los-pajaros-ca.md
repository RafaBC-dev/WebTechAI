# Raspberry Pi revela sonidos favoritos de los pájaros cantores

**Fecha:** 2026-04-28
**Categoría:** embebidos
**Tags:** robotica, linux, embebidos
**Título original:** Raspberry Pi reveals songbirds’ favourite sounds

---

## Introducción

Un equipo de investigadores canadienses ha desarrollado un sistema de bajo costo para estudiar las preferencias auditivas de los pájaros cantores utilizando una Raspberry Pi. Esto permite una mayor accesibilidad a la investigación en este campo.

## ¿Qué es?

El proyecto consiste en un sistema de estudio de preferencias auditivas de los pájaros cantores utilizando una Raspberry Pi como cerebro principal. Se utiliza un dispositivo de sonido de alta fidelidad y altavoces para reproducir sonidos de pájaros, mientras que sensores infrarrojos detectan el movimiento de los pájaros para activar la reproducción de los sonidos.

## ¿Cómo funciona?

Se utiliza una Raspberry Pi Zero 2 W como dispositivo principal, conectada a un dispositivo de sonido de alta fidelidad (HiFiBerry DAC+ Zero) y altavoces (8-ohm Dayton Audio). Los sensores infrarrojos (Adafruit IR Break Beam) detectan el movimiento de los pájaros para activar la reproducción de los sonidos. El sistema permite controlar varios parámetros y agregar nuevos experimentos.

## ¿Por qué importa?

Este sistema de bajo costo permite a los investigadores estudiar las preferencias auditivas de los pájaros cantores de manera más accesible y eficiente, lo que puede llevar a nuevos descubrimientos en el campo de la neuroetología de los pájaros.

## Consejo técnico

Si deseas crear un sistema similar, puedes utilizar la librería Raspbian para configurar la Raspberry Pi y el dispositivo de sonido de alta fidelidad. También puedes utilizar el software de código abierto Audacity para grabar y editar los sonidos de pájaros.

```bash
sudo apt-get install raspbian
```

---

**Fuente original:** [https://www.raspberrypi.com/news/raspberry-pi-reveals-songbirds-favourite-sounds/](https://www.raspberrypi.com/news/raspberry-pi-reveals-songbirds-favourite-sounds/)
