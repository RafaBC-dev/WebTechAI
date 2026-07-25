# CirkitScape Top HAT: una tarjeta de expansión para Raspberry Pi

**Fecha:** 2026-07-25
**Categoría:** embebidos
**Tags:** robotica, microcontroladores, software y linux
**Título original:** CirkitScape Top HAT adds extra GPIOs, RS-485, 3-channel ADC, four USB 2.0 ports to Raspberry Pi SBCs

---

## Introducción

CirkitScape ha lanzado la Top HAT, una tarjeta de expansión para Raspberry Pi que agrega funcionalidades adicionales como GPIOs, RS-485 y ADC. Esta tarjeta busca facilitar la prototipificación y el desarrollo de proyectos con Raspberry Pi.

## ¿Qué es?

La Top HAT es una tarjeta de expansión para Raspberry Pi que agrega 16 GPIOs adicionales a través de un expander I2C, un conector RS-485, un ADC de 3 canales y 12 bits, y cuatro puertos USB 2.0 adicionales a través de un hub USB.

## ¿Cómo funciona?

La Top HAT utiliza un expander I2C MCP23017 para agregar 16 GPIOs adicionales, un ADC ADS1015 para leer señales analógicas y un transceptor MAX485 para comunicarse a través de RS-485. La tarjeta también incluye un hub USB para proporcionar cuatro puertos USB 2.0 adicionales.

## ¿Por qué importa?

La Top HAT es importante porque permite a los desarrolladores de Raspberry Pi acceder a una mayor cantidad de GPIOs, ADC y puertos USB, lo que facilita la prototipificación y el desarrollo de proyectos de automatización, sensores y IoT.

## Consejo técnico

Si estás desarrollando un proyecto con Raspberry Pi, considera utilizar la Top HAT para agregar funcionalidades adicionales y simplificar tu diseño.

```bash
python -m smbus -s 1 0x12 0x34
```

---

**Fuente original:** [https://www.cnx-software.com/2026/07/24/cirkitscape-top-hat-adds-extra-gpios-rs-485-3-channel-adc-four-usb-2-0-ports-to-raspberry-pi-sbcs/](https://www.cnx-software.com/2026/07/24/cirkitscape-top-hat-adds-extra-gpios-rs-485-3-channel-adc-four-usb-2-0-ports-to-raspberry-pi-sbcs/)
