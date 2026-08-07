# Control remoto de múltiples sistemas con Raspberry Pi Pico y Pi Zero 2 W

**Fecha:** 2026-08-07
**Categoría:** embebidos
**Tags:** robotica, microcontroladores, software y linux
**Título original:** PICOTTY project enables multi-target serial remote management through Raspberry Pi Pico boards and Pi Zero 2 W SBC

---

## Introducción

El proyecto PICOTTY permite controlar y monitorear múltiples sistemas de forma remota utilizando Raspberry Pi Pico y Pi Zero 2 W. Esto es especialmente útil para sistemas headless que solo requieren controlar mediante teclado.

## ¿Qué es?

PICOTTY es un proyecto de código abierto que permite controlar y monitorear múltiples sistemas de forma remota utilizando Raspberry Pi Pico y Pi Zero 2 W como hub. Cada Pico board actúa como una Ethernet-connected USB keyboard, mientras que el Pi Zero 2 W gestiona todos los nodos conectados a él.

## ¿Cómo funciona?

El proyecto utiliza un Raspberry Pi Zero 2 W como hub que corre un servidor web en el puerto 8080 y un servidor TCP en el puerto 9000 para controlar los nodos. Los nodos Raspberry Pi Pico o Pico 2 se conectan a través de un WIZnet W5100S SPI a Ethernet HAT o un WIZnet W5100S-EVB-Pico o W5100S-EVB-Pico2. El firmware de CircuitPython se utiliza para emular una consola serial y un teclado USB.

## ¿Por qué importa?

Este proyecto es especialmente útil para sistemas headless que requieren controlar mediante teclado, como sistemas de virtualización como Proxmox VE. También puede ser utilizado para controlar otros sistemas que solo requieren controlar mediante teclado.

## Consejo técnico

Para empezar a utilizar PICOTTY, puedes descargar el código fuente de CircuitPython y la aplicación de Python de PICOTTY desde GitHub y configurar tu Raspberry Pi Zero 2 W y nodos Raspberry Pi Pico o Pico 2 según las instrucciones del proyecto.

```bash
git clone https://github.com/morpheuslord/picotty.git
```

---

**Fuente original:** [https://www.cnx-software.com/2026/08/06/picotty-project-enables-multi-target-serial-remote-management-through-raspberry-pi-pico-boards-and-pi-zero-2-w-sbc/](https://www.cnx-software.com/2026/08/06/picotty-project-enables-multi-target-serial-remote-management-through-raspberry-pi-pico-boards-and-pi-zero-2-w-sbc/)
