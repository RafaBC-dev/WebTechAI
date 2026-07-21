# Comunicación de radio a larga distancia con Raspberry Pi

**Fecha:** 2026-07-21
**Categoría:** embebidos
**Tags:** robotica, microcontroladores, software y linux
**Título original:** LoRa radio communication devices for Raspberry Pi

---

## Introducción

¿Necesitas enviar datos desde un proyecto basado en Raspberry Pi más allá del rango de tu red Wi-Fi? Existen soluciones más fiables y asequibles que la extensión de Wi-Fi o cables de Ethernet largos.

## ¿Qué es?

LoRa es un sistema de radio a larga distancia que transmite paquetes de datos pequeños a velocidades bajas (300bps a 50kbps), ideal para sensores IoT y similares. Su mayor ventaja es su resistencia a ruido y interferencia, lo que permite una distancia de hasta 15km en áreas rurales.

## ¿Cómo funciona?

LoRa utiliza las bandas de radio ISM (Industrial, Scientific, and Medical) y permite a los nodos enviar datos entre sí o utilizar un gateway LoRaWAN para recibir múltiples canales. También se pueden utilizar soluciones de 4G celular para velocidades más altas.

## ¿Por qué importa?

Esta tecnología importa porque permite la comunicación de datos a larga distancia de manera fiable y asequible, lo que es especialmente útil para proyectos IoT y sensores en áreas rurales.

## Consejo técnico

Asegúrate de verificar las regulaciones de radio de tu jurisdicción antes de implementar una solución LoRa, ya que existen limitaciones en la frecuencia, ciclo de trabajo y potencia de transmisión.

```bash
Crea un proyecto LoRa con el módulo SX1262 para Raspberry Pi Pico utilizando el código de ejemplo proporcionado en la documentación de Waveshare.
```

---

**Fuente original:** [https://www.raspberrypi.com/news/lora-radio-communication-devices-for-raspberry-pi/](https://www.raspberrypi.com/news/lora-radio-communication-devices-for-raspberry-pi/)
