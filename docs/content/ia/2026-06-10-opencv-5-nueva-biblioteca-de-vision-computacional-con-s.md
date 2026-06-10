# OpenCV 5: Nueva biblioteca de visión computacional con soporte para LLM/VLM

**Fecha:** 2026-06-10
**Categoría:** ia
**Tags:** ia-local, python, librerias
**Título original:** OpenCV 5 release – New DNN engine with enhanced ONNX and LLM/VLM support, Intel, Arm, and RISC-V hardware optimizations

---

## Introducción

La biblioteca de visión computacional OpenCV 5 ha sido lanzada con una nueva motor de redes neuronales que ofrece mejor cobertura de ONNX y soporte para modelos de lenguaje y visión. Esto significa que los modelos con formas dinámicas que fallaban en OpenCV 4.x deberían funcionar ahora.

## ¿Qué es?

OpenCV 5 es una biblioteca de visión computacional open-source que ofrece una variedad de herramientas y algoritmos para la visión computacional. La nueva versión incluye un motor de redes neuronales mejorado que ofrece mejor cobertura de ONNX y soporte para modelos de lenguaje y visión.

## ¿Cómo funciona?

El motor de redes neuronales de OpenCV 5 utiliza un gráfico de operaciones tipo que permite analizar y optimizar las redes neuronales. Esto permite que las redes neuronales con formas dinámicas funcionen correctamente y que se aprovechen al máximo las capacidades de hardware de los sistemas.

## ¿Por qué importa?

La nueva versión de OpenCV 5 es importante porque ofrece mejor cobertura de ONNX y soporte para modelos de lenguaje y visión. Esto significa que los desarrolladores pueden utilizar OpenCV para crear aplicaciones que utilicen modelos de lenguaje y visión, lo que puede ser útil en una variedad de campos, como la visión por computadora, la inteligencia artificial y la automatización.

## Consejo técnico

Si deseas aprovechar al máximo las capacidades de OpenCV 5, asegúrate de configurar tu proyecto con la opción ENGINE_AUTO, que intenta utilizar el motor de redes neuronales nuevo y cae en el clásico si el modelo falla a cargar.

```bash
ENGINE_AUTO
```

---

**Fuente original:** [https://www.cnx-software.com/2026/06/10/opencv-5-release-new-dnn-engine-with-enhanced-onnx-and-llm-vlm-support-intel-arm-and-risc-v-hardware-optimizations/](https://www.cnx-software.com/2026/06/10/opencv-5-release-new-dnn-engine-with-enhanced-onnx-and-llm-vlm-support-intel-arm-and-risc-v-hardware-optimizations/)
