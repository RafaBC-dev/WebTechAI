# Actualización de teclado de Nintendo Family BASIC a USB

**Fecha:** 2026-03-13
**Categoría:** embebidos
**Tags:** ia-local, microcontroladores, software-y-linux
**Título original:** Nintendo’s Family BASIC Keyboard Gets USB Upgrade

---

## Introducción

Un aficionado ha encontrado una forma de conectar un teclado de Nintendo Family BASIC a un ordenador moderno mediante una actualización USB. Esto permite utilizar este teclado en dispositivos actuales, como Raspberry Pi o ordenadores con Linux.

## ¿Qué es?

El Nintendo Family BASIC es un teclado diseñado para ser utilizado con la consola de juegos Nintendo Entertainment System (NES) en Japón, conocida como Family Computer (Famicom). Este teclado se puede conectar a un ordenador moderno mediante una actualización USB, lo que permite utilizarlo en dispositivos actuales.

## ¿Cómo funciona?

La actualización se realizó utilizando el firmware QMK en un microcontrolador Adafruit KB2040. Esto permite que el teclado se comunique con un ordenador moderno mediante un cable USB. El proceso de actualización involucró la implementación de la lógica de escaneo de teclas previamente reverse-engineerada por otro desarrollador.

## ¿Por qué importa?

Esta actualización permite utilizar un teclado histórico en dispositivos modernos, lo que puede ser interesante para aficionados a la tecnología y la historia de la informática. Además, esta actualización puede ser útil para aquellos que buscan utilizar un teclado antiguo en un entorno moderno.

## Consejo técnico

Si deseas actualizar tu propio teclado de Nintendo Family BASIC a USB, puedes encontrar los archivos de código en GitHub y seguir los pasos descritos en la documentación para implementar la actualización.

```bash
git clone https://github.com/lucasleadbetter/family-basic-keyboard-usb-upgrade.git
```

---

**Fuente original:** [https://hackaday.com/2026/03/12/nintendos-family-basic-keyboard-gets-usb-upgrade/](https://hackaday.com/2026/03/12/nintendos-family-basic-keyboard-gets-usb-upgrade/)
