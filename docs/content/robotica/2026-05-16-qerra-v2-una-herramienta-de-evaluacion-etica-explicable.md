# QERRA-v2: una herramienta de evaluación ética explicable para robots

**Fecha:** 2026-05-16
**Categoría:** robotica
**Tags:** robotica, linux, codigo
**Título original:** QERRA-v2 Classical — Explainable Ethical Scoring Engine with ROS 2 Bridge (open for feedback)

---

## Introducción

Un equipo de desarrolladores ha creado QERRA-v2, una herramienta de evaluación ética que utiliza 12 vectores centrados en el ser humano para evaluar la conducta de robots. Esta herramienta es especialmente útil en entornos de robótica y automatización.

## ¿Qué es?

QERRA-v2 es una herramienta de evaluación ética que utiliza 12 vectores centrados en el ser humano para evaluar la conducta de robots. Estos vectores se basan en principios éticos como la autonomía, la seguridad y la privacidad. La herramienta es 100% clásica, es decir, no utiliza redes neuronales y devuelve puntuaciones y razonamientos transparentes.

## ¿Cómo funciona?

QERRA-v2 se basa en la arquitectura SEMEV-12, que utiliza 12 vectores para evaluar la conducta de robots. La herramienta utiliza un puente ROS 2 para conectar con entornos de robótica y automatización. El puente se puede ejecutar de manera independiente o como un nodo completo que se suscribe a un tema de entrada y publica la puntuación, la decisión y el resultado completo de SEMEV-12.

## ¿Por qué importa?

QERRA-v2 es importante porque permite a los desarrolladores de robots evaluar la conducta de sus creaciones de manera ética y transparente. Esto es especialmente útil en entornos de robótica y automatización donde la seguridad y la privacidad son fundamentales.

## Consejo técnico

Si deseas utilizar QERRA-v2 en tu proyecto de robótica, asegúrate de revisar la documentación de SEMEV-12 y de configurar correctamente el puente ROS 2. Además, es recomendable que revises la documentación de ROS 2 para entender cómo funciona el puente y cómo integrarlo en tu proyecto.

```bash
ros2_bridge.py
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/qerra-v2-classical-explainable-ethical-scoring-engine-with-ros-2-bridge-open-for-feedback/54904](https://discourse.openrobotics.org/t/qerra-v2-classical-explainable-ethical-scoring-engine-with-ros-2-bridge-open-for-feedback/54904)
