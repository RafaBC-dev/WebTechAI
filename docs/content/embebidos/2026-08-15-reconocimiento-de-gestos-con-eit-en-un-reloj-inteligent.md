# Reconocimiento de gestos con EIT en un reloj inteligente

**Fecha:** 2026-08-15
**Categoría:** embebidos
**Tags:** robotica, microcontroladores, software-y-linux
**Título original:** EITWatch open-source ESP32-S3 smartwatch implements planar EIT hand gesture recognition

---

## Introducción

Investigadores de la Universidad de Northwestern han desarrollado EITWatch, un sistema de reconocimiento de gestos basado en tecnología de impedancia eléctrica que se ajusta a un reloj inteligente estándar. Este sistema utiliza un panel de ocho electrodos en la parte posterior del reloj para detectar cambios en la impedancia causados por el movimiento de músculos y tendones debajo de la piel.

## ¿Qué es?

EITWatch es un sistema de reconocimiento de gestos que utiliza tecnología de impedancia eléctrica para detectar cambios en la impedancia causados por el movimiento de músculos y tendones debajo de la piel. Se basa en un panel de ocho electrodos en la parte posterior del reloj y utiliza un protocolo de escaneo de múltiples profundidades para medir la impedancia en diferentes profundidades y ángulos.

## ¿Cómo funciona?

EITWatch utiliza un panel de ocho electrodos en la parte posterior del reloj para detectar cambios en la impedancia causados por el movimiento de músculos y tendones debajo de la piel. El sistema utiliza un protocolo de escaneo de múltiples profundidades, donde se mantiene un electrodo como fuente fija y se ciclea el electrodo negativo a través de los siete posiciones restantes. Esto permite medir la impedancia en diferentes profundidades y ángulos, lo que permite detectar gestos complejos.

## ¿Por qué importa?

EITWatch tiene aplicaciones en la robótica y la asistencia personal, ya que permite a los sistemas de asistencia personal reconocer y responder a gestos del usuario. También puede ser utilizado en aplicaciones de salud, como la detección de problemas de salud relacionados con el movimiento.

## Consejo técnico

Si deseas desarrollar un sistema de reconocimiento de gestos similar, puedes utilizar la plataforma ESP32-S3 y la biblioteca de desarrollo de Seeed Studio para crear un prototipo básico. Recuerda que debes ajustar la configuración del sistema para adaptarlo a tus necesidades específicas.

```bash
esp32-s3
```

---

**Fuente original:** [https://www.cnx-software.com/2026/08/14/eitwatch-open-source-esp32-s3-smartwatch-implements-planar-eit-hand-gesture-recognition/](https://www.cnx-software.com/2026/08/14/eitwatch-open-source-esp32-s3-smartwatch-implements-planar-eit-hand-gesture-recognition/)
