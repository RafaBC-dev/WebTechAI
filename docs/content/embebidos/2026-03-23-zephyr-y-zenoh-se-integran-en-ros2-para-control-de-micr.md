# Zephyr y Zenoh se integran en ROS2 para control de microcontroladores

**Fecha:** 2026-03-23
**Categoría:** embebidos
**Tags:** robotica, microcontroladores, linux
**Título original:** Zephyr Zenoh integration for ROS2 control

---

## Introducción

Un proyecto en curso busca integrar Zephyr y Zenoh en ROS2 para crear un controlador de microcontroladores que permita la comunicación directa con ROS2 sin necesidad de un agente intermedio. Esto podría mejorar la eficiencia y la escalabilidad de los sistemas de control de robots.

## ¿Qué es?

Zephyr es un sistema operativo de tiempo real para microcontroladores, mientras que Zenoh es un protocolo de comunicación que permite la transmisión de datos de manera eficiente. La integración de Zephyr y Zenoh en ROS2 permitiría a los desarrolladores crear controladores de microcontroladores que puedan comunicarse directamente con ROS2 sin necesidad de un agente intermedio.

## ¿Cómo funciona?

La integración se lograría mediante la creación de un módulo de Zephyr que pueda crear un controlador de ROS2 dentro del microcontrolador, utilizando el protocolo Zenoh para la comunicación. El módulo utilizaría la biblioteca MicroCDR para la serialización y deserialización de datos, y la biblioteca ROSIDL para la gestión de tipos de mensajes.

## ¿Por qué importa?

Esta integración podría mejorar la eficiencia y la escalabilidad de los sistemas de control de robots, permitiendo la comunicación directa entre el microcontrolador y ROS2 sin necesidad de un agente intermedio. Esto podría ser especialmente útil en aplicaciones que requieren una alta velocidad de comunicación y una baja latencia.

## Consejo técnico

Si deseas implementar esta integración en tu propio proyecto, considera utilizar la biblioteca MicroCDR para la serialización y deserialización de datos, y la biblioteca ROSIDL para la gestión de tipos de mensajes.

```bash
ros_idl_generate_c ros package
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/zephyr-zenoh-integration-for-ros2-control/53452](https://discourse.openrobotics.org/t/zephyr-zenoh-integration-for-ros2-control/53452)
