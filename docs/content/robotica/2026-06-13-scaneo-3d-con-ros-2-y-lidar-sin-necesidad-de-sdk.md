# Scaneo 3D con ROS 2 y LiDAR sin necesidad de SDK

**Fecha:** 2026-06-13
**Categoría:** robotica
**Tags:** robotica, linux, codigo
**Título original:** STS3215 pan/tilt + LD19: a no-SDK 3D scanning module for ROS 2 Jazzy

---

## Introducción

Un desarrollador ha creado un sistema de escaneo 3D utilizando ROS 2 y un LiDAR 2D sin necesidad de SDK. Este sistema puede ser utilizado en aplicaciones de robótica y automatización.

## ¿Qué es?

El sistema de escaneo 3D utiliza un plataforma de giro y tilte 2-DOF y un LiDAR 2D para capturar imágenes en 3D. El sistema se basa en ROS 2 y utiliza una asambleadora para crear un punto de nube 3D a partir de las imágenes capturadas.

## ¿Cómo funciona?

El sistema utiliza dos servos Feetech STS3215 para controlar la plataforma de giro y tilte, y un LiDAR LDROBOT LD19 para capturar las imágenes. La asambleadora utiliza la información de la plataforma de giro y tilte y las imágenes capturadas para crear un punto de nube 3D. El sistema también incluye un puente MQTT para permitir que un controlador externo pueda disparar las capturas y recibir un handshake de finalización.

## ¿Por qué importa?

Este sistema es importante porque permite la creación de escaneos 3D sin necesidad de SDK, lo que reduce la complejidad y el costo de implementación. También puede ser utilizado en aplicaciones de robótica y automatización, como la creación de mapas de entornos y la detección de objetos.

## Consejo técnico

Si deseas implementar un sistema de escaneo 3D similar, puedes utilizar la librería ROS 2 y la asambleadora proporcionada en el proyecto GitHub. También es recomendable utilizar un LiDAR 2D compatible con el sistema y configurar correctamente la plataforma de giro y tilte.

```bash
ros2 run pan_tilt_lidar pan_tilt_lidar_node
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/sts3215-pan-tilt-ld19-a-no-sdk-3d-scanning-module-for-ros-2-jazzy/55447](https://discourse.openrobotics.org/t/sts3215-pan-tilt-ld19-a-no-sdk-3d-scanning-module-for-ros-2-jazzy/55447)
