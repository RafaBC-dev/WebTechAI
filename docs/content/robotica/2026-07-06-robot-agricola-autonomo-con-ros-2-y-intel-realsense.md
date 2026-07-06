# Robot Agrícola Autónomo con ROS 2 y Intel RealSense

**Fecha:** 2026-07-06
**Categoría:** robotica
**Tags:** robotica, linux, codigo
**Título original:** Showcase: Beam AgroBot V2 – Autonomous Agricultural Robot Built with ROS 2, Nav2, MoveIt 2 and RealSense

---

## Introducción

Un ingeniero en mecánica ha desarrollado un robot agrícola autónomo utilizando ROS 2, Nav2 y Intel RealSense. Este proyecto busca integrar componentes de un sistema robótico completo en una plataforma única.

## ¿Qué es?

El Beam AgroBot V2 es un robot agrícola autónomo que utiliza ROS 2 Humble como plataforma de simulación y desarrollo. Combina diseño mecánico, simulación, descripción de robot, navegación, percepción, manipulación y control en una sola workspace.

## ¿Cómo funciona?

El robot utiliza Nav2 para navegación autónoma, SLAM Toolbox para mapeo, AMCL para localización y MoveIt 2 para control de un manipulador robótico de 5 grados de libertad. También utiliza Intel RealSense para detección de cultivos y precision watering.

## ¿Por qué importa?

Este proyecto es relevante porque busca integrar componentes de un sistema robótico completo en una plataforma única, lo que puede ser útil para aplicaciones agrícolas y de investigación.

## Consejo técnico

Si estás desarrollando un proyecto con ROS 2, considera utilizar la SLAM Toolbox para mapeo y navegación autónoma.

```bash
ros2 run nav2_map_server
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/showcase-beam-agrobot-v2-autonomous-agricultural-robot-built-with-ros-2-nav2-moveit-2-and-realsense/56187](https://discourse.openrobotics.org/t/showcase-beam-agrobot-v2-autonomous-agricultural-robot-built-with-ros-2-nav2-moveit-2-and-realsense/56187)
