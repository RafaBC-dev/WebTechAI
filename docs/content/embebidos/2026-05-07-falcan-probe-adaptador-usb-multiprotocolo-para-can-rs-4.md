# FalCAN Probe: adaptador USB multiprotocolo para CAN, RS-485 y RS-422

**Fecha:** 2026-05-07
**Categoría:** embebidos
**Tags:** robotica, embebidos, linux
**Título original:** FalCAN Probe is an open-source, STM32-based USB to CAN/RS-485/RS-422 adapter

---

## Introducción

El FalCAN Probe es un adaptador USB multiprotocolo que permite conectar un ordenador a redes CAN, RS-485 y RS-422. Esta herramienta es especialmente útil para desarrolladores de sistemas embebidos y de automatización industrial.

## ¿Qué es?

El FalCAN Probe es un adaptador USB compacto y abierto que utiliza un microcontrolador STM32F042 para conectar un ordenador a redes CAN, RS-485 y RS-422. Ofrece una interfaz USB 2.0 Full Speed y expone la interfaz USB nativa del MCU, junto con pines GPIO y SWD.

## ¿Cómo funciona?

El FalCAN Probe utiliza un firmware basado en una bifurcación del firmware de CandleLight, que soporta el módulo kernel gs_usb de Linux. Esto permite que el adaptador se conecte a un ordenador con Ubuntu o Raspberry Pi OS sin necesidad de instalar drivers personalizados. El modo de comunicación se selecciona mediante jumperes de hardware.

## ¿Por qué importa?

El FalCAN Probe es importante porque ofrece una solución flexible y abierta para conectar un ordenador a redes industriales. Puede ser utilizado como generador de tráfico de red, analizador de CAN o incluso como un programa de enlace ST-Link personalizado.

## Consejo técnico

Si deseas utilizar el FalCAN Probe con Linux, asegúrate de instalar el módulo kernel gs_usb y configurar el firmware para que se comporte como una interfaz CAN o RS-485/RS-422.

```bash
sudo modprobe gs_usb
```

---

**Fuente original:** [https://www.cnx-software.com/2026/05/07/falcan-probe-open-source-stm32-based-usb-to-can-adapter-rs485-rs422/](https://www.cnx-software.com/2026/05/07/falcan-probe-open-source-stm32-based-usb-to-can-adapter-rs485-rs422/)
