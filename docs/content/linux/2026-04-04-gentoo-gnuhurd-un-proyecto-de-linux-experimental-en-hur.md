# Gentoo GNU/Hurd: un proyecto de Linux experimental en Hurd

**Fecha:** 2026-04-04
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** No kidding: Gentoo GNU/Hurd

---

## Introducción

La comunidad Gentoo Linux ha anunciado el lanzamiento de un nuevo proyecto: Gentoo GNU/Hurd, un sistema operativo experimental basado en GNU Hurd. Aunque se trata de una versión en etapa de desarrollo, los desarrolladores han logrado crear un disco de imagen que puede ser probado con QEMU.

## ¿Qué es?

Gentoo GNU/Hurd es un sistema operativo experimental que combina el núcleo GNU Hurd con la distribución Linux Gentoo. GNU Hurd es un núcleo que se enfoca en la seguridad y la escalabilidad, mientras que Gentoo es conocida por su flexibilidad y personalización. El objetivo de este proyecto es crear un sistema operativo que ofrezca la mejor de ambas mundos.

## ¿Cómo funciona?

Para crear Gentoo GNU/Hurd, los desarrolladores han utilizado scripts para construir un disco de imagen que puede ser probado con QEMU. Esto permite a los usuarios experimentar con el sistema operativo sin necesidad de instalarlo en hardware físico. El proceso de construcción del disco de imagen se puede realizar localmente utilizando herramientas como QEMU.

## ¿Por qué importa?

Gentoo GNU/Hurd es importante porque ofrece una alternativa experimental a los sistemas operativos tradicionales. Puede ser de interés para desarrolladores y entusiastas de la tecnología que buscan explorar nuevas opciones y características. Además, el proyecto puede servir como una plataforma para probar y desarrollar nuevas tecnologías y herramientas.

## Consejo técnico

Si deseas probar Gentoo GNU/Hurd, puedes descargar el disco de imagen pre-preparado y ejecutarlo con QEMU utilizando el comando `qemu-system-x86_64 -m 2048 -drive if=none,file=<nombre_del_disco>.img,format=raw`.

```bash
qemu-system-x86_64 -m 2048 -drive if=none,file=<nombre_del_disco>.img,format=raw
```

---

**Fuente original:** [https://lwn.net/Articles/1066241/](https://lwn.net/Articles/1066241/)
