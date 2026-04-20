# Lenovo Legion Go y dispositivos Sony ganan soporte en Linux 7.1

**Fecha:** 2026-04-20
**Categoría:** linux
**Tags:** linux, robotica, codigo
**Título original:** New Lenovo Legion Go Drivers & More Sony HID Device Support In Linux 7.1

---

## Introducción

La versión en desarrollo de Linux 7.1 ha recibido actualizaciones en el subconjunto de dispositivos HID, lo que incluye soporte para nuevos dispositivos de control de juego y mejoras en la gestión de dispositivos.

## ¿Qué es?

El subconjunto de dispositivos HID (Human Interface Devices) es un conjunto de drivers y herramientas que permiten a Linux interactuar con dispositivos de control de juego, como controles de juego, teclados y ratones. Estos dispositivos son fundamentales para la experiencia de juego en Linux.

## ¿Cómo funciona?

Los drivers hid-lenovo-go y hid-lenovo-go-s han sido implementados para proporcionar soporte a los dispositivos Lenovo Legion Go. Estos drivers expenden configuraciones adicionales de los controles de juego, como la gestión de vibraciones, la configuración de LEDs RGB y la personalización de la experiencia de usuario. Además, se han agregado soporte a dispositivos de Sony Rock Band y DJ Hero Turntable, lo que permite a los usuarios utilizar estos dispositivos con Linux.

## ¿Por qué importa?

El soporte a estos dispositivos es importante porque permite a los usuarios de Linux disfrutar de una experiencia de juego más completa y personalizable. Los usuarios pueden ajustar configuraciones adicionales de los controles de juego y aprovechar al máximo sus dispositivos.

## Consejo técnico

Si tienes un dispositivo Lenovo Legion Go o un dispositivo de Sony Rock Band, puedes probar el soporte en Linux 7.1 ejecutando los comandos `sudo apt-get update` y `sudo apt-get install linux-image-7.1` para actualizar tu sistema y luego `sudo modprobe hid-lenovo-go` para cargar el driver.

```bash
sudo modprobe hid-lenovo-go
```

---

**Fuente original:** [https://www.phoronix.com/news/Linux-7.1-HID](https://www.phoronix.com/news/Linux-7.1-HID)
