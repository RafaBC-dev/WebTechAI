# Ataque CoT: cómo los modelos de IA pueden ser engañados

**Fecha:** 2026-07-03
**Categoría:** ia
**Tags:** llms, ia-local, herramientas
**Título original:** Chain-of-Thought Spoofing Targets Reasoning AI Models

---

## Introducción

Los investigadores han descubierto un nuevo ataque que puede hacer que los modelos de IA de lenguaje grande (LLMs) respondan de manera incorrecta. El ataque, llamado CoT Forgery, aprovecha la confusión entre el estilo de escritura y los metadatos de los modelos.

## ¿Qué es?

El CoT Forgery es un ataque que permite a los atacantes engañar a los modelos de IA de lenguaje grande (LLMs) haciéndoles creer que una razón convulsa es una conclusión ya alcanzada. Esto se logra escribiendo la razón en un estilo que imita el de la razón interna del modelo.

## ¿Cómo funciona?

Los LLMs priorizan el estilo de escritura sobre los metadatos, lo que les permite a los atacantes inyectar razones falsas que se parezcan a la razón interna del modelo. Esto hace que el modelo trate la razón falsa como una conclusión ya alcanzada, alterando la respuesta a una solicitud del usuario.

## ¿Por qué importa?

Este ataque es importante porque puede ser utilizado para engañar a los modelos de IA de lenguaje grande (LLMs) y hacer que respondan de manera incorrecta. Esto puede tener consecuencias graves en aplicaciones como la asistencia virtual, la traducción automática y la recomendación de contenido.

## Consejo técnico

Para mitigar este ataque, los desarrolladores de LLMs deben priorizar la seguridad y la verificación de los metadatos. Esto puede incluir la implementación de mecanismos de verificación de integridad y la utilización de algoritmos de aprendizaje automático que sean resistentes a los ataques de CoT Forgery.

```bash
No aplica
```

---

**Fuente original:** [https://hackaday.com/2026/07/02/chain-of-thought-spoofing-targets-reasoning-ai-models/](https://hackaday.com/2026/07/02/chain-of-thought-spoofing-targets-reasoning-ai-models/)
