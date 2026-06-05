# Prueba de rendimiento del scheduler BORE en CachyOS Linux

**Fecha:** 2026-06-05
**Categoría:** linux
**Tags:** linux, cachyos, scheduler, rendimiento
**Título original:** Benchmarking The BORE Scheduler Performance With CachyOS Linux

---

## Introducción

El scheduler BORE, diseñado para mejorar la respuesta de los sistemas bajo carga intensa, ha sido probado en CachyOS Linux. Los resultados muestran una mejora significativa en la respuesta del sistema y la experiencia del usuario.

## ¿Qué es?

El scheduler BORE (Burst-Oriented Response Enhancer) es una versión mejorada del scheduler EEVDF, diseñado para mejorar la respuesta del sistema bajo carga intensa. Introduce la concepto de 'burstiness', que permite ajustar la prioridad de tareas según su requerimiento de respuesta.

## ¿Cómo funciona?

El BORE scheduler ajusta la prioridad de tareas en función de su 'burstiness', que se calcula en función del tiempo de CPU consumido por cada tarea. Esto permite priorizar tareas que requieren una respuesta rápida, mejorando la experiencia del usuario.

## ¿Por qué importa?

El BORE scheduler es importante porque mejora la respuesta del sistema bajo carga intensa, lo que es especialmente relevante en entornos de escritorio y aplicaciones que requieren una respuesta rápida.

## Consejo técnico

Si deseas mejorar la respuesta de tu sistema Linux, prueba el scheduler BORE en CachyOS y ajusta la configuración según tus necesidades para obtener los mejores resultados.

```bash
linux-cachyos-bore
```

---

**Fuente original:** [https://www.phoronix.com/review/cachyos-bore](https://www.phoronix.com/review/cachyos-bore)
