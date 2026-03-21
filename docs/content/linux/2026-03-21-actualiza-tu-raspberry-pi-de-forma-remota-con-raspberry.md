# Actualiza tu Raspberry Pi de forma remota con Raspberry Pi Connect

**Fecha:** 2026-03-21
**Categoría:** linux
**Tags:** robotica, linux, codigo
**Título original:** New: Remote updates on Raspberry Pi Connect

---

## Introducción

Raspberry Pi Connect es una herramienta que permite acceder a tu Raspberry Pi desde cualquier lugar del mundo de forma segura y conveniente. Ahora, gracias a la nueva función de actualizaciones remotas, puedes actualizar el software de tu dispositivo sin necesidad de abrir una sesión de Connect.

## ¿Qué es?

Raspberry Pi Connect es una herramienta que permite acceder a tu Raspberry Pi desde cualquier lugar del mundo de forma segura y conveniente. La nueva función de actualizaciones remotas permite actualizar el software de tu dispositivo sin necesidad de abrir una sesión de Connect.

## ¿Cómo funciona?

La función de actualizaciones remotas utiliza el servidor de Connect para gestionar la actualización del software. Puedes crear un artefacto (un paquete que contiene el software actualizado) y ponerlo en un lugar accesible para el dispositivo. Cuando el dispositivo se conecte a Internet, Connect se encargará de instalar el artefacto.

## ¿Por qué importa?

La función de actualizaciones remotas es importante porque permite actualizar el software de tu dispositivo de forma fácil y conveniente, sin necesidad de estar físicamente conectado a él.

## Consejo técnico

Si deseas utilizar la función de actualizaciones remotas, asegúrate de instalar la última versión del paquete rpi-connect y rpi-connect-ota, y de habilitar la actualización experimental mediante el comando rpi-connect ota on.

```bash
$ sudo apt update
$ sudo apt install rpi-connect rpi-connect-ota
$ rpi-connect ota on
```

---

**Fuente original:** [https://www.raspberrypi.com/news/new-remote-updates-on-raspberry-pi-connect/](https://www.raspberrypi.com/news/new-remote-updates-on-raspberry-pi-connect/)
