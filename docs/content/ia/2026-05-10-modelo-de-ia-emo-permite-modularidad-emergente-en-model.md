# Modelo de IA EMO permite modularidad emergente en modelos de lenguaje

**Fecha:** 2026-05-10
**Categoría:** ia
**Tags:** llms, ia-local, benchmarks
**Título original:** EMO: Pretraining mixture of experts for emergent modularity

---

## Introducción

Los modelos de lenguaje grandes suelen ser sistemas monolíticos que requieren recursos intensivos, pero un nuevo modelo llamado EMO permite modularidad emergente, lo que reduce el costo computacional y permite usar solo una parte del modelo para tareas específicas.

## ¿Qué es?

EMO es un modelo de lenguaje que utiliza una mezcla de expertos (MoE) para permitir que la estructura modular emerja directamente de los datos sin depender de prioridades humanas. Esto significa que los expertos se organizan en grupos coherentes que pueden ser seleccionados y utilizados de manera independiente.

## ¿Cómo funciona?

EMO funciona entrenando una red neuronal con múltiples expertos que se activan solo para tokens específicos. Los expertos se organizan en grupos coherentes que pueden ser seleccionados y utilizados de manera independiente. El modelo se preentrena con una ruta de tokens a expertos basada en dominios semánticos predefinidos.

## ¿Por qué importa?

EMO importa porque permite reducir el costo computacional y permitir el uso de solo una parte del modelo para tareas específicas. Esto es especialmente útil para aplicaciones que requieren solo una pequeña parte de la capacidad del modelo. Además, EMO puede utilizarse como un modelo generalista fuerte cuando se utilizan todos los expertos juntos.

## Consejo técnico

Si deseas reducir el costo computacional de tus modelos de lenguaje, prueba EMO y selecciona solo los expertos necesarios para tu tarea específica. Puedes encontrar el código de EMO en GitHub y visualizar las características del modelo en emovisualization.netlify.app.

```bash
git clone https://github.com/allenai/EMO
```

---

**Fuente original:** [https://huggingface.co/blog/allenai/emo](https://huggingface.co/blog/allenai/emo)
