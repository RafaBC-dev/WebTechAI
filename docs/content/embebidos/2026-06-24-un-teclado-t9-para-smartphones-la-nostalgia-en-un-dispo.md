# Un teclado T9 para smartphones: la nostalgia en un dispositivo moderno

**Fecha:** 2026-06-24
**Categoría:** embebidos
**Tags:** robotica, microcontroladores, software y linux
**Título original:** A T9 Keyboard For Your Smartphone

---

## Introducción

Los smartphones modernos suelen tener teclados táctiles decentes, pero ¿recuerdas cuando teníamos que teclear en el teclado numérico? Un ingeniero ha recreado ese experiencio en un dispositivo moderno.

## ¿Qué es?

Un teclado T9 es un dispositivo que permite teclear en un smartphone utilizando el teclado numérico, similar a los teléfonos móviles de hace décadas. Este proyecto utiliza un teclado de un Nokia E52, un teléfono Symbian de 2009, y lo conecta a un smartphone moderno a través de Bluetooth.

## ¿Cómo funciona?

El teclado se construye a partir del teclado numérico del Nokia E52, que se encuentra sobre un circuito impreso personalizado (PCB) con interruptores táctiles Alps SKRK. Un microcontrolador ESP32-C6 lee los pulsos de los interruptores y envía los caracteres correspondientes a través de Bluetooth a un dispositivo compatible.

## ¿Por qué importa?

Este proyecto puede ser interesante para aquellos que buscan una forma alternativa de teclear en sus smartphones, o para aquellos que quieren experimentar con la nostalgia de los teléfonos móviles de hace décadas.

## Consejo técnico

Si deseas crear tu propio teclado T9, puedes utilizar el mismo microcontrolador ESP32-C6 y el mismo tipo de interruptores táctiles Alps SKRK. Recuerda que necesitarás un circuito impreso personalizado (PCB) para conectar los interruptores al microcontrolador.

```bash
Si deseas crear tu propio teclado T9, puedes utilizar el siguiente código para configurar el microcontrolador ESP32-C6: `idf.py flash`
```

---

**Fuente original:** [https://hackaday.com/2026/06/24/a-t9-keyboard-for-your-smartphone/](https://hackaday.com/2026/06/24/a-t9-keyboard-for-your-smartphone/)
