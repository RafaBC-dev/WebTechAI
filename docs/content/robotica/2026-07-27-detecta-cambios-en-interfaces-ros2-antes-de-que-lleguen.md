# Detecta cambios en interfaces ROS2 antes de que lleguen al robot

**Fecha:** 2026-07-27
**Categoría:** robotica
**Tags:** robotica, linux, codigo
**Título original:** roschema: catch breaking .msg/.srv/.action changes in CI, before they hit the robot

---

## Introducción

Un desarrollador ha creado una herramienta para detectar cambios en interfaces ROS2 antes de que se desplieguen en un robot, evitando problemas de compatibilidad y errores de serialización.

## ¿Qué es?

Roschema es una herramienta creada para detectar cambios en interfaces ROS2 (msg, srv y action) y evitar problemas de compatibilidad y errores de serialización. Funciona mediante la comparación de definiciones de interfaces contra un ref de Git, un directorio, un archivo de bag de MCAP o un archivo de bloqueo.

## ¿Cómo funciona?

Roschema compara las definiciones de interfaces contra un ref de Git, un directorio, un archivo de bag de MCAP o un archivo de bloqueo y clasifica cada cambio en wire, source, introspection y comportamiento. También llena convenciones de nombres y formatea canónicamente. Puede configurarse para ignorar o suprimir ciertas reglas.

## ¿Por qué importa?

Roschema es importante porque evita problemas de compatibilidad y errores de serialización en robots que utilizan interfaces ROS2. Esto se debe a que los cambios en las interfaces pueden hacer que los mensajes sean incompatibles entre nodos y los archivos de bag sean inaccesibles.

## Consejo técnico

Si estás trabajando con interfaces ROS2, considera utilizar roschema para detectar cambios y evitar problemas de compatibilidad. Puedes utilizar el comando `uvx roschema check --against origin/main` para verificar las definiciones de interfaces contra un ref de Git.

```bash
uvx roschema check --against origin/main
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/roschema-catch-breaking-msg-srv-action-changes-in-ci-before-they-hit-the-robot/56958](https://discourse.openrobotics.org/t/roschema-catch-breaking-msg-srv-action-changes-in-ci-before-they-hit-the-robot/56958)
