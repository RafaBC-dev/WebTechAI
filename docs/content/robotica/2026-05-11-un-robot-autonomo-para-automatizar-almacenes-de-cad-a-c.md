# Un robot autónomo para automatizar almacenes: de CAD a código

**Fecha:** 2026-05-11
**Categoría:** robotica
**Tags:** robotica, linux, codigo
**Título original:** Built an Autonomous Mobile Robot (AMR) for warehouse automation - from CAD to code

---

## Introducción

Un equipo de desarrolladores ha creado un robot autónomo que puede navegar y servir peticiones en un almacén. Este proyecto utiliza tecnologías como ROS 2, Nav2 y Gazebo para lograr la autonomía del robot.

## ¿Qué es?

El robot autónomo es un proyecto que utiliza tecnologías de robótica y visión artificial para crear un sistema que puede navegar y servir peticiones en un almacén. El robot utiliza un chasis diseñado en Fusion 360 y exportado a URDF, y se ha implementado utilizando ROS 2.

## ¿Cómo funciona?

El robot utiliza la biblioteca Nav2 para la navegación y planificación de rutas, y ArUco para la alineación precisa. La secuencia de puntos de referencia se utiliza para realizar tareas en múltiples estantes. La simulación y visualización se realizan utilizando Gazebo y RViz.

## ¿Por qué importa?

Este proyecto es relevante porque puede automatizar tareas en almacenes, lo que puede mejorar la eficiencia y reducir costos. El robot puede navegar y servir peticiones de manera autónoma, lo que puede ser especialmente útil en entornos con espacio limitado.

## Consejo técnico

Si deseas implementar un sistema de navegación autónoma en tu proyecto, considera utilizar la biblioteca Nav2 y la herramienta Gazebo para simular y visualizar tu sistema.

```bash
ros2 launch my_robot.launch.py
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/built-an-autonomous-mobile-robot-amr-for-warehouse-automation-from-cad-to-code/54698](https://discourse.openrobotics.org/t/built-an-autonomous-mobile-robot-amr-for-warehouse-automation-from-cad-to-code/54698)
