# Ataques de inyección de prompts: el peligro de la confusión de roles

**Fecha:** 2026-06-23
**Categoría:** ia
**Tags:** llms, ia-local, linux
**Título original:** Prompt Injection as Role Confusion

---

## Introducción

Un equipo de investigadores ha descubierto un método para burlar la seguridad de los modelos de lenguaje, aprovechando la confusión de roles que pueden experimentar al tratar con textos de diferentes fuentes.

## ¿Qué es?

La confusión de roles es un problema que ocurre cuando un modelo de lenguaje no puede distinguir entre texto de confianza y texto no confiable, lo que puede llevar a ataques de inyección de prompts que permiten a los atacantes manipular la respuesta del modelo.

## ¿Cómo funciona?

Los investigadores han demostrado que al agregar texto que imita el estilo de los bloques de pensamiento internos de un modelo de lenguaje, se puede confundir al modelo y hacer que responda de manera incorrecta. Esto se logra mediante la técnica de 'destyling', que consiste en reescribir el texto para que no se ajuste a la forma esperada en un bloque de rol.

## ¿Por qué importa?

La confusión de roles es un problema serio que puede permitir a los atacantes manipular los modelos de lenguaje para realizar tareas maliciosas, como proporcionar información falsa o promover la creación de drogas ilegales.

## Consejo técnico

Para mitigar este problema, los desarrolladores de modelos de lenguaje deben implementar mecanismos de seguridad que puedan detectar y prevenir la confusión de roles, como la verificación de la autenticidad de los bloques de rol y la utilización de técnicas de destyling para reescribir el texto de manera segura.

---

**Fuente original:** [https://simonwillison.net/2026/Jun/22/prompt-injection-as-role-confusion/#atom-everything](https://simonwillison.net/2026/Jun/22/prompt-injection-as-role-confusion/#atom-everything)
