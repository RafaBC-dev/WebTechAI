# Unificador de escáneres LiDAR para ROS2: sin depender de PCL

**Fecha:** 2026-06-05
**Categoría:** robotica
**Tags:** robotica, linux, codigo
**Título original:** 2D-Scan Merger for ROS2!

---

## Introducción

Los robots que utilizan múltiples escáneres LiDAR pueden beneficiarse de un nuevo proyecto que fusiona los datos de todos ellos en un solo escáner. Esto puede ser útil para algoritmos de navegación autónoma y detección de obstáculos.

## ¿Qué es?

El proyecto 2D-Scan Merger for ROS2 es un nodo de ROS2 que se suscribe a múltiples temas de LaserScan, sincroniza los datos en el tiempo, los transforma utilizando TF2 y publica un solo escáner fusionado. Esto se logra sin utilizar PointCloud2 ni dependencias de PCL.

## ¿Cómo funciona?

El nodo utiliza un thread pool persistente para realizar la proyección de rayos en paralelo y una proyección directa de polar a binario. También ofrece opciones de calidad de servicio (QoS) por tema y un mecanismo de sincronización de dos pasos para evitar la pérdida de datos en caso de fallos de sincronización parciales.

## ¿Por qué importa?

Este proyecto es importante porque permite a los robots que utilizan múltiples escáneres LiDAR fusionar los datos de todos ellos de manera eficiente y sin depender de PCL. Esto puede ser útil para aplicaciones de navegación autónoma y detección de obstáculos.

## Consejo técnico

Si estás trabajando con múltiples escáneres LiDAR en ROS2, considera utilizar el proyecto 2D-Scan Merger for ROS2 para fusionar los datos de manera eficiente. Puedes encontrar el proyecto en GitHub y contribuir a su desarrollo.

```bash
git clone https://github.com/ali-pahlevani/2D_Scan_Merger_ROS2.git
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/2d-scan-merger-for-ros2/55274](https://discourse.openrobotics.org/t/2d-scan-merger-for-ros2/55274)
