# Calculadora científica FPGA: diseño y construcción desde cero

**Fecha:** 2026-05-20
**Categoría:** linux
**Tags:** fpga, cpu, python
**Título original:** Designing an FPGA calculator from scratch

---

## Introducción

Un equipo de ingenieros ha diseñado y construido una calculadora científica desde cero, utilizando un FPGA Altera Cyclone II y una CPU personalizada. Esta calculadora utiliza el formato de números binarios decimales (BCD) y ofrece precisión decimal perfecta.

## ¿Qué es?

La calculadora científica es un dispositivo electrónico que utiliza un FPGA para realizar cálculos científicos. Se basa en el formato de números BCD, que representa cada dígito decimal como un nibble de 4 bits. Esto permite una precisión decimal perfecta y evita errores de conversión de punto flotante.

## ¿Cómo funciona?

La calculadora utiliza una CPU personalizada diseñada específicamente para trabajar con números BCD. La CPU se ejecuta en el FPGA y utiliza un conjunto de instrucciones de 12 bits. El proyecto incluye una herramienta de ensamblaje en Python y un microcódigo que se ejecuta en la CPU. Además, se ha creado una capa de scripting para funciones de alto nivel y una interfaz de usuario con teclado y pantalla.

## ¿Por qué importa?

Esta calculadora científica es importante porque ofrece una precisión decimal perfecta y una arquitectura diseñada específicamente para resolver problemas científicos. Esto la hace ideal para aplicaciones que requieren precisión y velocidad, como la física, la ingeniería y la matemática.

## Consejo técnico

Si deseas crear una calculadora científica similar, puedes empezar utilizando el FPGA Altera Cyclone II y la herramienta de ensamblaje en Python. Recuerda que es importante diseñar una CPU personalizada para trabajar con números BCD y utilizar un microcódigo que se ejecute en la CPU.

```bash
verilator --top-module calculadora --testbench testbench.v
```

---

**Fuente original:** [https://blog.adafruit.com/2026/05/19/designing-an-fpga-calculator-from-scratch/](https://blog.adafruit.com/2026/05/19/designing-an-fpga-calculator-from-scratch/)
