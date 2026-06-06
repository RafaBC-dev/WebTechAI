# Peppe's Ghost: un escáner LiDAR casero con Raspberry Pi

**Fecha:** 2026-06-06
**Categoría:** embebidos
**Tags:** robotica, linux, raspberry-pi
**Título original:** Peppe’s ghost LiDAR scanner

---

## Introducción

Un entusiasta ha creado un escáner LiDAR casero utilizando un Raspberry Pi 5 y un diseño 3D impresionado. El resultado es un dispositivo capaz de capturar el mundo en forma de punto nube.

## ¿Qué es?

Peppe's Ghost es un escáner LiDAR casero que utiliza un Raspberry Pi 5 como cerebro. El dispositivo es capaz de capturar el mundo en forma de punto nube utilizando un LiDAR sensor y dos módulos de cámara. El objetivo del proyecto es crear un dispositivo que pueda ser utilizado para misiones diversas, como la cartografía de cuevas o la apreciación de árboles antiguos.

## ¿Cómo funciona?

El escáner LiDAR casero utiliza un Raspberry Pi 5 que jala un LiDAR sensor, dos módulos de cámara y un sensor de movimiento. El LiDAR sensor envía datos a través de la interfaz Ethernet, mientras que las cámaras capturan imágenes en color sincronizadas. El sensor de movimiento se utiliza para sincronizar los datos de los diferentes sensores. El dispositivo utiliza un SSD para almacenar la gran cantidad de datos que se generan durante la captura de punto nube.

## ¿Por qué importa?

Peppe's Ghost es importante porque ofrece una solución casera y asequible para la captura de punto nube. El dispositivo puede ser utilizado para misiones diversas, como la cartografía de cuevas o la apreciación de árboles antiguos. Además, el uso de un Raspberry Pi 5 hace que el dispositivo sea fácil de programar y personalizar.

## Consejo técnico

Si deseas crear un escáner LiDAR casero similar, puedes utilizar el módulo de cámara de Raspberry Pi y el software de captura de punto nube de OpenCV. Puedes encontrar más información sobre la implementación en el proyecto de Peppe's Ghost en Instagram.

```bash
sudo apt-get install libopencv-dev
```

---

**Fuente original:** [https://www.raspberrypi.com/news/peppes-ghost-lidar-scanner/](https://www.raspberrypi.com/news/peppes-ghost-lidar-scanner/)
