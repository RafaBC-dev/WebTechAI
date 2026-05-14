# Clawdmeter: un panel de control DIY para monitorear tokens de Claude Code

**Fecha:** 2026-05-14
**Categoría:** embebidos
**Tags:** robotica, microcontroladores, software y linux
**Título original:** Clawdmeter – A DIY ESP32-S3 desk dashboard for Claude Code token usage monitoring

---

## Introducción

El proyecto Clawdmeter es un panel de control DIY que utiliza un ESP32-S3 para monitorear tokens de Claude Code en tiempo real. Este dispositivo es especialmente útil para desarrolladores que utilizan la tecnología de Claude Code en sus proyectos.

## ¿Qué es?

El Clawdmeter es un panel de control DIY que utiliza un ESP32-S3 para monitorear tokens de Claude Code en tiempo real. Se conecta a un ordenador a través de Bluetooth y muestra animaciones de pixel art que se aceleran a medida que se consume tokens. También muestra estadísticas y permite configurar la conexión Bluetooth.

## ¿Cómo funciona?

El Clawdmeter utiliza el ESP32-S3, un microcontrolador dual-core con capacidad de aceleración de AI, para monitorear tokens de Claude Code. Utiliza la biblioteca LVGL para crear una interfaz de usuario gráfica y la biblioteca NimBLE para comunicarse con el ordenador a través de Bluetooth. El dispositivo también puede funcionar como un teclado HID para enviar comandos a través de la conexión Bluetooth.

## ¿Por qué importa?

El Clawdmeter es importante porque permite a los desarrolladores monitorear tokens de Claude Code en tiempo real, lo que puede ayudar a evitar problemas de sobrecarga de tokens. También puede ser útil para aquellos que necesitan configurar la conexión Bluetooth con el ordenador.

## Consejo técnico

Si deseas crear un dispositivo similar al Clawdmeter, puedes utilizar el ESP32-S3 y la biblioteca LVGL para crear una interfaz de usuario gráfica. Utiliza la biblioteca NimBLE para comunicarte con el ordenador a través de Bluetooth y configura la conexión utilizando la herramienta de configuración de Bluetooth proporcionada por Waveshare.

```bash
Utiliza el comando `idf.py flash` para programar el ESP32-S3 con la biblioteca LVGL y la biblioteca NimBLE.
```

---

**Fuente original:** [https://www.cnx-software.com/2026/05/14/clawdmeter-a-diy-esp32-s3-desk-dashboard-for-claude-code-token-usage-monitoring/](https://www.cnx-software.com/2026/05/14/clawdmeter-a-diy-esp32-s3-desk-dashboard-for-claude-code-token-usage-monitoring/)
