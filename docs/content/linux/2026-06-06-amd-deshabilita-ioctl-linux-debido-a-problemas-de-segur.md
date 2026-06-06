# AMD deshabilita ioctl Linux debido a problemas de seguridad

**Fecha:** 2026-06-06
**Categoría:** linux
**Tags:** linux, seguridad, ioctl
**Título original:** Linux DRM Ioctl Developed By AMD Being Disabled Following Ongoing Security Issue

---

## Introducción

La empresa AMD ha deshabilitado una interfaz de ioctl en el kernel Linux debido a problemas de seguridad que han surgido después de su introducción. Esta medida se ha tomado después de que se identificara una vulnerabilidad que permitía a los usuarios del espacio de usuario desencadenar advertencias en el kernel.

## ¿Qué es?

El ioctl es una interfaz de programación de aplicaciones que permite a los usuarios del espacio de usuario interactuar con el kernel. En este caso, se trata de una interfaz llamada drm_gem_change_handle_ioctl() que permite reasignar handles de GEM. Esta interfaz fue desarrollada por AMD como parte de su iniciativa CRIU (Checkpoint and Restore in User-Space) para permitir la congelación de aplicaciones en ejecución y su restauración posterior.

## ¿Cómo funciona?

La interfaz drm_gem_change_handle_ioctl() permite a los usuarios del espacio de usuario reasignar handles de GEM, lo que es necesario para la congelación y restauración de aplicaciones en ejecución. Sin embargo, se ha identificado una vulnerabilidad que permite a los usuarios del espacio de usuario desencadenar advertencias en el kernel, lo que ha llevado a la deshabilitación de la interfaz.

## ¿Por qué importa?

La deshabilitación de esta interfaz es importante porque puede afectar a las aplicaciones que utilizan la iniciativa CRIU de AMD. Las aplicaciones que dependen de esta interfaz pueden no funcionar correctamente o incluso pueden ser vulnerables a ataques de seguridad.

## Consejo técnico

Si estás utilizando la iniciativa CRIU de AMD, es recomendable verificar si tu aplicación depende de la interfaz drm_gem_change_handle_ioctl() y, si es así, explorar alternativas para reasignar handles de GEM de manera segura.

```bash
drm_gem_change_handle_ioctl()
```

---

**Fuente original:** [https://www.phoronix.com/news/Linux-7.1-DRM-Change-Handle](https://www.phoronix.com/news/Linux-7.1-DRM-Change-Handle)
