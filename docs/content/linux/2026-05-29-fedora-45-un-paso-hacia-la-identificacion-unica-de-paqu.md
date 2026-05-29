# Fedora 45: un paso hacia la identificación única de paquetes de software

**Fecha:** 2026-05-29
**Categoría:** linux
**Tags:** ia-local, linux, codigo
**Título original:** Fedora 45 Considering Use Of PURL Metadata For Uniquely Identifying Software Packages

---

## Introducción

Fedora 45 está considerando la adopción de PURL (Package-URL) para identificar de manera única los paquetes de software. Esto permitiría una mapeo más sencillo entre proyectos de código fuente y paquetes de Fedora, lo que facilitaría la identificación de vulnerabilidades de seguridad.

## ¿Qué es?

PURL es una especificación que proporciona una URL estándar para identificar paquetes de software de manera universal. Permite especificar una versión particular del paquete y puede ser utilizado en diferentes sistemas de gestión de paquetes, como npm, Nuget, Gem, Docker Hub, PyPi, entre otros.

## ¿Cómo funciona?

PURL utiliza un formato de URL estándar para identificar paquetes de software. Por ejemplo, un paquete de npm podría ser identificado con la URL `npm:package-name@version`. Esto permite a los desarrolladores y a los sistemas de gestión de paquetes acceder a la información del paquete de manera sencilla y consistente.

## ¿Por qué importa?

La adopción de PURL en Fedora 45 permitiría una identificación más precisa y sencilla de los paquetes de software, lo que facilitaría la detección de vulnerabilidades de seguridad y la generación de SBOMs (Software Bill of Materials) para imágenes de contenedores.

## Consejo técnico

Si deseas utilizar PURL en tu proyecto, puedes comenzar investigando la especificación en GitHub y explorando herramientas como `pkgurl` para generar URLs PURL en tu código.

```bash
pkgurl
```

---

**Fuente original:** [https://www.phoronix.com/news/Fedora-45-Considering-PURL](https://www.phoronix.com/news/Fedora-45-Considering-PURL)
