# Monitoreo de calidad del aire en interiores con ESP32-S3 y SEN66

**Fecha:** 2026-04-29
**Categoría:** embebidos
**Tags:** robotica, microcontroladores, software y linux
**Título original:** MoreSense MS-07 – An ESP32-S3 indoor air quality monitor with SEN66 multisensor and Home Assistant support

---

## Introducción

La empresa MoreSense ha lanzado el MS-07, un monitoreo de calidad del aire para interiores que utiliza un microcontrolador ESP32-S3 y un sensor SEN66 multisensor. Este dispositivo permite la visualización en tiempo real de la calidad del aire, la temperatura y la humedad, y se puede integrar con sistemas de automatización como Home Assistant.

## ¿Qué es?

El MS-07 es un dispositivo de monitoreo de calidad del aire para interiores que utiliza un microcontrolador ESP32-S3 y un sensor SEN66 multisensor. Este sensor es capaz de medir la concentración de partículas en suspensión (PM1.0, PM2.5, PM4.0, PM10), óxidos de nitrógeno (NOx), compuestos orgánicos volátiles (VOCs) y dióxido de carbono (CO2).

## ¿Cómo funciona?

El dispositivo utiliza el microcontrolador ESP32-S3 para procesar los datos del sensor SEN66 y enviarlos a un sistema de automatización como Home Assistant. El sensor SEN66 es capaz de realizar una auto-calibración automática (ASC) para establecer un umbral de CO2 fresco y mantener la precisión de los mediciones. El dispositivo también cuenta con una pantalla táctil de 3,5 pulgadas para la visualización en tiempo real de los datos.

## ¿Por qué importa?

El MS-07 es importante porque permite la visualización en tiempo real de la calidad del aire en interiores, lo que puede ayudar a identificar problemas de salud y a tomar medidas para mejorar la calidad del aire. Además, se puede integrar con sistemas de automatización para controlar la ventilación y otros sistemas para mantener un ambiente saludable.

## Consejo técnico

Si deseas integrar el MS-07 con Home Assistant, puedes utilizar el comando `homeassistant add-on` para instalar el add-on de MoreSense y configurarlo para enviar los datos del sensor a Home Assistant.

```bash
homeassistant add-on
```

---

**Fuente original:** [https://www.cnx-software.com/2026/04/29/moresense-ms-07-an-esp32-s3-indoor-air-quality-monitor-with-sen66-multisensor-and-home-assistant-support/](https://www.cnx-software.com/2026/04/29/moresense-ms-07-an-esp32-s3-indoor-air-quality-monitor-with-sen66-multisensor-and-home-assistant-support/)
