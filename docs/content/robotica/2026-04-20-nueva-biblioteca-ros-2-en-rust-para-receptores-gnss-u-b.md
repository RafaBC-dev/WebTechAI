# Nueva biblioteca ROS 2 en Rust para receptores GNSS u-blox ZED-F9P

**Fecha:** 2026-04-20
**Categoría:** robotica
**Tags:** robotica, embebidos, linux
**Título original:** Oxide GNSS — a Rust-based ROS 2 driver for u-blox ZED-F9P with NTRIP and integrity monitoring

---

## Introducción

La comunidad de robótica y sistemas embebidos ha recibido una noticia importante con la creación de una nueva biblioteca ROS 2 en Rust para receptores GNSS u-blox ZED-F9P. Esta biblioteca, llamada oxide_gnss, permite a los desarrolladores obtener datos de posición, velocidad y dirección con facilidad y seguridad.

## ¿Qué es?

La biblioteca oxide_gnss es un driver de ROS 2 para receptores GNSS u-blox ZED-F9P que proporciona una forma sencilla y segura de obtener datos de posición, velocidad y dirección. Está construida con ros2-rust (rclrs) y está licenciada bajo la licencia MIT.

## ¿Cómo funciona?

La biblioteca oxide_gnss utiliza un enfoque basado en modos para configurar el receptor GNSS, permitiendo a los desarrolladores elegir entre diferentes configuraciones, como standalone, rover, base móvil o base estática. También incluye un cliente NTRIP integrado y un sistema de monitoreo de integridad para detectar posibles interferencias o falsificaciones.

## ¿Por qué importa?

Esta biblioteca es importante porque proporciona una forma sencilla y segura de obtener datos de posición, velocidad y dirección, lo que es fundamental para aplicaciones de robótica y sistemas embebidos. También permite a los desarrolladores integrar fácilmente el receptor GNSS en sus proyectos y monitorear la integridad de los datos.

## Consejo técnico

Si deseas empezar a utilizar la biblioteca oxide_gnss, te recomiendo consultar la documentación y los ejemplos de código proporcionados en el repositorio de GitHub. También es importante configurar correctamente el receptor GNSS y la configuración del cliente NTRIP para asegurarte de obtener datos precisos y seguros.

```bash
oxide_gnss_assign_serial
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/oxide-gnss-a-rust-based-ros-2-driver-for-u-blox-zed-f9p-with-ntrip-and-integrity-monitoring/54169](https://discourse.openrobotics.org/t/oxide-gnss-a-rust-based-ros-2-driver-for-u-blox-zed-f9p-with-ntrip-and-integrity-monitoring/54169)
