# Mejora tus modelos multimodales con Sentence Transformers

**Fecha:** 2026-04-17
**Categoría:** ia
**Tags:** ia-local, librerias, herramientas
**Título original:** Training and Finetuning Multimodal Embedding & Reranker Models with Sentence Transformers

---

## Introducción

La biblioteca Sentence Transformers ha lanzado una nueva versión con capacidades multimodales. Ahora puedes entrenar y fine-tune modelos que integren texto, imágenes, audio y video. Esto abre nuevas posibilidades para aplicaciones como la búsqueda semántica y la generación de texto basada en la recuperación.

## ¿Qué es?

Sentence Transformers es una biblioteca de Python para entrenar y utilizar modelos de embebedding y reranker. Estos modelos pueden manejar texto, imágenes, audio y video, y se pueden utilizar en aplicaciones como la búsqueda semántica y la generación de texto basada en la recuperación.

## ¿Cómo funciona?

Los modelos multimodales de Sentence Transformers se entrenan con una combinación de texto y multimodalidad. Puedes entrenar modelos que integren texto e imágenes, o modelos que integren texto, imágenes y audio. La biblioteca proporciona herramientas para entrenar y fine-tune estos modelos en tu propio datasets.

## ¿Por qué importa?

La capacidad de entrenar y fine-tune modelos multimodales es importante porque permite a los desarrolladores crear aplicaciones más avanzadas y personalizadas. Puedes entrenar modelos que se adapten a tus necesidades específicas y que puedan manejar diferentes tipos de datos.

## Consejo técnico

Si deseas entrenar un modelo multimodal con Sentence Transformers, recomiendo utilizar la función de fine-tuning para adaptar el modelo a tu propio dataset. Puedes utilizar la herramienta `CachedMultipleNegativesRankingLoss` para entrenar el modelo con una función de pérdida personalizada.

```bash
python -m sentence_transformers.train --model-name Qwen/Qwen3-VL-Embedding-2B --dataset-path /path/to/your/dataset --loss-function CachedMultipleNegativesRankingLoss
```

---

**Fuente original:** [https://huggingface.co/blog/train-multimodal-sentence-transformers](https://huggingface.co/blog/train-multimodal-sentence-transformers)
