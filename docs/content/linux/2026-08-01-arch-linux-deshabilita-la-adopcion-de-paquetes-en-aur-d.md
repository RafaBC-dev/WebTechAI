# Arch Linux deshabilita la adopción de paquetes en AUR debido a malware

**Fecha:** 2026-08-01
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Arch Linux disables AUR package adoption

---

## Introducción

El equipo de DevOps de Arch Linux ha anunciado que la adopción de paquetes abandonados en el Arch User Repository (AUR) ha sido deshabilitada debido a un ataque de malware. El ataque ha sido detectado y analizado por el equipo de seguridad de Arch Linux.

## ¿Qué es?

Arch Linux es una distribución de Linux conocida por su flexibilidad y personalización. El Arch User Repository (AUR) es un repositorio de paquetes que permite a los usuarios crear y compartir paquetes personalizados. Sin embargo, el AUR también es vulnerable a ataques de malware.

## ¿Cómo funciona?

El AUR funciona como un repositorio de paquetes que se pueden instalar en Arch Linux. Los usuarios pueden crear y compartir paquetes personalizados, pero también pueden ser vulnerables a ataques de malware. El equipo de DevOps de Arch Linux ha implementado medidas de seguridad para prevenir estos ataques, pero el ataque reciente ha demostrado que estas medidas no son suficientes.

## ¿Por qué importa?

El ataque de malware en el AUR es importante porque puede comprometer la seguridad de los sistemas de los usuarios. El malware puede instalar programas maliciosos, robar datos personales y causar daños a los sistemas. Es importante que los usuarios de Arch Linux tomen medidas de seguridad para proteger sus sistemas.

## Consejo técnico

Los usuarios de Arch Linux deben verificar la autenticidad de los paquetes que se instalan en su sistema. Pueden hacer esto verificando la firma digital de los paquetes y asegurándose de que se han instalado desde fuentes confiables.

```bash
pacman -S --noconfirm --needed <paquete>
```

---

**Fuente original:** [https://lwn.net/Articles/1086489/](https://lwn.net/Articles/1086489/)
