# Linux 7.2: un gran paso hacia la seguridad en el código con Rust

**Fecha:** 2026-06-15
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Linux 7.2 Introducing The Rust Zerocopy Library To Eliminate More "Unsafe" Code

---

## Introducción

La versión 7.2 del kernel de Linux ha sido lanzada con un gran conjunto de cambios en el código escrito en Rust. Esto incluye la integración de la biblioteca Zerocopy, que permite eliminar código 'inseguro' y mejorar la seguridad del código.

## ¿Qué es?

La biblioteca Zerocopy es una herramienta de código abierto que permite realizar manipulaciones de memoria de manera segura y eficiente. Ofrece derivables y macros para convertir entre secuencias de bytes y otros tipos de datos, lo que reduce la necesidad de código 'inseguro'.

## ¿Cómo funciona?

La biblioteca Zerocopy se integra en el kernel de Linux a través de una serie de cambios en el código Rust. Estos cambios incluyen la adición de derivables y macros para realizar manipulaciones de memoria de manera segura. Además, se han agregado mejoras en el análisis de código y en la generación de código para mejorar la eficiencia y la seguridad.

## ¿Por qué importa?

La integración de la biblioteca Zerocopy en el kernel de Linux es importante porque reduce la necesidad de código 'inseguro' y mejora la seguridad del código. Esto es especialmente relevante en sistemas críticos como el kernel de Linux, donde la seguridad es fundamental.

## Consejo técnico

Si estás trabajando con código Rust en Linux, considera utilizar la biblioteca Zerocopy para mejorar la seguridad y la eficiencia de tu código. Puedes comenzar por revisar la documentación oficial de la biblioteca y explorar sus características y funcionalidades.

```bash
rustup add zerocopy
```

---

**Fuente original:** [https://www.phoronix.com/news/Linux-7.2-Rust](https://www.phoronix.com/news/Linux-7.2-Rust)
