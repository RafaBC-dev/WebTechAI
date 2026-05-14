# Sensor LiDAR Matrix: una visión 3D para robots y aplicaciones

**Fecha:** 2026-05-14
**Categoría:** robotica
**Tags:** robotica, esp32, python
**Título original:** LiDAR Matrix Sensor Sees in 3D

---

## Introducción

Un equipo de Mellow_Labs ha experimentado con sensores LiDAR Matrix y ha logrado integrarlos en un robot para crear una visión 3D. Esto abre nuevas posibilidades para la navegación autónoma y la detección de obstáculos.

## ¿Qué es?

Un sensor LiDAR Matrix es un dispositivo que utiliza tecnología de tiempo de vuelo para crear una imagen 2D de la distancia de objetos en su entorno. Se compone de una matriz de 64 sensores que pueden detectar distancias desde 2 cm hasta 3,5 metros.

## ¿Cómo funciona?

El sensor LiDAR Matrix funciona creando una matriz de distancias en 2D mediante la lectura de los sensores individuales. El robot utiliza esta información para crear una visión 3D de su entorno. El equipo de Mellow_Labs utilizó un LLM (Modelo de Lenguaje Lógico) para escribir la mayoría del código y realizar iteraciones para optimizar el funcionamiento del sensor.

## ¿Por qué importa?

Esta tecnología puede ser utilizada en aplicaciones de navegación autónoma, detección de obstáculos y mapeo de entornos. El sensor LiDAR Matrix puede ser especialmente útil en entornos complejos o hostiles donde la visión 3D es esencial.

## Consejo técnico

Si deseas integrar un sensor LiDAR Matrix en tu propio proyecto de robotica, considera utilizar una plataforma como ESP32 y una biblioteca de código como Python para leer y procesar los datos del sensor.

```bash
python -m pip install esp32
```

---

**Fuente original:** [https://hackaday.com/2026/05/14/lidar-matrix-sensor-sees-in-3d/](https://hackaday.com/2026/05/14/lidar-matrix-sensor-sees-in-3d/)
