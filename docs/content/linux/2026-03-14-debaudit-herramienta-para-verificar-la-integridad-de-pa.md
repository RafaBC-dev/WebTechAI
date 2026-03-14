# Debaudit: herramienta para verificar la integridad de paquetes Debian

**Fecha:** 2026-03-14
**Categoría:** linux
**Tags:** herramientas, seguridad, debian
**Título original:** debauit Announced As Debian Source Package Auditor

---

## Introducción

La seguridad del software es cada vez más importante, y Debian ha anunciado una herramienta para ayudar a proteger la cadena de suministro de software. Debaudit es un conjunto de herramientas diseñadas para verificar la integridad y reproducibilidad de paquetes Debian.

## ¿Qué es?

Debaudit es un conjunto de herramientas y servicios que verifican la integridad y reproducibilidad de paquetes Debian. Está compuesto por tres herramientas: upstream2orig, git2dsc y git2orig. Estas herramientas verifican que el paquete en Debian sea una representación fiel del código original del upstream y que el paquete en el repositorio Git sea consistente con el paquete en el archivo de Debian.

## ¿Cómo funciona?

Debaudit funciona comprobando la integridad de los paquetes Debian mediante la verificación de la consistencia entre el código original del upstream y el paquete en el repositorio Git. Las herramientas upstream2orig, git2dsc y git2orig se encargan de verificar que el paquete en Debian sea una representación fiel del código original del upstream y que el paquete en el repositorio Git sea consistente con el paquete en el archivo de Debian.

## ¿Por qué importa?

Debaudit es importante porque ayuda a garantizar la seguridad del software y la integridad de la cadena de suministro de software. Al verificar la consistencia entre el código original del upstream y el paquete en el repositorio Git, Debaudit ayuda a detectar cualquier alteración maliciosa que pueda haber ocurrido durante el proceso de empaquetado.

## Consejo técnico

Si deseas utilizar Debaudit, puedes empezar por instalar las herramientas upstream2orig, git2dsc y git2orig en tu sistema Debian. Luego, puedes utilizar estas herramientas para verificar la integridad de los paquetes Debian y garantizar la seguridad del software.

```bash
apt-get install upstream2orig git2dsc git2orig
```

---

**Fuente original:** [https://www.phoronix.com/news/Debian-debaudit](https://www.phoronix.com/news/Debian-debaudit)
