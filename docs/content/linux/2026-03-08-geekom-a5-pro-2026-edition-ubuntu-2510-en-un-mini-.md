# GEEKOM A5 Pro 2026 Edition: Ubuntu 25.10 en un mini PC AMD Ryzen 5 7530U

**Fecha:** 2026-03-08
**Categoría:** linux
**Tags:** Ubuntu, Linux, AMD Ryzen 5 7530U, mini PC, dual boot
**Título original:** GEEKOM A5 Pro 2026 Edition Review – Part 3: Ubuntu 25.10 on an AMD Ryzen 5 7530U mini PC

---

## Introducción

El mini PC GEEKOM A5 Pro 2026 Edition, equipado con un procesador AMD Ryzen 5 7530U, ha sido probado con Ubuntu 25.10. Esta review muestra cómo se comporta el sistema bajo Linux, incluyendo pruebas de rendimiento, temperatura y consumo de energía. ¿Cómo se instala Ubuntu en este mini PC y qué resultados se obtienen?

## ¿Qué es?

Ubuntu 25.10 es una versión actualizada del sistema operativo Linux, diseñado para funcionar en una variedad de hardware, incluyendo mini PCs como el GEEKOM A5 Pro 2026 Edition. Este sistema operativo ofrece una alternativa a Windows 11, permitiendo a los usuarios aprovechar las características y ventajas de Linux en su dispositivo de cómputo portátil

## ¿Cómo funciona?

Para instalar Ubuntu 25.10 en el GEEKOM A5 Pro 2026 Edition, se requiere reducir el tamaño de la partición de Windows 11 y luego insertar un dispositivo USB con la imagen de instalación de Ubuntu. El proceso de instalación se realiza mediante un asistente de instalación, que guía al usuario a través de las opciones de configuración y particionamiento del disco duro. Una vez instalado, Ubuntu 25.10 se puede ejecutar en modo dual boot con Windows 11, permitiendo al usuario seleccionar entre los dos sistemas operativos al iniciar el dispositivo

## ¿Por qué importa?

La capacidad de ejecutar Ubuntu 25.10 en el GEEKOM A5 Pro 2026 Edition ofrece varias ventajas, incluyendo una mayor flexibilidad y personalización del sistema, así como la posibilidad de aprovechar las características y herramientas de Linux en un dispositivo de cómputo portátil. Además, la compatibilidad con el procesador AMD Ryzen 5 7530U permite al usuario aprovechar el rendimiento y eficiencia energética de este procesador en un entorno Linux

## Consejo técnico

Si deseas instalar Ubuntu 25.10 en tu mini PC, asegúrate de reducir el tamaño de la partición de Windows 11 antes de comenzar el proceso de instalación. También es recomendable verificar la compatibilidad del dispositivo USB con la imagen de instalación de Ubuntu para evitar problemas durante la instalación

```bash
sudo parted /dev/sda resizepart 1 512M && sudo mkfs.vfat /dev/sda1 && sudo mount /dev/sda1 /mnt && sudo usb-creator-kernel-efi /mnt/usb-creator.iso
```

---

**Fuente original:** [https://www.cnx-software.com/2026/03/07/geekom-a5-pro-2026-edition-review-part-3-ubuntu-25-10-on-an-amd-ryzen-5-7530u-mini-pc/](https://www.cnx-software.com/2026/03/07/geekom-a5-pro-2026-edition-review-part-3-ubuntu-25-10-on-an-amd-ryzen-5-7530u-mini-pc/)
