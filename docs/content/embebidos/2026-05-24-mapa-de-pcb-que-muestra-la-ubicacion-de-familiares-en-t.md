# Mapa de PCB que muestra la ubicación de familiares en tiempo real

**Fecha:** 2026-05-24
**Categoría:** embebidos
**Tags:** robotica, microcontroladores, software-y-linux
**Título original:** PCB Map Display Keeps An Eye On Family

---

## Introducción

Un ingeniero ha creado un mapa de PCB que muestra la ubicación de sus familiares en tiempo real, utilizando un array de LEDs RGB y un ESP32 para recibir datos de ubicación a través de MQTT

## ¿Qué es?

Un mapa de PCB es una placa de circuito impreso que se utiliza para producir arte visual funcional, en este caso, un mapa del área de East Bay en California. El mapa se crea utilizando la capa superior de cobre para las carreteras y la capa de soldadura para el terreno y las carreteras

## ¿Cómo funciona?

El mapa se conecta a un array de 64x32 LEDs RGB que se encienden en función de la ubicación de los familiares, que se reciben a través de MQTT desde sus dispositivos móviles. El ESP32 se encarga de procesar los datos y controlar los LEDs

## ¿Por qué importa?

Este proyecto es relevante porque muestra cómo la tecnología de PCB se puede utilizar para crear arte visual interactivo y útil, y cómo la integración de IoT y MQTT puede ser utilizada para crear sistemas de seguimiento de ubicación en tiempo real

## Consejo técnico

Si deseas crear un proyecto similar, puedes utilizar la librería de ESP32 para MQTT y conectar un array de LEDs RGB a tu proyecto, asegurándote de configurar correctamente la capa de soldadura y la capa de cobre en tu mapa de PCB

```bash
git clone https://github.com/jonathan/pcb-map-display
```

---

**Fuente original:** [https://hackaday.com/2026/05/23/pcb-map-display-keeps-an-eye-on-family/](https://hackaday.com/2026/05/23/pcb-map-display-keeps-an-eye-on-family/)
