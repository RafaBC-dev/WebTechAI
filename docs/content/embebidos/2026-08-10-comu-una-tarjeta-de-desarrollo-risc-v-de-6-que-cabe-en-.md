# Comu: una tarjeta de desarrollo RISC-V de $6 que cabe en un puerto USB

**Fecha:** 2026-08-10
**Categoría:** embebidos
**Tags:** robotica, microcontroladores, software y linux
**Título original:** Comu is a $6 tiny CH32V203 RISC-V development board that fits inside a USB port

---

## Introducción

La industria de las tarjetas de desarrollo ha dado un paso más con la presentación de Comu, una tarjeta de desarrollo RISC-V de solo $6 que cabe en un puerto USB. Esta pequeña tarjeta de desarrollo es ideal para proyectos de código abierto y experimentación con microcontroladores RISC-V.

## ¿Qué es?

Comu es una tarjeta de desarrollo de código abierto que se basa en el microcontrolador WCH CH32V203, un procesador RISC-V de 32 bits con una velocidad de reloj de 144 MHz. La tarjeta mide solo 13 x 9.4 mm y cuenta con 6 pines GPIO, 4 botones capacitivos y 2 LEDs. También cuenta con una memoria de 20 KB de SRAM y 224 KB de Flash.

## ¿Cómo funciona?

Comu se puede programar con C/C++ utilizando el proyecto ch32fun, y también se puede utilizar con Rust, Arduino IDE y WCH-HAL. La tarjeta cuenta con un bootloader personalizado de 2 KB que deja disponible 28 KB de memoria de Flash para aplicaciones del usuario. La programación se puede realizar a través de la interfaz USB Type-A.

## ¿Por qué importa?

Comu es importante porque ofrece una plataforma de desarrollo económica y flexible para proyectos de código abierto y experimentación con microcontroladores RISC-V. La tarjeta es ideal para desarrolladores que buscan una plataforma de desarrollo ligera y fácil de usar.

## Consejo técnico

Si deseas empezar a trabajar con Comu, te recomendamos descargar el proyecto ch32fun y utilizar el bootloader personalizado para programar la tarjeta. También puedes utilizar la herramienta MounRiver Studio IDE para programar la tarjeta con WCH-HAL.

```bash
git clone https://github.com/ch32fun/ch32fun
```

---

**Fuente original:** [https://www.cnx-software.com/2026/08/10/comu-6-tiny-ch32v203-risc-v-development-board-that-fits-inside-a-usb-port/](https://www.cnx-software.com/2026/08/10/comu-6-tiny-ch32v203-risc-v-development-board-that-fits-inside-a-usb-port/)
