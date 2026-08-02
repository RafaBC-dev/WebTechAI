# Arch Linux deshabilita la adopción de paquetes en AUR debido a malware

**Fecha:** 2026-08-02
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Arch Linux disables AUR package adoption

---

## Introducción

La comunidad de Arch Linux ha sido golpeada por una serie de ataques maliciosos que han llevado a la deshabilitación de la adopción de paquetes en el Arch User Repository (AUR). Los atacantes han estado utilizando el AUR para difundir malware en sistemas de usuarios.

## ¿Qué es?

El Arch User Repository (AUR) es un repositorio de paquetes de software creado por la comunidad de Arch Linux. Es un lugar donde los usuarios pueden compartir y mantener paquetes de software que no están disponibles en el repositorio oficial de Arch Linux.

## ¿Cómo funciona?

La adopción de paquetes en AUR permite a los usuarios adoptar paquetes abandonados y mantenerlos actualizados. Sin embargo, en este caso, los atacantes han estado utilizando esta función para difundir malware en sistemas de usuarios. La adopción de paquetes ha sido deshabilitada para evitar que más usuarios sean afectados.

## ¿Por qué importa?

La deshabilitación de la adopción de paquetes en AUR es importante porque puede afectar a los usuarios que dependen de esta función para mantener sus paquetes de software actualizados. También es un recordatorio de la importancia de la seguridad en la comunidad de Arch Linux.

## Consejo técnico

Si eres un usuario de Arch Linux, es recomendable que revises tus paquetes de software y actualices cualquier paquete que esté afectado por el malware. Puedes utilizar el comando `pacman -S --refresh` para actualizar tus paquetes y `pacman -S --sync` para sincronizar tus paquetes con el repositorio oficial.

```bash
pacman -S --refresh && pacman -S --sync
```

---

**Fuente original:** [https://lwn.net/Articles/1086489/](https://lwn.net/Articles/1086489/)
