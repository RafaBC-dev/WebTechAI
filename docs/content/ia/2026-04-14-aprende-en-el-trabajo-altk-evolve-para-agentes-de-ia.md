# Aprende en el trabajo: ALTK-Evolve para agentes de IA

**Fecha:** 2026-04-14
**Categoría:** ia
**Tags:** ia-local, agentes, benchmarks
**Título original:** ALTK‑Evolve: On‑the‑Job Learning for AI Agents

---

## Introducción

Los agentes de IA repiten errores y no transfieren lecciones a nuevas situaciones debido a su incapacidad para aprender principios. ALTK-Evolve cambia esto.

## ¿Qué es?

ALTK-Evolve es un sistema de memoria a largo plazo para agentes de IA que les permite aprender de sus experiencias y aplicar principios a nuevas situaciones. Convierte las trazas de interacción en directrices reutilizables y filtra la información para inyectar solo la guía relevante en el momento de la acción.

## ¿Cómo funciona?

ALTK-Evolve funciona como un ciclo continuo: captura las trazas de interacción del agente, extrae patrones estructurales y persiste los candidatos como entidades. Utiliza una capa de interacción para capturar información como declaraciones del usuario, pensamientos, llamadas a herramientas y resultados.

## ¿Por qué importa?

ALTK-Evolve resuelve el problema de que los agentes de IA no acumulan sabiduría sobre el entorno y no pueden generalizar de sus experiencias. Esto es especialmente importante en tareas complejas y multi-pasos, donde la precisión y la adaptabilidad son cruciales.

## Consejo técnico

Para implementar ALTK-Evolve en tus proyectos de IA, considera utilizar herramientas de observabilidad como Langfuse o OpenTelemetry para capturar información de las trazas de interacción y extraer patrones estructurales.

```bash
langfuse
```

---

**Fuente original:** [https://huggingface.co/blog/ibm-research/altk-evolve](https://huggingface.co/blog/ibm-research/altk-evolve)
