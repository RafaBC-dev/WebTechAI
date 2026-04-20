# ROS2 CLI con soporte de color: un cambio visual agradable

**Fecha:** 2026-04-20
**Categoría:** robotica
**Tags:** robotica, linux, codigo
**Título original:** Colorful ROS2 Command Line!

---

## Introducción

La comunidad de ROS2 ha lanzado una actualización interesante para el comando de línea ros2cli, que permite visualizar la salida de comandos y resultados con colores. Esto puede mejorar la legibilidad y la experiencia del usuario. ¿Qué cambios concretos se han realizado y por qué puede ser útil?

## ¿Qué es?

ROS2 CLI es una herramienta de línea de comandos desarrollada por la comunidad de ROS2, que permite interactuar con el entorno de desarrollo de ROS2 de manera sencilla y eficiente. Se utiliza para realizar tareas como la gestión de nodos, la ejecución de comandos y la visualización de resultados.

## ¿Cómo funciona?

La actualización de ros2cli incluye el soporte de color, que se puede activar mediante la variable de entorno ROS_COLORIZED_OUTPUT=1. Esto permite que los resultados y mensajes de error se visualicen con colores, lo que puede mejorar la legibilidad y la experiencia del usuario. La implementación se ha realizado mediante una actualización del código fuente de ros2cli.

## ¿Por qué importa?

La adición de soporte de color a ros2cli puede ser útil para desarrolladores y usuarios de ROS2 que necesitan visualizar resultados y mensajes de error de manera clara y eficiente. Esto puede reducir el tiempo de respuesta y mejorar la productividad en tareas de desarrollo y depuración.

## Consejo técnico

Si deseas activar el soporte de color en ros2cli, asegúrate de establecer la variable de entorno ROS_COLORIZED_OUTPUT=1 antes de ejecutar el comando. Puedes hacer esto mediante la línea de comandos o mediante la configuración de tu entorno de desarrollo.

```bash
ROS_COLORIZED_OUTPUT=1
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/colorful-ros2-command-line/54165](https://discourse.openrobotics.org/t/colorful-ros2-command-line/54165)
