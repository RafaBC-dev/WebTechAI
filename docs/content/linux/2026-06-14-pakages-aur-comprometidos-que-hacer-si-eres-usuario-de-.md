# Pakages AUR comprometidos: ¿qué hacer si eres usuario de Arch Linux?

**Fecha:** 2026-06-14
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Hundreds of AUR packages compromised

---

## Introducción

La comunidad de Arch Linux ha detectado un ataque a la base de datos de paquetes AUR, lo que ha permitido a un atacante introducir un paquete malicioso. Es posible que usuarios de Arch Linux hayan instalado actualizaciones comprometidas.

## ¿Qué es?

El Arch User Repository (AUR) es una base de datos de paquetes de software para la distribución de sistema operativo Arch Linux. Es un repositorio de paquetes de código abierto donde los usuarios pueden compartir y colaborar en la creación de paquetes de software.

## ¿Cómo funciona?

Los paquetes AUR se crean y se mantienen por la comunidad de usuarios de Arch Linux. Los paquetes se comparten en un repositorio público y se pueden instalar mediante el gestor de paquetes Pacman. Sin embargo, en este caso, un atacante ha introducido un paquete malicioso en el repositorio.

## ¿Por qué importa?

El ataque a la base de datos de paquetes AUR puede haber permitido a un atacante acceder a información sensible de los usuarios de Arch Linux. Los usuarios que hayan instalado actualizaciones comprometidas deben tomar medidas para proteger sus sistemas.

## Consejo técnico

Los usuarios de Arch Linux deben verificar si han instalado paquetes comprometidos y eliminarlos si es necesario. Pueden hacer esto consultando la lista de paquetes comprometidos y verificando si han instalado alguno de ellos.

```bash
pacman -Qi <nombre del paquete> (para verificar la versión instalada de un paquete) y pacman -R <nombre del paquete> (para eliminar un paquete)
```

---

**Fuente original:** [https://lwn.net/Articles/1077718/](https://lwn.net/Articles/1077718/)
