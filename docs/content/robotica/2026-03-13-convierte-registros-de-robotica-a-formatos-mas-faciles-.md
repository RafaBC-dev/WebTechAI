# Convierte registros de robótica a formatos más fáciles de trabajar

**Fecha:** 2026-03-13
**Categoría:** robotica
**Tags:** python, librerias, herramientas
**Título original:** Hephaes: Open-source ROS1/2 Logs to Parquet/TFRecord converter

---

## Introducción

Un proyecto de código abierto llamado Hephaes ha sido creado para simplificar la conversión de registros de robótica a formatos más fáciles de analizar y procesar. Esto puede ser especialmente útil para desarrolladores de robótica que trabajan con grandes cantidades de datos.

## ¿Qué es?

Hephaes es un paquete de código abierto de Python diseñado para convertir registros de robótica de formatos como bag/mcap a formatos más fáciles de trabajar, como Parquet y TFRecord. Estos formatos son ideales para la análisis y procesamiento de datos, y también son compatibles con pipelines de aprendizaje automático de TensorFlow.

## ¿Cómo funciona?

El paquete Hephaes utiliza Python para leer registros de robótica en formatos como bag/mcap y convertirlos a Parquet y TFRecord. Además, genera un archivo manifest.json que actúa como una capa de indexación básica para mantener el seguimiento de los resultados y la metadata. Está planeado expandir esta función con características como etiquetado basado en VLM y soporte para la conversión de datos en vivo desde ROS.

## ¿Por qué importa?

Hephaes puede ser una herramienta valiosa para desarrolladores de robótica que necesitan analizar y procesar grandes cantidades de datos. Al convertir registros de robótica a formatos más fáciles de trabajar, Hephaes puede ayudar a acelerar el desarrollo de aplicaciones de robótica y mejorar la eficiencia en la industria.

## Consejo técnico

Si estás trabajando con registros de robótica y necesitas convertirlos a formatos más fáciles de analizar, considera utilizar Hephaes. Puedes instalar el paquete desde PyPI y comenzar a trabajar con él de inmediato.

```bash
pip install hephaes
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/hephaes-open-source-ros1-2-logs-to-parquet-tfrecord-converter/53181](https://discourse.openrobotics.org/t/hephaes-open-source-ros1-2-logs-to-parquet-tfrecord-converter/53181)
