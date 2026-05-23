# Reverso de motor de Unitree GO-M8018-6: un logro en la robótica

**Fecha:** 2026-05-23
**Categoría:** robotica
**Tags:** robotica, embebidos, linux
**Título original:** Unitree GO-M8018-6 Motor Reverse Engineering

---

## Introducción

Un ingeniero ha logrado reverse-engineer el motor de un robot quadruped de bajo costo, permitiendo la creación de firmware personalizado y abriendo la puerta a una mayor accesibilidad en la robótica.

## ¿Qué es?

El motor de Unitree GO-M8018-6 es un componente de alta tecnología que incluye un reduador, encoder magnético, inverter de tres fases, sensor de corriente, bus RS-485 y un microcontrolador Cortex-M0. Su objetivo es proporcionar un actuator compacto para aplicaciones de robótica.

## ¿Cómo funciona?

El proceso de reverse-engineering involucró la identificación del microcontrolador y otros componentes a través de un análisis de la placa de circuito impreso (PCB) y la utilización de herramientas como X-ray y OpenOCD. Se logró acceder al firmware y extraer la clave de encriptación, permitiendo la creación de firmware personalizado.

## ¿Por qué importa?

Este logro es importante porque abre la puerta a una mayor accesibilidad en la robótica, permitiendo a desarrolladores crear firmware personalizado y mejorar la seguridad de los sistemas. Además, puede dar una nueva vida al robot quadruped Go2, que ha sido afectado por problemas de seguridad.

## Consejo técnico

Para comenzar a trabajar con este motor, es recomendable utilizar herramientas como OpenOCD y SWD para acceder al firmware y extraer la clave de encriptación. También es importante estudiar la documentación de la placa de circuito impreso y el microcontrolador para entender su funcionamiento.

```bash
openocd -f interface/swd2.jtag -c 'swdp_scan; init; halt; mww 0x40000000 0x12345678; mww 0x40000004 0x90abcdef; resume; cbreak; halt'
```

---

**Fuente original:** [https://hackaday.com/2026/05/23/unitree-go-m8018-6-motor-reverse-engineering/](https://hackaday.com/2026/05/23/unitree-go-m8018-6-motor-reverse-engineering/)
