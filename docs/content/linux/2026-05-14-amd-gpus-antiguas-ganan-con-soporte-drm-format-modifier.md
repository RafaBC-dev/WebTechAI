# AMD GPUs antiguas ganan con soporte DRM format modifiers en Linux

**Fecha:** 2026-05-14
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Older AMD GPUs Score Another Open-Source Driver Win From Valve: DRM Format Modifiers

---

## Introducción

Valve ha lanzado una actualización para las GPU AMD antiguas, permitiendo el uso de DRM format modifiers en Linux. Esto significa que los usuarios pueden disfrutar de mejoras en el rendimiento y compatibilidad con aplicaciones de gráficos en estas GPU antiguas.

## ¿Qué es?

Los DRM format modifiers son una característica que proporciona detalles sobre la forma en que se almacenan y se manejan los buffers de imagen en la memoria gráfica. Esto puede mejorar el rendimiento y la compatibilidad con aplicaciones de gráficos que utilizan tecnologías como Vulkan o OpenGL.

## ¿Cómo funciona?

La actualización implementa DRM format modifiers en la GPU AMD utilizando la tecnología AMDGPU, que es el driver de kernel para las GPU AMD. Esto se logra mediante la adición de un nuevo conjunto de comandos y funciones en el driver de kernel y en la biblioteca de usuario RADV/RadeonSI.

## ¿Por qué importa?

Esta actualización es importante porque permite que los usuarios de GPU AMD antiguas puedan disfrutar de mejoras en el rendimiento y compatibilidad con aplicaciones de gráficos. Esto es especialmente relevante para aquellos que utilizan tecnologías como Vulkan o OpenGL en sus aplicaciones de gráficos.

## Consejo técnico

Si estás utilizando una GPU AMD antigua en Linux, es recomendable actualizar tu driver de kernel y tu biblioteca de usuario RADV/RadeonSI para aprovechar las mejoras en el rendimiento y compatibilidad que ofrece esta actualización.

```bash
sudo apt-get update && sudo apt-get install linux-modules-extra-$(uname -r) && sudo apt-get install mesa-utils
```

---

**Fuente original:** [https://www.phoronix.com/news/AMD-DRM-Format-Modifiers-GCN](https://www.phoronix.com/news/AMD-DRM-Format-Modifiers-GCN)
