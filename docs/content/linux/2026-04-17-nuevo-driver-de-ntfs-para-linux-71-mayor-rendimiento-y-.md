# Nuevo driver de NTFS para Linux 7.1: mayor rendimiento y estabilidad

**Fecha:** 2026-04-17
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** New NTFS File-System Driver Submitted For Linux 7.1

---

## Introducción

El proyecto NTFSPLUS ha sido reemplazado por un nuevo driver de NTFS para Linux 7.1, que ofrece mayor rendimiento y estabilidad que el actual driver NTFS3. Este nuevo driver ha sido desarrollado por Namjae Jeon y está disponible para su revisión en Linux-Next.

## ¿Qué es?

El nuevo driver de NTFS es un proyecto de código abierto que busca mejorar la experiencia de usuario de Linux al interactuar con sistemas de archivos NTFS. Se basa en el código original del driver de NTFS y ha sido actualizado para aprovechar las últimas tecnologías del kernel de Linux, como IOmap y folio integration.

## ¿Cómo funciona?

El nuevo driver de NTFS se ha construido a partir del código original del driver de NTFS, pero ha sido actualizado para incluir nuevas características y mejoras en rendimiento. Esto se ha logrado gracias a la integración de tecnologías modernas del kernel de Linux, como IOmap y folio integration, que permiten una mejor gestión de la memoria y la IO.

## ¿Por qué importa?

El nuevo driver de NTFS importa porque ofrece una mejor experiencia de usuario de Linux al interactuar con sistemas de archivos NTFS. Esto se debe a que el nuevo driver es más estable y ofrece un mejor rendimiento que el actual driver NTFS3, lo que significa que los usuarios pueden esperar una mejor experiencia al trabajar con archivos y directorios en sistemas de archivos NTFS.

## Consejo técnico

Si deseas probar el nuevo driver de NTFS, puedes revisar el pull request en Linux-Next y seguir las instrucciones para compilar y instalar el nuevo driver.

```bash
git clone https://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git && git checkout -b ntfsplus && git pull origin ntfsplus
```

---

**Fuente original:** [https://www.phoronix.com/news/New-NTFS-Driver-Submitted-Linux](https://www.phoronix.com/news/New-NTFS-Driver-Submitted-Linux)
