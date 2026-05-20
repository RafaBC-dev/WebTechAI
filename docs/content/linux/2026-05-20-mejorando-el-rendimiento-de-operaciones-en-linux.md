# Mejorando el rendimiento de operaciones en Linux

**Fecha:** 2026-05-20
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** [$] In search of faster this_cpu operations

---

## Introducción

El rendimiento de las operaciones en Linux se está mejorando gracias a un cambio fundamental en cómo se accede a variables por CPU. Este cambio podría mejorar el rendimiento en una amplia gama de arquitecturas.

## ¿Qué es?

Las operaciones this_cpu en el kernel de Linux están diseñadas para acelerar el acceso a variables por CPU. Sin embargo, su rendimiento varía dependiendo de la arquitectura del procesador.

## ¿Cómo funciona?

Yang Shi propuso un cambio en cómo funcionan estas operaciones para mejorar el rendimiento en una variedad de arquitecturas. El cambio implica una reorganización de cómo se accede a las variables por CPU.

## ¿Por qué importa?

Este cambio podría mejorar el rendimiento en sistemas con arquitecturas diferentes, lo que es importante para aplicaciones que requieren alta velocidad y eficiencia.

## Consejo técnico

Para probar el rendimiento de las operaciones this_cpu en tu sistema, puedes utilizar el comando `perf` con la opción `-e this_cpu` para medir el tiempo de ejecución de las operaciones.

```bash
perf -e this_cpu
```

---

**Fuente original:** [https://lwn.net/Articles/1073395/](https://lwn.net/Articles/1073395/)
