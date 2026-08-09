# ROS2: Nueva característica de contenedores de desarrollo y actualización de plantilla de workspace

**Fecha:** 2026-08-09
**Categoría:** linux
**Tags:** robotica, linux, codigo
**Título original:** ROS2 Dev Container Feature + Workspace Update

---

## Introducción

La comunidad de ROS2 ha lanzado una nueva característica para los contenedores de desarrollo, que permite seleccionar la distribución de ROS2 en el archivo devcontainer.json y utilizar la misma configuración tanto para el desarrollo local como para la integración continua. Esto ha llevado a una actualización de la plantilla de workspace de VSCode para utilizar esta característica en lugar de las imágenes de Docker predefinidas.

## ¿Qué es?

ROS2 es una plataforma de software de código abierto para la robótica y la automatización, que permite a los desarrolladores crear aplicaciones de software para robots y sistemas embebidos. La característica de contenedores de desarrollo es una herramienta que permite a los desarrolladores crear entornos de desarrollo aislados y reproducibles para sus proyectos de ROS2.

## ¿Cómo funciona?

La característica de contenedores de desarrollo de ROS2 permite a los desarrolladores seleccionar la distribución de ROS2 en el archivo devcontainer.json, que es un archivo de configuración que define el entorno de desarrollo. Luego, la herramienta de contenedores de desarrollo crea un contenedor de desarrollo a partir de la distribución seleccionada, que incluye todas las herramientas y dependencias necesarias para el desarrollo de ROS2. Esto permite a los desarrolladores trabajar en su proyecto de ROS2 de manera aislada y reproducible, sin afectar el entorno de desarrollo local.

## ¿Por qué importa?

La característica de contenedores de desarrollo de ROS2 es importante porque permite a los desarrolladores crear entornos de desarrollo aislados y reproducibles, lo que facilita la colaboración y la integración continua. Además, esta característica reduce la complejidad de la configuración de los entornos de desarrollo y permite a los desarrolladores enfocarse en el desarrollo de su proyecto.

## Consejo técnico

Si estás utilizando ROS2 con contenedores de desarrollo, puedes aprovechar esta característica seleccionando la distribución de ROS2 en el archivo devcontainer.json y utilizando la plantilla de workspace actualizada de VSCode.

```bash
devcontainer.json: { "distro": "lyrical", "package": "desktop" }
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/ros2-dev-container-feature-workspace-update/57243](https://discourse.openrobotics.org/t/ros2-dev-container-feature-workspace-update/57243)
