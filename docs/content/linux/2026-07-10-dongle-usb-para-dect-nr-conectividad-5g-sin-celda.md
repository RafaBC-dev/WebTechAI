# Dongle USB para DECT NR+: conectividad 5G sin celda

**Fecha:** 2026-07-10
**Categoría:** linux
**Tags:** robotica, embebidos, linux
**Título original:** Norik Systems introduces nRF9151-based USB Dongle for DECT NR+ deployments

---

## Introducción

La empresa Norik Systems ha lanzado un dongle USB basado en el nRF9151 de Nordic Semiconductor, diseñado para trabajar como nodo hijo o gateway USB en redes DECT NR+.

## ¿Qué es?

El DECT NR+ es un estándar 5G no celular para aplicaciones de largo alcance y bajo consumo de energía, que opera a 1,9 GHz y admite hasta un millón de nodos a través de topologías de malla, estrella y punto a punto. El dongle USB de Norik permite a los desarrolladores agregar fácilmente DECT NR+ a gateways o nodos hijos.

## ¿Cómo funciona?

El dongle se conecta directamente a un puerto USB y se muestra como un dispositivo serial y depurador. Viene pre-flashado con firmware de consola que permite a los desarrolladores descubrir redes, unirse a ellas o crear redes privadas, realizar pruebas de enlace y evaluar el rendimiento de la radio a través de una terminal serial. También se puede reprogramar con aplicaciones personalizadas utilizando ejemplos de código abierto incluidos en la SDK Zephyr de Nordic.

## ¿Por qué importa?

Este dongle USB es importante porque permite a los desarrolladores crear aplicaciones de IoT y redes inalámbricas de largo alcance sin necesidad de una conexión celular. También ofrece una forma sencilla de agregar DECT NR+ a gateways o nodos hijos, lo que puede ser útil para aplicaciones de IoT y redes de sensores.

## Consejo técnico

Si deseas crear una aplicación de IoT que utilice DECT NR+, puedes utilizar el dongle USB de Norik y la SDK Zephyr de Nordic para desarrollar y depurar tu aplicación. Recuerda que debes reprogramar el dongle con tu aplicación personalizada utilizando los ejemplos de código abierto incluidos en la SDK.

```bash
nrfjprog -f nrf9151 -e <nombre_del_firmware>
```

---

**Fuente original:** [https://www.cnx-software.com/2026/07/09/norik-systems-introduces-nrf9151-based-usb-dongle-for-dect-nr-deployments/](https://www.cnx-software.com/2026/07/09/norik-systems-introduces-nrf9151-based-usb-dongle-for-dect-nr-deployments/)
