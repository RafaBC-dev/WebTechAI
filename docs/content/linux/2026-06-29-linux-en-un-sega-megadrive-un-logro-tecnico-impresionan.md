# Linux en un Sega Megadrive: un logro técnico impresionante

**Fecha:** 2026-06-29
**Categoría:** linux
**Tags:** linux, microcontroladores, embebidos
**Título original:** It’s Linux, on a Sega Megadrive

---

## Introducción

Después de más de 30 años, se ha logrado instalar Linux en un Sega Megadrive, una consola de juegos de la época que parecía imposible de modificar. Esta noticia sorprende a la comunidad de tecnología y nos hace reflexionar sobre la capacidad de adaptación de Linux.

## ¿Qué es?

LinuxMD es un proyecto que consiste en instalar el kernel de Linux en un Sega Megadrive, utilizando un periférico de almacenamiento SD. Esto permite ejecutar aplicaciones Linux en una consola que originalmente estaba diseñada para ejecutar juegos de 16 bits.

## ¿Cómo funciona?

El proyecto utiliza el kernel de Linux compilado con la opción -nommu, que permite ejecutar Linux en arquitecturas sin unidad de gestión de memoria (MMU). Esto se logra gracias a la compatibilidad del Motorola 68000, el procesador original de la consola. El sistema utiliza smolutils y una versión reducida de coreutils para proporcionar una experiencia de usuario básica.

## ¿Por qué importa?

Este proyecto es importante porque demuestra la capacidad de adaptación de Linux y su capacidad para ejecutarse en una amplia variedad de plataformas. También muestra la posibilidad de utilizar Linux en dispositivos antiguos, lo que puede ser útil para preservar la historia de la tecnología y proporcionar una experiencia de usuario moderna en dispositivos obsoletos.

## Consejo técnico

Si deseas probar Linux en tu Sega Megadrive, asegúrate de utilizar un periférico de almacenamiento SD compatible y configura el kernel de Linux con la opción -nommu para evitar problemas de compatibilidad.

```bash
sudo apt-get install linux-headers-68000
```

---

**Fuente original:** [https://hackaday.com/2026/06/29/its-linux-on-a-sega-megadrive/](https://hackaday.com/2026/06/29/its-linux-on-a-sega-megadrive/)
