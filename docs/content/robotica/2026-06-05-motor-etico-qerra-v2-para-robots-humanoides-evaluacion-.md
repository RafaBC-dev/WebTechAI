# Motor ético QERRA-v2 para robots humanoides: evaluación explicada

**Fecha:** 2026-06-05
**Categoría:** robotica
**Tags:** robotica, ia-local, python
**Título original:** QERRA-v2 Classical: Explainable Ethical Safety Gates & Behavior Tree Integration (v2.0.0-alpha)

---

## Introducción

Un equipo de investigación ha desarrollado un motor ético para robots humanoides que evalúa las acciones de manera explicada. Este sistema es crucial para garantizar la seguridad y la ética en la toma de decisiones de los robots.

## ¿Qué es?

QERRA-v2 es un motor ético clásico diseñado para evaluar las acciones de robots humanoides de manera explicada. Se basa en el marco SEMEV-12, que considera 12 vectores éticos. Su objetivo es actuar como una 'puerta de seguridad' en la ejecución de tareas de los robots.

## ¿Cómo funciona?

QERRA-v2 utiliza un servidor de acción no bloqueante con un tiempo límite de latencia de 800ms. Si el llamado a la API remota supera este tiempo, el sistema se reemplaza por una evaluación local en el CPU. La evaluación se realiza utilizando SentenceTransformers en el CPU, lo que reduce el tiempo de ejecución a ~31ms.

## ¿Por qué importa?

Este motor ético es crucial para garantizar la seguridad y la ética en la toma de decisiones de los robots humanoides. Permite evaluar las acciones de manera explicada y prevenir errores que puedan causar daños a personas o propiedades.

## Consejo técnico

Si deseas integrar QERRA-v2 en tu proyecto de robótica, asegúrate de utilizar la biblioteca PyTrees para implementar un nodo de condición de comportamiento no bloqueante.

```bash
ros2_bridge.py
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/qerra-v2-classical-explainable-ethical-safety-gates-behavior-tree-integration-v2-0-0-alpha/55281](https://discourse.openrobotics.org/t/qerra-v2-classical-explainable-ethical-safety-gates-behavior-tree-integration-v2-0-0-alpha/55281)
