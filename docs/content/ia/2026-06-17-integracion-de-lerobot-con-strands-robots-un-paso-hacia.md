# Integración de LeRobot con Strands Robots: un paso hacia la robótica autónoma

**Fecha:** 2026-06-17
**Categoría:** ia
**Tags:** robotica, ia-local, herramientas
**Título original:** From the Hugging Face Hub to robot hardware with Strands Agents and LeRobot

---

## Introducción

La integración de LeRobot con Strands Robots permite a los desarrolladores crear agentes de robótica autónoma que pueden aprender y adaptarse en entornos reales. Esto abre nuevas posibilidades para la automatización y la robótica en diversas industrias.

## ¿Qué es?

Strands Robots es un SDK de código abierto de AWS que expone abstracciones de robots, simulación y la pila de LeRobot como herramientas de agente que se pueden componer en un solo agente de Strands. La integración con LeRobot permite a los desarrolladores crear agentes que pueden aprender y adaptarse en entornos reales.

## ¿Cómo funciona?

La integración de LeRobot con Strands Robots funciona mediante la creación de un agente que se compone de herramientas de LeRobot, como la grabación de demostraciones en simulación, la ejecución de políticas en hardware y la coordinación de robots remotos. La pila de LeRobot es responsable de la grabación y la calibración en hardware, mientras que Strands AgentTools se encargan de la orquestación del agente.

## ¿Por qué importa?

La integración de LeRobot con Strands Robots es importante porque permite a los desarrolladores crear agentes de robótica autónoma que pueden aprender y adaptarse en entornos reales. Esto abre nuevas posibilidades para la automatización y la robótica en diversas industrias, como la logística, la manufactura y la atención médica.

## Consejo técnico

Si deseas experimentar con la integración de LeRobot con Strands Robots, puedes clonar el ejemplo de aplicación de GitHub y ejecutarlo en tu laptop en simulación. Solo necesitarás cambiar un argumento de comandos para desplegar el agente en hardware.

```bash
git clone https://github.com/strands-robots/examples/lerobot/hub_to_hardware.py
```

---

**Fuente original:** [https://huggingface.co/blog/amazon/strands-lerobot-hub-to-hardware](https://huggingface.co/blog/amazon/strands-lerobot-hub-to-hardware)
