# Navegación semántica en la frontera con AMD Strix Halo

**Fecha:** 2026-07-17
**Categoría:** robotica
**Tags:** robotica, ia-local, linux
**Título original:** [Nav2] AMD Strix Halo Based SAM3 Semantic Navigation

---

## Introducción

AMD y Meta han desarrollado una tecnología de navegación semántica que permite a los robots navegar en entornos complejos con precisión y seguridad. Esta tecnología utiliza el modelo SAM3 de Meta y se ejecuta en la GPU del AMD Strix Halo.

## ¿Qué es?

La navegación semántica es una técnica que permite a los robots identificar y navegar en diferentes tipos de superficies y obstáculos en un entorno. En este caso, el modelo SAM3 de Meta es capaz de segmentar el entorno en diferentes clases, como pisos, aceras, cables, personas y pallets, y proporcionar máscaras de píxeles para cada clase. Esto permite a los robots tomar decisiones de comportamiento basadas en lo que realmente ven en el entorno.

## ¿Cómo funciona?

El modelo SAM3 de Meta se ejecuta en la GPU del AMD Strix Halo, que proporciona una gran potencia de procesamiento para la segmentación del entorno. El modelo utiliza textos de instrucción para segmentar el entorno y proporcionar máscaras de píxeles para cada clase. El resultado se integra con la pila de planificación y costmap de Nav2 para permitir a los robots navegar en el entorno de manera segura y precisa.

## ¿Por qué importa?

Esta tecnología es importante porque permite a los robots navegar en entornos complejos con precisión y seguridad. Esto tiene aplicaciones en la automatización de procesos industriales, la logística y la exploración espacial, entre otros. Además, la capacidad de segmentar el entorno en diferentes clases permite a los robots tomar decisiones de comportamiento más informadas y adaptarse mejor a los cambios en el entorno.

## Consejo técnico

Si deseas experimentar con la navegación semántica en tu propio proyecto de robótica, puedes descargar el código abierto y seguir el tutorial proporcionado en el blog de Meta. También puedes utilizar la biblioteca de segmentación de Meta para integrar la navegación semántica en tu propio código.

```bash
python -m pip install meta-ai-sam3
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/nav2-amd-strix-halo-based-sam3-semantic-navigation/56703](https://discourse.openrobotics.org/t/nav2-amd-strix-halo-based-sam3-semantic-navigation/56703)
