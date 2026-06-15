# Mejoras en el scheduler de Linux 7.2 para Intel y AMD

**Fecha:** 2026-06-15
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Cache Aware Scheduling Merged For Linux 7.2 For Boosting Modern Intel & AMD CPUs

---

## Introducción

El scheduler de Linux 7.2 ha sido actualizado con una nueva característica llamada Cache Aware Scheduling, que busca mejorar el rendimiento de los procesadores Intel y AMD al optimizar la localidad de cache.

## ¿Qué es?

Cache Aware Scheduling es una característica que intenta colocar tareas que comparten datos en la misma región de cache para reducir los accesos a la cache y mejorar el rendimiento. Esto es especialmente útil en procesadores con múltiples niveles de cache.

## ¿Cómo funciona?

La característica utiliza la configuración de cache del procesador para decidir dónde colocar las tareas. Al colocar tareas que comparten datos en la misma región de cache, se reduce la cantidad de accesos a la cache y se mejora el rendimiento. Esto se logra mediante la configuración de la opción CONFIG_SCHED_CACHE en el kernel de Linux.

## ¿Por qué importa?

Esta característica es importante porque puede mejorar el rendimiento de aplicaciones que utilizan múltiples procesadores y cache. También puede ser útil en escenarios en los que se necesitan reducir los accesos a la cache para mejorar la eficiencia energética.

## Consejo técnico

Para aprovechar esta característica, es recomendable verificar la configuración de cache del procesador y ajustar la configuración del kernel de Linux para que se utilice la opción CONFIG_SCHED_CACHE.

```bash
Verificar la configuración de cache del procesador: `lscpu`
```

---

**Fuente original:** [https://www.phoronix.com/news/Linux-7.2-Scheduler](https://www.phoronix.com/news/Linux-7.2-Scheduler)
