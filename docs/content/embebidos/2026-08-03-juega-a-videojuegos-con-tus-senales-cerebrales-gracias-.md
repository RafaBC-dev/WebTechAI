# Juega a videojuegos con tus señales cerebrales gracias a Octopus 16

**Fecha:** 2026-08-03
**Categoría:** embebidos
**Tags:** robotica, microcontroladores, software y linux
**Título original:** Play games with your brain signals using Octopus 16 wireless EEG device

---

## Introducción

La empresa PiEEG ha lanzado Octopus 16, un dispositivo de señales cerebrales inalámbrico que permite jugar a videojuegos sin necesidad de manos ni implantes. Este dispositivo es una herramienta revolucionaria para la interacción humana con la tecnología.

## ¿Qué es?

Octopus 16 es un dispositivo de señales cerebrales que utiliza 16 electrodos para medir señales cerebrales, electromiografía y electrocardiografía. Se conecta a un tablero de desarrollo XIAO ESP32-S3 y actúa como un gamepad BLE HID. El software es de código abierto y se puede encontrar en GitHub.

## ¿Cómo funciona?

El dispositivo se coloca en la cabeza y los 18 pinos de contacto se conectan con el cráneo. El XIAO ESP32-S3 actúa como un gamepad BLE HID y se integra con el servidor PiEEG. El software utiliza dos convertidores analógicos-digitales Texas Instruments ADS131M08 de 24 bits y 8 canales para medir las señales cerebrales.

## ¿Por qué importa?

Octopus 16 puede revolucionar la forma en que interactuamos con la tecnología. Permite a las personas con discapacidad física jugar a videojuegos y utilizar dispositivos electrónicos de manera más independiente. También puede ser utilizado en aplicaciones médicas para estudiar la actividad cerebral.

## Consejo técnico

Para empezar a utilizar Octopus 16, descarga el software de código abierto de GitHub y sigue las instrucciones para conectar el dispositivo a tu XIAO ESP32-S3. Asegúrate de seguir las recomendaciones de seguridad para evitar dañar tus electrodos cerebrales.

```bash
git clone https://github.com/pi-eeg/octopus-16.git
```

---

**Fuente original:** [https://www.cnx-software.com/2026/08/02/play-games-with-your-brain-signals-using-octopus-16-wireless-eeg-device/](https://www.cnx-software.com/2026/08/02/play-games-with-your-brain-signals-using-octopus-16-wireless-eeg-device/)
