# Gentoo: la distribución Linux que construye software desde fuentes

**Fecha:** 2026-05-29
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Górny: why Gentoo?

---

## Introducción

El desarrollador de Gentoo, Michał Górny, ha escrito un artículo detallado sobre la filosofía y propósito de esta distribución Linux. Gentoo es conocida por ser una distribución source-first, lo que significa que se instalan aplicaciones desde fuentes, en lugar de utilizar paquetes binarios.

## ¿Qué es?

Gentoo es una distribución Linux que se enfoca en la construcción de software desde fuentes. Esto significa que los usuarios pueden instalar aplicaciones desde código fuente, lo que les da un mayor control sobre la configuración y personalización de su sistema. Gentoo también tiene un enfoque en la comunidad y la colaboración, con un objetivo de crear un entorno amigable y acogedor para los usuarios.

## ¿Cómo funciona?

La herramienta de gestión de paquetes de Gentoo, llamada Portage, es responsable de construir y instalar aplicaciones desde fuentes. Portage utiliza un sistema de dependencias para asegurarse de que todas las dependencias necesarias sean instaladas antes de instalar una aplicación. Esto hace que la instalación de aplicaciones sea relativamente fácil y automática.

## ¿Por qué importa?

Gentoo es importante porque ofrece a los usuarios un mayor control sobre su sistema y les permite personalizarlo según sus necesidades. También es una excelente opción para aquellos que desean aprender sobre la construcción de software desde fuentes y la gestión de paquetes.

## Consejo técnico

Si deseas probar Gentoo, puedes comenzar por instalar la herramienta Portage y configurarla para que construya aplicaciones desde fuentes. Puedes hacer esto ejecutando el comando `emerge --sync` para sincronizar los repositorios y luego `emerge <aplicación>` para instalar una aplicación específica.

```bash
emerge --sync
```

---

**Fuente original:** [https://lwn.net/Articles/1075148/](https://lwn.net/Articles/1075148/)
