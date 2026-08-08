# Un filesystem diseñado para fallar: FailFS

**Fecha:** 2026-08-08
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** This Filesystem is Born to Fail

---

## Introducción

El nuevo filesystem FailFS, que se espera incluir en Linux 7.3, tiene un objetivo sorprendente: fallar en todas las operaciones. Pero ¿por qué y cómo funciona?

## ¿Qué es?

FailFS es un filesystem pseudo que devuelve EOPNOTSUPP en todas las operaciones, lo que significa que no admite ninguna acción. Su objetivo es proporcionar una base mínima para aplicaciones que necesitan acceder a archivos y directorios específicos.

## ¿Cómo funciona?

Cuando un proceso utiliza FailFS como directorio raíz o actual, la búsqueda de directorios y archivos se vuelve inútil. Los procesos deben utilizar explicitamente file descriptors para acceder a archivos y directorios específicos. Esto significa que un sandbox manager puede abrir un directorio y pasar el descriptor al proceso, que puede acceder a los archivos y directorios debajo de él.

## ¿Por qué importa?

FailFS ofrece una forma más segura de crear sandboxs, ya que los procesos no pueden acceder a archivos y directorios que no les han sido explícitamente proporcionados. Esto puede ser especialmente útil en entornos de seguridad críticos, como sistemas de confianza.

## Consejo técnico

Si deseas aprovechar las características de FailFS en tu proyecto, considera utilizar el comando `openat()` para acceder a archivos y directorios específicos. Esto te permitirá crear sandboxs más seguros y controlados.

```bash
openat()
```

---

**Fuente original:** [https://hackaday.com/2026/08/07/this-filesystem-is-born-to-fail/](https://hackaday.com/2026/08/07/this-filesystem-is-born-to-fail/)
