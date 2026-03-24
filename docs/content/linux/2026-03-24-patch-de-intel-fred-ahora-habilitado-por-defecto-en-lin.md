# Patch de Intel FRED ahora habilitado por defecto en Linux

**Fecha:** 2026-03-24
**Categoría:** linux
**Tags:** ia-local, linux, codigo
**Título original:** Patch Posted To Enable Intel FRED By Default On Linux

---

## Introducción

Intel ha publicado un parche para habilitar por defecto la tecnología FRED en Linux, lo que puede mejorar el rendimiento en sistemas con procesadores Core Ultra Series 3 y Xeon Diamond Rapids.

## ¿Qué es?

FRED es una tecnología de Intel que permite una mejor gestión de eventos y devolución de resultados, lo que puede mejorar el rendimiento en aplicaciones que utilizan procesos concurrentes. Está disponible en procesadores Core Ultra Series 3 y Xeon Diamond Rapids, y también se espera que esté disponible en AMD Zen 6.

## ¿Cómo funciona?

FRED funciona habilitando la gestión de eventos y devolución de resultados en el núcleo del sistema operativo, lo que permite a los procesadores aprovechar al máximo su capacidad para procesar múltiples tareas simultáneamente. El parche de Intel habilita FRED por defecto en sistemas que lo soportan, aunque sigue siendo posible deshabilitarlo mediante la opción de comando `fred=off`.

## ¿Por qué importa?

La habilitación de FRED por defecto puede mejorar el rendimiento en aplicaciones que utilizan procesos concurrentes, como compiladores, motores de bases de datos y aplicaciones de videojuegos. Esto puede ser especialmente beneficioso en sistemas con procesadores Core Ultra Series 3 y Xeon Diamond Rapids, que están diseñados para aprovechar al máximo la tecnología FRED.

## Consejo técnico

Si estás utilizando un sistema con procesador Core Ultra Series 3 o Xeon Diamond Rapids, puedes habilitar FRED mediante la opción de comando `fred=on` en el arranque del sistema. Esto puede mejorar el rendimiento en aplicaciones que utilizan procesos concurrentes.

```bash
fred=on
```

---

**Fuente original:** [https://www.phoronix.com/news/Intel-FRED-By-Default-Patch](https://www.phoronix.com/news/Intel-FRED-By-Default-Patch)
