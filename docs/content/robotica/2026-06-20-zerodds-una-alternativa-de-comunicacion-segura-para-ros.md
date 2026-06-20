# ZeroDDS: una alternativa de comunicación segura para ROS 2

**Fecha:** 2026-06-20
**Categoría:** robotica
**Tags:** robotica, linux, codigo
**Título original:** ZeroDDS: a pure-Rust RMW for ROS 2 (rc.3), built against 349 real ROS↔DDS pain reports

---

## Introducción

ZeroDDS es un proyecto que busca abordar los problemas de comunicación en ROS 2, una plataforma de robótica de código abierto. Después de recopilar 349 informes de problemas reales, los desarrolladores han creado una solución alternativa que es segura, escalable y fácil de usar.

## ¿Qué es?

ZeroDDS es un sistema de comunicación de datos distribuidos (DDS) escrito en Rust, que se integra con ROS 2 para proporcionar una comunicación segura y confiable entre nodos. Utiliza la tecnología RTPS 2.5 y es compatible con la plataforma ROS 2.

## ¿Cómo funciona?

ZeroDDS funciona creando un sistema de comunicación que se basa en la tecnología DDS. Los nodos se comunican entre sí a través de un sistema de publicación y suscripción, y la plataforma utiliza la tecnología RTPS 2.5 para garantizar la seguridad y la confiabilidad de la comunicación. Además, ZeroDDS utiliza la tecnología de memoria compartida para reducir la latencia y mejorar el rendimiento.

## ¿Por qué importa?

ZeroDDS importa porque resuelve los problemas de comunicación en ROS 2, como la incompatibilidad entre nodos y la pérdida de conexión en redes inalámbricas. Además, proporciona una solución escalable y segura para la comunicación entre nodos en entornos de robótica de código abierto.

## Consejo técnico

Si estás utilizando ROS 2 y tienes problemas de comunicación, prueba utilizar ZeroDDS como alternativa de comunicación segura y confiable. Puedes instalarlo mediante el comando `ros2 run zerodds` y configurarlo para que se comunique con tus nodos de ROS 2.

```bash
ros2 run zerodds
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/zerodds-a-pure-rust-rmw-for-ros-2-rc-3-built-against-349-real-ros-dds-pain-reports/55581](https://discourse.openrobotics.org/t/zerodds-a-pure-rust-rmw-for-ros-2-rc-3-built-against-349-real-ros-dds-pain-reports/55581)
