# Espressif lanza SDK para cerraduras inteligentes Aliro basadas en ESP32-C o ESP32-H

**Fecha:** 2026-07-18
**Categoría:** embebidos
**Tags:** microcontroladores, esp32, software y linux
**Título original:** Espressif releases SDK for Aliro smart door locks based on ESP32-C or ESP32-H SoCs

---

## Introducción

Espressif Systems ha lanzado el SDK para Aliro, una tecnología de acceso digital para cerraduras inteligentes que utiliza NFC, Bluetooth LE o BLE+UWB. Este estándar busca reducir la fragmentación y permitir a los usuarios utilizar carteras compatibles de Google, Apple, Samsung y otros con dispositivos Aliro.

## ¿Qué es?

Aliro es un estándard de acceso digital para cerraduras inteligentes que utiliza NFC, Bluetooth LE o BLE+UWB. Es similar a Matter, pero enfocado en el ecosistema de cerraduras inteligentes en lugar del hogar inteligente en general.

## ¿Cómo funciona?

El SDK de Espressif para Aliro (ESP-Aliro) soporta características como la fase expedida estándar, la fase expedida rápida, el envío de certificados de lector a través del comando AUTH1/LoadCert, la búsqueda de claves de acceso a partir de la clave pública y el intercambio de comandos. Actualmente solo funciona con NFC para aplicaciones de toque para desbloquear, aunque se planea soporte para Bluetooth LE y BLE+UWB.

## ¿Por qué importa?

La tecnología Aliro permite a los usuarios utilizar carteras compatibles de Google, Apple, Samsung y otros con dispositivos Aliro, reduciendo la fragmentación y aumentando la interoperabilidad entre diferentes sistemas de acceso.

## Consejo técnico

Para empezar a trabajar con Aliro, descarga el SDK de Espressif desde GitHub y explora la documentación para aprender a implementar las características de Aliro en tus proyectos de cerraduras inteligentes.

```bash
git clone https://github.com/espressif/esp-aliro
```

---

**Fuente original:** [https://www.cnx-software.com/2026/07/17/espressif-releases-sdk-for-aliro-smart-door-locks-based-on-esp32-c-or-esp32-h-socs/](https://www.cnx-software.com/2026/07/17/espressif-releases-sdk-for-aliro-smart-door-locks-based-on-esp32-c-or-esp32-h-socs/)
