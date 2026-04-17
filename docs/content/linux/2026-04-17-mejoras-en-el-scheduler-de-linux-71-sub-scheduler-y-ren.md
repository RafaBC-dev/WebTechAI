# Mejoras en el scheduler de Linux 7.1: sub-scheduler y rendimiento mejorado

**Fecha:** 2026-04-17
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Linux 7.1 sched_ext Brings cgroup Sub-Scheduler Groundwork, Idle SMT Sibling Improvement

---

## Introducción

El kernel de Linux 7.1 está recibiendo importantes mejoras en su scheduler, lo que permitirá a los desarrolladores crear sub-schedulers personalizados y mejorar el rendimiento en sistemas con múltiples núcleos.

## ¿Qué es?

El scheduler de Linux es el componente responsable de asignar recursos al sistema operativo y a las aplicaciones. El scheduler extensible (sched_ext) permite a los desarrolladores crear programas de BPF (Berkeley Packet Filter) que definan el comportamiento de la programación de tareas. Esto permite una mayor flexibilidad y personalización en la programación de tareas.

## ¿Cómo funciona?

El scheduler extensible utiliza un enfoque de programación de tareas basado en BPF, que permite a los desarrolladores crear programas que definan el comportamiento de la programación de tareas. El scheduler también incluye una estructura de cgroup (control group) que permite a los desarrolladores crear sub-schedulers personalizados. Esto permite una mayor flexibilidad y personalización en la programación de tareas.

## ¿Por qué importa?

Estas mejoras en el scheduler de Linux 7.1 permitirán a los desarrolladores crear sub-schedulers personalizados que se adapten a las necesidades específicas de sus aplicaciones. Esto puede mejorar el rendimiento y la eficiencia del sistema, especialmente en sistemas con múltiples núcleos.

## Consejo técnico

Si deseas aprovechar al máximo el scheduler extensible de Linux 7.1, es recomendable familiarizarte con la herramienta BPF y aprender a crear programas de BPF que definan el comportamiento de la programación de tareas.

```bash
bpftrace -e 'trace sched_ext:sub_scheduler'
```

---

**Fuente original:** [https://www.phoronix.com/news/Linux-7.1-sched-ext](https://www.phoronix.com/news/Linux-7.1-sched-ext)
