# Mejora en el rendimiento de juegos DX12 en Linux gracias a Intel

**Fecha:** 2026-03-25
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Intel's Vulkan Linux Driver Lands New Feature To Boost DX12 Game Performance

---

## Introducción

Intel ha lanzado una actualización para su driver Vulkan Linux que mejora el rendimiento de juegos que utilizan Direct3D 12 (DX12) en Linux. Esta mejora se logra gracias a una característica llamada BTP+BTI RCC Keying.

## ¿Qué es?

BTP+BTI RCC Keying es una característica que permite mejorar el rendimiento de juegos DX12 en Linux. Funciona mediante la modificación de la forma en que el driver Vulkan Linux accede a la memoria gráfica. En lugar de utilizar solo el índice de la tabla de enlace, se utiliza la suma del índice y el puntero de la tabla de enlace como etiqueta en la caché de estado.

## ¿Cómo funciona?

La actualización del driver Vulkan Linux incluye una serie de parches que permiten habilitar la característica BTP+BTI RCC Keying. Esta característica depende de una actualización del kernel Xe que se encuentra en desarrollo. Los parches incluyen también algunas correcciones y actualizaciones del driver ANV.

## ¿Por qué importa?

Esta mejora es importante porque permite mejorar el rendimiento de juegos DX12 en Linux, lo que es especialmente relevante para aquellos que utilizan Steam Play con Proton + VKD3D-Proton. La mejora se ha probado en diferentes juegos y ha demostrado ser efectiva.

## Consejo técnico

Si deseas aprovechar esta mejora, asegúrate de tener la versión más reciente del driver Vulkan Linux y del kernel Xe. También es importante verificar que la característica BTP+BTI RCC Keying esté habilitada en la configuración del driver.

```bash
anv_state_cache_perf_fix=1
```

---

**Fuente original:** [https://www.phoronix.com/news/Intel-ANV-BTP-BTI-RCC-Keying](https://www.phoronix.com/news/Intel-ANV-BTP-BTI-RCC-Keying)
