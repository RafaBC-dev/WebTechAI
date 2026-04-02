# Mejoras en el controlador de GPU AMD para Linux 7.1

**Fecha:** 2026-04-02
**Categoría:** linux
**Tags:** linux, gpu, amd
**Título original:** AMD GPU Driver Sees DC Idle Manager & Multi-SDMA Engine Optimization For Linux 7.1

---

## Introducción

El controlador de GPU AMD ha visto importantes mejoras con la inclusión de un administrador de estado de inactividad DC y un motor de múltiples SDMA para Linux 7.1. Estas mejoras buscan mejorar el rendimiento y la eficiencia en escenarios de uso intensivo de gráficos.

## ¿Qué es?

El controlador de GPU AMD es un software de código abierto que permite a los usuarios de Linux aprovechar al máximo la potencia de sus tarjetas gráficas AMD. El administrador de estado de inactividad DC es un componente que ayuda a reducir el consumo de energía en situaciones de inactividad, mientras que el motor de múltiples SDMA permite a los usuarios aprovechar la capacidad de múltiples motores de copia de la tarjeta gráfica para realizar tareas de llenado y limpieza de buffers de manera más eficiente.

## ¿Cómo funciona?

El administrador de estado de inactividad DC utiliza un mecanismo de histeresis para determinar si se debe insertar un retraso en la transición entre estados de inactividad para evitar un consumo de energía negativo. El motor de múltiples SDMA, por otro lado, utiliza un algoritmo de programación circular para asignar tareas de llenado y limpieza de buffers a los diferentes motores de copia de la tarjeta gráfica de manera eficiente.

## ¿Por qué importa?

Estas mejoras son importantes porque permiten a los usuarios de Linux aprovechar al máximo la potencia de sus tarjetas gráficas AMD, especialmente en escenarios de uso intensivo de gráficos. También ayudan a reducir el consumo de energía y mejorar la eficiencia en situaciones de inactividad.

## Consejo técnico

Si deseas aprovechar las mejoras del motor de múltiples SDMA, asegúrate de actualizar tu controlador de GPU AMD a la versión más reciente y configurar el algoritmo de programación circular en tu sistema.

```bash
sudo apt-get update && sudo apt-get install libdrm-amdgpu1
```

---

**Fuente original:** [https://www.phoronix.com/news/AMDGPU-Linux-7.1-Multi-SDMA](https://www.phoronix.com/news/AMDGPU-Linux-7.1-Multi-SDMA)
