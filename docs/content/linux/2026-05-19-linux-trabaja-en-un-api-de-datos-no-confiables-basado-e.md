# Linux trabaja en un API de datos no confiables basado en Rust

**Fecha:** 2026-05-19
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** The Linux Kernel Working On A Rust-Based Untrusted Data API

---

## Introducción

El kernel de Linux está mejorando su seguridad con un nuevo API que marca los datos no confiables recibidos desde el espacio de usuario. Esto ayudará a prevenir problemas de seguridad y bugs.

## ¿Qué es?

El API de datos no confiables es un nuevo conjunto de funciones y tipos de datos que permiten marcar los datos recibidos desde el espacio de usuario como no confiables. Esto permite a los desarrolladores validar y sanitizar estos datos antes de utilizarlos en el kernel.

## ¿Cómo funciona?

El API de datos no confiables utiliza un nuevo tipo de datos llamado `UntrustedData` que marca los datos como no confiables. También se ha agregado un nuevo trait llamado `validate` que permite validar estos datos. El inicializador de este API es el código de I/O vector (IOV).

## ¿Por qué importa?

Este API importa porque ayuda a mejorar la seguridad del kernel de Linux al permitir que los desarrolladores marquen y validen los datos no confiables recibidos desde el espacio de usuario. Esto reduce el riesgo de problemas de seguridad y bugs.

## Consejo técnico

Si estás trabajando con código de I/O vector (IOV), considera utilizar el nuevo API de datos no confiables para marcar y validar tus datos. Puedes empezar por revisar el código de `validate` y `UntrustedData` para entender cómo funciona.

```bash
git clone https://git.kernel.org/pub/scm/linux/kernel/git/gregkh/driver-core.git -b untrusted
```

---

**Fuente original:** [https://www.phoronix.com/news/Linux-Kernel-Untrusted-Data-API](https://www.phoronix.com/news/Linux-Kernel-Untrusted-Data-API)
