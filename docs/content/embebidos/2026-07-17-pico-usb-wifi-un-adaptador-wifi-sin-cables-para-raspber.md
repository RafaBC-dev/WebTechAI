# Pico-USB-WiFi: un adaptador WiFi sin cables para Raspberry Pi Pico W

**Fecha:** 2026-07-17
**Categoría:** embebidos
**Tags:** robotica, microcontroladores, software-y-linux
**Título original:** pico-usb-wifi firmware converts the Raspberry Pi Pico W into a driverless USB WiFi adapter

---

## Introducción

Un desarrollador ha creado un firmware que convierte el Raspberry Pi Pico W en un adaptador WiFi sin cables, compatible con Windows, Linux, macOS y otros sistemas operativos. Esto permite usar el Pico W como una conexión WiFi sin necesidad de cables.

## ¿Qué es?

Pico-USB-WiFi es un proyecto de firmware abierto que convierte el Raspberry Pi Pico W en un adaptador WiFi sin cables. Utiliza el chip Infineon CYW43439 para crear una conexión WiFi transparente entre el módulo de red inalámbrico y las interfaces USB. Esto permite usar el Pico W como una conexión WiFi sin necesidad de cables.

## ¿Cómo funciona?

El firmware implementa una puente de capa 2 transparente entre el módulo de red inalámbrico y las interfaces USB. Esto permite que los paquetes de datos se transmitan entre la red inalámbrica y la conexión USB. El Pico W se expone como un dispositivo USB CDC-NCM, lo que permite la comunicación con otros dispositivos USB.

## ¿Por qué importa?

Este proyecto es útil para aquellos que necesitan una conexión WiFi sin cables, como en situaciones de emergencia o cuando no se dispone de un cable de red. También puede ser utilizado para crear una conexión WiFi en dispositivos que no tienen una conexión WiFi integrada.

## Consejo técnico

Si deseas probar el Pico-USB-WiFi, asegúrate de instalar el firmware correcto en tu Raspberry Pi Pico W y configurar la conexión WiFi según las instrucciones del proyecto.

```bash
picocom /dev/ttyACM0
```

---

**Fuente original:** [https://www.cnx-software.com/2026/07/16/pico-usb-wifi-converts-the-raspberry-pi-pico-w-into-a-driverless-usb-wifi-adapter/](https://www.cnx-software.com/2026/07/16/pico-usb-wifi-converts-the-raspberry-pi-pico-w-into-a-driverless-usb-wifi-adapter/)
