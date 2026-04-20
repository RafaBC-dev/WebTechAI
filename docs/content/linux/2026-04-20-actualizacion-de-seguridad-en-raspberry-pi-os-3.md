# Actualización de seguridad en Raspberry Pi OS

**Fecha:** 2026-04-20
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** A security update for Raspberry Pi OS

---

## Introducción

La versión 6.2 de Raspberry Pi OS ha sido lanzada con una actualización de seguridad importante. A partir de ahora, las cuentas de usuario regulares ya no tendrán acceso sin contraseña a la ejecución de comandos administrativos.

## ¿Qué es?

Raspberry Pi OS es la distribución de Linux oficial para los dispositivos Raspberry Pi. Esta versión 6.2 es una actualización que incluye cambios y correcciones de errores realizados en los últimos meses.

## ¿Cómo funciona?

En Linux, existen dos tipos de cuentas de usuario: regulares y administradores. Los administradores tienen acceso a partes del sistema que los usuarios regulares no pueden modificar. Para realizar acciones administrativas sin tener que cambiar de cuenta, se utiliza el comando `sudo`, que permite ejecutar comandos como si fueran administradores. A partir de ahora, para utilizar `sudo`, se necesitará ingresar la contraseña del usuario.

## ¿Por qué importa?

Esta actualización es importante porque previene la posibilidad de que un atacante pueda acceder a la cuenta de un usuario y realizar acciones administrativas sin ser detectado. Esto se logra mediante la desactivación de la ejecución de `sudo` sin contraseña.

## Consejo técnico

Si actualizaste a la versión 6.2 de Raspberry Pi OS, asegúrate de verificar que tu cuenta de usuario tenga una contraseña fuerte y única para evitar que un atacante pueda acceder a tu cuenta.

```bash
sudo
```

---

**Fuente original:** [https://www.raspberrypi.com/news/a-security-update-for-raspberry-pi-os/](https://www.raspberrypi.com/news/a-security-update-for-raspberry-pi-os/)
