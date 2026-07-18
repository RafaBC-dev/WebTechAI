# M5Stack Core2 se convierte en un reproductor de Codex Micro con firmware abierto

**Fecha:** 2026-07-18
**Categoría:** ia
**Tags:** llms, agentes, esp32, arduino
**Título original:** M5Stack Core2 gets open-source firmware to reproduce OpenAI’s Codex Micro features

---

## Introducción

IAMLIUBO ha creado un firmware para el controlador IoT M5Stack Core2 que reproduce las características del Codex Micro, un dispositivo de $230 para agentes de código abierto de OpenAI. Esto permite a los desarrolladores controlar y monitorear agentes de código más fácilmente.

## ¿Qué es?

El proyecto consiste en un firmware abierto para el M5Stack Core2 que reproduce las características del Codex Micro. Este firmware utiliza la pantalla táctil de 2 pulgadas del dispositivo ESP32 para crear una interfaz de usuario similar a la del Codex Micro, con seis teclas de agente, seis teclas de comando, cuatro direcciones del joystick y acciones de dial.

## ¿Cómo funciona?

El firmware se construyó con PlatformIO y el framework Arduino, y se encuentra disponible en GitHub. El dispositivo se presenta como un dispositivo HID BLE compatible con Work Louder's Codex Micro data, y la aplicación ChatGPT para escritorio maneja el estado de la tarea, el estado de la batería, la reasignación de comandos y la integración de empujar a hablar.

## ¿Por qué importa?

Este proyecto es importante porque permite a los desarrolladores controlar y monitorear agentes de código de OpenAI de manera más fácil y accesible, sin necesidad de gastar $230 en el dispositivo original. Además, se puede utilizar con la aplicación ChatGPT para escritorio en macOS y Windows.

## Consejo técnico

Si deseas reproducir las características del Codex Micro en tu propio dispositivo, puedes utilizar el firmware abierto de IAMLIUBO y la pantalla táctil de 2 pulgadas del M5Stack Core2. Puedes encontrar el código y las instrucciones en GitHub.

```bash
platformio init --board=m5stack-core2-freertos
```

---

**Fuente original:** [https://www.cnx-software.com/2026/07/18/m5stack-core2-gets-open-source-firmware-to-reproduce-openais-codex-micro-features/](https://www.cnx-software.com/2026/07/18/m5stack-core2-gets-open-source-firmware-to-reproduce-openais-codex-micro-features/)
