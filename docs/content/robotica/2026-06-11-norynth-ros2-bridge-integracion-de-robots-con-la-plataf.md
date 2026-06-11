# Norynth ROS2 Bridge: integración de robots con la plataforma de nube

**Fecha:** 2026-06-11
**Categoría:** robotica
**Tags:** robotica, linux, codigo
**Título original:** norynth/ros2-bridge — ROS2 fleet management, telemetry & command dispatch

---

## Introducción

La empresa Norynth Robotics ha lanzado un paquete ROS2 llamado norynth/ros2-bridge, que permite integrar robots con la plataforma de nube de la empresa. Esto abre la puerta a una gestión más eficiente de flotas de robots y la capacidad de enviar comandos y recibir datos en tiempo real.

## ¿Qué es?

El norynth/ros2-bridge es un paquete ROS2 que permite a los robots conectarse a la plataforma de nube de Norynth Robotics. Esto incluye la sincronización de la flota, la transmisión de telemetría y la recepción de comandos. El paquete también admite la gestión de misiones y la supervisión de los robots.

## ¿Cómo funciona?

El norynth/ros2-bridge funciona mediante la publicación de temas ROS2 (como la batería, la odometría y el estado del robot) en la plataforma de nube de Norynth Robotics. Los comandos recibidos de la plataforma se convierten en temas ROS2 que se pueden leer por los robots. El paquete admite las versiones Humble, Iron y Rolling de ROS2.

## ¿Por qué importa?

La integración de robots con la plataforma de nube de Norynth Robotics permite a los desarrolladores crear aplicaciones más complejas y eficientes. Los robots pueden ser gestionados de manera remota, lo que reduce la necesidad de intervención humana en el campo. Además, la plataforma de nube proporciona herramientas para la supervisión y el análisis de datos, lo que ayuda a mejorar la toma de decisiones.

## Consejo técnico

Si deseas integrar tus robots con la plataforma de nube de Norynth Robotics, asegúrate de revisar la documentación de ROS2 y la API de la plataforma de nube. Utiliza herramientas como `ros2 run` y `ros2 topic echo` para publicar y leer temas ROS2.

```bash
ros2 run norynth/ros2-bridge
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/norynth-ros2-bridge-ros2-fleet-management-telemetry-command-dispatch/55402](https://discourse.openrobotics.org/t/norynth-ros2-bridge-ros2-fleet-management-telemetry-command-dispatch/55402)
