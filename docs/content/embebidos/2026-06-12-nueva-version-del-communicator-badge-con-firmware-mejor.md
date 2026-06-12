# Nueva versión del Communicator Badge con firmware mejorado

**Fecha:** 2026-06-12
**Categoría:** embebidos
**Tags:** robotica, microcontroladores, software-y-linux
**Título original:** The Hackaday Communicator Badge, Re-Imagined With New Firmware

---

## Introducción

El Communicator Badge ha regresado con una nueva versión que incluye mejoras significativas en su firmware. Esta actualización permite una mayor eficiencia y funcionalidad al dispositivo, convirtiéndolo en una herramienta más útil para los usuarios.

## ¿Qué es?

El Communicator Badge es un dispositivo de mano con teclado QWERTY, radio LoRa y procesador ESP32. Fue diseñado para ser un gadget útil para la comunicación y la conexión con otros dispositivos. La nueva versión del firmware incluye soporte para Meshtastic y una mayor eficiencia en la batería.

## ¿Cómo funciona?

El Communicator Badge utiliza MicroPython como firmware y está basado en la plataforma ESP-IDF. La nueva versión del firmware utiliza FreeRTOS como sistema operativo y soporta Meshtastic, una plataforma de comunicación de dispositivos inalámbricos. Esto permite a los usuarios conectarse a otros dispositivos y compartir datos de manera segura.

## ¿Por qué importa?

La nueva versión del Communicator Badge es importante porque ofrece una mayor funcionalidad y eficiencia. Los usuarios pueden utilizar el dispositivo para comunicarse con otros dispositivos y compartir datos de manera segura. Además, la actualización del firmware permite una mayor duración de la batería, lo que hace que el dispositivo sea más práctico para uso diario.

## Consejo técnico

Si deseas actualizar el firmware de tu Communicator Badge, asegúrate de seguir las instrucciones proporcionadas en la documentación oficial. Utiliza la herramienta ESP-IDF para instalar el nuevo firmware y asegúrate de que tu dispositivo esté configurado correctamente.

```bash
espidf flash --chip esp32 --port /dev/ttyUSB0
```

---

**Fuente original:** [https://hackaday.com/2026/06/12/the-hackaday-communicator-badge-re-imagined-with-new-firmware/](https://hackaday.com/2026/06/12/the-hackaday-communicator-badge-re-imagined-with-new-firmware/)
