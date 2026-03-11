# ros2_info: Herramienta de información para ROS2 en un solo comando

**Fecha:** 2026-03-11
**Categoría:** robotica
**Tags:** herramientas, ros2, linux
**Título original:** ros2_info — A fastfetch-like system info tool for ROS2

---

## Introducción

Los desarrolladores de Open Robotics han creado una herramienta llamada ros2_info que permite obtener información detallada sobre el entorno de ROS2 con solo un comando. Esto incluye detalles sobre el distrito de ROS2, nodos, tópicos, servicios y acciones en ejecución, así como estadísticas del sistema y actualizaciones pendientes.

## ¿Qué es?

ros2_info es una herramienta de sistema que proporciona una instantánea completa del entorno de ROS2. Muestra información sobre el distrito de ROS2, nodos, tópicos, servicios y acciones en ejecución, y también detecta automáticamente el middleware DDS en uso. Además, muestra los espacios de trabajo de colcon, el estado de construcción y los paquetes ROS2 instalados, agrupados por categoría.

## ¿Cómo funciona?

La herramienta funciona creando un espacio de trabajo de colcon y construyendo el proyecto con el comando `colcon build --symlink-install`. Luego, se puede ejecutar la herramienta con el comando `ros2 run ros2_info ros2_info` o con la opción `--interactive` para una interfaz gráfica en el navegador.

## ¿Por qué importa?

ros2_info es importante porque proporciona una forma rápida y fácil de obtener información detallada sobre el entorno de ROS2, lo que puede ahorrar tiempo y esfuerzo a los desarrolladores. Además, puede ayudar a identificar problemas y a optimizar el rendimiento del sistema.

## Consejo técnico

Si estás trabajando con ROS2, te recomiendo instalar ros2_info y utilizarlo para obtener información detallada sobre tu entorno. Esto te permitirá identificar problemas y optimizar el rendimiento de tu sistema.

```bash
ros2 run ros2_info ros2_info
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/ros2-info-a-fastfetch-like-system-info-tool-for-ros2/53105](https://discourse.openrobotics.org/t/ros2-info-a-fastfetch-like-system-info-tool-for-ros2/53105)
