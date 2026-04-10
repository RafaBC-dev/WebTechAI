# Raspberry Pi recibe HAT de radio digital con AM, FM, DAB y HD

**Fecha:** 2026-04-10
**Categoría:** embebidos
**Tags:** robotica, microcontroladores, software y linux
**Título original:** Raspberry Pi SBC gets (analog and) digital radio HAT with AM, FM, DAB, DAB+, HD radio

---

## Introducción

Raspiaudio ha lanzado un nuevo HAT para Raspberry Pi que agrega soporte para radios digitales, incluyendo AM, FM, DAB y HD. Esto abre nuevas posibilidades para proyectos de radio en Raspberry Pi.

## ¿Qué es?

El HAT Digital Radio V1 es una placa que se conecta a Raspberry Pi y agrega soporte para radios digitales. Incluye un receptor de radio digital Skyworth Si4689-A10 y soporta AM, FM, DAB y HD. También incluye una antena SMA y un altavoz integrado.

## ¿Cómo funciona?

El HAT utiliza el receptor de radio digital Skyworth Si4689-A10 para recibir señales de radio digital. El receptor es capaz de recibir señales de AM, FM, DAB y HD y las envía a Raspberry Pi a través de la interfaz SPI o I2C. Raspberry Pi entonces procesa las señales y las reproduce a través del altavoz integrado o a través de una conexión de audio externa.

## ¿Por qué importa?

El HAT Digital Radio V1 es importante porque permite a los usuarios de Raspberry Pi crear proyectos de radio digital sin necesidad de comprar hardware adicional. Esto abre nuevas posibilidades para proyectos de radio en Raspberry Pi, como crear radios digitales, reproducir radio en línea y más.

## Consejo técnico

Si deseas crear un proyecto de radio digital con Raspberry Pi, primero asegúrate de instalar el software de Raspiaudio en tu Raspberry Pi. Luego, conecta el HAT Digital Radio V1 a tu Raspberry Pi y configura el software para que se conecte al receptor de radio digital.

```bash
git clone https://github.com/RASPIAUDIOadmin/
```

---

**Fuente original:** [https://www.cnx-software.com/2026/04/10/raspberry-pi-sbc-gets-digital-radio-hat-with-am-fm-dab-dab-hd-radio/](https://www.cnx-software.com/2026/04/10/raspberry-pi-sbc-gets-digital-radio-hat-with-am-fm-dab-dab-hd-radio/)
