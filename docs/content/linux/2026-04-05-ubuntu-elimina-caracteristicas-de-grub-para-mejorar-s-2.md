# Ubuntu elimina características de GRUB para mejorar seguridad

**Fecha:** 2026-04-05
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** [$] Ubuntu's GRUBby plans

---

## Introducción

Ubuntu, una de las distribuciones de Linux más populares, está a punto de eliminar algunas características de su gestor de arranque GRUB para mejorar su seguridad. Aunque GRUB es el gestor de arranque más utilizado en sistemas x86_64 Linux, ha tenido una serie de vulnerabilidades en el pasado.

## ¿Qué es?

GRUB (GNU GRUB 2) es el gestor de arranque más utilizado en sistemas x86_64 Linux. Ofrece una amplia variedad de características, como la capacidad de leer desde diferentes sistemas de archivos, manejar sistemas con UEFI o BIOS, y permitir a los usuarios personalizar la imagen de inicio. Sin embargo, estas características vienen con un precio: una serie de vulnerabilidades en el pasado.

## ¿Cómo funciona?

GRUB se ejecuta en el momento del arranque del sistema y permite a los usuarios elegir qué sistema de archivos montar y qué programa ejecutar. Puede leer desde diferentes sistemas de archivos, incluyendo ext2, ext3, ext4, FAT, y NTFS. También puede manejar sistemas con UEFI o BIOS, lo que lo hace compatible con una amplia variedad de hardware.

## ¿Por qué importa?

La eliminación de características de GRUB es importante porque puede mejorar la seguridad del sistema. Al reducir el número de características, se reduce el riesgo de vulnerabilidades. Además, la eliminación de características puede ayudar a simplificar el código y mejorar la estabilidad del sistema.

## Consejo técnico

Si estás utilizando GRUB en tu sistema Ubuntu, puedes verificar qué características están habilitadas y deshabilitar aquellas que no necesitas. Puedes hacer esto ejecutando el comando `sudo grub-mkconfig -o /boot/grub/grub.cfg` y luego editando el archivo `/boot/grub/grub.cfg` para deshabilitar las características no necesarias.

```bash
sudo grub-mkconfig -o /boot/grub/grub.cfg
```

---

**Fuente original:** [https://lwn.net/Articles/1065420/](https://lwn.net/Articles/1065420/)
