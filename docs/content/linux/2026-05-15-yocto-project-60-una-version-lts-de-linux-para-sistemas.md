# Yocto Project 6.0: una versión LTS de Linux para sistemas embebidos

**Fecha:** 2026-05-15
**Categoría:** linux
**Tags:** linux, embebidos, codigo
**Título original:** Yocto Project 6.0 “Wrynose” released with Linux 6.18 LTS

---

## Introducción

La comunidad de Yocto Project ha lanzado la versión 6.0 de su framework, que incluye Linux 6.18 LTS y una serie de mejoras importantes. Esta versión es especialmente relevante debido a su soporte largo plazo de 4 años y su mejora en la seguridad y la conformidad con la normativa europea.

## ¿Qué es?

El Yocto Project es un framework para crear distribuciones de Linux personalizadas para sistemas embebidos. Permite a los desarrolladores crear sistemas operativos adaptados a las necesidades específicas de sus dispositivos. La versión 6.0 es una versión LTS (Long Term Support), lo que significa que será soportada durante al menos 4 años.

## ¿Cómo funciona?

La versión 6.0 de Yocto Project incluye actualizaciones del kernel Linux 6.18 LTS, herramientas de compilación como GCC 15.2 y LLVM 22.1, y mejoras en la seguridad y la gestión de dependencias. También se ha agregado soporte para la generación de SBOM (Software Bill of Materials) y la integración de herramientas de seguridad como OpenSSL.

## ¿Por qué importa?

Esta versión es importante porque proporciona una plataforma estable y segura para desarrollar sistemas embebidos. La mejora en la seguridad y la conformidad con la normativa europea es especialmente relevante en un momento en que la seguridad de los sistemas informáticos es un tema cada vez más importante. Además, la versión 6.0 incluye mejoras en la gestión de dependencias y la generación de SBOM, lo que facilita la creación de sistemas operativos personalizados.

## Consejo técnico

Si estás trabajando con Yocto Project, te recomendamos utilizar la herramienta `bitbake-setup` para configurar tus directorios de construcción y mejorar la reutilización de configuraciones de construcción. También es importante actualizar tu versión de OpenSSL para deshabilitar el soporte para TLS 1.0 y 1.1 por defecto.

```bash
bitbake-setup
```

---

**Fuente original:** [https://www.cnx-software.com/2026/05/14/yocto-project-6-0-wrynose-released-with-linux-6-18-lts/](https://www.cnx-software.com/2026/05/14/yocto-project-6-0-wrynose-released-with-linux-6-18-lts/)
