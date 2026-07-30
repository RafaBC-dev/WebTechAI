# Modificadores de formato DRM para GPUs AMD antiguas en Linux 7.3

**Fecha:** 2026-07-30
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** DRM Format Modifiers For Old AMD GPUs Coming With Linux 7.3: Thanks Valve

---

## Introducción

La próxima versión de Linux, Linux 7.3, incluirá mejoras significativas para las GPUs AMD antiguas. Entre ellas, la implementación de modificadores de formato DRM, gracias a la colaboración de Valve.

## ¿Qué es?

Los modificadores de formato DRM son una característica que proporciona detalles sobre la organización de los buffers de imágenes, como la tilización, compresión y otros atributos. Esto puede mejorar el rendimiento y permitir uso más versátil de las GPU.

## ¿Cómo funciona?

La implementación de modificadores de formato DRM en Linux 7.3 permitirá a las GPU AMD antiguas, como las de la serie Radeon HD 7000, aprovechar al máximo sus capacidades. Esto se logra mediante la inclusión de soporte para modificadores de formato DRM en el driver AMDGPU.

## ¿Por qué importa?

Esto es importante porque permitirá a los desarrolladores aprovechar al máximo las capacidades de las GPU AMD antiguas, lo que puede mejorar el rendimiento de aplicaciones como los compositores de Wayland y las capas de OpenGL sobre Vulkan.

## Consejo técnico

Si tienes una GPU AMD antigua, puedes probar la versión beta de Linux 7.3 para ver si los modificadores de formato DRM mejoran el rendimiento de tus aplicaciones. Recuerda que es importante verificar la compatibilidad de tu hardware antes de instalar la versión beta.

```bash
sudo apt-get update && sudo apt-get install linux-7.3-beta
```

---

**Fuente original:** [https://www.phoronix.com/news/Linux-7.3-AMDGPU-GFX6-Modifiers](https://www.phoronix.com/news/Linux-7.3-AMDGPU-GFX6-Modifiers)
