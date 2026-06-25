# Control de robots con lenguaje natural a través de MCP

**Fecha:** 2026-06-25
**Categoría:** ia
**Tags:** llms, robotica, linux
**Título original:** Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP)

---

## Introducción

La comunidad de Open-RMF se reunirá para presentar una forma innovadora de controlar flotas de robots mediante comandos en lenguaje natural. Este avance podría revolucionar la forma en que interactuamos con los robots en entornos como almacenes y fábricas.

## ¿Qué es?

El Model Context Protocol (MCP) es una tecnología que permite a los sistemas de inteligencia artificial (IA) interactuar con otros sistemas y aplicaciones de manera más flexible y natural. En este caso, se está utilizando MCP para controlar flotas de robots en entornos de Open-RMF, permitiendo a los usuarios dar comandos en lenguaje natural para que los robots realicen tareas específicas.

## ¿Cómo funciona?

El sistema utiliza un servidor MCP que expone la API de Open-RMF como herramientas llamables por los modelos de lenguaje (LLMs). Luego, un agente convierte los comandos en lenguaje natural en misiones de varios pasos que se envían a Open-RMF, que las ejecuta en un robot simulado en NVIDIA Isaac Sim. El resultado se visualiza en RViz.

## ¿Por qué importa?

Este avance es importante porque permite a los usuarios interactuar con los robots de manera más natural y flexible, lo que podría mejorar la eficiencia y la seguridad en entornos como almacenes y fábricas. Además, podría abrir nuevas posibilidades para la integración de IA y robótica en diferentes industrias.

## Consejo técnico

Si deseas experimentar con MCP y Open-RMF, puedes empezar a explorar la documentación de Open-RMF y MCP para ver cómo se pueden integrar los modelos de lenguaje (LLMs) con la API de Open-RMF. Puedes empezar con un proyecto simple, como controlar un robot simulado en NVIDIA Isaac Sim.

```bash
python -m openrmf.mcp.server
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687](https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687)
