# ReTerminal D1001: un display táctil de 8 pulgadas con ESP32-P4 y WiFi 6

**Fecha:** 2026-03-20
**Categoría:** embebidos
**Tags:** robotica, microcontroladores, software y linux
**Título original:** 8-inch ESP32-P4 touch display offers WiFi 6, BLE, 802.15.4 connectivity, optional 4G LTE and LoRaWAN

---

## Introducción

Seeed Studio ha lanzado el reTerminal D1001, un display táctil de 8 pulgadas con conectividad WiFi 6, Bluetooth 5.x y 802.15.4. Este dispositivo está diseñado para aplicaciones de HMI y puede ser utilizado como kit de desarrollo.

## ¿Qué es?

El reTerminal D1001 es un dispositivo de interfaz de usuario (HMI) que combina un display táctil de 8 pulgadas con un procesador ESP32-P4 y un módulo de comunicaciones inalámbricas ESP32-C6. Este dispositivo está equipado con una cámara de 2MP, un micrófono dual y un altavoz de 2W.

## ¿Cómo funciona?

El reTerminal D1001 está basado en el procesador ESP32-P4, que cuenta con un núcleo de 32 bits RISC-V de alto rendimiento y un núcleo de bajo consumo. El dispositivo también cuenta con 32MB de PSRAM y 32MB de QSPI NOR Flash. La comunicación se realiza a través del módulo ESP32-C6, que ofrece conectividad WiFi 6, Bluetooth 5.x y 802.15.4.

## ¿Por qué importa?

El reTerminal D1001 es relevante porque ofrece una plataforma de desarrollo para crear aplicaciones de HMI con conectividad inalámbrica. Esto permite a los desarrolladores crear dispositivos inteligentes que puedan interactuar con el usuario de manera intuitiva.

## Consejo técnico

Si deseas utilizar el reTerminal D1001 como kit de desarrollo, asegúrate de instalar el framework ESP-IDF y seguir las instrucciones para cargar el firmware de fábrica (ESPBrookesia).

```bash
espidf flash --port /dev/ttyUSB0 --baud 115200 --chip esp32 --port 0x3 --flash-size 4MB
```

---

**Fuente original:** [https://www.cnx-software.com/2026/03/20/8-inch-esp32-p4-touch-display-offers-wifi-6-ble-802-15-4-connectivity-optional-4g-lte-and-lorawan/](https://www.cnx-software.com/2026/03/20/8-inch-esp32-p4-touch-display-offers-wifi-6-ble-802-15-4-connectivity-optional-4g-lte-and-lorawan/)
