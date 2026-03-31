# Nueva versión de SystemRescue para reparar sistemas en crisis

**Fecha:** 2026-03-31
**Categoría:** linux
**Tags:** linux, herramientas, rescate-de-sistemas
**Título original:** SystemRescue 13.00 released

---

## Introducción

La versión 13.00 de SystemRescue ha sido lanzada, ofreciendo una herramienta de rescate de sistemas en vivo basada en Arch Linux para reparar sistemas en crisis. Esta herramienta es esencial para cualquier administrador de sistemas que necesite recuperar datos, crear copias de seguridad de discos o restablecer contraseñas perdidas.

## ¿Qué es?

SystemRescue es una distribución de Linux que se ejecuta desde un disco en vivo y ofrece una herramienta de rescate de sistemas para reparar problemas de hardware o software. Basada en Arch Linux, SystemRescue incluye herramientas para reparar sistemas, recuperar datos y crear copias de seguridad de discos.

## ¿Cómo funciona?

SystemRescue utiliza el kernel 6.18.20 LTS y actualiza las herramientas y módulos de bcachefs a la versión 1.37.3. La distribución incluye una variedad de herramientas para realizar tareas de rescate de sistemas, como la recuperación de archivos, la creación de copias de seguridad de discos y el restablecimiento de contraseñas perdidas.

## ¿Por qué importa?

SystemRescue es fundamental para cualquier administrador de sistemas que necesite reparar un sistema en crisis. Con esta herramienta, es posible recuperar datos importantes, crear copias de seguridad de discos y restablecer contraseñas perdidas, lo que puede evitar pérdidas de tiempo y dinero.

## Consejo técnico

Si estás utilizando SystemRescue, asegúrate de actualizar las herramientas y módulos de bcachefs a la versión 1.37.3 para aprovechar las últimas mejoras y correcciones.

```bash
sudo pacman -S bcachefs-tools bcachefs-kernel-module
```

---

**Fuente original:** [https://lwn.net/Articles/1065480/](https://lwn.net/Articles/1065480/)
