# Router industrial de bordillo con Raspberry Pi CM4/CM5 para IoT

**Fecha:** 2026-08-10
**Categoría:** embebidos
**Tags:** robotica, embebidos, linux
**Título original:** Raspberry Pi CM4/CM5-based WisGate Connect Router RAK7392 offers 2.5GbE, mini PCIe, and WisBlock expansion

---

## Introducción

RAKwireless ha lanzado el WisGate Connect Router RAK7392, un router industrial de bordillo basado en Raspberry Pi Compute Module 4/5 (CM4/CM5) diseñado para aplicaciones IoT de vanguardia. Este dispositivo revolucionario elimina la necesidad de múltiples placas y adaptadores USB para implementaciones complejas.

## ¿Qué es?

El WisGate Connect Router RAK7392 es un router industrial de bordillo que combina la potencia de Raspberry Pi CM4/CM5 con una amplia gama de características y conectividad. Ofrece tres puertos Ethernet Gigabit, uno de 2,5 GbE, expansión inalámbrica a través de una ranura mini PCIe y conectores WisBlock para sensores e I/O.

## ¿Cómo funciona?

El router utiliza un procesador Broadcom BCM2711 (CM4) o BCM2712 (CM5) para ofrecer una velocidad de procesamiento de hasta 2,4 GHz. La memoria y almacenamiento dependen del módulo seleccionado. La conectividad se maneja mediante NetworkManager, permitiendo configurar direcciones IP estáticas, credenciales Wi-Fi o APNs celulares de manera sencilla.

## ¿Por qué importa?

Este router industrial de bordillo resuelve problemas complejos en aplicaciones IoT, como la conversión de Modbus a MQTT y la transmisión de paquetes LoRaWAN. Ofrece una solución integral para implementaciones de vanguardia, reduciendo la necesidad de múltiples dispositivos y adaptadores.

## Consejo técnico

Para aprovechar al máximo el WisGate Connect Router RAK7392, es recomendable utilizar la herramienta RAKPiOS, una versión personalizada de Raspberry Pi OS que viene preconfigurada con todos los controladores necesarios, mejoras de seguridad y un entorno de Docker preinstalado.

```bash
Para configurar el router, utilice el comando `sudo raspi-config` para acceder a la configuración de la interfaz gráfica y `sudo nmcli` para configurar la conectividad de red.
```

---

**Fuente original:** [https://www.cnx-software.com/2026/08/10/raspberry-pi-cm4-cm5-based-wisgate-connect-router-rak7392-offers-2-5gbe-mini-pcie-and-wisblock-expansion/](https://www.cnx-software.com/2026/08/10/raspberry-pi-cm4-cm5-based-wisgate-connect-router-rak7392-offers-2-5gbe-mini-pcie-and-wisblock-expansion/)
