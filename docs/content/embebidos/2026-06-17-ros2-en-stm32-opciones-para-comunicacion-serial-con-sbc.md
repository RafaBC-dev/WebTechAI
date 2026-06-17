# ROS2 en STM32: opciones para comunicación serial con SBC

**Fecha:** 2026-06-17
**Categoría:** embebidos
**Tags:** robotica, microcontroladores, software y linux
**Título original:** ROS2 on STM32 serial to SBC

---

## Introducción

Un desarrollador está buscando la mejor forma de conectar un microcontrolador STM32 con un SBC (Sistema en un Chip) para crear un robot con ROS2. Explora tres opciones para la comunicación serial.

## ¿Qué es?

ROS2 (Robot Operating System 2) es una plataforma de software para la robótica que permite la comunicación entre diferentes componentes de un robot. Un SBC es un sistema en un chip que puede ejecutar un sistema operativo y realizar tareas de cómputo. Un microcontrolador STM32 es un procesador pequeño que se utiliza en aplicaciones de control y medición.

## ¿Cómo funciona?

El desarrollador está explorando tres opciones para conectar el STM32 con el SBC: micro-ROS, Zenoh-Pico y Pico-ROS. Cada opción tiene sus ventajas y desventajas, y el desarrollador busca experiencia y consejos de otros para determinar la mejor opción.

## ¿Por qué importa?

La conexión entre el STM32 y el SBC es crucial para la creación de un robot con ROS2. La elección de la opción correcta puede afectar la estabilidad, la velocidad y la fiabilidad del robot.

## Consejo técnico

Si estás considerando utilizar ROS2 con un STM32 y un SBC, investiga la documentación de Zenoh-Pico y Pico-ROS, y considera la posibilidad de utilizar la herramienta Zenoh-bridge-dds para facilitar la comunicación entre los dos componentes.

```bash
zenoh-bridge-dds
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/ros2-on-stm32-serial-to-sbc/55510](https://discourse.openrobotics.org/t/ros2-on-stm32-serial-to-sbc/55510)
