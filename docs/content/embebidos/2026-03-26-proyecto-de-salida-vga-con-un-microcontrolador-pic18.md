# Proyecto de salida VGA con un microcontrolador PIC18

**Fecha:** 2026-03-26
**Categoría:** embebidos
**Tags:** robotica, microcontroladores, linux
**Título original:** VGA Output From A PIC18

---

## Introducción

Un ingeniero ha logrado conectar un microcontrolador PIC18 a un monitor VGA, mostrando una imagen de 360x480 píxeles con hasta 16 colores. Este proyecto demuestra la capacidad de los microcontroladores para realizar tareas complejas como la salida de vídeo.

## ¿Qué es?

El proyecto consiste en conectar un microcontrolador PIC18F47K42 a un monitor VGA para mostrar una imagen. El microcontrolador utiliza un cristal de 14.3182 MHz para generar las señales de vídeo necesarias. La salida VGA se logra mediante la utilización de multiplexores y resistores para generar las señales de color.

## ¿Cómo funciona?

El microcontrolador PIC18F47K42 utiliza el timer interno para generar las señales de vídeo, incluyendo HSYNC, VSYNC y las señales de color. El cristal de 14.3182 MHz se utiliza para dividir las señales del timer y generar las frecuencias necesarias para la salida VGA. Los multiplexores y resistores se utilizan para generar las señales de color.

## ¿Por qué importa?

Este proyecto es importante porque demuestra la capacidad de los microcontroladores para realizar tareas complejas como la salida de vídeo. Esto abre nuevas posibilidades para la creación de dispositivos que requieren salida de vídeo, como monitores de código de barras o sistemas de visualización de datos.

## Consejo técnico

Si deseas implementar una salida VGA en tu propio proyecto, puedes utilizar el código y la documentación proporcionados por el ingeniero que realizó este proyecto. Puedes descargar el código desde GitHub y adaptarlo a tus necesidades.

```bash
git clone https://github.com/grecotron/vga-pic18
```

---

**Fuente original:** [https://hackaday.com/2026/03/25/vga-output-from-a-pic18/](https://hackaday.com/2026/03/25/vga-output-from-a-pic18/)
