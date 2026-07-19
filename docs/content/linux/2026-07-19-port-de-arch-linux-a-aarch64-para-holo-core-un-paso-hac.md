# Port de Arch Linux a aarch64 para Holo Core: un paso hacia la compatibilidad

**Fecha:** 2026-07-19
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Building an Arch Linux aarch64 port for Holo Core (Collabora blog)

---

## Introducción

Collabora, en colaboración con Valve, ha publicado un post sobre su trabajo en el port de Arch Linux a aarch64 para Holo Core, un sistema de juego basado en Arm. Este proyecto busca hacer que Arch Linux sea compatible con la arquitectura aarch64, lo que permitirá ejecutar el sistema operativo en dispositivos con procesadores Arm.

## ¿Qué es?

Holo Core es un sistema de juego desarrollado por Valve que utiliza la arquitectura aarch64. El port de Arch Linux a aarch64 es un proyecto que busca hacer que el sistema operativo sea compatible con esta arquitectura, lo que permitirá ejecutar el sistema en dispositivos con procesadores Arm. El objetivo es crear un sistema que pueda ejecutar aplicaciones de Steam en dispositivos con procesadores Arm.

## ¿Cómo funciona?

El port de Arch Linux a aarch64 se ha realizado utilizando la infraestructura desarrollada por Collabora. El proceso consiste en crear un sistema que pueda construir el sistema operativo desde cero y mantenerse actualizado con los cambios en el código fuente de Arch Linux. El sistema utiliza la herramienta de construcción de Arch Linux para crear paquetes binarios y una imagen de contenedor para dispositivos aarch64.

## ¿Por qué importa?

Este proyecto es importante porque permitirá a los desarrolladores de aplicaciones de Steam ejecutar sus aplicaciones en dispositivos con procesadores Arm. También permitirá a los usuarios de dispositivos con procesadores Arm disfrutar de una experiencia de juego más completa y compatible con la arquitectura aarch64.

## Consejo técnico

Si deseas crear un contenedor de aarch64 en un host x86_64, puedes utilizar la herramienta de construcción de Arch Linux llamada `makechrootpkg` y seguir las instrucciones proporcionadas en el post de Collabora.

```bash
makechrootpkg
```

---

**Fuente original:** [https://lwn.net/Articles/1083392/](https://lwn.net/Articles/1083392/)
