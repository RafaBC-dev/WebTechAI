# Demostración de rechazo de outliers en FusionCore, un paquete de fusión de sensores ROS 2

**Fecha:** 2026-04-09
**Categoría:** robotica
**Tags:** robotica, linux, codigo
**Título original:** FusionCore demo: GPS outlier rejection in a ROS 2 filter built to replace robot_localization

---

## Introducción

La empresa FusionCore ha demostrado la eficacia de su paquete de fusión de sensores ROS 2 en una demostración de rechazo de outliers en un entorno de simulación. Esta tecnología es fundamental en la robótica para garantizar la precisión y la estabilidad de los sistemas de navegación.

## ¿Qué es?

FusionCore es un paquete de fusión de sensores ROS 2 que combina datos de IMU, encoders de rueda y GPS para proporcionar una ubicación precisa y estable. Reemplaza al paquete deprecado robot_localization y utiliza el algoritmo de fusión de Kalman UKF a una frecuencia de 100 Hz.

## ¿Cómo funciona?

El paquete FusionCore utiliza un algoritmo de fusión de Kalman UKF para combinar los datos de los diferentes sensores. El algoritmo utiliza la distancia de Mahalanobis para detectar y rechazar los outliers, que son valores anormales que pueden afectar la precisión de la ubicación. En la demostración, se inyectó un valor anormal en el sistema, pero el paquete FusionCore lo detectó y lo rechazó instantáneamente.

## ¿Por qué importa?

La demostración de FusionCore muestra la importancia de la precisión y la estabilidad en la robótica. La tecnología de fusión de sensores es fundamental para garantizar que los robots puedan navegar de manera precisa y segura en entornos complejos.

## Consejo técnico

Si deseas implementar una tecnología de fusión de sensores en tu proyecto de robótica, puedes utilizar el paquete FusionCore y ajustar el algoritmo de fusión de Kalman UKF para adaptarlo a tus necesidades específicas.

```bash
git clone https://github.com/manankharwar/fusioncore
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/fusioncore-demo-gps-outlier-rejection-in-a-ros-2-filter-built-to-replace-robot-localization/53887](https://discourse.openrobotics.org/t/fusioncore-demo-gps-outlier-rejection-in-a-ros-2-filter-built-to-replace-robot-localization/53887)
