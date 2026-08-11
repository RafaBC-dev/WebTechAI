# AMR autónomo para almacén con ROS 2, Gazebo y Nav2

**Fecha:** 2026-08-11
**Categoría:** robotica
**Tags:** robotica, linux, python
**Título original:** Autonomous Warehouse AMR with ROS 2 Jazzy, Gazebo Harmonic and Nav2

---

## Introducción

Un desarrollador ha creado un proyecto de AMR autónomo para almacén utilizando ROS 2, Gazebo y Nav2. Este proyecto permite simular la navegación de un robot en un entorno de almacén, detectando obstáculos y realizando misiones. La creación de este proyecto es relevante ahora mismo debido a la creciente demanda de tecnología autónoma en la logística y la automatización de procesos.

## ¿Qué es?

Un AMR (Autonomous Mobile Robot) es un robot que puede moverse de manera autónoma en un entorno determinado. En este caso, el proyecto consiste en crear un AMR que pueda navegar en un entorno de almacén, utilizando tecnologías como ROS 2, Gazebo y Nav2. El robot está equipado con un sensor de LiDAR 2D y puede detectar obstáculos y realizar misiones definidas en archivos YAML.

## ¿Cómo funciona?

El proyecto utiliza ROS 2 como framework de software para la creación de robots autónomos. Gazebo es utilizado para simular el entorno de almacén, mientras que Nav2 se utiliza para la navegación y la detección de obstáculos. El robot utiliza AMCL para la localización, robot_localization EKF para la odometría y SmacPlanner2D para la planificación de rutas. El proyecto también incluye un sistema de misiones que permite definir misiones en archivos YAML y un panel de control para monitorear el progreso de la misión.

## ¿Por qué importa?

Este proyecto es relevante porque resuelve problemas comunes en la logística y la automatización de procesos, como la navegación de robots en entornos complejos y la detección de obstáculos. La creación de este proyecto también puede ayudar a mejorar la eficiencia y la precisión en la automatización de procesos.

## Consejo técnico

Si deseas crear un proyecto similar, puedes utilizar el código de este proyecto como base y adaptarlo a tus necesidades. También puedes investigar sobre la integración de ROS 2 con otros frameworks de software y la creación de misiones en archivos YAML.

```bash
Para lanzar el proyecto, puedes utilizar el comando `ros2 launch autonomous_warehouse_amr.launch.py`
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/autonomous-warehouse-amr-with-ros-2-jazzy-gazebo-harmonic-and-nav2/57292](https://discourse.openrobotics.org/t/autonomous-warehouse-amr-with-ros-2-jazzy-gazebo-harmonic-and-nav2/57292)
