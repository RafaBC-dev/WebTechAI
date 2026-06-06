# QERRA-v2: Evaluador Ético Expliquible para Robótica Humanoide

**Fecha:** 2026-06-06
**Categoría:** robotica
**Tags:** robotica, ia-local, python
**Título original:** QERRA-v2 Classical: Explainable Ethical Safety Gates & Behavior Tree Integration (v2.0.0-alpha)

---

## Introducción

Un equipo de investigación ha desarrollado QERRA-v2, un evaluador ético expliquible para robots humanoides que ayuda a tomar decisiones seguras y éticas. Este proyecto es crucial para la robótica avanzada y la IA.

## ¿Qué es?

QERRA-v2 es un evaluador ético expliquible diseñado para robots humanoides que evalúa decisiones en tiempo real mediante un marco de 12 vectores éticos (SEMEV-12). Este sistema actúa como una 'puerta de seguridad ética' en la ejecución de tareas robóticas.

## ¿Cómo funciona?

QERRA-v2 utiliza un servidor de acción no bloqueante (ros2_bridge.py) que evalúa decisiones en tiempo real. Si la llamada a una API remota excede los 800ms, el sistema se reemplaza por una evaluación local en el CPU. También integra un árbol de comportamiento (qerra_condition_node.py) que actúa como una puerta de seguridad ética antes de que el robot realice una acción.

## ¿Por qué importa?

QERRA-v2 es importante porque resuelve problemas de seguridad y ética en la robótica avanzada. Ayuda a los robots humanoides a tomar decisiones seguras y éticas en tiempo real, lo que reduce el riesgo de accidentes y daños.

## Consejo técnico

Si estás desarrollando un proyecto de robótica, considera utilizar QERRA-v2 para evaluar decisiones éticas en tiempo real. Puedes utilizar la herramienta de evaluación de SEMEV-12 para integrarla en tu proyecto.

```bash
ros2_bridge.py
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/qerra-v2-classical-explainable-ethical-safety-gates-behavior-tree-integration-v2-0-0-alpha/55281](https://discourse.openrobotics.org/t/qerra-v2-classical-explainable-ethical-safety-gates-behavior-tree-integration-v2-0-0-alpha/55281)
