# NVK Vulkan Driver de NVIDIA ahora admite DLSS en Linux

**Fecha:** 2026-06-20
**Categoría:** linux
**Tags:** linux, ia-local, herramientas
**Título original:** Open-Source NVIDIA NVK Vulkan Driver Now Supports DLSS

---

## Introducción

El driver NVK de Vulkan de NVIDIA ha alcanzado un importante hito: ahora admite la tecnología de supermuestreo de aprendizaje profundo (DLSS) en Linux. Esto significa que los jugadores de Linux pueden disfrutar de una experiencia de juego más fluida y detallada en juegos que utilizan DLSS.

## ¿Qué es?

El NVK Vulkan Driver es un driver de código abierto para la tecnología Vulkan de NVIDIA. Vulkan es una API de gráficos que permite a los desarrolladores crear aplicaciones de alta performance y baja latencia. El NVK Driver es una implementación de Vulkan para Linux que permite a los usuarios aprovechar las características de gráficos de NVIDIA en su sistema Linux.

## ¿Cómo funciona?

Para que el NVK Driver pueda admitir DLSS, se necesita la extensión VK_NVX_binary_import, que permite a los aplicativos importar binarios de CUDA de NVIDIA y ejecutarlos en la GPU. La extensión VK_NVX_binary_import se ha implementado en el NVK Driver mediante un pull request que se ha fusionado en la versión 26.2-devel de Mesa. Esto significa que los jugadores de Linux pueden ahora utilizar DLSS en juegos que lo admiten.

## ¿Por qué importa?

La admisión de DLSS en el NVK Driver es importante porque permite a los jugadores de Linux disfrutar de una experiencia de juego más fluida y detallada en juegos que utilizan DLSS. Esto es especialmente relevante para los jugadores que utilizan sistemas Linux para jugar juegos que no están disponibles en Linux o que no tienen una versión optimizada para Linux.

## Consejo técnico

Si deseas utilizar DLSS en el NVK Driver, debes establecer la variable de entorno NVK_EXPERIMENTAL=dlss. Esto activará la función de DLSS en el NVK Driver y permitirá que los juegos que lo admiten utilicen la tecnología de supermuestreo de aprendizaje profundo.

```bash
NVK_EXPERIMENTAL=dlss
```

---

**Fuente original:** [https://www.phoronix.com/news/Mesa-NVK-Vulkan-Does-DLSS](https://www.phoronix.com/news/Mesa-NVK-Vulkan-Does-DLSS)
