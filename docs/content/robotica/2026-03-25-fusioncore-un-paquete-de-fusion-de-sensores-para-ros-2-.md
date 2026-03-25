# FusionCore: un paquete de fusión de sensores para ROS 2 Jazzy

**Fecha:** 2026-03-25
**Categoría:** robotica
**Tags:** robotica, linux, codigo
**Título original:** FusionCore, which is a ROS 2 Jazzy sensor fusion package (robot_localization replacement)

---

## Introducción

El paquete de fusión de sensores FusionCore ha sido creado para resolver el problema de la falta de una herramienta de fusión de sensores fácil de usar para ROS 2 Jazzy. Con la desaparición de robot_localization, los desarrolladores de robots necesitaban una alternativa confiable y sencilla.

## ¿Qué es?

FusionCore es un paquete de ROS 2 Jazzy que fusiona datos de sensores IMU, encoders de ruedas y GPS/GNSS para obtener una estimación de posición confiable y precisa. Utiliza un filtro de Kalman no lineal (UKF) para combinar los datos de los sensores y proporcionar una estimación de posición en 3D.

## ¿Cómo funciona?

FusionCore utiliza un UKF para combinar los datos de los sensores IMU, encoders de ruedas y GPS/GNSS. El paquete también incluye una función de fusión de GNSS en coordenadas ECEF (coordenadas geocéntricas) para evitar problemas de zona UTM. Además, FusionCore puede fusionar datos de dos antenas de GPS para obtener una estimación de dirección precisa.

## ¿Por qué importa?

FusionCore es importante porque proporciona una herramienta de fusión de sensores fácil de usar y confiable para desarrolladores de robots que utilizan ROS 2 Jazzy. El paquete puede fusionar datos de diferentes sensores para obtener una estimación de posición precisa y confiable, lo que es fundamental para la navegación y la localización en robots.

## Consejo técnico

Si estás desarrollando un robot con GPS y encoders de ruedas en ROS 2 Jazzy, considera utilizar FusionCore para fusionar los datos de los sensores y obtener una estimación de posición precisa y confiable. Puedes encontrar el paquete en GitHub y configurarlo con una sola archivo YAML.

```bash
git clone https://github.com/manankharwar/fusioncore
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/fusioncore-which-is-a-ros-2-jazzy-sensor-fusion-package-robot-localization-replacement/53502](https://discourse.openrobotics.org/t/fusioncore-which-is-a-ros-2-jazzy-sensor-fusion-package-robot-localization-replacement/53502)
