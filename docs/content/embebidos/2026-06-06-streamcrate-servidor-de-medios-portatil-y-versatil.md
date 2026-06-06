# StreamCrate: servidor de medios portátil y versátil

**Fecha:** 2026-06-06
**Categoría:** embebidos
**Tags:** robotica, linux, raspberry-pi
**Título original:** StreamCrate: portable media server

---

## Introducción

Daveed Walzer, un entusiasta de la tecnología, ha creado un servidor de medios portátil y versátil llamado StreamCrate, que utiliza una Raspberry Pi 4 y ofrece una autonomía de 10 horas con una batería de 20.000mAh.

## ¿Qué es?

StreamCrate es un servidor de medios portátil que permite reproducir contenido de medios en dispositivos conectados a través de Wi-Fi o HDMI. Se basa en una Raspberry Pi 4 y utiliza una unidad de disco duro de 5TB para almacenar una copia sincronizada de la biblioteca de medios de Daveed.

## ¿Cómo funciona?

StreamCrate utiliza la Raspberry Pi OS Lite y lanza automáticamente el reproductor de medios cuando se detecta un dispositivo HDMI conectado. El servidor utiliza Jellyfin como reproductor de medios y Kodi para reproducir contenido en dispositivos conectados a través de HDMI.

## ¿Por qué importa?

StreamCrate es importante porque ofrece una solución portátil y versátil para reproducir contenido de medios en cualquier lugar. También permite a los usuarios almacenar una copia sincronizada de su biblioteca de medios en una unidad de disco duro de 5TB.

## Consejo técnico

Si deseas crear un servidor de medios portátil similar a StreamCrate, puedes utilizar una Raspberry Pi 4 y una unidad de disco duro de 5TB. Recuerda instalar la Raspberry Pi OS Lite y configurar Jellyfin y Kodi para reproducir contenido en dispositivos conectados.

```bash
sudo apt-get update && sudo apt-get install jellyfin kodi
```

---

**Fuente original:** [https://www.raspberrypi.com/news/streamcrate-portable-media-server/](https://www.raspberrypi.com/news/streamcrate-portable-media-server/)
