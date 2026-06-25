# Control de brazos robóticos en paralelo: transporte seguro y estable

**Fecha:** 2026-06-25
**Categoría:** linux
**Tags:** robotica, ia-local, herramientas
**Título original:** Tightly-Coupled Bimanual Control - Safe and Stable Dual Arm Transport

---

## Introducción

Desarrolladores de ROBOTIS han creado un paquete de control de movimiento para robots con dos brazos que permite transporte seguro y estable de objetos. Este avance es fundamental para la robótica y la investigación en inteligencia artificial.

## ¿Qué es?

El paquete de control de movimiento 'cyclo_control' es una herramienta desarrollada por ROBOTIS que permite controlar dos brazos robóticos en paralelo de manera segura y estable. Utiliza la tecnología de programación cuadrática para calcular las trayectorias de los brazos en tiempo real.

## ¿Cómo funciona?

El 'Bimanual Controller' es el núcleo del paquete de control de movimiento. Conecta los dos brazos robóticos con un enlace virtual rígido, lo que permite calcular las trayectorias coordinadas en tiempo real. El usuario solo necesita especificar la posición objetivo del objeto virtual.

## ¿Por qué importa?

Este avance es fundamental para la robótica y la investigación en inteligencia artificial. Permite la creación de robots con dos brazos que puedan transportar objetos de manera segura y estable, lo que abre nuevas posibilidades en aplicaciones como la logística, la manufactura y la asistencia médica.

## Consejo técnico

Prueba el paquete de control de movimiento 'cyclo_control' con el ROBOTIS AI Worker y ajusta las parámetros de control para optimizar el transporte de objetos en tus proyectos de robótica.

```bash
qp - Una herramienta de programación cuadrática para calcular trayectorias en tiempo real.
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/tightly-coupled-bimanual-control-safe-and-stable-dual-arm-transport/55685](https://discourse.openrobotics.org/t/tightly-coupled-bimanual-control-safe-and-stable-dual-arm-transport/55685)
