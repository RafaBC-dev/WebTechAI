# Soporte para tarjetas gráficas Barco MXRT en Linux gracias a AMD

**Fecha:** 2026-06-20
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** AMD-Powered Barco MXRT Graphics Cards Finally Seeing Linux Driver Support

---

## Introducción

La empresa Barco ha estado utilizando tarjetas gráficas basadas en GPU de AMD para sus sistemas de visualización médica, pero hasta ahora solo habían sido compatibles con Windows. Sin embargo, un desarrollador ha creado un parche para agregar soporte a estas tarjetas en Linux.

## ¿Qué es?

Las tarjetas gráficas Barco MXRT son una serie de adaptadores gráficos diseñados para sistemas de visualización médica que utilizan GPU de AMD. Estas tarjetas permiten la visualización de múltiples monitores y son utilizadas en aplicaciones médicas como la radiología y la ecografía.

## ¿Cómo funciona?

El parche creado por el desarrollador Matthew Jacob agrega soporte a varias tarjetas gráficas Barco MXRT en el driver de kernel Linux AMDGPU. Esto permite que estas tarjetas funcionen correctamente en Linux, incluyendo la visualización de múltiples monitores.

## ¿Por qué importa?

El soporte para estas tarjetas gráficas en Linux es importante porque permite a los desarrolladores y usuarios utilizar estas tarjetas en entornos Linux, lo que puede ser útil en aplicaciones médicas y de visualización que requieren una gran cantidad de recursos gráficos.

## Consejo técnico

Si deseas probar el soporte para las tarjetas gráficas Barco MXRT en Linux, asegúrate de instalar el parche AMDGPU y verificar que tu sistema de kernel esté actualizado.

```bash
sudo apt-get update && sudo apt-get install linux-headers-$(uname -r) && sudo modprobe amdgpu
```

---

**Fuente original:** [https://www.phoronix.com/news/AMD-Barco-MXRT-Linux-Patch](https://www.phoronix.com/news/AMD-Barco-MXRT-Linux-Patch)
