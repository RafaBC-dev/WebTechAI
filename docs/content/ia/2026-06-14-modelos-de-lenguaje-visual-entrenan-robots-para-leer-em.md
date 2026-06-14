# Modelos de lenguaje visual entrenan robots para leer emociones humanas

**Fecha:** 2026-06-14
**Categoría:** ia
**Tags:** robotica, ia-local, benchmarks
**Título original:** Visual Language Models Train Robots to Read Human Emotions

---

## Introducción

Los robots pueden ser más efectivos al trabajar con humanos si pueden leer sus emociones. Un estudio reciente ha entrenado robots para reconocer emociones humanas mediante la combinación de expresiones faciales y factores contextuales.

## ¿Qué es?

Los investigadores han entrenado un robot para leer emociones humanas utilizando un modelo de visión de lenguaje (VLM). El VLM es similar a los modelos de lenguaje grandes, como ChatGPT, pero puede procesar entradas visuales. Los investigadores entrenaron el VLM para que reconociera emociones humanas en videos de robots interactuando con humanos.

## ¿Cómo funciona?

El VLM se entrenó utilizando videos de robots interactuando con humanos. Los voluntarios describieron las emociones expresadas por los humanos en los videos, teniendo en cuenta factores contextuales, como la postura y el lenguaje corporal. El VLM luego fue comparado con un sistema de inteligencia artificial convencional que solo se basaba en expresiones faciales.

## ¿Por qué importa?

Este estudio es importante porque muestra que los robots pueden ser más efectivos al trabajar con humanos si pueden leer sus emociones. Esto puede mejorar la colaboración y la comunicación entre humanos y robots en entornos de trabajo y en la vida cotidiana.

## Consejo técnico

Si deseas entrenar un modelo de visión de lenguaje para reconocer emociones humanas, puedes utilizar la biblioteca OpenCV para procesar imágenes y la biblioteca TensorFlow para entrenar el modelo.

```bash
python -m tensorflow_model_server --port=9000 --model_config_path=model_config.json
```

---

**Fuente original:** [https://spectrum.ieee.org/robot-emotions-visual-language-models](https://spectrum.ieee.org/robot-emotions-visual-language-models)
