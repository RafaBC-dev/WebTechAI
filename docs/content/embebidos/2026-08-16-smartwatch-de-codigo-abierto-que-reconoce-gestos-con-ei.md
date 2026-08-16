# Smartwatch de código abierto que reconoce gestos con EIT

**Fecha:** 2026-08-16
**Categoría:** embebidos
**Tags:** robotica, microcontroladores, software-y-linux
**Título original:** EITWatch open-source ESP32-S3 smartwatch implements planar EIT hand gesture recognition

---

## Introducción

Los investigadores de la Universidad Northwestern han creado un smartwatch de código abierto que puede reconocer gestos de la mano utilizando tecnología de tomografía de impedancia eléctrica (EIT). Este dispositivo, llamado EITWatch, se ajusta a un diseño estándar de reloj inteligente y utiliza una placa de circuito impreso (PCB) para detectar cambios en la impedancia causados por el movimiento de músculos y tendones debajo de la piel.

## ¿Qué es?

EITWatch es un sistema de gestión de EIT de código abierto que se basa en una placa ESP32-S3 de Seeed Studio y ocho electrodos dispuestos en la parte posterior del caso del reloj. Estos electrodos detectan cambios en la impedancia causados por el movimiento de la mano y envían señales a la placa de circuito impreso, que las procesa y reconoce los gestos.

## ¿Cómo funciona?

El sistema EITWatch utiliza una técnica de escaneo multi-fondo para detectar cambios en la impedancia en diferentes profundidades y ángulos. Esto se logra mediante la utilización de una matriz de 8x8 electrodos dispuestos en una rueda de 31 mm de diámetro, que se ajusta a un diseño estándar de reloj inteligente. La placa de circuito impreso procesa las señales de los electrodos y reconoce los gestos de la mano.

## ¿Por qué importa?

EITWatch puede tener aplicaciones en la medicina, la rehabilitación y la asistencia a personas con discapacidad. También puede ser utilizado en la industria para mejorar la eficiencia y la seguridad en la manipulación de objetos.

## Consejo técnico

Si deseas crear un sistema de EIT similar, puedes utilizar la placa ESP32-S3 de Seeed Studio y la biblioteca de EITWatch, que se encuentra disponible en GitHub. Asegúrate de seguir las instrucciones de configuración y programación para asegurarte de que tu sistema funcione correctamente.

```bash
git clone https://github.com/EITWatch/EITWatch.git
```

---

**Fuente original:** [https://www.cnx-software.com/2026/08/14/eitwatch-open-source-esp32-s3-smartwatch-implements-planar-eit-hand-gesture-recognition/](https://www.cnx-software.com/2026/08/14/eitwatch-open-source-esp32-s3-smartwatch-implements-planar-eit-hand-gesture-recognition/)
