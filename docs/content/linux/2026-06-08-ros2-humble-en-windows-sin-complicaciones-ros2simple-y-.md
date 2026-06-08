# ROS2 Humble en Windows sin complicaciones: Ros2Simple y Rviz2Windows

**Fecha:** 2026-06-08
**Categoría:** linux
**Tags:** robotica, linux, codigo
**Título original:** Pre-built ROS2 Humble Windows SDK + Standalone RViz2 (No Toolchain Required)

---

## Introducción

Después de años de complicaciones, los desarrolladores de ROS2 en Windows pueden respirar aliviados. Dos proyectos recientes han simplificado la vida de los programadores: Ros2Simple y Rviz2Windows.

## ¿Qué es?

Ros2Simple es un SDK precompilado de ROS2 Humble para Windows x64 que permite a los desarrolladores construir aplicaciones ROS2 utilizando CMake directamente, sin necesidad de una herramienta de compilación nativa de ROS2. Rviz2Windows, por otro lado, es una versión independiente de RViz2 para Windows que puede ejecutarse simplemente al doblar el archivo de ejecutable.

## ¿Cómo funciona?

Ros2Simple se basa en la versión de ROS2 Humble para Windows x64 Debug y permite a los desarrolladores construir aplicaciones ROS2 utilizando CMake directamente, sin necesidad de una herramienta de compilación nativa de ROS2. Rviz2Windows, por otro lado, se construyó a partir de la fuente de ROS2 Humble y incluye todas las dependencias necesarias (Qt5, Ogre3D) para funcionar de manera independiente en Windows.

## ¿Por qué importa?

Estos proyectos importan porque permiten a los desarrolladores de ROS2 en Windows trabajar de manera más sencilla y eficiente, sin necesidad de configurar herramientas de compilación complejas o instalar dependencias adicionales.

## Consejo técnico

Si deseas empezar a trabajar con ROS2 en Windows, descarga Ros2Simple y Rviz2Windows y sigue las instrucciones de construcción para empezar a desarrollar aplicaciones ROS2 de manera sencilla.

```bash
cmake .. && cmake --build . --config Debug
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/pre-built-ros2-humble-windows-sdk-standalone-rviz2-no-toolchain-required/55340](https://discourse.openrobotics.org/t/pre-built-ros2-humble-windows-sdk-standalone-rviz2-no-toolchain-required/55340)
