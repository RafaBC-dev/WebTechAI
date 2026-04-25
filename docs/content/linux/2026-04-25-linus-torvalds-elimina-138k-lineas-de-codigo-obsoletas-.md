# Linus Torvalds elimina 138k líneas de código obsoletas del kernel de Linux

**Fecha:** 2026-04-25
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Farewell ISDN, Ham Radio & Old Network Drivers: Linus Torvalds Merges 138k L.O.C. Removal

---

## Introducción

Linus Torvalds ha eliminado una gran cantidad de código obsoleto del kernel de Linux, incluyendo soporte para ISDN, radio amateur y adaptadores de red antiguos. Esta eliminación se debe a una serie de informes de errores generados por modelos de lenguaje de gran tamaño que han encontrado problemas en estos drivers.

## ¿Qué es?

El kernel de Linux es el núcleo del sistema operativo Linux, que gestiona la comunicación entre hardware y software. Los drivers son programas que permiten a Linux interactuar con hardware específico, como adaptadores de red y dispositivos de almacenamiento.

## ¿Cómo funciona?

Los drivers de red en Linux se encargan de manejar la comunicación entre el hardware de red y el kernel. Los drivers obsoletos, como los para ISDN y radio amateur, se habían mantenido en el kernel debido a la presencia de usuarios activos, pero con la llegada de modelos de lenguaje de gran tamaño, estos drivers se han vuelto un problema debido a los informes de errores generados.

## ¿Por qué importa?

La eliminación de estos drivers obsoletos reduce la complejidad del kernel de Linux y elimina posibles fuentes de errores. Esto también permite a los desarrolladores enfocarse en mejorar y mantener los drivers más importantes y actuales.

## Consejo técnico

Si estás utilizando un sistema Linux antiguo con drivers obsoletos, es posible que debas actualizar a una versión más reciente del kernel para evitar problemas de seguridad y estabilidad.

```bash
Si deseas verificar la versión actual del kernel en tu sistema Linux, puedes utilizar el comando `uname -a` en la terminal.
```

---

**Fuente original:** [https://www.phoronix.com/news/Linux-7.1-Removes-Old-Net](https://www.phoronix.com/news/Linux-7.1-Removes-Old-Net)
