# GreenBoost: Un driver open-source para aumentar la memoria de NVIDIA

**Fecha:** 2026-03-15
**Categoría:** ia
**Tags:** llms, ia-local, herramientas
**Título original:** Open-Source "GreenBoost" Driver Aims To Augment NVIDIA GPUs vRAM With System RAM & NVMe To Handle Larger LLMs

---

## Introducción

Un desarrollador independiente ha creado un driver open-source llamado GreenBoost que busca aumentar la memoria de NVIDIA en sistemas Linux. Esto permitirá ejecutar modelos de LLM más grandes que no encajan en la memoria dedicada de la tarjeta gráfica.

## ¿Qué es?

GreenBoost es un módulo de kernel open-source que se conecta a la memoria de NVIDIA y utiliza la memoria del sistema y almacenamiento NVMe para aumentar la capacidad de memoria disponible. Esto se logra mediante un layer de caché CUDA que permite ejecutar modelos de LLM más grandes sin necesidad de modificar el software de CUDA.

## ¿Cómo funciona?

GreenBoost funciona mediante un módulo de kernel que asigna páginas de memoria DDR4 y las exporta como file descriptors DMA-BUF. El GPU puede importar estas páginas como memoria externa CUDA, lo que permite acceder a ellas como si fueran memoria del dispositivo. El shim de CUDA intercepta las llamadas a memoria CUDA y redirige las solicitudes a memoria grande a GreenBoost.

## ¿Por qué importa?

GreenBoost importa porque permite ejecutar modelos de LLM más grandes que no encajan en la memoria dedicada de la tarjeta gráfica, lo que es relevante para aplicaciones de IA que requieren grandes cantidades de memoria. Esto también permite mejorar el rendimiento de las aplicaciones de IA al reducir la cantidad de veces que se accede a la memoria del sistema.

## Consejo técnico

Si estás utilizando una tarjeta gráfica NVIDIA con una memoria limitada, considera utilizar GreenBoost para aumentar la capacidad de memoria disponible. Esto puede mejorar significativamente el rendimiento de tus aplicaciones de IA.

```bash
sudo insmod greenboost.ko
```

---

**Fuente original:** [https://www.phoronix.com/news/Open-Source-GreenBoost-NVIDIA](https://www.phoronix.com/news/Open-Source-GreenBoost-NVIDIA)
