# Gentoo Linux llega al Hurd: un nuevo destino para la distribución

**Fecha:** 2026-04-05
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** No kidding: Gentoo GNU/Hurd

---

## Introducción

La comunidad de Gentoo Linux ha logrado un hito importante al portar su distribución al kernel GNU Hurd. Aunque se trata de un proyecto experimental, esto abre nuevas posibilidades para los usuarios y desarrolladores que buscan explorar nuevas tecnologías.

## ¿Qué es?

Gentoo GNU/Hurd es una versión de la distribución Linux Gentoo que utiliza el kernel GNU Hurd en lugar del tradicional Linux. El Hurd es un proyecto de kernel que busca ofrecer una alternativa a Linux y proporcionar una mayor seguridad y estabilidad.

## ¿Cómo funciona?

Para utilizar Gentoo GNU/Hurd, se puede descargar una imagen de disco preparada y ejecutarla en una máquina virtual utilizando QEMU. Los desarrolladores de Gentoo han proporcionado scripts para construir la imagen localmente y facilitar el trabajo en el proyecto.

## ¿Por qué importa?

Este proyecto es importante porque ofrece una oportunidad para explorar nuevas tecnologías y mejorar la seguridad y estabilidad de los sistemas operativos. Además, puede ser una alternativa interesante para aquellos que buscan evitar el kernel Linux.

## Consejo técnico

Si deseas probar Gentoo GNU/Hurd, puedes descargar la imagen de disco preparada y ejecutarla en QEMU. Recuerda que se trata de un proyecto experimental, así que prepárate para encontrar algunos problemas y romper algunas cosas.

```bash
qemu-system-x86_64 -m 2048 -vnc :0 -hda gentoo-hurd.img
```

---

**Fuente original:** [https://lwn.net/Articles/1066241/](https://lwn.net/Articles/1066241/)
