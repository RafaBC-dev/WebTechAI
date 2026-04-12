# Aprende en el trabajo: ALTK-Evolve revoluciona la inteligencia artificial

**Fecha:** 2026-04-12
**Categoría:** ia
**Tags:** ia-local, agentes, benchmarks
**Título original:** ALTK‑Evolve: On‑the‑Job Learning for AI Agents

---

## Introducción

La mayoría de los agentes de inteligencia artificial repiten errores y no transfieren lecciones a nuevas situaciones debido a que se basan en transcripciones en lugar de aprender principios. ALTK-Evolve cambia esto.

## ¿Qué es?

ALTK-Evolve es un sistema de memoria a largo plazo para agentes de inteligencia artificial que puede ayudar a los agentes a mejorar con el tiempo, aprendiendo de y utilizando pautas generadas a partir de ejecuciones previas.

## ¿Cómo funciona?

El sistema funciona como un ciclo continuo que captura trayectorias completas de agentes (declaraciones de usuario, pensamientos, llamadas a herramientas, resultados) en una capa de interacción (por ejemplo, Langfuse o otra herramienta de observabilidad basada en OpenTelemetry). Los extractores pluggables minan las trazas para patrones estructurales y las persisten como entidades candidatas.

## ¿Por qué importa?

ALTK-Evolve puede mejorar la confiabilidad de los agentes, especialmente en tareas complejas, sin aumentar la complejidad del contexto. Esto es especialmente importante en aplicaciones críticas como la aviación, donde la capacidad de los agentes para aprender y adaptarse es fundamental.

## Consejo técnico

Para implementar ALTK-Evolve en tu proyecto de inteligencia artificial, considera utilizar herramientas de observabilidad como Langfuse o OpenTelemetry para capturar trayectorias de agentes y extracciones pluggables para identificar patrones estructurales.

```bash
Langfuse o OpenTelemetry para capturar trayectorias de agentes
```

---

**Fuente original:** [https://huggingface.co/blog/ibm-research/altk-evolve](https://huggingface.co/blog/ibm-research/altk-evolve)
