# Robótica vs. atletas: robots que juegan ping-pong y corren maratones

**Fecha:** 2026-05-01
**Categoría:** robotica
**Tags:** robotica, ia-local, linux
**Título original:** Video Friday: Who Wins in Robot vs. Pro Ping-Pong Player?

---

## Introducción

En el mundo de la robótica, se están desarrollando sistemas cada vez más avanzados que pueden competir con los humanos en tareas físicas complejas. Recientemente, se han presentado varios proyectos que demuestran la capacidad de los robots para jugar ping-pong y correr maratones.

## ¿Qué es?

El proyecto Ringbot Quad es un robot monociclo con cuatro patas que combina la locomoción en ruedas y patas. Este robot puede cambiar entre dos modos de locomoción: modo de conducción, en el que las patas ayudan a mantener el equilibrio y la dirección, y modo de caminata, en el que las patas soportan el cuerpo para la locomoción cuadrúpeda. Además, se han presentado robots humanoides que han corrido una maratón en China, y un robot llamado AthenaZero que puede juntar objetos con la mano.

## ¿Cómo funciona?

Ringbot Quad utiliza cuatro módulos de conducción individuales, cada uno con una pierna articulada, para proporcionar movilidad versátil y eficiente. Las patas de Ringbot Quad pueden ayudar a mantener el equilibrio y la dirección en el modo de conducción, y soportar el cuerpo en el modo de caminata. Los robots humanoides utilizan tecnología de aprendizaje automático para correr la maratón, mientras que AthenaZero utiliza sensores y algoritmos para controlar la mano y juntar objetos.

## ¿Por qué importa?

Estos proyectos demuestran la capacidad de los robots para realizar tareas físicas complejas y competir con los humanos. También pueden tener aplicaciones en la automatización de tareas y la mejora de la eficiencia en la industria.

## Consejo técnico

Si deseas desarrollar un robot que pueda cambiar entre diferentes modos de locomoción, considera utilizar una plataforma de control de movimientos como la librería MoveIt! para ROS (Robot Operating System). Esto te permitirá crear un sistema de control de movimientos flexible y adaptable.

```bash
ros2 run moveit_demo --ros-args --ros-args __ns:=/move_group
```

---

**Fuente original:** [https://spectrum.ieee.org/video-friday-ping-pong-robot](https://spectrum.ieee.org/video-friday-ping-pong-robot)
