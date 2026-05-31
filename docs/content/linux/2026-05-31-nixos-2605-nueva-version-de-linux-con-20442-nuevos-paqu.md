# NixOS 26.05: Nueva versión de Linux con 20.442 nuevos paquetes

**Fecha:** 2026-05-31
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** NixOS 26.05 Released With 20,442 New Packages, Stage 1 Now Based On systemd By Default

---

## Introducción

La distribución de Linux NixOS ha lanzado su versión 26.05, que incluye 20.442 nuevos paquetes y actualiza 20.641 existentes. Esta versión también cambia su implementación de inicialización por defecto a systemd.

## ¿Qué es?

NixOS es una distribución de Linux basada en el gestor de paquetes Nix, que permite a los usuarios crear entornos de desarrollo y producción aislados y reproducibles. Utiliza un sistema de paquetes llamado Nixpkgs, que incluye una gran cantidad de paquetes y herramientas.

## ¿Cómo funciona?

NixOS utiliza un sistema de inicialización llamado Stage 1, que se encarga de preparar el sistema para que se inicie correctamente. En la versión 26.05, se cambia esta implementación por defecto a systemd, que es un gestor de inicialización popular y robusto. Esto permite a los usuarios aprovechar las características de systemd, como la gestión de servicios y la inicialización de red.

## ¿Por qué importa?

Esta versión de NixOS es importante porque incluye una gran cantidad de actualizaciones de paquetes, incluyendo la versión 50 de GNOME y la versión 15 del compilador GCC. Además, la implementación de systemd por defecto ofrece una mayor estabilidad y flexibilidad al sistema.

## Consejo técnico

Si estás interesado en probar NixOS, puedes descargar la versión 26.05 desde el sitio web oficial de NixOS y seguir las instrucciones de instalación para crear un entorno de desarrollo aislado y reproducible.

```bash
nixos-rebuild switch
```

---

**Fuente original:** [https://www.phoronix.com/news/NixOS-26.05-Released](https://www.phoronix.com/news/NixOS-26.05-Released)
