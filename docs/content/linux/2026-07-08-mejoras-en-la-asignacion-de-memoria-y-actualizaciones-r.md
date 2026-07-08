# Mejoras en la asignación de memoria y actualizaciones RCU en Linux

**Fecha:** 2026-07-08
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** [$] Faster RCUs and lockless memory allocation

---

## Introducción

Puranjay Mohan ha presentado una serie de mejoras en la asignación de memoria y actualizaciones de lectura en el sistema operativo Linux. Estas mejoras buscan mejorar la eficiencia y la estabilidad del sistema.

## ¿Qué es?

La asignación de memoria en Linux se realiza mediante el sistema de memoria dinámica, que asigna y libera memoria a medida que es necesaria. Las actualizaciones de lectura (RCU) son un mecanismo que permite a los procesos leer datos sin bloquear la ejecución del sistema. Las mejoras presentadas por Puranjay Mohan buscan mejorar la eficiencia y la estabilidad de este mecanismo.

## ¿Cómo funciona?

La mejora se logra mediante la implementación de una nueva función llamada kmalloc_nolock(), que permite la asignación de memoria sin bloquear la ejecución del sistema. Esta función interactúa con el sistema de RCU para permitir la asignación de memoria de manera segura y eficiente.

## ¿Por qué importa?

Estas mejoras son importantes porque permiten a los desarrolladores crear aplicaciones más eficientes y estables en Linux. Además, estas mejoras pueden ser aplicadas a una variedad de sistemas y aplicaciones, lo que las hace más ampliamente útiles.

## Consejo técnico

Si deseas aprovechar las mejoras en la asignación de memoria y actualizaciones RCU en Linux, puedes probar la función kmalloc_nolock() en tu código de desarrollo. Puedes encontrar más información sobre esta función en la documentación de Linux.

```bash
kmalloc_nolock()
```

---

**Fuente original:** [https://lwn.net/Articles/1081009/](https://lwn.net/Articles/1081009/)
