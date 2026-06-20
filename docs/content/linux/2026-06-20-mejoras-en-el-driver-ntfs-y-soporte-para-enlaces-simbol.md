# Mejoras en el driver NTFS y soporte para enlaces simbólicos en Linux 7.2

**Fecha:** 2026-06-20
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** New NTFS Driver Sees Hardening & Fixes, Windows Native Symlinks With Linux 7.2

---

## Introducción

El driver NTFS de Linux ha recibido importantes mejoras en la versión 7.2, incluyendo soporte para enlaces simbólicos nativos de Windows y una mayor hardening contra metadatos malformados.

## ¿Qué es?

El driver NTFS es un componente del kernel de Linux que permite la lectura y escritura de sistemas de archivos NTFS, utilizados principalmente en sistemas operativos Windows. El soporte para enlaces simbólicos nativos de Windows permite que los enlaces simbólicos creados en Windows sean reconocidos y seguidos en Linux.

## ¿Cómo funciona?

El driver NTFS utiliza la API de Linux para interactuar con el sistema de archivos NTFS. El soporte para enlaces simbólicos nativos de Windows se implementa mediante la validación y resolución de enlaces simbólicos en el momento de la montaje del sistema de archivos. La hardening contra metadatos malformados se logra mediante la validación de atributos, listas de atributos, raíces de índices y otros componentes del sistema de archivos.

## ¿Por qué importa?

Estas mejoras en el driver NTFS son importantes porque permiten una mayor compatibilidad y seguridad en la lectura y escritura de sistemas de archivos NTFS en Linux. Además, el soporte para enlaces simbólicos nativos de Windows facilita la integración de Linux con sistemas operativos Windows.

## Consejo técnico

Si deseas aprovechar las mejoras del driver NTFS en Linux 7.2, asegúrate de actualizar tu kernel a la versión 7.2 y de utilizar las opciones de montaje adecuadas para habilitar el soporte para enlaces simbólicos nativos de Windows.

```bash
mount -o ntfs-3g,uid=1000,gid=1000,umask=022 /dev/sda1 /mnt
```

---

**Fuente original:** [https://www.phoronix.com/news/Linux-7.2-NTFS-Improvements](https://www.phoronix.com/news/Linux-7.2-NTFS-Improvements)
