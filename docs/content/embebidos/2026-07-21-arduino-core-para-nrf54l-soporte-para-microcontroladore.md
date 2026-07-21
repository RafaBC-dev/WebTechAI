# Arduino Core para nRF54L: Soporte para microcontroladores inalámbricos

**Fecha:** 2026-07-21
**Categoría:** embebidos
**Tags:** arduino, microcontroladores, embebidos
**Título original:** nRF54L Arduino Core project brings Arduino support to Nordic Semi nRF54L wireless SoCs

---

## Introducción

Nordic Semiconductor ha lanzado recientemente el nRF54L, un microcontrolador inalámbrico con tecnología Bluetooth LE. Sin embargo, no hay soporte oficial para este chip en el IDE de Arduino. Lolren ha decidido cambiar eso con el proyecto nRF54L Arduino Core.

## ¿Qué es?

El nRF54L Arduino Core es un proyecto de código abierto que proporciona soporte para el microcontrolador nRF54L en el IDE de Arduino. Esto permite a los desarrolladores utilizar el nRF54L con la familiaridad de la plataforma Arduino.

## ¿Cómo funciona?

El proyecto utiliza la API de Nordic Semiconductor para acceder a las funciones del nRF54L. Esto incluye la configuración de la conexión Bluetooth LE, la gestión de la memoria y la implementación de protocolos como Zigbee y Thread.

## ¿Por qué importa?

El nRF54L Arduino Core es importante porque permite a los desarrolladores aprovechar las características del nRF54L, como la conectividad Bluetooth LE y la capacidad de ejecutar protocolos de red. Esto puede ser útil en aplicaciones como la automatización del hogar, la monitorización de sensores y la comunicación inalámbrica.

## Consejo técnico

Para empezar a utilizar el nRF54L Arduino Core, agrega la siguiente URL al gestor de paquetes del IDE de Arduino: https://raw.githubusercontent.com/lolren/nrf54-arduino-core/main/package_nrf54l15clean_index.json

```bash
Preferences → Additional Boards Manager URLs
```

---

**Fuente original:** [https://www.cnx-software.com/2026/07/21/nrf54l-arduino-core-project-brings-arduino-support-to-nordic-semi-nrf54l-wireless-socs/](https://www.cnx-software.com/2026/07/21/nrf54l-arduino-core-project-brings-arduino-support-to-nordic-semi-nrf54l-wireless-socs/)
