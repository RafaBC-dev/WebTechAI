# Curobo_ros v2: un wrapper de planificación de movimiento acelerado por GPU

**Fecha:** 2026-08-04
**Categoría:** linux
**Tags:** robotica, python, librerias
**Título original:** Curobo_ros v2 – GPU-accelerated motion planning wrapper, now on cuRobo v0.8.0

---

## Introducción

La versión 2.0 de curobo_ros, un wrapper de planificación de movimiento para ROS 2, ha sido actualizada con una serie de mejoras significativas. Entre ellas, una nueva arquitectura de percepción nativa, una API de planificación de movimiento unificada y soporte para la GPU. Esto permite a los desarrolladores crear sistemas de robótica más eficientes y precisos.

## ¿Qué es?

curobo_ros es un wrapper de planificación de movimiento para ROS 2 que utiliza la tecnología cuRobo para planificar rutas óptimas para robots. La versión 2.0 ha sido actualizada con una serie de mejoras que incluyen una nueva arquitectura de percepción nativa y una API de planificación de movimiento unificada.

## ¿Cómo funciona?

La versión 2.0 de curobo_ros utiliza una arquitectura de percepción nativa que incluye un mapeador de TSDF y ESDF en la GPU. Esto permite a los desarrolladores crear sistemas de robótica más eficientes y precisos. La API de planificación de movimiento unificada permite a los desarrolladores planificar rutas óptimas para robots utilizando una variedad de métodos, incluyendo planificación de movimiento en una sola posición, planificación de movimiento en batch y planificación de movimiento en múltiples entornos.

## ¿Por qué importa?

La versión 2.0 de curobo_ros es importante porque permite a los desarrolladores crear sistemas de robótica más eficientes y precisos. Esto puede ser especialmente útil en aplicaciones que requieren una alta precisión y velocidad, como la fabricación, la medicina y la exploración espacial.

## Consejo técnico

Si estás desarrollando un sistema de robótica y deseas aprovechar las mejoras de la versión 2.0 de curobo_ros, asegúrate de actualizar tus dependencias a Python 3.10, CUDA 12 y Torch 2.5 (cu12) o 2.9 (cu13).

```bash
pip install -U curobo_ros
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/curobo-ros-v2-gpu-accelerated-motion-planning-wrapper-now-on-curobo-v0-8-0/57147](https://discourse.openrobotics.org/t/curobo-ros-v2-gpu-accelerated-motion-planning-wrapper-now-on-curobo-v0-8-0/57147)
