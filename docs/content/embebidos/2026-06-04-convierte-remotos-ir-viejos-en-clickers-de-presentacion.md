# Convierte remotos IR viejos en clickers de presentación con un RP2040 y firmware TTVKTR

**Fecha:** 2026-06-04
**Categoría:** embebidos
**Tags:** robotica, microcontroladores, software y linux
**Título original:** Convert old IR remote controls into presentation clickers using an RP2040 USB board and open-source TTVKTR firmware

---

## Introducción

Un proyecto de firmware abierto llamado TTVKTR permite convertir remotos IR viejos en clickers de presentación para presentaciones y reuniones. Esto reduce la cantidad de basura electrónica y ofrece una solución sostenible.

## ¿Qué es?

El proyecto TTVKTR es un firmware abierto que se ejecuta en una placa Raspberry Pi RP2040 USB. Recibe códigos IR de un receptor IR estándar y los traduce en informes HID USB basados en una configuración JSON almacenada en el filesystem del dispositivo.

## ¿Cómo funciona?

El firmware TTVKTR utiliza un receptor IR estándar de 38 kHz y un LED RGB para mostrar la selección de capas. Los usuarios pueden asignar botones, aprender códigos IR y configurar layouts a través de una herramienta de configuración web similar a VIA o QMK.

## ¿Por qué importa?

Este proyecto importa porque reduce la cantidad de basura electrónica y ofrece una solución sostenible para convertir remotos IR viejos en clickers de presentación. También es una excelente oportunidad para aprender sobre firmware y electrónica.

## Consejo técnico

Si quieres implementar este proyecto, asegúrate de utilizar un receptor IR estándar de 38 kHz y un LED RGB compatible con el firmware TTVKTR. También es recomendable utilizar una placa Raspberry Pi RP2040-Zero debido a su tamaño compacto y precio asequible.

```bash
Para configurar el firmware TTVKTR, utiliza la herramienta de configuración web y sigue estos pasos: 1) asigna botones, 2) aprende códigos IR y 3) configura layouts.
```

---

**Fuente original:** [https://www.cnx-software.com/2026/06/04/convert-old-ir-remote-controls-into-presentation-clickers-using-an-rp2040-usb-board-and-open-source-ttvktr-firmware/](https://www.cnx-software.com/2026/06/04/convert-old-ir-remote-controls-into-presentation-clickers-using-an-rp2040-usb-board-and-open-source-ttvktr-firmware/)
