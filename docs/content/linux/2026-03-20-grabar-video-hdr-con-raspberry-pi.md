# Grabar video HDR con Raspberry Pi

**Fecha:** 2026-03-20
**Categoría:** linux
**Tags:** robotica, microcontroladores, software-y-linux
**Título original:** Recording HDR Video With A Raspberry Pi

---

## Introducción

El equipo de Raspberry Pi puede conectarse a una variedad de cámaras compatibles. Un usuario llamado Collimated Beard ha estado explorando el uso del sensor de cámara IMX585 de Sony, que puede capturar contenido HDR en resolución 4K.

## ¿Qué es?

El IMX585 es un sensor de cámara de Sony que puede capturar contenido HDR en resolución 4K. Para hacerlo funcionar con Raspberry Pi, se necesita una cámara compatible con este sensor y realizar algunas configuraciones adicionales.

## ¿Cómo funciona?

Para grabar video HDR con Raspberry Pi, se necesita una cámara con el sensor IMX585 y realizar algunas configuraciones adicionales. Esto incluye compilar el kernel con cambios y configurar las herramientas Video4Linux2 para habilitar la función de grabación HDR.

## ¿Por qué importa?

Grabar video HDR con Raspberry Pi puede ser útil para capturar imágenes de alta calidad en entornos con un amplio rango dinámico. Esto puede ser especialmente útil para aplicaciones como la cinematografía y la documentación de eventos.

## Consejo técnico

Si deseas grabar video HDR con Raspberry Pi, asegúrate de compilar el kernel con cambios y configurar las herramientas Video4Linux2 correctamente. También es importante encontrar una cámara compatible con el sensor IMX585.

```bash
sudo make menuconfig
```

---

**Fuente original:** [https://hackaday.com/2026/03/19/recording-hdr-video-with-a-raspberry-pi/](https://hackaday.com/2026/03/19/recording-hdr-video-with-a-raspberry-pi/)
