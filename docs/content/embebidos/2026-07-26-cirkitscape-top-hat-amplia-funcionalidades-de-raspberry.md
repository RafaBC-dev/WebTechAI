# CirkitScape Top HAT: amplía funcionalidades de Raspberry Pi con GPIOs adicionales

**Fecha:** 2026-07-26
**Categoría:** embebidos
**Tags:** robotica, microcontroladores, software-y-linux
**Título original:** CirkitScape Top HAT adds extra GPIOs, RS-485, 3-channel ADC, four USB 2.0 ports to Raspberry Pi SBCs

---

## Introducción

CirkitScape ha lanzado el Top HAT, una placa de expansión para Raspberry Pi que agrega 16 GPIOs adicionales, un conector RS-485, un conversor analógico-digital de 3 canales y cuatro puertos USB 2.0. Esto facilita la prototipificación, el monitoreo de sensores y la automatización de proyectos con Raspberry Pi.

## ¿Qué es?

El Top HAT es una placa de expansión para Raspberry Pi que agrega funcionalidades adicionales a través de un expander I2C, un conector RS-485, un conversor analógico-digital de 3 canales y cuatro puertos USB 2.0. Esto permite a los usuarios aprovechar al máximo la potencia de Raspberry Pi en proyectos de IoT, automatización y prototipificación.

## ¿Cómo funciona?

La placa de expansión utiliza un expander I2C para agregar 16 GPIOs adicionales, un conversor analógico-digital ADS1015 para leer señales analógicas de 3 canales y un conector RS-485 para comunicarse con dispositivos RS-485. Los cuatro puertos USB 2.0 se conectan a través de un hub USB 2.0. La placa es compatible con Raspberry Pi OS y no requiere firmware personalizado.

## ¿Por qué importa?

El Top HAT es relevante para proyectos de IoT, automatización y prototipificación que requieren la adición de sensores, actuadores y dispositivos periféricos a Raspberry Pi. También es útil para proyectos que requieren comunicación serial o RS-485.

## Consejo técnico

Para aprovechar al máximo el Top HAT, es recomendable utilizar la biblioteca pyserial para comunicarse con dispositivos RS-485 y la biblioteca gpiozero para controlar los GPIOs adicionales.

```bash
pip install pyserial gpiozero
```

---

**Fuente original:** [https://www.cnx-software.com/2026/07/24/cirkitscape-top-hat-adds-extra-gpios-rs-485-3-channel-adc-four-usb-2-0-ports-to-raspberry-pi-sbcs/](https://www.cnx-software.com/2026/07/24/cirkitscape-top-hat-adds-extra-gpios-rs-485-3-channel-adc-four-usb-2-0-ports-to-raspberry-pi-sbcs/)
