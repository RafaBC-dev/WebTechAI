# OpenC6 BIOS: un proyecto de firmware para ESP32-C6 con actualizaciones en vivo

**Fecha:** 2026-06-25
**Categoría:** embebidos
**Tags:** robotica, embebidos, esp32
**Título original:** OpenC6 BIOS project brings PC-like firmware to ESP32-C6 MCU with network boot and OTA update support

---

## Introducción

Un equipo de desarrolladores ha lanzado OpenC6 BIOS, un proyecto de firmware que permite a los dispositivos con ESP32-C6 ejecutar código de aplicaciones separado del firmware base, lo que facilita la actualización y el mantenimiento de los sistemas.

## ¿Qué es?

OpenC6 BIOS es un proyecto de firmware abierto que se basa en la arquitectura ESP32-C6 y permite ejecutar código de aplicaciones separado del firmware base. Esto significa que los desarrolladores pueden crear pequeñas cargas de trabajo que se puedan cargar y ejecutar en el dispositivo sin necesidad de recompilar el firmware completo.

## ¿Cómo funciona?

El BIOS se ejecuta primero después del arranque y realiza la inicialización del hardware. Luego expone servicios a través de una interfaz de aplicación binaria definida (ABI), lo que permite a las cargas de trabajo de aplicaciones acceder a funciones del BIOS sin necesidad de enlazar con el firmware completo. Las cargas de trabajo de aplicaciones pueden ser cargadas en memoria RAM o flash (XIP) y utilizar servicios del BIOS a través de la ABI.

## ¿Por qué importa?

OpenC6 BIOS es importante porque permite a los desarrolladores crear sistemas más flexibles y escalables. Permite la actualización de cargas de trabajo de aplicaciones sin necesidad de recompilar el firmware completo, lo que reduce el tiempo de desarrollo y mejora la eficiencia. Además, permite la ejecución de cargas de trabajo de aplicaciones separadas del firmware base, lo que facilita la depuración y el mantenimiento de los sistemas.

## Consejo técnico

Si estás desarrollando un proyecto con ESP32-C6, considera utilizar OpenC6 BIOS para crear un sistema más flexible y escalable. Puedes utilizar la interfaz de aplicación binaria definida (ABI) para acceder a servicios del BIOS y crear pequeñas cargas de trabajo que se puedan cargar y ejecutar en el dispositivo.

```bash
esp32-idf flash --chip esp32 --port /dev/ttyUSB0 --baud 921600 --before-default-cmd "erase_flash"
```

---

**Fuente original:** [https://www.cnx-software.com/2026/06/25/openc6-bios-project-brings-pc-like-firmware-to-esp32-c6-mcu-with-network-boot-and-ota-support/](https://www.cnx-software.com/2026/06/25/openc6-bios-project-brings-pc-like-firmware-to-esp32-c6-mcu-with-network-boot-and-ota-support/)
