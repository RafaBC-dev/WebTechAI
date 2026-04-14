# Transformadores de oraciones: multimodalidad y reordenación de modelos

**Fecha:** 2026-04-14
**Categoría:** ia
**Tags:** ia-local, librerias, herramientas
**Título original:** Multimodal Embedding & Reranker Models with Sentence Transformers

---

## Introducción

La biblioteca Sentence Transformers ha lanzado una actualización importante que permite codificar y comparar textos, imágenes, audio y videos utilizando la misma API. Esto abre nuevas posibilidades para aplicaciones como búsqueda semántica, recuperación de información y más.

## ¿Qué es?

Los modelos multimodales son una extensión de los modelos de embebedad tradicionales, que convierten textos en vectores fijos. Los modelos multimodales mapean entradas de diferentes modalidades (texto, imágenes, audio o video) en un espacio de embebedad compartido, lo que permite comparar textos con imágenes o viceversa.

## ¿Cómo funciona?

Para utilizar los modelos multimodales, se requiere instalar las dependencias extras para las modalidades necesarias. Luego, se puede cargar un modelo, codificar imágenes y comparar textos e imágenes utilizando la misma función de similitud. Los modelos reranker pueden evaluar la relevancia de pares mixtos de modalidades.

## ¿Por qué importa?

Los modelos multimodales abren nuevas posibilidades para aplicaciones como la búsqueda visual de documentos, la búsqueda cruz-modal y las pipinas de RAG multimodales. Esto puede mejorar la eficiencia y la precisión en tareas de recuperación de información y búsqueda semántica.

## Consejo técnico

Si deseas utilizar los modelos multimodales de Sentence Transformers, instala las dependencias extras para las modalidades necesarias utilizando pip: `pip install -U sentence-transformers[image]` o `pip install -U sentence-transformers[audio]`.

```bash
pip install -U sentence-transformers[image]
```

---

**Fuente original:** [https://huggingface.co/blog/multimodal-sentence-transformers](https://huggingface.co/blog/multimodal-sentence-transformers)
