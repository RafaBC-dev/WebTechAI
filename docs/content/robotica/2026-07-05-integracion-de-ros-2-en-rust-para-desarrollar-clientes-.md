# Integración de ROS 2 en Rust para desarrollar clientes ROS 2

**Fecha:** 2026-07-05
**Categoría:** robotica
**Tags:** robotica, codigo, linux
**Título original:** Announcing ros-env: Access ROS 2 messages from Rust with just Cargo

---

## Introducción

Los desarrolladores de robótica pueden ahora crear clientes ROS 2 en Rust sin necesidad de utilizar Colcon o la biblioteca ros2_rust. Esto se logra gracias a la biblioteca ros-env, que permite acceder a los mensajes ROS 2 desde cualquier paquete en el entorno ROS 2.

## ¿Qué es?

ros-env es una biblioteca de Rust que permite acceder a los mensajes ROS 2 de manera unificada. Se puede utilizar como una dependencia de Cargo y se integra con la herramienta rosidl_generator_rs para generar código Rust para los mensajes ROS 2.

## ¿Cómo funciona?

La biblioteca ros-env se utiliza para importar los mensajes ROS 2 en el código Rust. Por ejemplo, se puede utilizar la línea `use ros_env::shape_msgs::msg::Plane;` para importar el mensaje `Plane` del paquete `shape_msgs`. La biblioteca ros-env se encarga de encontrar el paquete y cargar el mensaje correspondiente.

## ¿Por qué importa?

La integración de ROS 2 en Rust es importante para los desarrolladores de robótica que buscan crear clientes ROS 2 de manera eficiente y fácil de usar. La biblioteca ros-env simplifica el proceso de acceso a los mensajes ROS 2 y permite a los desarrolladores enfocarse en la lógica de su aplicación.

## Consejo técnico

Si deseas utilizar la biblioteca ros-env en tu proyecto, asegúrate de agregarla como dependencia de Cargo en tu archivo `Cargo.toml` y utilizar la herramienta rosidl_generator_rs para generar código Rust para los mensajes ROS 2.

```bash
rosidl_generator_rs
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/announcing-ros-env-access-ros-2-messages-from-rust-with-just-cargo/56141](https://discourse.openrobotics.org/t/announcing-ros-env-access-ros-2-messages-from-rust-with-just-cargo/56141)
