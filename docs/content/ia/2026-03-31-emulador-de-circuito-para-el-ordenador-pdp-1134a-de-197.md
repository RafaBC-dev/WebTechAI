# Emulador de circuito para el ordenador PDP-11/34A de 1976

**Fecha:** 2026-03-31
**Categoría:** ia
**Tags:** ia-local, herramientas, linux
**Título original:** A circuit-level software emulator for the PDP-11/34A

---

## Introducción

Damien Boureille ha creado un emulador de circuito para el ordenador PDP-11/34A de 1976, un proyecto que reproduce la CPU del ordenador original a nivel de circuito para ayudar con la depuración y el desarrollo de software.

## ¿Qué es?

El proyecto 11/34 es un emulador de circuito que reproduce la CPU del PDP-11/34A a nivel de circuito, utilizando una traducción de C de los esquemas del ordenador original y consultando tablas ROM. El emulador incluye una CPU virtual KD11-EA y reproduce la lógica combinacional y los generadores de reloj del ordenador original.

## ¿Cómo funciona?

El emulador utiliza una traducción de C de los esquemas del ordenador original y consultando tablas ROM para reproducir la lógica combinacional y los generadores de reloj del ordenador. Esto se ha elegido en lugar de utilizar un nivel de gate-level (Verilog) para que el emulador sea lo suficientemente bajo nivel para reproducir errores de hardware, pero lo suficientemente rápido para ejecutar programas.

## ¿Por qué importa?

Este emulador es importante porque permite a los desarrolladores de software y a los ingenieros de hardware reproducir la comportamiento del ordenador PDP-11/34A a nivel de circuito, lo que puede ayudar a resolver problemas de depuración y a mejorar la comprensión del funcionamiento del ordenador.

## Consejo técnico

Si deseas probar el emulador 11/34, puedes descargarlo desde GitHub y ejecutarlo en tu máquina local. También puedes probar algunos de los programas y sistemas incluidos en el emulador, como el juego de la vida o la versión V6 UNIX del ordenador.

```bash
git clone https://github.com/damien-boureille/11-34.git
```

---

**Fuente original:** [https://blog.adafruit.com/2026/03/30/a-circuit-level-software-emulator-for-the-pdp-11-34a/](https://blog.adafruit.com/2026/03/30/a-circuit-level-software-emulator-for-the-pdp-11-34a/)
