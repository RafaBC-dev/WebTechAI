# SCINTIX P4: un módulo de cálculo compatible con Raspberry Pi

**Fecha:** 2026-06-17
**Categoría:** embebidos
**Tags:** robotica, microcontroladores, software-y-linux
**Título original:** SCINTIX P4 ESP32-P4 Compute Module works with (some) Raspberry Pi CM4/CM5 carrier boards (Crowdfunding)

---

## Introducción

La empresa RELOC ha lanzado el SCINTIX P4, un módulo de cálculo basado en el ESP32-P4 que es compatible con las placas de carrier de Raspberry Pi CM4/CM5. Este módulo ofrece una gran cantidad de características, incluyendo conectividad inalámbrica, interfaces de video y audio, y una gran cantidad de GPIO.

## ¿Qué es?

El SCINTIX P4 es un módulo de cálculo que utiliza el procesador dual-core RISC-V ESP32-P4, que cuenta con instrucciones de AI y una FPU de precisión simple. También incluye un procesador LP (low-power) de un solo núcleo, un acelerador de procesamiento de píxeles 2D, un decodificador de vídeo H.264 y un decodificador de imágenes JPEG.

## ¿Cómo funciona?

El SCINTIX P4 se conecta a las placas de carrier de Raspberry Pi CM4/CM5 a través de dos conectores de 100 pines, que permiten acceder a interfaces como la MIPI DSI, la MIPI CSI, el Ethernet y los GPIO. El módulo también cuenta con una conexión USB Type-C para programación y alimentación.

## ¿Por qué importa?

El SCINTIX P4 es importante porque ofrece una forma de utilizar el procesador ESP32-P4 en proyectos que requieren una gran cantidad de recursos y características, como la robótica y la automatización. También es una opción interesante para aquellos que buscan una solución de cálculo más eficiente y flexible que la Raspberry Pi.

## Consejo técnico

Si deseas utilizar el SCINTIX P4 con la Raspberry Pi, asegúrate de utilizar la biblioteca de drivers de Espressif para ESP-IDF, que es compatible con el módulo. También es recomendable utilizar la herramienta de desarrollo de Espressif, IDF Toolchain, para compilar y depurar tu código.

```bash
idf.py build
```

---

**Fuente original:** [https://www.cnx-software.com/2026/06/17/scintix-p4-esp32-p4-compute-module-raspberry-pi-cm4-cm5-carrier-boards/](https://www.cnx-software.com/2026/06/17/scintix-p4-esp32-p4-compute-module-raspberry-pi-cm4-cm5-carrier-boards/)
