# Aprende la técnica de evitación de colisiones con el enfoque de ventana dinámica

**Fecha:** 2026-04-27
**Categoría:** robotica
**Tags:** robotica, ia-local, python
**Título original:** New collision avoidance exercise at Unibotics robot programming website: DWA

---

## Introducción

La Unibotics ha lanzado un nuevo ejercicio de práctica en su sitio web de programación de robots para aprender la técnica de evitación de colisiones con el enfoque de ventana dinámica (DWA). Este algoritmo es similar al CVM de Reid Simmons y se utiliza en el stack de navegación Nav2 de Open Navigation LLC.

## ¿Qué es?

El enfoque de ventana dinámica (DWA) es un algoritmo de evitación de colisiones para robots que se basa en la idea de que el robot debe evitar colisionar con obstáculos en su entorno. El algoritmo analiza la velocidad y la dirección del robot y los obstáculos para determinar la mejor ruta para evitar colisiones.

## ¿Cómo funciona?

El DWA funciona analizando la velocidad y la dirección del robot y los obstáculos en el entorno. Luego, el algoritmo determina la mejor ruta para evitar colisiones mediante la creación de una ventana dinámica que se mueve a lo largo de la trayectoria del robot. La ventana dinámica se utiliza para evaluar la seguridad de la ruta y determinar si es necesario cambiar la trayectoria del robot.

## ¿Por qué importa?

El DWA es importante porque proporciona una forma eficiente y efectiva de evitar colisiones en entornos complejos. Este algoritmo se utiliza en la navegación local del stack de navegación Nav2 de Open Navigation LLC, lo que lo hace relevante para la programación de robots y la inteligencia artificial.

## Consejo técnico

Si deseas practicar con el DWA, puedes utilizar el ejercicio de práctica disponible en la Unibotics. También puedes explorar la documentación del stack de navegación Nav2 y aprender más sobre la implementación del DWA en ROS.

```bash
ros2 run nav2_local_planner local_planner_dwa
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/new-collision-avoidance-exercise-at-unibotics-robot-programming-website-dwa/54330](https://discourse.openrobotics.org/t/new-collision-avoidance-exercise-at-unibotics-robot-programming-website-dwa/54330)
