# GNOME 51 retira soporte a drivers NVIDIA heredados

**Fecha:** 2026-06-05
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** GNOME 51 Retires Legacy NVIDIA Driver Support With Removing EGLStreams

---

## Introducción

La versión 51 de GNOME marca un cambio importante en la forma en que se interactúa con los drivers NVIDIA en Linux. A partir de esta versión, se retiran los soportes a los drivers heredados, lo que debería mejorar la estabilidad y la seguridad del sistema.

## ¿Qué es?

GNOME es un entorno de escritorio popular para Linux, y la versión 51 es una actualización importante que incluye la eliminación del soporte a los drivers NVIDIA heredados. Estos drivers se basaban en EGLStreams, una tecnología que no fue adoptada ampliamente por otros fabricantes de hardware.

## ¿Cómo funciona?

La eliminación del soporte a los drivers heredados se logra mediante la remoción de la implementación de EGLStreams en Mutter, el componente de GNOME responsable de la gestión de la ventana. Esto permite que el sistema se centre en el uso de la tecnología DMA-BUF, que es más estable y segura.

## ¿Por qué importa?

La eliminación de los drivers heredados debería mejorar la estabilidad y la seguridad del sistema, ya que elimina una fuente potencial de errores y vulnerabilidades. Además, esto permite que los desarrolladores de GNOME se centren en la mejora de la experiencia de usuario y la funcionalidad del entorno de escritorio.

## Consejo técnico

Si estás utilizando GNOME 51 y tienes problemas con los drivers NVIDIA, puedes intentar actualizar a la última versión de los drivers oficiales de NVIDIA, que ya soportan la tecnología DMA-BUF.

```bash
sudo apt-get update && sudo apt-get install nvidia-driver
```

---

**Fuente original:** [https://www.phoronix.com/news/GNOME-51-Drops-EGLStreams](https://www.phoronix.com/news/GNOME-51-Drops-EGLStreams)
