# Smart Escala IoT con ESP32 y HX711: lectura precisa de peso sin código adicional

**Fecha:** 2026-03-16
**Categoría:** embebidos
**Tags:** esp32, robotica, embebidos
**Título original:** SparkFun OpenScale IoT – An ESP32 board with HX711 ADC for smart scales with WiFi and Bluetooth connectivity

---

## Introducción

La SparkFun OpenScale IoT es un proyecto de escala inteligente con conectividad WiFi y Bluetooth que permite leer datos de peso con precisión sin necesidad de escribir código adicional. Esta escala es ideal para aplicaciones de monitorización y control de peso en tiempo real.

## ¿Qué es?

La SparkFun OpenScale IoT es un módulo de escala inteligente basado en el ESP32 que utiliza el HX711 como amplificador de señal de peso. Esto permite leer datos de peso con precisión y calibrar la escala sin necesidad de escribir código adicional. La escala también cuenta con conectividad WiFi y Bluetooth para transmitir datos en tiempo real.

## ¿Cómo funciona?

La escala utiliza el HX711 para amplificar la señal de peso de la célula de carga, que luego se envía al ESP32 para ser procesada y transmitida a través de WiFi o Bluetooth. La escala también cuenta con un sensor de temperatura onboard y un conector Qwiic para agregar sensores adicionales.

## ¿Por qué importa?

La SparkFun OpenScale IoT es importante porque permite a los desarrolladores crear aplicaciones de monitorización y control de peso en tiempo real sin necesidad de escribir código adicional. Esto es especialmente útil en aplicaciones como la monitorización de peso de animales en granjas o la medición de peso en tiempo real en industrias como la alimentaria o la farmacéutica.

## Consejo técnico

Para configurar la escala, puedes utilizar el comando `idf.py menuconfig` para acceder a la configuración de la escala y ajustar los parámetros de medición y transmisión de datos.

```bash
idf.py menuconfig
```

---

**Fuente original:** [https://www.cnx-software.com/2026/03/16/sparkfun-openscale-iot-an-esp32-board-with-hx711-adc-for-smart-scales-with-wifi-and-bluetooth-connectivity/](https://www.cnx-software.com/2026/03/16/sparkfun-openscale-iot-an-esp32-board-with-hx711-adc-for-smart-scales-with-wifi-and-bluetooth-connectivity/)
