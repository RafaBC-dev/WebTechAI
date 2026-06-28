# Gestión de espacios de trabajo ROS2 con ws: una herramienta útil

**Fecha:** 2026-06-28
**Categoría:** robotica
**Tags:** robotica, linux, codigo
**Título original:** Ros-ws: ROS2 workspace management tool

---

## Introducción

Los desarrolladores de ROS2 a menudo trabajan en múltiples proyectos, cada uno con su propio espacio de trabajo. Una herramienta reciente llamada ws simplifica la gestión de estos espacios de trabajo y la configuración de los entornos de desarrollo.

## ¿Qué es?

ws es una herramienta de línea de comandos diseñada para gestionar espacios de trabajo de ROS2. Permite crear, cambiar y automatizar la configuración de los entornos de desarrollo para cada proyecto.

## ¿Cómo funciona?

Para crear un nuevo espacio de trabajo, se utiliza el comando `ws create` seguido del nombre del espacio de trabajo y la ruta del repositorio. Una vez creado, se puede cambiar al espacio de trabajo con `ws switch` y configurar la fuente de la configuración de ROS2 con `source $(ws locate)/install/setup.bash`.

## ¿Por qué importa?

ws simplifica la gestión de espacios de trabajo de ROS2 y reduce la complejidad de la configuración de los entornos de desarrollo. Esto permite a los desarrolladores trabajar de manera más eficiente y enfocarse en la creación de aplicaciones de robótica.

## Consejo técnico

Para configurar la fuente de la configuración de ROS2 en un entorno de desarrollo, agrega la siguiente línea a tu archivo `.bashrc`: `source $(ws locate)/install/setup.bash`. Esto asegurará que la configuración de ROS2 esté disponible en todas las ventanas de comandos.

```bash
ws create, ws switch, source $(ws locate)/install/setup.bash
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/ros-ws-ros2-workspace-management-tool/55736](https://discourse.openrobotics.org/t/ros-ws-ros2-workspace-management-tool/55736)
