# Pila de desarrollo AngstromIO: una pila de 9 mm que se conecta a un USB-C

**Fecha:** 2026-03-26
**Categoría:** embebidos
**Tags:** microcontroladores, embebidos, arduino
**Título original:** AngstromIO – A tiny 9.0 x 8.9 mm ATtiny1616 board that fits on top of a USB-C connector

---

## Introducción

La empresa Dieu-de-l-elec ha lanzado una pila de desarrollo extremadamente pequeña basada en el microcontrolador ATtiny1616 de Microchip. Esta pila, llamada AngstromIO, mide solo 9,0 x 8,9 mm y se conecta a un puerto USB-C para recibir alimentación.

## ¿Qué es?

La AngstromIO es una pila de desarrollo abierta que incluye un microcontrolador ATtiny1616, dos LEDs RGB addressables y acceso a varias GPIO, incluyendo I2C, UART y UPDI para programación. Esta pila es ideal para proyectos embebidos con espacio limitado.

## ¿Cómo funciona?

La AngstromIO utiliza el microcontrolador ATtiny1616, que se programa mediante el protocolo UPDI. La pila incluye una conexión USB-C para recibir alimentación y una conexión UPDI para programación. La pila también incluye dos LEDs RGB addressables y acceso a varias GPIO.

## ¿Por qué importa?

La AngstromIO es importante porque ofrece una solución pequeña y eficiente para proyectos embebidos con espacio limitado. La pila es compatible con el IDE Arduino y permite utilizar bibliotecas como Wire y tinyNeoPixel para comunicación I2C y control de LEDs.

## Consejo técnico

Para programar la AngstromIO, utiliza el IDE Arduino y la biblioteca megaTinyCore. Puedes utilizar la biblioteca Wire para comunicación I2C y la biblioteca tinyNeoPixel para control de LEDs.

```bash
Arduino IDE + megaTinyCore + Wire + tinyNeoPixel
```

---

**Fuente original:** [https://www.cnx-software.com/2026/03/26/angstromio-a-tiny-9-0-x-8-9-mm-attiny1616-board-that-fits-on-top-of-a-usb-c-connector/](https://www.cnx-software.com/2026/03/26/angstromio-a-tiny-9-0-x-8-9-mm-attiny1616-board-that-fits-on-top-of-a-usb-c-connector/)
