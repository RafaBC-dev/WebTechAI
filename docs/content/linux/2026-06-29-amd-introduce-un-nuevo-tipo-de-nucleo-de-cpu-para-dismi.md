# AMD introduce un nuevo tipo de núcleo de CPU para disminuir el consumo de energía

**Fecha:** 2026-06-29
**Categoría:** linux
**Tags:** linux, amd, cpu
**Título original:** AMD Linux Patches Introduce New "Low Power" CPU Core Type

---

## Introducción

AMD ha presentado un nuevo tipo de núcleo de CPU llamado 'Low Power' que está diseñado para minimizar el consumo de energía durante cargas de trabajo de fondo o de espera. Esto es especialmente relevante para plataformas heterogéneas de AMD.

## ¿Qué es?

El nuevo tipo de núcleo de CPU 'Low Power' es un componente de la arquitectura de AMD que está diseñado para reducir el consumo de energía en situaciones de carga de trabajo de fondo o de espera. Este tipo de núcleo es diferente de los núcleos de eficiencia (dense) existentes, que están diseñados para minimizar el consumo de energía en situaciones de alta carga de trabajo.

## ¿Cómo funciona?

El nuevo tipo de núcleo de CPU 'Low Power' se reporta a través del código de CPUID de AMD y se utiliza la infraestructura de topología de x86 en el kernel de Linux para reportar su tipo de núcleo. Esto permite a los desarrolladores de software distinguir entre núcleos de baja potencia y núcleos de eficiencia.

## ¿Por qué importa?

El nuevo tipo de núcleo de CPU 'Low Power' es importante porque permite a los desarrolladores de software optimizar su código para aprovechar al máximo la reducción de consumo de energía en plataformas de AMD. Esto puede llevar a una mayor eficiencia energética y una reducción de los costos de energía en aplicaciones de alto rendimiento.

## Consejo técnico

Si estás trabajando con plataformas de AMD y quieres aprovechar al máximo la reducción de consumo de energía, asegúrate de verificar el tipo de núcleo de CPU de tus sistemas y ajustar tu código para aprovechar la reducción de consumo de energía en núcleos de baja potencia.

```bash
Para verificar el tipo de núcleo de CPU de tu sistema, puedes utilizar el comando `cat /sys/kernel/debug/x86/topo/cpus/*` en un sistema Linux.
```

---

**Fuente original:** [https://www.phoronix.com/news/AMD-Low-Power-CPU-Core-Linux](https://www.phoronix.com/news/AMD-Low-Power-CPU-Core-Linux)
