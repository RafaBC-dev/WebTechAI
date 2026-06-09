# Rendimiento de tarjetas SD en CircuitPython: qué funcionan mejor

**Fecha:** 2026-06-09
**Categoría:** linux
**Tags:** microcontroladores, python, herramientas
**Título original:** SD Card Performance in CircuitPython #CircuitPython #AdafruitLearningSystem @Adafruit

---

## Introducción

La velocidad de las tarjetas SD es crucial en proyectos de robótica y electrónica. Un equipo de Adafruit ha realizado un estudio exhaustivo para determinar qué tarjetas y configuraciones funcionan mejor en CircuitPython.

## ¿Qué es?

CircuitPython es una versión de Python diseñada para microcontroladores, que permite a los desarrolladores crear aplicaciones de robótica y electrónica de manera sencilla. Las tarjetas SD son una herramienta común en estos proyectos, ya que permiten almacenar datos y programas en un formato fácil de leer.

## ¿Cómo funciona?

El estudio de Adafruit comparó el rendimiento de varias tarjetas SD en diferentes configuraciones, incluyendo SDIO y SPI, y diferentes tamaños de tarjeta y sistemas de archivos. Los resultados muestran que el SDIO es mejor para transferencias de datos en masa, mientras que el SPI es más rápido para escrituras pequeñas.

## ¿Por qué importa?

Este estudio es importante porque proporciona una guía clara para elegir la tarjeta SD adecuada para proyectos de robótica y electrónica. Al seleccionar la tarjeta adecuada, los desarrolladores pueden mejorar la velocidad y eficiencia de sus proyectos.

## Consejo técnico

Si estás trabajando con CircuitPython y tarjetas SD, considera utilizar una tarjeta de más de 32 GB con un sistema de archivos exFAT, ya que esto puede mejorar significativamente el rendimiento.

```bash
No aplica
```

---

**Fuente original:** [https://blog.adafruit.com/2026/06/08/sd-card-performance-in-circuitpython-circuitpython-adafruitlearningsystem-adafruit/](https://blog.adafruit.com/2026/06/08/sd-card-performance-in-circuitpython-circuitpython-adafruitlearningsystem-adafruit/)
