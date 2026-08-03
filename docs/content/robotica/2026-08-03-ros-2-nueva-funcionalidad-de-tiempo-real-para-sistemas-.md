# ROS 2: Nueva funcionalidad de tiempo real para sistemas embebidos

**Fecha:** 2026-08-03
**Categoría:** robotica
**Tags:** robotica, embebidos, linux
**Título original:** ROS 2 Realtime Support Package

---

## Introducción

La comunidad de ROS 2 ha lanzado una nueva funcionalidad de tiempo real que permite a los desarrolladores crear sistemas embebidos más precisos y confiables. Esta funcionalidad es especialmente importante para aplicaciones de robótica y automatización.

## ¿Qué es?

La nueva funcionalidad de tiempo real de ROS 2 es un paquete llamado `ros2_realtime_support` que proporciona una forma de crear sistemas embebidos que satisfagan los requisitos de tiempo real. Este paquete ofrece una forma de gestionar los atributos de hilos y ejecutores de forma eficiente y precisa.

## ¿Cómo funciona?

Para utilizar la funcionalidad de tiempo real de ROS 2, los desarrolladores deben agregar la descripción del paquete a los archivos `CMakeLists.txt` y `package.xml`, agregar un archivo de configuración en formato YAML, cambiar la rutina principal en el archivo de fuente y cambiar las llamadas a `rclcpp::init` y `rclcpp::shutdown` al espacio de nombres `rclcpp_realtime`. Además, los ejecutores deben ser capaces de aplicar atributos de hilos proporcionados por `rclcpp_realtime`.

## ¿Por qué importa?

Esta funcionalidad es importante para aplicaciones de robótica y automatización que requieren precisión y confiabilidad. Al utilizar la funcionalidad de tiempo real de ROS 2, los desarrolladores pueden crear sistemas embebidos que satisfagan los requisitos de tiempo real y proporcionen una forma más eficiente y precisa de gestionar los atributos de hilos y ejecutores.

## Consejo técnico

Para aprovechar al máximo la funcionalidad de tiempo real de ROS 2, los desarrolladores deben leer la documentación y los ejemplos proporcionados en el paquete `ros2_realtime_support`. Esto les permitirá entender mejor cómo utilizar la funcionalidad y cómo aplicarla en sus proyectos.

```bash
ros2 run ros2_realtime_support examples_rclcpp_realtime
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/ros-2-realtime-support-package/57113](https://discourse.openrobotics.org/t/ros-2-realtime-support-package/57113)
