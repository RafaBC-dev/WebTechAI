# Mejoras en Linux 7.2 aumentan el rendimiento de MongoDB en un 30-100%

**Fecha:** 2026-06-25
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** MGLRU Improvement Yielding Nice Gains On Linux 7.2: MongoDB 30~100% Higher Throughput

---

## Introducción

La versión 7.2 del kernel de Linux ha sido actualizada con varias mejoras en la gestión de memoria, lo que ha llevado a un aumento significativo en el rendimiento de MongoDB en ciertas cargas de trabajo.

## ¿Qué es?

MGLRU es un algoritmo de reutilización de memoria que ayuda a liberar memoria asignada a procesos que ya no la necesitan. La mejora en MGLRU permite una reutilización más eficiente de la memoria y reduce el tiempo de respuesta en ciertas cargas de trabajo.

## ¿Cómo funciona?

La mejora en MGLRU se logra mediante la optimización del bucle de reutilización de memoria y la gestión de escrituras sucias. Esto permite una reutilización más eficiente de la memoria y reduce el tiempo de respuesta en ciertas cargas de trabajo. Además, la mejora también incluye la capacidad de pausar y reanudar el seguimiento de DAMON sin perder su estado actual.

## ¿Por qué importa?

Estas mejoras en MGLRU importan porque pueden mejorar significativamente el rendimiento de aplicaciones como MongoDB en ciertas cargas de trabajo. Esto puede ser especialmente importante en entornos de alta disponibilidad y rendimiento donde cada milisegundo cuenta.

## Consejo técnico

Si estás utilizando MongoDB en un entorno de alta disponibilidad y rendimiento, considera actualizar a la versión 7.2 del kernel de Linux para aprovechar las mejoras en MGLRU y mejorar el rendimiento de tu aplicación.

```bash
sudo apt-get update && sudo apt-get install linux-image-7.2
```

---

**Fuente original:** [https://www.phoronix.com/news/Linux-7.2-MM](https://www.phoronix.com/news/Linux-7.2-MM)
