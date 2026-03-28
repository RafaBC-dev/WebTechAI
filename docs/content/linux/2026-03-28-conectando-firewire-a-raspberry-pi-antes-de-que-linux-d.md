# Conectando FireWire a Raspberry Pi antes de que Linux deje de soportarlo

**Fecha:** 2026-03-28
**Categoría:** linux
**Tags:** robotica, linux, embebidos
**Título original:** Using FireWire on a Raspberry Pi Before Linux Drops Support

---

## Introducción

La tecnología FireWire ha estado en declive desde que Apple y Sony se pasaron a USB, pero ahora Linux seguirá su ejemplo en 2029. Sin embargo, un desarrollador ha encontrado una forma de hacer que funcione en Raspberry Pi.

## ¿Qué es?

FireWire es una tecnología de transferencia de datos y control remoto que se utilizaba en dispositivos de audiovisuales y otros de alta gama. Aunque ya no es soportado por Apple y Sony, todavía se puede utilizar en Linux y Windows.

## ¿Cómo funciona?

Para conectar FireWire a Raspberry Pi, se necesita un adaptador mini PCIe a FireWire y un Mini PCIe HAT en el RPi 5. Después de instalar el adaptador, se necesita recompilar el kernel de Linux con soporte para FireWire y activar el dispositivo en la capa de dispositivo.

## ¿Por qué importa?

Esta solución es importante porque permite a los usuarios de Linux seguir utilizando dispositivos FireWire, como cámaras y grabadores de video, durante otros tres años antes de que Linux deje de soportarlo.

## Consejo técnico

Si quieres utilizar FireWire en tu Raspberry Pi, asegúrate de instalar el adaptador mini PCIe a FireWire y recompilar el kernel de Linux con soporte para FireWire. También es importante activar el dispositivo en la capa de dispositivo.

```bash
lspci
```

---

**Fuente original:** [https://hackaday.com/2026/03/27/using-firewire-on-a-raspberry-pi-before-linux-drops-support/](https://hackaday.com/2026/03/27/using-firewire-on-a-raspberry-pi-before-linux-drops-support/)
