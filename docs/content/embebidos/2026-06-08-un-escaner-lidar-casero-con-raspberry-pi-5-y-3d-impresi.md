# Un escáner LiDAR casero con Raspberry Pi 5 y 3D impresión

**Fecha:** 2026-06-08
**Categoría:** embebidos
**Tags:** robotica, diseño-3d, raspberry-pi
**Título original:** Peppe’s ghost LiDAR scanner

---

## Introducción

Un entusiasta de la robótica ha creado un escáner LiDAR casero utilizando un Raspberry Pi 5 y una impresión 3D. El resultado es un dispositivo capaz de capturar el mundo en forma de nube de puntos.

## ¿Qué es?

Un escáner LiDAR es un dispositivo que utiliza un haz de luz para crear una representación tridimensional de un entorno. En este caso, el escáner casero utiliza un LiDAR sensor para capturar la información y un Raspberry Pi 5 para procesarla y almacenarla en forma de nube de puntos.

## ¿Cómo funciona?

El escáner casero utiliza un Raspberry Pi 5 como cerebro, que se encarga de sincronizar la captura de imágenes con un LiDAR sensor y un IMU (acelerómetro y giroscopio). Las imágenes se capturan utilizando dos módulos de cámara Raspberry Pi CSI, mientras que el LiDAR sensor envía sus datos a través de la interfaz Ethernet. El escáner también incluye botones y una luz de estado para indicar cuando se está capturando información.

## ¿Por qué importa?

Este escáner casero puede ser utilizado para una variedad de aplicaciones, como la cartografía de cuevas, la apreciación de árboles antiguos, la arqueología y la detección de baches en carreteras. Además, el uso de un Raspberry Pi 5 y una impresión 3D hace que el dispositivo sea accesible y asequible para los entusiastas de la robótica.

## Consejo técnico

Si deseas crear un escáner LiDAR casero similar, puedes utilizar la librería OpenCV para procesar las imágenes y la biblioteca Python de Raspberry Pi para controlar el dispositivo.

```bash
pip install opencv-python
```

---

**Fuente original:** [https://www.raspberrypi.com/news/peppes-ghost-lidar-scanner/](https://www.raspberrypi.com/news/peppes-ghost-lidar-scanner/)
