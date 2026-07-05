# Mejora significativa en la latencia de submisión de tareas en Linux DRM

**Fecha:** 2026-07-05
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Linux DRM Scheduler Patches Yield Massive Improvement For Job Submission Latency

---

## Introducción

Los desarrolladores de Linux han presentado un conjunto de parches para mejorar la latencia de submisión de tareas en el gerente de renderizado directo (DRM). Esto es especialmente importante para sistemas sobrecargados con procesos de CPU en ejecución.

## ¿Qué es?

El DRM (Direct Rendering Manager) es un módulo del kernel de Linux que se encarga de la gestión de la gráfica en tiempo real. El gerente de DRM utiliza workqueues para la ejecución de tareas asincrónicas, pero esto puede causar retrasos en la submisión de tareas cuando el sistema está sobrecargado.

## ¿Cómo funciona?

Los parches propuestos reemplazan el uso de workqueues con kthread_work, que es una forma más eficiente de ejecutar tareas asincrónicas. Esto permite una mejor gestión de la carga de trabajo y reduce la latencia de submisión de tareas.

## ¿Por qué importa?

La mejora en la latencia de submisión de tareas es importante para aplicaciones que requieren una respuesta rápida, como compositores de video y juegos. Esto también puede mejorar la experiencia del usuario en sistemas sobrecargados.

## Consejo técnico

Si deseas probar los parches propuestos, puedes encontrar el código en el listado dri-devel. Recuerda que es importante seguir las instrucciones de compilación y configuración para evitar problemas de compatibilidad.

```bash
git clone https://git.kernel.org/pub/scm/linux/kernel/git/dri/drm.git
```

---

**Fuente original:** [https://www.phoronix.com/news/DRM-Scheduler-Lower-Job-Submit](https://www.phoronix.com/news/DRM-Scheduler-Lower-Job-Submit)
