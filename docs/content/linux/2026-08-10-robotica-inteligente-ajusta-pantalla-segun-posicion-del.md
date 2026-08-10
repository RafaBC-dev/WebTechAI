# Robótica inteligente ajusta pantalla según posición del usuario

**Fecha:** 2026-08-10
**Categoría:** linux
**Tags:** robotica, ia-local, linux
**Título original:** ROS 2 Based Face Tracking Display Control with PiPER Robotic Arm

---

## Introducción

Un equipo de investigación ha desarrollado un sistema de trabajo inteligente que utiliza una mano robótica para ajustar la pantalla según la posición del usuario. Este proyecto combina tecnologías de visión artificial, robótica y control de movimiento para crear un entorno de trabajo más cómodo y eficiente.

## ¿Qué es?

El proyecto se basa en la integración de una mano robótica PiPER, una cámara RGB-D Orbbec y el sistema de robótica ROS 2. El sistema utiliza la detección de rostros con YOLOv5-Face y la percepción de profundidad para calcular la posición del usuario en 3D y controlar la mano robótica para ajustar la pantalla.

## ¿Cómo funciona?

El sistema funciona mediante la siguiente secuencia de pasos: la cámara RGB-D captura la imagen del usuario, YOLOv5-Face detecta el rostro y extrae los puntos de referencia, luego se calcula la posición del usuario en 3D utilizando la percepción de profundidad. Finalmente, se publica la posición del usuario y se calcula la posición objetivo de la pantalla, generando comandos de movimiento para la mano robótica.

## ¿Por qué importa?

Este proyecto es importante porque puede mejorar la comodidad y la eficiencia en entornos de trabajo que requieren la manipulación de pantallas o dispositivos electrónicos. También puede ser utilizado en aplicaciones de realidad aumentada y virtual.

## Consejo técnico

Si deseas implementar un sistema similar, puedes comenzar investigando sobre la integración de la cámara RGB-D Orbbec con ROS 2 y YOLOv5-Face. También es importante considerar la seguridad y la estabilidad del sistema, especialmente en entornos de trabajo que requieren la manipulación de objetos pesados o peligrosos.

```bash
sudo apt-get install ros-humble-ros-base
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/ros-2-based-face-tracking-display-control-with-piper-robotic-arm/57270](https://discourse.openrobotics.org/t/ros-2-based-face-tracking-display-control-with-piper-robotic-arm/57270)
