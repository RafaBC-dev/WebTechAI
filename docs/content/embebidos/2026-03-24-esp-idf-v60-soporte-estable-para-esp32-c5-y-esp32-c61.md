# ESP-IDF v6.0: soporte estable para ESP32-C5 y ESP32-C61

**Fecha:** 2026-03-24
**Categoría:** embebidos
**Tags:** esp32, embebidos, linux
**Título original:** ESP-IDF v6.0 framework adds support for ESP32-C5 and ESP32-C61, preview for ESP32-H21 and ESP32-H4

---

## Introducción

Espressif Systems ha lanzado el framework ESP-IDF v6.0 con soporte estable para los microcontroladores ESP32-C5 y ESP32-C61. Además, se incluye soporte previo para ESP32-H21 y ESP32-H4, así como mejoras en la instalación, seguridad y herramientas.

## ¿Qué es?

ESP-IDF es un framework de desarrollo de software para microcontroladores ESP32, que permite a los desarrolladores crear aplicaciones de Internet de las cosas (IoT) y otros proyectos embebidos. El framework proporciona una serie de herramientas y bibliotecas para facilitar el desarrollo de software para estos dispositivos.

## ¿Cómo funciona?

El ESP-IDF v6.0 implementa un nuevo instalador de framework llamado ESP-IDF Installation Manager (EIM), que simplifica el proceso de instalación del framework y de los IDEs compatibles. También incluye soporte para la biblioteca Picolibc, que reemplaza a Newlib y ofrece un menor pie de memoria y mejor rendimiento en dispositivos con recursos limitados.

## ¿Por qué importa?

El ESP-IDF v6.0 es importante porque ofrece soporte estable para los microcontroladores ESP32-C5 y ESP32-C61, lo que significa que los desarrolladores pueden crear aplicaciones de IoT y otros proyectos embebidos con mayor confianza. Además, las mejoras en la instalación, seguridad y herramientas hacen que el desarrollo de software sea más fácil y eficiente.

## Consejo técnico

Si estás desarrollando aplicaciones de IoT con ESP-IDF, considera migrar a la biblioteca Picolibc para aprovechar sus ventajas en términos de memoria y rendimiento.

```bash
idf.py --preset production build
```

---

**Fuente original:** [https://www.cnx-software.com/2026/03/24/esp-idf-v6-0-framework-adds-support-for-esp32-c5-and-esp32-c61-preview-for-esp32-h21-and-esp32-h4/](https://www.cnx-software.com/2026/03/24/esp-idf-v6-0-framework-adds-support-for-esp32-c5-and-esp32-c61-preview-for-esp32-h21-and-esp32-h4/)
