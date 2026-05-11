# EMO: un modelo de IA que emerge la modularidad de forma autónoma

**Fecha:** 2026-05-11
**Categoría:** ia
**Tags:** llms, ia-local, python
**Título original:** EMO: Pretraining mixture of experts for emergent modularity

---

## Introducción

Los modelos de lenguaje grandes suelen ser monolíticos, pero las aplicaciones a menudo necesitan solo una pequeña parte de sus capacidades. El nuevo modelo EMO de Allen AI permite utilizar solo una pequeña parte de sus expertos para una tarea específica sin perder rendimiento.

## ¿Qué es?

EMO es un modelo de IA que utiliza una técnica llamada 'mixture of experts' (MoE) para dividir su estructura en pequeños expertos que se activan solo para inputs específicos. Esto permite utilizar solo una pequeña parte de los expertos para una tarea específica sin perder rendimiento.

## ¿Cómo funciona?

EMO utiliza una arquitectura MoE que consta de múltiples expertos pequeños que se activan solo para inputs específicos. Los expertos se dividen en grupos coherentes que pueden ser utilizados de forma selectiva y compuesta. El modelo se preentrena de forma end-to-end para que la estructura modular emerja directamente de los datos sin depender de prioridades humanas.

## ¿Por qué importa?

EMO es importante porque permite utilizar solo una pequeña parte de los expertos de un modelo de IA grande para una tarea específica sin perder rendimiento. Esto reduce el costo computacional y de memoria necesarios para utilizar el modelo completo.

## Consejo técnico

Si deseas utilizar EMO en tu proyecto, puedes comenzar explorando la colección de modelos en Hugging Face y la documentación de Allen AI. Puedes utilizar la biblioteca PyTorch para entrenar y utilizar el modelo.

```bash
pip install transformers
```

---

**Fuente original:** [https://huggingface.co/blog/allenai/emo](https://huggingface.co/blog/allenai/emo)
