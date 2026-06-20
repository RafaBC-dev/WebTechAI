# Pine64 lanza PineVoice, un altavoz inteligente de $50 para Home Assistant

**Fecha:** 2026-06-20
**Categoría:** embebidos
**Tags:** robotica, embebidos, linux
**Título original:** Pine64 Pinevoice – A $50 RISC-V Smart Speaker for Home Assistant based on Bouffalo Lab BL606P MCU

---

## Introducción

Pine64 ha lanzado PineVoice, un altavoz inteligente de bajo costo basado en el microcontrolador Bouffalo Lab BL606P. Este dispositivo es ideal para integrarlo con Home Assistant y disfrutar de una experiencia de voz asistida en casa.

## ¿Qué es?

PineVoice es un altavoz inteligente que utiliza el microcontrolador Bouffalo Lab BL606P, un procesador RISC-V con WiFi, Bluetooth y Zigbee. Este dispositivo cuenta con dos micrófonos, un altavoz, un puerto USB 2.0 OTG y varias luces RGB.

## ¿Cómo funciona?

El Bouffalo Lab BL606P es un procesador RISC-V con dos núcleos: un núcleo D0 con un procesador T-Head C906 de 64 bits a 480 MHz y un núcleo M0 con un procesador T-Head E907 de 32 bits a 320 MHz. El dispositivo cuenta con 544KB de RAM y 16MB de PSRAM, lo que lo hace ideal para aplicaciones de voz asistida.

## ¿Por qué importa?

PineVoice es importante porque ofrece una solución de bajo costo para integrar la voz asistida en casa con Home Assistant. Esto permite a los usuarios controlar sus dispositivos inteligentes con solo hablar, lo que es especialmente útil para personas con discapacidad o que buscan una experiencia de voz más natural.

## Consejo técnico

Si deseas integrar PineVoice con Home Assistant, debes configurar el dispositivo para utilizar el protocolo ESPHome en lugar del protocolo Wyoming Satellite, que ya está descontinuado.

```bash
esp-home
```

---

**Fuente original:** [https://www.cnx-software.com/2026/06/20/pine64-pinevoice-a-50-risc-v-smart-speaker-for-home-assistant-based-on-bouffalo-lab-bl606p-mcu/](https://www.cnx-software.com/2026/06/20/pine64-pinevoice-a-50-risc-v-smart-speaker-for-home-assistant-based-on-bouffalo-lab-bl606p-mcu/)
