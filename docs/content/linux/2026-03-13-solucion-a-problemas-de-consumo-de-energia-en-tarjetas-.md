# Solución a problemas de consumo de energía en tarjetas gráficas AMD

**Fecha:** 2026-03-13
**Categoría:** linux
**Tags:** llms, ia-local, linux
**Título original:** Linux 7.0 AMDGPU Fixing Idle Power Issue For RDNA4 GPUs After Compute Workloads

---

## Introducción

La empresa AMD está trabajando en solucionar un problema de consumo de energía excesivo en sus tarjetas gráficas RDNA4 después de realizar tareas de cómputo intensivas. Este problema ha sido detectado en sistemas que utilizan Linux y ha causado un aumento en el consumo de energía incluso cuando la tarjeta gráfica está en estado de inactividad.

## ¿Qué es?

Linux 7.0 es una versión actualizada del sistema operativo Linux, que incluye mejoras y correcciones en el soporte para hardware de AMD. La AMDGPU es un controlador de kernel que permite a Linux interactuar con las tarjetas gráficas AMD. El MES (Memory Encryption System) es un sistema de cifrado de memoria que protege la información sensible en la memoria de la tarjeta gráfica.

## ¿Cómo funciona?

El problema se debe a que el MES firmware actualizado puede causar un consumo de energía anormal en las tarjetas gráficas RDNA4 después de realizar tareas de cómputo intensivas. Para solucionar esto, se ha agregado un chequeo en el controlador AMDGPU para ajustar el temporizador de sobresubscripción de memoria, lo que permite a Linux trabajar alrededor del problema sin necesidad de actualizar el firmware. Además, se está trabajando en la creación de un nuevo firmware MES que resuelva el problema de fondo.

## ¿Por qué importa?

Este problema es importante porque puede causar un aumento en el consumo de energía y un calentamiento excesivo en las tarjetas gráficas, lo que puede afectar la vida útil del hardware y la eficiencia energética del sistema. La solución proporcionada por Linux 7.0 y el controlador AMDGPU ayudará a prevenir este problema y a mantener el rendimiento y la eficiencia del sistema.

## Consejo técnico

Si estás utilizando una tarjeta gráfica AMD en un sistema con Linux, asegúrate de actualizar a la versión 7.0 del kernel y del controlador AMDGPU para aprovechar la solución proporcionada para este problema. También es recomendable verificar la versión del firmware MES y actualizarla a la versión más reciente si es necesario.

```bash
sudo apt-get update && sudo apt-get install linux-image-7.0-amd64
```

---

**Fuente original:** [https://www.phoronix.com/news/Linux-7-Fix-Idle-RDNA4-Compute](https://www.phoronix.com/news/Linux-7-Fix-Idle-RDNA4-Compute)
