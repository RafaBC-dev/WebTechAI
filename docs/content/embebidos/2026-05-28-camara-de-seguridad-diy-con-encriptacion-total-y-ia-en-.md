# Cámara de seguridad DIY con encriptación total y IA en el Raspberry Pi

**Fecha:** 2026-05-28
**Categoría:** embebidos
**Tags:** robotica, linux, ia-local
**Título original:** Privacy-focused, open-source Raspberry Pi Zero 2W DIY security camera offers end-to-end encryption, on-device AI

---

## Introducción

Secluso es un sistema de cámara de seguridad DIY que utiliza el Raspberry Pi para ofrecer encriptación total y detección de humanos, mascotas y vehículos. Es una alternativa a las cámaras inteligentes comerciales que envían video en vivo a la nube.

## ¿Qué es?

Secluso es un sistema de cámara de seguridad DIY que utiliza el Raspberry Pi Zero 2 W como núcleo y la Raspberry Pi Camera Module para capturar video. Ofrece encriptación total y detección de humanos, mascotas y vehículos mediante IA en el dispositivo.

## ¿Cómo funciona?

El sistema utiliza Messaging Layer Security (MLS) para encriptar el video y los metadatos, y un servidor de relay para enviar notificaciones a la aplicación móvil. La IA se ejecuta en el dispositivo y detecta humanos, mascotas y vehículos en el video capturado.

## ¿Por qué importa?

Secluso es importante porque ofrece una alternativa a las cámaras inteligentes comerciales que envían video en vivo a la nube, lo que puede ser un problema de privacidad. También ofrece una forma de implementar IA en dispositivos de seguridad DIY de manera segura.

## Consejo técnico

Para implementar Secluso en tu Raspberry Pi, asegúrate de utilizar la versión más reciente del sistema operativo y actualiza el firmware de la cámara antes de comenzar. También es recomendable utilizar un servidor de relay seguro para enviar notificaciones a la aplicación móvil.

```bash
sudo apt-get update && sudo apt-get install secluso-os
```

---

**Fuente original:** [https://www.cnx-software.com/2026/05/28/privacy-focused-open-source-raspberry-pi-zero-2w-diy-security-camera-offers-end-to-end-encryption-on-device-ai/](https://www.cnx-software.com/2026/05/28/privacy-focused-open-source-raspberry-pi-zero-2w-diy-security-camera-offers-end-to-end-encryption-on-device-ai/)
