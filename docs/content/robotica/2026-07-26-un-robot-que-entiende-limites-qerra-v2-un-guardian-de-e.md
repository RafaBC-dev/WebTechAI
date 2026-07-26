# Un robot que entiende límites: QERRA-v2, un guardián de ejecución moral

**Fecha:** 2026-07-26
**Categoría:** robotica
**Tags:** robotica, ia-local, linux
**Título original:** QERRA-v2: Implementing a Moral-Boundary Execution Guard in Webots (TIAGo AMR)

---

## Introducción

Un equipo de investigación ha creado un sistema de seguridad para robots que va más allá de evitar obstáculos físicos. QERRA-v2 es un sistema que evalúa la intención detrás de las instrucciones de un humano y bloquea la ejecución si se cruzan límites morales.

## ¿Qué es?

QERRA-v2 es un sistema de seguridad para robots que evalúa la intención detrás de las instrucciones de un humano. Utiliza una evaluación de semántica local para calcular un puntaje de riesgo antes de permitir la ejecución de una tarea. Si el puntaje de riesgo es alto, el sistema bloquea la ejecución y comunica el rechazo al robot.

## ¿Cómo funciona?

QERRA-v2 está compuesto por dos capas de evaluación: la capa de evaluación moral y la capa de seguridad física. La capa de evaluación moral utiliza una biblioteca de sentencias transformadoras para calcular un puntaje de riesgo basado en 12 vectores inmutables. Si el puntaje de riesgo es alto, la capa de seguridad física se activa y bloquea la ejecución del robot.

## ¿Por qué importa?

QERRA-v2 es importante porque permite a los robots entender límites morales y evitar situaciones peligrosas. Esto es especialmente relevante en entornos de trabajo donde los robots interactúan con humanos y pueden estar expuestos a presiones o instrucciones peligrosas.

## Consejo técnico

Si deseas implementar un sistema de seguridad similar en tu propio proyecto de robotica, considera utilizar la biblioteca de sentencias transformadoras 'sentence-transformers' para calcular un puntaje de riesgo basado en la intención detrás de las instrucciones de un humano.

```bash
pip install sentence-transformers
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/qerra-v2-implementing-a-moral-boundary-execution-guard-in-webots-tiago-amr/56956](https://discourse.openrobotics.org/t/qerra-v2-implementing-a-moral-boundary-execution-guard-in-webots-tiago-amr/56956)
