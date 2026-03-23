# Nueva versión del ESP32-P4 requiere diseño de PCB y firmware actualizados

**Fecha:** 2026-03-23
**Categoría:** embebidos
**Tags:** esp32, embebidos, linux
**Título original:** ESP32-P4 revision 3.0 gains new power rail, requires new PCB design and firmware

---

## Introducción

La empresa Espressif ha lanzado una nueva versión del ESP32-P4, un microcontrolador dual-core de 400 MHz, que incluye cambios importantes en la configuración de pines y la necesidad de una actualización del firmware. Esto afecta a diseñadores de hardware y desarrolladores de software que trabajan con esta tecnología.

## ¿Qué es?

El ESP32-P4 es un microcontrolador dual-core de 400 MHz basado en el procesador RISC-V, diseñado para aplicaciones de IoT y embebidas. La versión 3.0 de este microcontrolador incluye cambios importantes en la configuración de pines y la necesidad de una actualización del firmware.

## ¿Cómo funciona?

La versión 3.0 del ESP32-P4 convierte el pin 54 de la placa de circuito impreso (PCB) de un pin no conectado a un rail de alimentación (VDD_HP_1). Esto requiere la adición de componentes adicionales y la actualización del firmware para que funcione correctamente. La actualización del firmware implica recompilar el código utilizando la configuración adecuada en el framework ESP-IDF.

## ¿Por qué importa?

Estos cambios son importantes para diseñadores de hardware y desarrolladores de software que trabajan con el ESP32-P4, ya que requieren una actualización del diseño de PCB y del firmware para que la tecnología funcione correctamente. Esto puede afectar a la estabilidad y la eficiencia de las aplicaciones que utilizan este microcontrolador.

## Consejo técnico

Si estás trabajando con el ESP32-P4, asegúrate de verificar la versión de tu microcontrolador y actualizar el firmware utilizando la configuración adecuada en el framework ESP-IDF. Esto te permitirá aprovechar al máximo las características de la versión 3.0 de este microcontrolador.

```bash
CONFIG_ESP32P4_REV_MIN
```

---

**Fuente original:** [https://www.cnx-software.com/2026/03/23/esp32-p4-revision-3-0-gains-new-power-rail-requires-new-pcb-design-and-firmware/](https://www.cnx-software.com/2026/03/23/esp32-p4-revision-3-0-gains-new-power-rail-requires-new-pcb-design-and-firmware/)
