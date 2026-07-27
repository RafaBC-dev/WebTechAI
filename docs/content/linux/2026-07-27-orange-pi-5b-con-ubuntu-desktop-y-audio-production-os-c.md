# Orange Pi 5B con Ubuntu Desktop y Audio Production OS con Bluetooth/Wi-Fi solucionados

**Fecha:** 2026-07-27
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Orange Pi 5B SBC gets Ubuntu Desktop and Audio Production OS images with Bluetooth/Wi-Fi fix missed for 8 years

---

## Introducción

Después de 8 años de espera, se han solucionado dos problemas críticos en el módulo Bluetooth/Wi-Fi del Orange Pi 5B, lo que permite utilizar Ubuntu Desktop y Audio Production OS en este SBC. Un desarrollador ha creado dos imágenes de Ubuntu 24.04 basadas en el proyecto ubuntu-rockchip, que incluyen estas soluciones.

## ¿Qué es?

El Orange Pi 5B es un SBC (Single-Board Computer) que utiliza el procesador Rockchip RK3588 y tiene problemas con el módulo Bluetooth/Wi-Fi Ampak AP6275P. El proyecto ubuntu-rockchip es una iniciativa para crear imágenes de Ubuntu que funcionen en este SBC. Después de que el desarrollador original se retiró, un nuevo desarrollador ha creado dos imágenes de Ubuntu que incluyen soluciones para estos problemas.

## ¿Cómo funciona?

Las dos imágenes de Ubuntu, Pi Desktop y Pi Studio, se basan en el proyecto ubuntu-rockchip y incluyen soluciones para los problemas de Bluetooth/Wi-Fi. La primera imagen, Pi Desktop, es una versión de escritorio de Ubuntu que incluye una solución para el problema de Bluetooth muerto al arrancar, mientras que la segunda imagen, Pi Studio, es una versión para producción de audio que incluye una solución para el problema de audio estropeado al escanear Wi-Fi.

## ¿Por qué importa?

Estas soluciones son importantes porque permiten utilizar Ubuntu Desktop y Audio Production OS en el Orange Pi 5B, lo que abre nuevas posibilidades para desarrolladores y usuarios que buscan un SBC con estas características. Además, estas soluciones pueden ser aplicadas a otros SBC que compartan el mismo problema de Bluetooth/Wi-Fi.

## Consejo técnico

Si deseas utilizar Ubuntu Desktop o Audio Production OS en tu Orange Pi 5B, puedes descargar las imágenes de Ubuntu creadas por este desarrollador y seguir las instrucciones para instalarlas. También puedes investigar el proyecto ubuntu-rockchip y contribuir con tus propias soluciones para mejorar la compatibilidad de Ubuntu con este SBC.

```bash
sudo apt update && sudo apt install ubuntu-rockchip-ubuntu-desktop
```

---

**Fuente original:** [https://www.cnx-software.com/2026/07/27/orange-pi-5b-sbc-gets-ubuntu-desktop-and-audio-production-os-images-with-bluetooth-wi-fi-fix-missed-for-8-years/](https://www.cnx-software.com/2026/07/27/orange-pi-5b-sbc-gets-ubuntu-desktop-and-audio-production-os-images-with-bluetooth-wi-fi-fix-missed-for-8-years/)
