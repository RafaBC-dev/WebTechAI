# BIGTREETECH Panda Sense Pro: monitoreo de calidad del aire inteligente para impresoras 3D

**Fecha:** 2026-07-05
**Categoría:** embebidos
**Tags:** robotica, microcontroladores, software y linux
**Título original:** BIGTREETECH Panda Sense Pro 8-in-1 smart air quality monitor works with Home Assistant and Klipper for 3D printers

---

## Introducción

BIGTREETECH ha lanzado el Panda Sense Pro, un monitoreo de calidad del aire inteligente para entornos de impresión 3D. Este dispositivo mide en tiempo real partículas, gases, temperatura y humedad, ayudando a los usuarios a monitorizar la calidad del aire mientras imprimen. Se integra con plataformas de automatización y sistemas de impresión 3D para controlar el entorno de impresión de manera inteligente.

## ¿Qué es?

El Panda Sense Pro es un dispositivo de monitoreo de calidad del aire que combina sensores de partículas, gases y temperatura para medir la calidad del aire en tiempo real. Incluye sensores de partículas PM2.5 y PM10, CO2, HCHO, eTVOC y AQI, así como un sensor de temperatura y humedad. El dispositivo también cuenta con una pantalla táctil de 3,5 pulgadas y conectividad Wi-Fi.

## ¿Cómo funciona?

El Panda Sense Pro utiliza sensores de partículas, gases y temperatura para medir la calidad del aire en tiempo real. Los datos se procesan en el dispositivo y se envían a la plataforma de automatización Home Assistant o Moonraker para controlar el entorno de impresión de manera inteligente. El dispositivo también almacena datos históricos de 24 horas y 30 días.

## ¿Por qué importa?

El Panda Sense Pro importa porque permite a los usuarios de impresoras 3D monitorizar la calidad del aire en tiempo real y controlar el entorno de impresión de manera inteligente. Esto puede ayudar a reducir la contaminación del aire y mejorar la calidad de la impresión.

## Consejo técnico

Si deseas integrar el Panda Sense Pro con Home Assistant, puedes utilizar la librería MQTT para enviar y recibir datos entre el dispositivo y la plataforma de automatización.

```bash
mqtt subscribe -t 'panda/sense/pro' -h '192.168.1.100'
```

---

**Fuente original:** [https://www.cnx-software.com/2026/07/04/bigtreetech-panda-sense-pro-8-in-1-smart-air-quality-monitor-works-with-home-assistant-and-klipper-for-3d-printers/](https://www.cnx-software.com/2026/07/04/bigtreetech-panda-sense-pro-8-in-1-smart-air-quality-monitor-works-with-home-assistant-and-klipper-for-3d-printers/)
