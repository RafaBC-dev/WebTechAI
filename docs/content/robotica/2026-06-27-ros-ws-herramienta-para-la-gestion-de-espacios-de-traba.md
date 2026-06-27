# ROS-Ws: Herramienta para la gestión de espacios de trabajo de ROS2

**Fecha:** 2026-06-27
**Categoría:** robotica
**Tags:** robotica, linux, codigo
**Título original:** Ros-ws: ROS2 workspace management tool

---

## Introducción

La gestión de múltiples proyectos en ROS2 puede ser un desafío. Una herramienta reciente llamada ROS-Ws busca simplificar la tarea de cambiar entre espacios de trabajo y automatizar la fuente de configuración.

## ¿Qué es?

ROS-Ws es una herramienta diseñada para facilitar la gestión de espacios de trabajo en ROS2. Permite crear, cambiar y automatizar la fuente de configuración de espacios de trabajo de manera rápida y sencilla.

## ¿Cómo funciona?

Para utilizar ROS-Ws, se crea un nuevo espacio de trabajo con `colcon build` y se registra automáticamente. Luego, se puede cambiar entre espacios de trabajo con el comando `ws switch` y automatizar la fuente de configuración en el archivo `bashrc` con `source $(ws locate)/install/setup.bash`.

## ¿Por qué importa?

ROS-Ws es importante porque resuelve el problema de la gestión de múltiples proyectos en ROS2, lo que puede ser un desafío para los desarrolladores. Al automatizar la fuente de configuración, se reduce el tiempo de configuración y se mejora la productividad.

## Consejo técnico

Para utilizar ROS-Ws, crea un nuevo espacio de trabajo con `mkdir ~/ws_name && cd ~/ws_name` y luego registra el espacio de trabajo con `ws create . /opt/ros/jazzy`. Luego, puedes cambiar entre espacios de trabajo con `ws switch ws_name` y automatizar la fuente de configuración en el archivo `bashrc`.

```bash
ws create . /opt/ros/jazzy
ws switch ws_name
cd ~/ws_name
source $(ws locate)/install/setup.bash
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/ros-ws-ros2-workspace-management-tool/55736](https://discourse.openrobotics.org/t/ros-ws-ros2-workspace-management-tool/55736)
