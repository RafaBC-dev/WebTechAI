# Detecta cambios en interfaces ROS 2 antes de desplegar

**Fecha:** 2026-07-26
**Categoría:** robotica
**Tags:** robotica, linux, codigo
**Título original:** roschema: catch breaking .msg/.srv/.action changes in CI, before they hit the robot

---

## Introducción

Un desarrollador ha creado una herramienta llamada roschema para detectar cambios en interfaces ROS 2 antes de que se desplieguen, evitando problemas de compatibilidad y errores de lectura de archivos de registro.

## ¿Qué es?

Roschema es una herramienta que difiere las definiciones de interfaces ROS 2 (msg, srv, action) con una referencia de Git, un directorio, un archivo de registro MCAP o un archivo de bloqueo, y clasifica cada cambio según su tipo (compatibilidad de cable, fuente, introspección o comportamiento).

## ¿Cómo funciona?

La herramienta utiliza un sistema de reglas para clasificar los cambios y puede configurarse para ignorar o suprimir ciertos tipos de cambios. También incluye un formateador canónico y una acción de GitHub para integrarse con flujos de trabajo de CI.

## ¿Por qué importa?

Roschema es importante porque permite a los desarrolladores detectar cambios en interfaces ROS 2 antes de que se desplieguen, evitando problemas de compatibilidad y errores de lectura de archivos de registro. Esto puede ahorrar tiempo y esfuerzo en la resolución de problemas y mejorar la estabilidad del sistema.

## Consejo técnico

Si estás trabajando con interfaces ROS 2, considera utilizar roschema para detectar cambios y mejorar la compatibilidad de tu código. Puedes configurar la herramienta para ignorar o suprimir ciertos tipos de cambios y utilizar el formateador canónico para mantener un estilo coherente en tus definiciones de interfaz.

```bash
uvx roschema check --against origin/main
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/roschema-catch-breaking-msg-srv-action-changes-in-ci-before-they-hit-the-robot/56958](https://discourse.openrobotics.org/t/roschema-catch-breaking-msg-srv-action-changes-in-ci-before-they-hit-the-robot/56958)
