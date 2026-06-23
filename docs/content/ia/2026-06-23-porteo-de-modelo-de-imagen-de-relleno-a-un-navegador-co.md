# Porteo de modelo de imagen de relleno a un navegador con Claude Code

**Fecha:** 2026-06-23
**Categoría:** ia
**Tags:** ia-local, linux, codigo
**Título original:** Porting the Moebius 0.2B image inpainting model to run in the browser with Claude Code

---

## Introducción

Un desarrollador ha logrado portar un modelo de relleno de imágenes a un navegador web utilizando Claude Code y WebGPU. Esto permite que los usuarios puedan utilizar la tecnología de relleno de imágenes en sus navegadores sin necesidad de software específico.

## ¿Qué es?

Moebius es un framework de relleno de imágenes ligero que utiliza un modelo de 10B-Level para rellenar áreas de una imagen. El modelo requiere PyTorch y NVIDIA CUDA para funcionar, pero el desarrollador ha logrado portarlo a un navegador web utilizando Claude Code y WebGPU.

## ¿Cómo funciona?

El desarrollador utilizó Claude Code para preguntar sobre la viabilidad del proyecto y luego utilizó WebGPU para crear una implementación del modelo de relleno de imágenes en el navegador. El modelo utiliza ONNX Runtime Web en el backend de WebGPU para funcionar.

## ¿Por qué importa?

Este proyecto es importante porque permite que los usuarios puedan utilizar la tecnología de relleno de imágenes en sus navegadores web sin necesidad de software específico. Esto abre nuevas posibilidades para aplicaciones de relleno de imágenes en línea.

## Consejo técnico

Si deseas portar un modelo de IA a un navegador web, considera utilizar Claude Code y WebGPU como herramientas para facilitar el proceso. Asegúrate de investigar sobre ONNX Runtime Web y cómo utilizarlo en tu proyecto.

```bash
ONNX Runtime Web
```

---

**Fuente original:** [https://simonwillison.net/2026/Jun/22/porting-moebius/#atom-everything](https://simonwillison.net/2026/Jun/22/porting-moebius/#atom-everything)
