# Control remoto universal con ESP32-S3 y tecnologías de última generación

**Fecha:** 2026-07-17
**Categoría:** embebidos
**Tags:** robotica, microcontroladores, software-y-linux
**Título original:** OpenInfrared Point is an ESP32-S3 powered universal remote hub with Infrared, BLE, NFC, audio streaming (Crowdfunding)

---

## Introducción

La empresa OpenInfrared Point ha lanzado un control remoto universal que utiliza la tecnología ESP32-S3 para controlar dispositivos compatibles desde un smartphone. Este dispositivo elimina la necesidad de controles remotos dedicados y ofrece una experiencia de control remoto inalámbrica y segura.

## ¿Qué es?

El OpenInfrared Point es un control remoto universal que utiliza la tecnología ESP32-S3 para controlar dispositivos compatibles como televisores, proyectores, receptores de audio, aire acondicionado, luces y otros dispositivos. Puede aprender códigos IR de controles remotos existentes y soporta control inalámbrico por infrarrojo, IP y Bluetooth Low Energy (BLE).

## ¿Cómo funciona?

El dispositivo utiliza el SoC ESP32-S3, que cuenta con un procesador dual-core Tensilica LX7 de hasta 240 MHz y 512KB de SRAM, para aprender códigos IR de controles remotos existentes y controlar dispositivos compatibles. También cuenta con una entrada de audio de 3.5mm para streaming de audio directo a un dispositivo móvil. El control remoto se puede acceder mediante un código QR o un tag NFC integrado.

## ¿Por qué importa?

El OpenInfrared Point importa porque ofrece una experiencia de control remoto inalámbrica y segura, sin necesidad de controles remotos dedicados. También permite la integración con sistemas de automatización como Home Assistant, Apple Home, Alexa, Google y Smartthings.

## Consejo técnico

Si deseas aprovechar al máximo el OpenInfrared Point, asegúrate de aprender a utilizar la API HTTP integrada para integrarlo con tus sistemas de automatización favoritos y personalizar tus controles remotos.

```bash
curl -X GET 'http://[dirección_IP_del_dispositivo]/api/config' -H 'Authorization: Bearer [token_de_acceso]'
```

---

**Fuente original:** [https://www.cnx-software.com/2026/07/16/openinfrared-point-esp32-s3-universal-remote-hub-infrared-ble-nfc-audio-streaming/](https://www.cnx-software.com/2026/07/16/openinfrared-point-esp32-s3-universal-remote-hub-infrared-ble-nfc-audio-streaming/)
