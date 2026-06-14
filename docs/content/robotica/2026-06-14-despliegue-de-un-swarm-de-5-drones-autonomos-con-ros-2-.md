# Despliegue de un swarm de 5 drones autónomos con ROS 2 y micro-ROS

**Fecha:** 2026-06-14
**Categoría:** robotica
**Tags:** robotica, drones, ros2
**Título original:** Swarm Drone Challenge 2026 — 5 drone swarm open-sourced, uROS, ROS2

---

## Introducción

Un equipo de desarrolladores ha lanzado un swarm de 5 drones autónomos que utiliza la tecnología ROS 2 y micro-ROS para coordinar sus acciones. Este proyecto es relevante ahora mismo debido a su aplicación en la robótica y la automatización.

## ¿Qué es?

El proyecto consiste en un swarm de 5 drones que se comunican entre sí y con un estación de tierra para coordinar sus acciones y realizar tareas en un escenario de captura de bandera. Los drones están equipados con sensores y cámaras para percibir su entorno y tomar decisiones en tiempo real.

## ¿Cómo funciona?

La coordinación del swarm se realiza mediante un nodo determinista en la estación de tierra que asigna roles a cada drone y envía waypoints a sus controladores. Los drones están equipados con micro-ROS, que actúa como puente entre la estación de tierra y los controladores de vuelo. Los controladores de vuelo utilizan MAVLink para comunicarse con la estación de tierra y realizar tareas en tiempo real.

## ¿Por qué importa?

Este proyecto es importante porque demuestra la capacidad de los drones autónomos para coordinar sus acciones y realizar tareas complejas en un entorno dinámico. También muestra la aplicación de la tecnología ROS 2 y micro-ROS en la robótica y la automatización.

## Consejo técnico

Si deseas implementar un swarm de drones autónomos en tu proyecto, puedes utilizar la tecnología ROS 2 y micro-ROS para coordinar sus acciones. Puedes empezar por instalar ROS 2 en tu estación de tierra y configurar los drones con micro-ROS y MAVLink.

```bash
sudo apt-get install ros2
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/swarm-drone-challenge-2026-5-drone-swarm-open-sourced-uros-ros2/55467](https://discourse.openrobotics.org/t/swarm-drone-challenge-2026-5-drone-swarm-open-sourced-uros-ros2/55467)
