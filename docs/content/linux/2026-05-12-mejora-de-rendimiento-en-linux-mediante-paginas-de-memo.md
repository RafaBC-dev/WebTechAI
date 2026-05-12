# Mejora de rendimiento en Linux mediante páginas de memoria de 64KB

**Fecha:** 2026-05-12
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** [$] Providing 64KB base pages with 4KB kernels, two different ways

---

## Introducción

El equipo de desarrollo de Linux ha estado trabajando en mejorar el rendimiento de la memoria en los sistemas operativos. En la reciente conferencia Linux Storage, Filesystem, Memory Management, and BPF Summit, se presentaron dos opciones para permitir que los procesos utilicen páginas de memoria de 64KB en sistemas con kernels de 4KB.

## ¿Qué es?

Las páginas de memoria son unidades de almacenamiento en la memoria RAM que se utilizan para almacenar datos de los procesos. Los kernels de 4KB son la unidad básica de almacenamiento en la memoria RAM utilizada por el sistema operativo. Permitir páginas de memoria de 64KB puede mejorar el rendimiento al reducir la cantidad de páginas necesarias para almacenar datos, pero puede aumentar el uso de memoria.

## ¿Cómo funciona?

La primera opción permite a cada proceso utilizar su propia página de memoria de 64KB, mientras que la segunda opción utiliza una página de memoria de 64KB para todo el sistema. Esto se logra mediante la creación de una estructura de datos que mantiene la información de las páginas de memoria de 64KB y su correspondencia con las páginas de memoria de 4KB utilizadas por el kernel.

## ¿Por qué importa?

Esta mejora puede ser beneficiosa para aplicaciones que requieren un gran uso de memoria, como bases de datos y sistemas de archivo. También puede mejorar el rendimiento de sistemas con kernels de 4KB que necesitan acceder a grandes cantidades de datos.

## Consejo técnico

Si deseas probar la opción de páginas de memoria de 64KB en tu sistema Linux, puedes utilizar el comando `echo 64 > /proc/meminfo` para establecer la página de memoria de 64KB como la página de memoria predeterminada.

```bash
echo 64 > /proc/meminfo
```

---

**Fuente original:** [https://lwn.net/Articles/1071484/](https://lwn.net/Articles/1071484/)
