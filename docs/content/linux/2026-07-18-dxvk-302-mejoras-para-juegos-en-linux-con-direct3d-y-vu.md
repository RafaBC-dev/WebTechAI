# DXVK 3.0.2: Mejoras para juegos en Linux con Direct3D y Vulkan

**Fecha:** 2026-07-18
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** DXVK 3.0.2 Released With Improved Hang Debugging, Handful Of Game Fixes

---

## Introducción

Valve ha lanzado la versión 3.0.2 de DXVK, una herramienta que permite ejecutar juegos de Windows en Linux utilizando la API Vulkan. Esta actualización incluye mejoras para resolver problemas de juegos específicos y facilitar la depuración de problemas de hardware.

## ¿Qué es?

DXVK es una herramienta de código abierto que implementa las API de Direct3D 8, 9, 10 y 11 sobre la API Vulkan, permitiendo a los desarrolladores ejecutar juegos de Windows en Linux. Esto se logra mediante la traducción de llamadas de la API de Direct3D a llamadas de la API Vulkan.

## ¿Cómo funciona?

DXVK utiliza la API Vulkan para renderizar gráficos y ejecutar instrucciones de la API de Direct3D. Esto permite a los juegos de Windows ser ejecutados en Linux sin necesidad de una emulación completa de la API de Direct3D. DXVK también incluye una herramienta de depuración que permite a los desarrolladores identificar y resolver problemas de hardware.

## ¿Por qué importa?

DXVK es importante porque permite a los desarrolladores de juegos ejecutar sus juegos en Linux, lo que facilita la creación de contenido para la plataforma. Además, las mejoras en DXVK resuelven problemas específicos de juegos, lo que mejora la experiencia del usuario.

## Consejo técnico

Si estás experimentando problemas de hardware con DXVK, prueba establecer la variable de entorno DXVK_DEBUG=hang para obtener más información sobre el problema y ayudar a los desarrolladores a resolverlo.

```bash
DXVK_DEBUG=hang
```

---

**Fuente original:** [https://www.phoronix.com/news/DXVK-3.0.2-Released](https://www.phoronix.com/news/DXVK-3.0.2-Released)
