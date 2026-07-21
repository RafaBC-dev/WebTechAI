# Reinicio frío para gráficos Intel en Linux: una herramienta de recuperación

**Fecha:** 2026-07-21
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Cold Reset Recovery Coming Together To Better Help Intel GPUs On Linux

---

## Introducción

Los ingenieros de Intel están trabajando en una herramienta de recuperación para gráficos Intel en Linux que permite reiniciar el dispositivo de gráficos de manera fría en caso de errores persistentes.

## ¿Qué es?

La herramienta de recuperación de reinicio frío es un método para manejar errores en los gráficos Intel que requieren un reinicio completo del dispositivo para recuperarse. Esto se logra mediante un reinicio frío, que es diferente a un reinicio caliente, que solo reinicia el sistema operativo. El reinicio frío es necesario para eliminar errores persistentes en el dispositivo de gráficos, como errores en la Unidad de Gestión de Potencia (PUNIT).

## ¿Cómo funciona?

La herramienta de recuperación de reinicio frío se integra en el gestor de renderizado directo (DRM) y utiliza un nuevo método de recuperación llamado DRM_WEDGE_RECOVERY_COLD_RESET. Cuando se detecta un error que requiere un reinicio frío, el DRM notifica al espacio de usuario a través de un evento uevent, que a su vez puede tomar medidas para reiniciar el dispositivo de gráficos de manera fría.

## ¿Por qué importa?

Esta herramienta es importante porque permite a los usuarios de Linux con gráficos Intel recuperarse de errores persistentes sin tener que reiniciar completamente el sistema. Esto puede ser especialmente útil en escenarios de alta disponibilidad, donde un reinicio completo del sistema puede ser costoso en términos de tiempo y recursos.

## Consejo técnico

Si estás experimentando errores persistentes en tus gráficos Intel en Linux, puedes probar la herramienta de recuperación de reinicio frío utilizando el comando `dri-devel` para obtener más información sobre la implementación y cómo utilizarla.

```bash
dri-devel
```

---

**Fuente original:** [https://www.phoronix.com/news/Intel-Cold-Reset-Recovery-Linux](https://www.phoronix.com/news/Intel-Cold-Reset-Recovery-Linux)
