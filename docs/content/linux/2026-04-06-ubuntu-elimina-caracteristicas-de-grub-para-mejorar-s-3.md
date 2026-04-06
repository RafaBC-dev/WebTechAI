# Ubuntu elimina características de GRUB para mejorar seguridad

**Fecha:** 2026-04-06
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** [$] Ubuntu's GRUBby plans

---

## Introducción

Ubuntu ha anunciado planes para eliminar algunas características de GRUB, el bootloader más utilizado en sistemas Linux x86_64, para mejorar su perfil de seguridad. Esto se debe a la aparición de vulnerabilidades en el pasado.

## ¿Qué es?

GRUB (GNU GRUB 2) es el bootloader más utilizado en sistemas Linux x86_64. Soporta la lectura de archivos de sistemas de archivos variados, maneja el arranque de sistemas modernos con UEFI o legacy con BIOS, y permite a los usuarios personalizar la imagen de arranque.

## ¿Cómo funciona?

GRUB se ejecuta antes de que el sistema operativo se inicie, cargando el kernel y la configuración del sistema. Las características a eliminar incluyen la capacidad de leer archivos de sistemas de archivos no compatibles y la personalización de la imagen de arranque.

## ¿Por qué importa?

La eliminación de estas características puede mejorar la seguridad de GRUB, reduciendo la superficie de ataque para los vulnerabilidades. Sin embargo, esto también puede limitar la compatibilidad con ciertos sistemas de archivos y la personalización de la imagen de arranque.

## Consejo técnico

Si estás utilizando GRUB en tu sistema Ubuntu, es recomendable actualizar a la versión más reciente para asegurarte de que estás protegido contra las vulnerabilidades conocidas. Puedes hacer esto ejecutando el comando `sudo apt update && sudo apt full-upgrade`.

```bash
sudo apt update && sudo apt full-upgrade
```

---

**Fuente original:** [https://lwn.net/Articles/1065420/](https://lwn.net/Articles/1065420/)
