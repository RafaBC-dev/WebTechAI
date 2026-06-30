# Control Offboard con PX4 y ROS 2: una solución segura para drones autónomos

**Fecha:** 2026-06-30
**Categoría:** robotica
**Tags:** robotica, drones, linux
**Título original:** Offboard Control with PX4 & ROS 2 (Micro XRCE-DDS)

---

## Introducción

Los desarrolladores de drones autónomos saben que el modo Offboard de PX4 puede ser un desafío. Sin embargo, una solución reciente utiliza ROS 2 y Micro XRCE-DDS para implementar un estado de máquina no bloqueante que garantiza la seguridad y estabilidad del vuelo.

## ¿Qué es?

El modo Offboard de PX4 es un estado de vuelo en el que el drone se controla a través de una conexión externa, como un sistema de navegación o una estación de control. Sin embargo, para evitar problemas de seguridad, PX4 requiere que el drone reciba una serie continua de setpoints (órdenes de vuelo) antes de permitir el cambio de modo. La solución reciente utiliza ROS 2 y Micro XRCE-DDS para implementar un estado de máquina no bloqueante que garantiza la seguridad y estabilidad del vuelo.

## ¿Cómo funciona?

La solución utiliza un estado de máquina no bloqueante que se ejecuta en un hilo separado, utilizando el timer `rclcpp::Node::create_wall_timer` de ROS 2. El estado de máquina cuenta hasta 20 ciclos (1 segundo) y publica setpoints dummy para satisfacer el requisito de PX4. Luego, publica el comando Offboard y, finalmente, publica los setpoints reales del trayecto a 20 Hz.

## ¿Por qué importa?

Esta solución es importante porque resuelve un problema común en la programación de drones autónomos y proporciona una forma segura y estable de cambiar el modo Offboard de PX4. Además, utiliza tecnologías como ROS 2 y Micro XRCE-DDS, que son ampliamente utilizadas en la industria de la robótica.

## Consejo técnico

Si estás desarrollando un sistema de drones autónomos, considera utilizar un estado de máquina no bloqueante como la solución presentada en este artículo. Puedes utilizar el timer `rclcpp::Node::create_wall_timer` de ROS 2 para implementar un estado de máquina que se ejecute en un hilo separado y garantice la seguridad y estabilidad del vuelo.

```bash
rclcpp::Node::create_wall_timer(50, std::bind(&EstadoDeMáquina::callback, this))
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/offboard-control-with-px4-ros-2-micro-xrce-dds/55936](https://discourse.openrobotics.org/t/offboard-control-with-px4-ros-2-micro-xrce-dds/55936)
