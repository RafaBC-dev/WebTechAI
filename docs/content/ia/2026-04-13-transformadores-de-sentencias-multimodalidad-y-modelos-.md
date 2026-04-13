# Transformadores de Sentencias: multimodalidad y modelos de reordenación

**Fecha:** 2026-04-13
**Categoría:** ia
**Tags:** ia-local, librerias, python
**Título original:** Multimodal Embedding & Reranker Models with Sentence Transformers

---

## Introducción

La biblioteca de transformadores de sentencias ha lanzado una actualización significativa que permite la codificación y comparación de textos, imágenes, audio y videos utilizando la misma API familiar. Esto abre nuevas posibilidades para aplicaciones como la búsqueda semántica y la generación de texto basada en la recuperación.

## ¿Qué es?

Los modelos multimodales de codificación y reordenación son una extensión de los modelos de codificación tradicionales, que convierten textos en vectores de tamaño fijo. Los modelos multimodales mapean entradas de diferentes modalidades (texto, imágenes, audio o video) en un espacio de codificación compartido, permitiendo comparar textos con imágenes o viceversa utilizando funciones de similitud conocidas.

## ¿Cómo funciona?

Para utilizar los modelos multimodales, es necesario instalar las dependencias adicionales para las modalidades necesarias. Luego, se pueden cargar modelos, codificar imágenes y comparar textos con imágenes utilizando la misma API. Los modelos de reordenación multimodales pueden evaluar la relevancia de pares de elementos mixtos de modalidades.

## ¿Por qué importa?

Esto importa porque permite aplicaciones como la búsqueda visual de documentos, la búsqueda transmodal y las pipelines de RAG (Retrieval-Augmented Generation) que funcionan en diferentes modalidades.

## Consejo técnico

Instala las dependencias adicionales para las modalidades necesarias utilizando pip, por ejemplo: `pip install -U sentence-transformers[image]`.

```bash
pip install -U sentence-transformers[image]
```

---

**Fuente original:** [https://huggingface.co/blog/multimodal-sentence-transformers](https://huggingface.co/blog/multimodal-sentence-transformers)
