# Peppe's Ghost: Un Escáner LiDAR Casero con Raspberry Pi

**Fecha:** 2026-06-07
**Categoría:** embebidos
**Tags:** robotica, diseño-3d, linux
**Título original:** Peppe’s ghost LiDAR scanner

---

## Introducción

Un entusiasta de la robótica ha creado un escáner LiDAR casero utilizando un Raspberry Pi 5 y un shell 3D impreso. Este dispositivo puede capturar el mundo como un punto nube y ha generado mucha expectación en la comunidad de diseñadores, arquitectos y entusiastas de la robótica.

## ¿Qué es?

Peppe's Ghost es un escáner LiDAR casero creado utilizando un Raspberry Pi 5 y un shell 3D impreso. Este dispositivo utiliza un sensor LiDAR para capturar el mundo como un punto nube, que es una representación tridimensional del entorno. El escáner también cuenta con cámaras RGB y un IMU para obtener información adicional sobre el entorno.

## ¿Cómo funciona?

El escáner Peppe's Ghost utiliza un Raspberry Pi 5 como cerebro, que se encarga de gestionar la información de los diferentes sensores. El sensor LiDAR envía su datos a través de la interfaz Ethernet, mientras que las cámaras RGB y el IMU proporcionan información adicional sobre el entorno. El escáner también cuenta con botones y un LED de estado para indicar cuando se está realizando una escaneo.

## ¿Por qué importa?

Peppe's Ghost es importante porque puede ser utilizado para una variedad de aplicaciones, como la cartografía de cuevas, la apreciación de árboles antiguos, la arqueología y la detección de baches. El escáner también puede ser utilizado para crear modelos tridimensionales del entorno, lo que puede ser útil para diseñadores y arquitectos.

## Consejo técnico

Si deseas crear un escáner LiDAR casero similar, puedes utilizar el software Raspbian en tu Raspberry Pi y configurar el sensor LiDAR para que envíe sus datos a través de la interfaz Ethernet. También puedes utilizar la biblioteca OpenCV para procesar los datos de las cámaras RGB y crear modelos tridimensionales del entorno.

```bash
sudo apt-get update && sudo apt-get install libopenmpi-dev libopenmpi-dbg libopenmpi-contrib
```

---

**Fuente original:** [https://www.raspberrypi.com/news/peppes-ghost-lidar-scanner/](https://www.raspberrypi.com/news/peppes-ghost-lidar-scanner/)
