# Comunicación de radio a larga distancia para Raspberry Pi

**Fecha:** 2026-07-20
**Categoría:** embebidos
**Tags:** robotica, embebidos, linux
**Título original:** LoRa radio communication devices for Raspberry Pi

---

## Introducción

Si necesitas enviar datos desde un proyecto basado en Raspberry Pi más allá de la red Wi-Fi de tu hogar, hay soluciones más fiables que usar un extensor de Wi-Fi o un cable Ethernet muy largo. LoRa es un sistema de radio a larga distancia que puede transmitir pequeños paquetes de datos a velocidades bajas, ideal para sensores IoT y similares.

## ¿Qué es?

LoRa es un sistema de radio a larga distancia que puede transmitir pequeños paquetes de datos a velocidades bajas (300bps a 50kbps) y tiene una gran resistencia a la interferencia y ruido, lo que le permite cubrir una distancia de hasta 15km en áreas rurales. Puede enviar datos a otros nodos LoRa o utilizar un gateway LoRaWAN para recibir múltiples canales.

## ¿Cómo funciona?

Para utilizar LoRa con Raspberry Pi, se puede conectar un módulo LoRa a un Raspberry Pi Pico, que es un microcontrolador muy pequeño y eficiente. El módulo LoRa se puede conectar a un batería LiPo para funcionar de manera remota. El sistema LoRa utiliza la banda ISM (Industrial, Scientific y Médica) para transmitir datos, lo que significa que no requiere licencia para transmitir, pero sí debe cumplir con los parámetros regionales establecidos por las autoridades locales.

## ¿Por qué importa?

LoRa es importante porque ofrece una solución fiable y asequible para transmitir datos a larga distancia, lo que es ideal para proyectos IoT y sensores que requieren una gran autonomía y resistencia a la interferencia.

## Consejo técnico

Si estás utilizando LoRa con Raspberry Pi, asegúrate de elegir el módulo LoRa adecuado para tu región y de seguir las instrucciones del fabricante para configurar el sistema correctamente. También es importante verificar las regulaciones de radio de tu país antes de empezar a transmitir.

```bash
sudo apt-get install liblora-dev
```

---

**Fuente original:** [https://www.raspberrypi.com/news/lora-radio-communication-devices-for-raspberry-pi/](https://www.raspberrypi.com/news/lora-radio-communication-devices-for-raspberry-pi/)
