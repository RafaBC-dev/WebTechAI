# Vulnerabilidad en Linux permite leer archivos de root a usuarios no privilegiados

**Fecha:** 2026-05-15
**Categoría:** linux
**Tags:** linux, seguridad, vulnerabilidad
**Título original:** Linux's Latest Vulnerability Allows Reading Root-Owned Files By Unprivileged Users

---

## Introducción

La comunidad de Linux ha detectado una nueva vulnerabilidad que permite a usuarios no privilegiados leer archivos de propiedad de root. Esta vulnerabilidad, llamada ssh-keysign-pwn, ha sido informada por Qualys y ya ha sido corregida en el kernel de Linux.

## ¿Qué es?

La vulnerabilidad ssh-keysign-pwn es un problema de seguridad en el kernel de Linux que permite a usuarios no privilegiados leer archivos de propiedad de root. Esto se debe a una configuración incorrecta en el comportamiento del ptrace, un mecanismo de seguimiento de procesos.

## ¿Cómo funciona?

El ptrace es un mecanismo que permite a un proceso seguir el comportamiento de otro proceso. En el caso de la vulnerabilidad ssh-keysign-pwn, un usuario no privilegiado puede utilizar el ptrace para leer archivos de propiedad de root. Esto se logra mediante la manipulación de la configuración del ptrace en el kernel de Linux.

## ¿Por qué importa?

Esta vulnerabilidad es importante porque puede permitir a un atacante acceder a información confidencial de un sistema Linux. Además, afecta a todas las versiones del kernel de Linux hasta la fecha, lo que significa que cualquier sistema Linux puede estar vulnerable.

## Consejo técnico

Para mitigar esta vulnerabilidad, es importante actualizar el kernel de Linux a la versión más reciente. Además, es recomendable utilizar herramientas de seguridad como Qualys para detectar y corregir vulnerabilidades en el sistema.

```bash
sudo apt-get update && sudo apt-get install linux-image-$(uname -r)
```

---

**Fuente original:** [https://www.phoronix.com/news/Linux-ssh-keysign-pwn](https://www.phoronix.com/news/Linux-ssh-keysign-pwn)
