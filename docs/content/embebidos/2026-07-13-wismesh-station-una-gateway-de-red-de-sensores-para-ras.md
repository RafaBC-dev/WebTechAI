# WisMesh Station: una gateway de red de sensores para Raspberry Pi

**Fecha:** 2026-07-13
**Categoría:** embebidos
**Tags:** robotica, embebidos, linux
**Título original:** WisMesh Station Review – Telemetry, MQTT, and Grafana tested on a Raspberry Pi 4-based Meshtastic gateway

---

## Introducción

RAKwireless ha lanzado el WisMesh Station, una gateway de red de sensores basada en Raspberry Pi 4 que permite crear redes de sensores inalámbricas de larga distancia. Esta tecnología promete revolucionar la forma en que se conectan los dispositivos IoT en áreas rurales o remotas.

## ¿Qué es?

El WisMesh Station es una plataforma de red de sensores que utiliza la tecnología LoRaWAN para conectar dispositivos IoT en áreas de larga distancia. Está basada en un Raspberry Pi 4 y utiliza la placa de expansión RAK6421 WisMesh Pi HAT+, que incluye un módulo LoRa y un módulo GNSS. La plataforma también incluye cuatro slots para sensores y dos slots para entradas/analogías.

## ¿Cómo funciona?

El WisMesh Station funciona conectando dispositivos IoT a la red de sensores a través de la tecnología LoRaWAN. Los datos se envían a la plataforma, que los analiza y los almacena en una base de datos. La plataforma también puede enviar notificaciones y alertas a los dispositivos conectados. La plataforma utiliza la biblioteca Meshtastic para crear la red de sensores y la biblioteca MQTT para la comunicación entre dispositivos.

## ¿Por qué importa?

El WisMesh Station importa porque permite crear redes de sensores inalámbricas de larga distancia en áreas rurales o remotas, lo que es especialmente útil para aplicaciones como la agricultura, la minería y la gestión de infraestructuras. También permite la creación de redes de sensores para monitorear el medio ambiente y la salud pública.

## Consejo técnico

Para empezar a trabajar con el WisMesh Station, es recomendable instalar la biblioteca Meshtastic y configurar la plataforma para utilizar la frecuencia de radio adecuada para tu ubicación. También es importante configurar la plataforma para utilizar la biblioteca MQTT para la comunicación entre dispositivos.

```bash
meshtasticd -f <frecuencia_de_radio> -c <configuracion_de_red>
```

---

**Fuente original:** [https://www.cnx-software.com/2026/07/13/wismesh-station-review-telemetry-mqtt-and-grafana-tested-on-a-raspberry-pi-4-based-meshtastic-gateway/](https://www.cnx-software.com/2026/07/13/wismesh-station-review-telemetry-mqtt-and-grafana-tested-on-a-raspberry-pi-4-based-meshtastic-gateway/)
