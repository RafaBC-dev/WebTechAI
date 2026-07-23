# Descubre la nRF54L15 Discovery: un devboard con CMSIS-DAP debugger

**Fecha:** 2026-07-23
**Categoría:** embebidos
**Tags:** robotica, embebidos, linux
**Título original:** Icy Electronics nRF54L15 Discovery devboard integrates a snappable nRF52820 CMSIS-DAP debugger

---

## Introducción

La nRF54L15 Discovery es un devboard compacto para aplicaciones IoT que integra un CMSIS-DAP debugger/programador y soporta protocolos como Bluetooth LE, Thread y Zigbee.

## ¿Qué es?

La nRF54L15 Discovery es un devboard compacto que integra un nRF52820 CMSIS-DAP debugger/programador para aplicaciones IoT. Se trata de un sistema en módulo que incluye un nRF54L15 wireless SoC, un nRF52820 debugger SoC y un nPM1300 PMIC.

## ¿Cómo funciona?

El devboard se basa en un nRF54L15 wireless SoC que incluye un Arm Cortex-M33 a 128 MHz, un RISC-V coprocesador y 256 KB de SRAM. El nRF52820 debugger SoC incluye un Arm Cortex-M4 a 64 MHz y 32 KB de RAM. El nPM1300 PMIC proporciona alimentación a 5V a través de USB-C y soporta carga de batería LiPo.

## ¿Por qué importa?

La nRF54L15 Discovery es relevante para desarrolladores de aplicaciones IoT que necesitan un devboard compacto y versátil para prototipar y desarrollar proyectos. Soporta protocolos como Bluetooth LE, Thread, Zigbee y Matter, y se puede utilizar con Zephyr RTOS, el nRF Connect SDK y (Micro)Python.

## Consejo técnico

Para empezar a trabajar con la nRF54L15 Discovery, asegúrate de descargar el nRF Connect SDK y seguir las instrucciones de configuración para tu sistema operativo. Luego, puedes utilizar el CMSIS-DAP debugger para depurar y programar tu proyecto.

```bash
nrfjprog --family NRF52 --part nrf52820 --command erase
```

---

**Fuente original:** [https://www.cnx-software.com/2026/07/23/icy-electronics-nrf54l15-discovery-devboard-integrates-a-snappable-nrf52820-cmsis-dap-debugger/](https://www.cnx-software.com/2026/07/23/icy-electronics-nrf54l15-discovery-devboard-integrates-a-snappable-nrf52820-cmsis-dap-debugger/)
