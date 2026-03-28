# Lanzamiento del Thing Plus – ESP32-C5: una placa de desarrollo con WiFi 6 y compatibilidad con Feather

**Fecha:** 2026-03-28
**Categoría:** embebidos
**Tags:** esp32, robotica, microcontroladores
**Título original:** SparkFun Thing Plus – ESP32-C5 board offers dual-band WiFi 6, Adafruit Feather pinout, LiPo battery support

---

## Introducción

SparkFun ha lanzado el Thing Plus – ESP32-C5, una placa de desarrollo que combina la compatibilidad con Feather con la tecnología WiFi 6 del ESP32-C5. Este lanzamiento es relevante ahora mismo debido a la estabilidad del software y la adición de características clave como los actualizaciones de firmware por OTA.

## ¿Qué es?

El Thing Plus – ESP32-C5 es una placa de desarrollo basada en el ESP32-C5, un SoC que incluye un procesador RISC-V de 32 bits, memoria SRAM y PSRAM, y conectividad WiFi 6 y Bluetooth 5.0 LE. La placa es compatible con la pinout de Feather y cuenta con una ranura para tarjeta MicroSD y un conector Qwiic.

## ¿Cómo funciona?

La placa Thing Plus – ESP32-C5 utiliza el ESP32-C5 como procesador principal, que se encarga de la conectividad WiFi 6 y Bluetooth 5.0 LE. La placa también cuenta con una ranura para tarjeta MicroSD y un conector Qwiic para conectar periféricos I2C. El software de la placa se basa en el ESP-IDF v6.0 y se puede programar con MicroPython o C.

## ¿Por qué importa?

El Thing Plus – ESP32-C5 es importante porque ofrece una plataforma de desarrollo estable y segura para proyectos de IoT y smart home. La placa es compatible con la tecnología WiFi 6 y cuenta con características como los actualizaciones de firmware por OTA, lo que la hace ideal para aplicaciones remotas y de confianza.

## Consejo técnico

Para aprovechar al máximo la placa Thing Plus – ESP32-C5, recomiendo utilizar la librería MicroPython para programar la placa y aprovechar las características de WiFi 6 y Bluetooth 5.0 LE. También es recomendable utilizar el conector Qwiic para conectar periféricos I2C y aprovechar la ranura para tarjeta MicroSD para almacenar datos.

```bash
import machine
import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('TU_RED', 'TU_CONTRASEÑA')
```

---

**Fuente original:** [https://www.cnx-software.com/2026/03/27/sparkfun-thing-plus-esp32-c5-board-offers-dual-band-wifi-6-adafruit-feather-pinout-lipo-battery-support/](https://www.cnx-software.com/2026/03/27/sparkfun-thing-plus-esp32-c5-board-offers-dual-band-wifi-6-adafruit-feather-pinout-lipo-battery-support/)
