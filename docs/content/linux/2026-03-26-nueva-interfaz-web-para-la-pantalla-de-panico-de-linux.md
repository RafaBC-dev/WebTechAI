# Nueva interfaz web para la pantalla de pánico de Linux

**Fecha:** 2026-03-26
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Fedora 45 Plan Approved For Web Frontend To Linux's "Blue Screen of Death" DRM Panic

---

## Introducción

La comunidad de Fedora ha aprobado un cambio importante en la pantalla de pánico de Linux, que ahora incluirá una interfaz web para facilitar la resolución de problemas de kernel. Esto permitirá a los usuarios capturar y compartir fácilmente los errores de kernel.

## ¿Qué es?

La pantalla de pánico de Linux, también conocida como 'Blue Screen of Death', es una pantalla que se muestra cuando el kernel de Linux experimenta un error crítico. La nueva interfaz web permitirá a los usuarios capturar y compartir fácilmente los errores de kernel, lo que facilitará la resolución de problemas y la depuración.

## ¿Cómo funciona?

La nueva interfaz web se basará en la tecnología DRM Panic, que permite a los usuarios capturar y compartir los errores de kernel en forma de un código QR. El código QR llevará a una página web donde se mostrará la información de kernel en una forma más amigable y fácil de entender.

## ¿Por qué importa?

La nueva interfaz web permitirá a los usuarios capturar y compartir fácilmente los errores de kernel, lo que facilitará la resolución de problemas y la depuración. Esto será especialmente útil para los desarrolladores de software y los administradores de sistemas que necesitan depurar y solucionar problemas de kernel.

## Consejo técnico

Si deseas probar la nueva interfaz web de la pantalla de pánico de Linux, asegúrate de tener Fedora 45 instalada y configura la opción de DRM Panic en tu kernel. Puedes hacer esto ejecutando el comando `echo 'drm.panic_on_oops=1' > /sys/module/drm/parameters/panic_on_oops` y reiniciando tu sistema.

```bash
echo 'drm.panic_on_oops=1' > /sys/module/drm/parameters/panic_on_oops
```

---

**Fuente original:** [https://www.phoronix.com/news/Fedora-45-To-Get-DRM-Panic-Web](https://www.phoronix.com/news/Fedora-45-To-Get-DRM-Panic-Web)
