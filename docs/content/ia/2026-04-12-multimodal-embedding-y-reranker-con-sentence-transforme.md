# Multimodal Embedding y Reranker con Sentence Transformers

**Fecha:** 2026-04-12
**Categoría:** ia
**Tags:** ia-local, librerias, linux, codigo
**Título original:** Multimodal Embedding & Reranker Models with Sentence Transformers

---

## Introducción

La biblioteca Sentence Transformers ha lanzado una actualización significativa que permite a los desarrolladores trabajar con multimodalidad, es decir, con textos, imágenes, audio y videos, utilizando la misma API. Esto abre nuevas posibilidades para aplicaciones como la búsqueda semántica y la generación de texto basada en la recuperación.

## ¿Qué es?

Los modelos multimodales son una extensión de los modelos de embebedad tradicionales, que convierten textos en vectores fijos. Los modelos multimodales mapean entradas de diferentes modalidades (textos, imágenes, audio, o video) en un espacio de embebedad compartido, permitiendo comparar textos con imágenes o viceversa utilizando las mismas funciones de similitud.

## ¿Cómo funciona?

Para trabajar con multimodalidad, se requieren algunas dependencias adicionales. Se pueden instalar las extras para las modalidades necesarias utilizando pip, por ejemplo, para soporte de imágenes se puede instalar 'sentence-transformers[image]'. Los modelos multimodales pueden ser utilizados para tareas como la búsqueda visual de documentos, la búsqueda cruz-modal y las pipelines de RAG multimodal.

## ¿Por qué importa?

Esta actualización es importante porque permite a los desarrolladores trabajar con multimodalidad de manera más sencilla y eficiente, abriendo nuevas posibilidades para aplicaciones como la búsqueda semántica y la generación de texto basada en la recuperación.

## Consejo técnico

Si deseas trabajar con multimodalidad, instala las extras necesarias utilizando pip y comienza a experimentar con los modelos multimodales de Sentence Transformers.

```bash
pip install -U 'sentence-transformers[image]'
```

---

**Fuente original:** [https://huggingface.co/blog/multimodal-sentence-transformers](https://huggingface.co/blog/multimodal-sentence-transformers)
