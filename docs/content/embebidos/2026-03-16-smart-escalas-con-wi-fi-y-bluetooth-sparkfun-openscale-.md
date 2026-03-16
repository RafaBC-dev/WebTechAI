# Smart Escalas con Wi-Fi y Bluetooth: SparkFun OpenScale IoT

**Fecha:** 2026-03-16
**Categoría:** embebidos
**Tags:** esp32, robotica, microcontroladores
**Título original:** SparkFun OpenScale IoT – An ESP32 board with HX711 ADC for smart scales with WiFi and Bluetooth connectivity

---

## Introducción

SparkFun ha lanzado un nuevo proyecto llamado OpenScale IoT, un módulo de escalas inteligentes basado en ESP32 que permite leer datos de peso con precisión sin necesidad de escribir código personalizado.

## ¿Qué es?

El SparkFun OpenScale IoT es un módulo de escalas inteligentes que utiliza el procesador ESP32 para leer datos de peso con precisión. Se conecta a la red Wi-Fi y Bluetooth, permitiendo la transmisión en vivo de datos y actualizaciones de firmware por OTA. También cuenta con una salida serial y una conexión Qwiic I²C para agregar sensores o displays adicionales.

## ¿Cómo funciona?

El módulo utiliza el HX711 24-bit ADC para amplificar los datos de la escala y realizar la calibración y compensación de temperatura. El procesador ESP32 se encarga de procesar los datos y enviarlos a la red Wi-Fi o Bluetooth. El módulo también cuenta con un regulador de tensión de 3.3V para alimentar el ESP32.

## ¿Por qué importa?

El SparkFun OpenScale IoT es importante porque permite a los desarrolladores crear escalas inteligentes con Wi-Fi y Bluetooth sin necesidad de escribir código personalizado. Esto abre nuevas posibilidades para la creación de aplicaciones de monitoreo de peso en tiempo real, como la gestión de inventarios o la supervisión de la condición física.

## Consejo técnico

Para comenzar a trabajar con el SparkFun OpenScale IoT, es recomendable conectar el módulo a una computadora con Linux y utilizar la herramienta `esptool` para configurar el firmware y establecer la conexión Wi-Fi.

```bash
esptool --baud 115200 --port /dev/ttyUSB0 --chip esp32 --baud 115200 --port /dev/ttyUSB0 --chip esp32
```

---

**Fuente original:** [https://www.cnx-software.com/2026/03/16/sparkfun-openscale-iot-an-esp32-board-with-hx711-adc-for-smart-scales-with-wifi-and-bluetooth-connectivity/](https://www.cnx-software.com/2026/03/16/sparkfun-openscale-iot-an-esp32-board-with-hx711-adc-for-smart-scales-with-wifi-and-bluetooth-connectivity/)
