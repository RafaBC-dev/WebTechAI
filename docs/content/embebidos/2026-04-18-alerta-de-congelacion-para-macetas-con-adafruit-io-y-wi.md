# Alerta de Congelación para Macetas con Adafruit IO y WipperSnapper

**Fecha:** 2026-04-18
**Categoría:** embebidos
**Tags:** robotica, microcontroladores, software-y-linux
**Título original:** No-Code Seedling Frost Alert and New WipperSnapper Components. What’s new with Adafruit IO and the Adafruit Learning System.

---

## Introducción

¿Quieres proteger tus macetas de la congelación nocturna? Un equipo de Adafruit ha creado un dispositivo de alerta de congelación que utiliza Adafruit IO y WipperSnapper para enviar notificaciones a tu teléfono cuando se prevé una temperatura bajo cero.

## ¿Qué es?

El dispositivo de alerta de congelación es un proyecto que utiliza un QT Py ESP32-S3 y Adafruit IO para detectar la temperatura y enviar notificaciones a tu teléfono cuando se prevé una congelación nocturna. El dispositivo también tiene una función de iluminación ambiental que se enciende cuando se prevé una congelación.

## ¿Cómo funciona?

El dispositivo utiliza un sensor de temperatura para detectar la temperatura ambiente y un módulo de comunicación para enviar notificaciones a tu teléfono. El dispositivo también utiliza la plataforma WipperSnapper para programar la función de alerta de congelación y la función de iluminación ambiental.

## ¿Por qué importa?

Este dispositivo es importante porque permite a los jardineros proteger sus macetas de la congelación nocturna, lo que puede causar daños graves a las plantas. El dispositivo también es útil para aquellos que desean monitorear la temperatura en su jardín o patio.

## Consejo técnico

Si deseas crear un dispositivo de alerta de congelación similar, asegúrate de utilizar un sensor de temperatura de alta precisión y un módulo de comunicación confiable. También es importante programar la función de alerta de congelación utilizando la plataforma WipperSnapper.

```bash
wipper_snapper configure --sensor temperatura --notificacion 'Teléfono de Emergencia'
```

---

**Fuente original:** [https://blog.adafruit.com/2026/04/17/no-code-seedling-frost-alert-and-new-wippersnapper-components-whats-new-with-adafruit-io-and-the-adafruit-learning-system/](https://blog.adafruit.com/2026/04/17/no-code-seedling-frost-alert-and-new-wippersnapper-components-whats-new-with-adafruit-io-and-the-adafruit-learning-system/)
