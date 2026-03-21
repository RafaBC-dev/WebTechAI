# Monitoreo de temperatura y humedad con Raspberry Pi

**Fecha:** 2026-03-21
**Categoría:** embebidos
**Tags:** robotica, microcontroladores, software y linux
**Título original:** Raspberry Pi Temperature & Humidity Network Monitor #Raspberrypi

---

## Introducción

Un proyecto de monitoreo de temperatura y humedad en tiempo real utilizando un Raspberry Pi y un sensor de temperatura y humedad. Esto puede ser útil para detectar problemas de humedad en un hogar o negocio.

## ¿Qué es?

El proyecto consiste en utilizar un Raspberry Pi para leer datos de temperatura y humedad de un sensor conectado y enviarlos a una red local o remota. Esto permite monitorear en tiempo real la temperatura y humedad en un área específica.

## ¿Cómo funciona?

El proyecto utiliza un Raspberry Pi Modelo B, un sensor de temperatura y humedad de AdaFruit y un caso para proteger el equipo. El sensor envía datos al Raspberry Pi, que los procesa y los envía a una red local o remota utilizando protocolos de red como HTTP o MQTT.

## ¿Por qué importa?

Este proyecto es importante porque permite detectar problemas de humedad en un hogar o negocio de manera temprana, lo que puede evitar daños a la propiedad y reducir costos de reparación.

## Consejo técnico

Si deseas implementar un proyecto similar, considera utilizar la librería RPi.GPIO para interactuar con el sensor y enviar datos a una red local o remota utilizando protocolos de red como HTTP o MQTT.

```bash
sudo apt-get install rpi-gpio
```

---

**Fuente original:** [https://blog.adafruit.com/2026/03/20/raspberry-pi-temperature-humidity-network-monitor-raspberrypi/](https://blog.adafruit.com/2026/03/20/raspberry-pi-temperature-humidity-network-monitor-raspberrypi/)
