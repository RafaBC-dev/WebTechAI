# Bcachefs 1.37: un sistema de archivos avanzado para Linux

**Fecha:** 2026-03-16
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Bcachefs 1.37 Released With Linux 7.0 Support, Erasure Coding Stable & New Sub-Commands

---

## Introducción

El proyecto Bcachefs ha lanzado una nueva versión, 1.37, que incluye soporte para Linux 7.0, codificación de erasures estables y nuevas opciones de comando. Esta actualización es importante para los usuarios de Linux que buscan un sistema de archivos más seguro y eficiente.

## ¿Qué es?

Bcachefs es un sistema de archivos de próxima generación, basado en Linux, que ofrece una copia en escritura (copy-on-write) y una codificación de erasures para garantizar la integridad de los datos. Se trata de un proyecto de código abierto que busca mejorar la seguridad y la eficiencia de los sistemas de archivos en Linux.

## ¿Cómo funciona?

Bcachefs utiliza una codificación de erasures para garantizar la integridad de los datos. Esto significa que si se produce un error en la escritura de datos, el sistema puede detectarlo y corregirlo automáticamente. Además, Bcachefs ofrece una opción de rewind para restaurar el sistema a un estado anterior en caso de error.

## ¿Por qué importa?

Esta actualización es importante porque ofrece una mayor seguridad y eficiencia para los usuarios de Linux. El soporte para Linux 7.0 significa que los usuarios pueden aprovechar las últimas características y mejoras del kernel. La codificación de erasures estables garantiza que los datos sean seguros y fiables.

## Consejo técnico

Si estás utilizando Bcachefs, te recomendamos probar la opción de rewind para restaurar el sistema a un estado anterior en caso de error. Esto te permitirá evaluar la estabilidad del sistema y asegurarte de que tus datos estén seguros.

```bash
bcachefs subvolume list
```

---

**Fuente original:** [https://www.phoronix.com/news/Bcachefs-1.37-Released](https://www.phoronix.com/news/Bcachefs-1.37-Released)
