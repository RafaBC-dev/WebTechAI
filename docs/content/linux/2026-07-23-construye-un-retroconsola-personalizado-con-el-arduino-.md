# Construye un retroconsola personalizado con el Arduino UNO Q Arcade bundle

**Fecha:** 2026-07-23
**Categoría:** linux
**Tags:** robotica, arduino, linux
**Título original:** Arduino UNO Q Arcade bundle lets you build a custom retro gaming console for about $90

---

## Introducción

El Arduino UNO Q Arcade bundle es un kit que permite a los usuarios crear una retroconsola personalizada para jugar a juegos clásicos con una gran variedad de opciones de control y configuración.

## ¿Qué es?

El Arduino UNO Q Arcade bundle es un kit que combina el Arduino UNO Q, un SBC con 4GB de almacenamiento, con una serie de módulos I2C que pueden ser conectados de manera daisy-chain para crear un controlador de juego personalizado. El kit incluye módulos para joystick, botones y movimiento, y puede ser utilizado para jugar a juegos clásicos y desarrollar juegos personalizados.

## ¿Cómo funciona?

El Arduino UNO Q Arcade bundle funciona mediante la conexión de los módulos I2C al SBC a través de cables Qwiic. El SBC procesa los datos de los módulos y emula dispositivos HID estándar para juegos o desarrollo. El software utilizado es Debian Linux, y se proporciona un script de Python que traduce los eventos de los módulos en datos de teclado y ratón virtuales.

## ¿Por qué importa?

Este kit importa porque permite a los usuarios crear una retroconsola personalizada con una gran variedad de opciones de control y configuración, y también puede ser utilizado para desarrollar juegos personalizados utilizando la plataforma Godot.

## Consejo técnico

Si deseas utilizar el Arduino UNO Q Arcade bundle para jugar a juegos clásicos, asegúrate de descargar y configurar RetroArch, una emulación de consolas clásicas que se puede ejecutar en el SBC.

```bash
sudo apt-get install retroarch
```

---

**Fuente original:** [https://www.cnx-software.com/2026/07/22/arduino-uno-q-arcade-bundle-lets-you-build-a-custom-retro-gaming-console/](https://www.cnx-software.com/2026/07/22/arduino-uno-q-arcade-bundle-lets-you-build-a-custom-retro-gaming-console/)
