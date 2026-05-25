# Hacking un walkie-talkie de video para ejecutar DOOM

**Fecha:** 2026-05-25
**Categoría:** embebidos
**Tags:** robotica, microcontroladores, software-y-linux
**Título original:** Hacking a Video Walkie Talkie’s TXW818 MCU and Running DOOM

---

## Introducción

Un entusiasta de la ingeniería inversa ha descubierto que los walkie-talkies de video baratos que se venden en línea contienen un microcontrolador potente que puede ser hackeado para ejecutar juegos como DOOM. Esto abre la puerta a una variedad de posibilidades para los entusiastas de la electrónica y la programación.

## ¿Qué es?

El proyecto consiste en hackear un walkie-talkie de video barato para que pueda ejecutar el juego clásico DOOM. El walkie-talkie utiliza un microcontrolador TXW818 que cuenta con un procesador CK803 de 240 MHz y 272 kB de memoria SRAM, así como soporte para BLE y Wi-Fi. El objetivo es crear un dispositivo que pueda ejecutar juegos de manera independiente.

## ¿Cómo funciona?

Para llevar a cabo este proyecto, se necesita descargar el CDK IDE y compilar el código fuente. Luego, se puede cargar el código en un módulo STM32F103 'Blue Pill' para que se pueda ejecutar en el walkie-talkie. El proceso implica trabajar con el SDK del microcontrolador, que puede ser un poco complicado de usar, pero ofrece una gran cantidad de funcionalidades.

## ¿Por qué importa?

Este proyecto es importante porque muestra que es posible hackear dispositivos electrónicos comunes para darles nuevas funciones y posibilidades. Esto puede abrir la puerta a una variedad de aplicaciones y proyectos innovadores, especialmente en el ámbito de la robótica y la electrónica.

## Consejo técnico

Si deseas probar este proyecto, asegúrate de descargar el CDK IDE y compilar el código fuente correctamente. También es importante tener en cuenta que el SDK del microcontrolador puede ser un poco complicado de usar, así que no dudes en buscar recursos adicionales si lo necesitas.

```bash
cdk ide --download
```

---

**Fuente original:** [https://hackaday.com/2026/05/24/hacking-a-video-walkie-talkies-txw818-mcu-and-running-doom/](https://hackaday.com/2026/05/24/hacking-a-video-walkie-talkies-txw818-mcu-and-running-doom/)
