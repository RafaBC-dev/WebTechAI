# Fusión de sensores para robots: un nuevo paquete de ROS 2 Jazzy

**Fecha:** 2026-03-29
**Categoría:** robotica
**Tags:** robotica, linux, codigo
**Título original:** Looking for real hardware testers: FusionCore ROS 2 Jazzy sensor fusion

---

## Introducción

Un desarrollador busca pruebas de hardware para su paquete de fusión de sensores, que combina IMU, encoders de ruedas y GPS para obtener una estimación de posición precisa y confiable.

## ¿Qué es?

FusionCore es un paquete de ROS 2 Jazzy diseñado para reemplazar robot_localization. Combina sensores como IMU, encoders de ruedas y GPS para obtener una estimación de posición precisa y confiable en tiempo real.

## ¿Cómo funciona?

FusionCore utiliza un filtro basado en el algoritmo de Kalman (UKF) para combinar las señales de los sensores y obtener una estimación de posición en coordenadas ECEF (Earth-Centered, Earth-Fixed). También incluye la estimación automática de sesgo de IMU y la detección de outliers mediante la regla de Mahalanobis.

## ¿Por qué importa?

Este paquete es importante para los desarrolladores de robots que buscan una solución de fusión de sensores confiable y precisa. FusionCore es una alternativa a robot_localization, que ha sido deprecado, y ofrece una configuración YAML simple y no requiere ajustes manuales de covarianza.

## Consejo técnico

Si estás utilizando robot_localization y has encontrado problemas con la configuración, prueba FusionCore y comparte tu configuración para que el desarrollador pueda adaptar el paquete a tus necesidades específicas.

```bash
Abrir un issue en el repositorio de GitHub de FusionCore: https://github.com/manankharwar/fusioncore
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/looking-for-real-hardware-testers-fusioncore-ros-2-jazzy-sensor-fusion/53616](https://discourse.openrobotics.org/t/looking-for-real-hardware-testers-fusioncore-ros-2-jazzy-sensor-fusion/53616)
