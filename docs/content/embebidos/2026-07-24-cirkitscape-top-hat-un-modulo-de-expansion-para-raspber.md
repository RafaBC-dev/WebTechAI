# CirkitScape Top HAT: un módulo de expansión para Raspberry Pi

**Fecha:** 2026-07-24
**Categoría:** embebidos
**Tags:** robotica, microcontroladores, software y linux
**Título original:** CirkitScape Top HAT adds extra GPIOs, RS-485, 3-channel ADC, four USB 2.0 ports to Raspberry Pi SBCs

---

## Introducción

CirkitScape ha lanzado un módulo de expansión llamado Top HAT para Raspberry Pi, que agrega funciones adicionales como GPIO, RS-485, ADC y puertos USB. Esto facilita la creación de prototipos y proyectos de automatización.

## ¿Qué es?

El CirkitScape Top HAT es un módulo de expansión para Raspberry Pi que agrega 16 GPIO adicionales a través de un expander I2C, un conector RS-485, un ADC de 3 canales de 12 bits y cuatro puertos USB 2.0 adicionales a través de un hub USB.

## ¿Cómo funciona?

El módulo utiliza un expander I2C MCP23017 para agregar GPIO adicionales, un ADC ADS1015 para leer señales analógicas y un transceptor MAX485 para comunicarse con dispositivos RS-485. Los puertos USB se conectan a un hub USB para proporcionar cuatro puertos adicionales.

## ¿Por qué importa?

El CirkitScape Top HAT es importante para proyectos de automatización, sensores y IoT, ya que proporciona una forma fácil de agregar funciones adicionales a Raspberry Pi sin necesidad de agregar módulos adicionales.

## Consejo técnico

Si estás trabajando con Raspberry Pi, considera utilizar el CirkitScape Top HAT para agregar funciones adicionales a tu proyecto. Puedes instalar el módulo y utilizar las bibliotecas de Python proporcionadas para controlarlo.

```bash
pip install smbus pyserial gpiozero
```

---

**Fuente original:** [https://www.cnx-software.com/2026/07/24/cirkitscape-top-hat-adds-extra-gpios-rs-485-3-channel-adc-four-usb-2-0-ports-to-raspberry-pi-sbcs/](https://www.cnx-software.com/2026/07/24/cirkitscape-top-hat-adds-extra-gpios-rs-485-3-channel-adc-four-usb-2-0-ports-to-raspberry-pi-sbcs/)
