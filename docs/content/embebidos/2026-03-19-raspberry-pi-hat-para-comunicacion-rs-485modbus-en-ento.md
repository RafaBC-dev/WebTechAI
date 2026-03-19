# Raspberry Pi HAT para comunicación RS-485/Modbus en entornos industriales

**Fecha:** 2026-03-19
**Categoría:** embebidos
**Tags:** robotica, embebidos, linux
**Título original:** Industrial RS-485/Modbus Raspberry Pi HAT works with OpenPLC, supports 7V-32V DC input

---

## Introducción

EngineElectronicAccessories ha presentado el 'Industrial RS485 / Modbus HAT', un dispositivo para Raspberry Pi diseñado para comunicación en entornos industriales. Este HAT permite la comunicación a larga distancia mediante el estándar RS-485 y es compatible con el software OpenPLC.

## ¿Qué es?

El Industrial RS485 / Modbus HAT es un dispositivo para Raspberry Pi que permite la comunicación RS-485/Modbus en entornos industriales. Se trata de un HAT que se conecta a la placa Raspberry Pi y proporciona una interfaz RS-485 con transceptor integrado y protección contra sobretensiones. También acepta voltaje de 7V a 32V DC, lo que permite alimentar tanto el HAT como la placa Raspberry Pi directamente desde una fuente de 24V.

## ¿Cómo funciona?

El HAT utiliza la interfaz UART de la placa Raspberry Pi y proporciona una conexión RS-485 a través de 5 pines de tornillos pesados. El transceptor RS-485 está protegido contra sobretensiones mediante diodos TVS. El HAT también incluye LEDs de diagnóstico para la transmisión y recepción de datos.

## ¿Por qué importa?

Este HAT es importante para proyectos de automatización industrial, monitoreo y control, ya que permite la comunicación a larga distancia y es compatible con el software OpenPLC. También es útil para proyectos de energía, como la lectura de medidores inteligentes y la interfaz con sistemas de baterías solares.

## Consejo técnico

Si deseas utilizar este HAT con OpenPLC, asegúrate de configurar la interfaz UART en la placa Raspberry Pi y de ajustar los parámetros de comunicación según las especificaciones del HAT.

```bash
sudo raspi-config -i
```

---

**Fuente original:** [https://www.cnx-software.com/2026/03/19/industrial-rs485-modbus-raspberry-pi-hat-works-with-openplc-supports-7v-32v-dc-input/](https://www.cnx-software.com/2026/03/19/industrial-rs485-modbus-raspberry-pi-hat-works-with-openplc-supports-7v-32v-dc-input/)
