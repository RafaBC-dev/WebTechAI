# Ros2_lingua: un capa de registro de capacidades para LLMs más seguras

**Fecha:** 2026-07-16
**Categoría:** ia
**Tags:** robotica, llms, linux
**Título original:** ros2_lingua: a runtime capability-registration layer so LLMs only call actions that actually exist

---

## Introducción

Los LLMs (modelos de lenguaje de aprendizaje automático) están cada vez más integrados con robots, pero esto puede llevar a problemas de seguridad y estabilidad. Ros2_lingua es un proyecto que busca resolver estos problemas mediante un capa de registro de capacidades que permite a los LLMs interactuar de manera segura con los robots.

## ¿Qué es?

Ros2_lingua es un proyecto que permite a los robots registrarse de manera dinámica en tiempo de ejecución, lo que significa que los LLMs solo pueden interactuar con las capacidades que están disponibles en ese momento. Esto evita que los LLMs intenten llamar a acciones que no existen o que no están disponibles.

## ¿Cómo funciona?

Ros2_lingua funciona mediante un registro de capacidades que se actualiza en tiempo de ejecución. Los robots se registran en este registro, proporcionando información sobre sus capacidades, como nombre, descripción y parámetros. Luego, los LLMs pueden interactuar con estas capacidades de manera segura, ya que solo pueden llamar a las acciones que están disponibles en el registro.

## ¿Por qué importa?

Ros2_lingua importa porque permite a los LLMs interactuar de manera segura con los robots, evitando problemas de seguridad y estabilidad. Esto es especialmente importante en entornos de producción, donde la seguridad y la estabilidad son fundamentales.

## Consejo técnico

Si estás trabajando con LLMs y robots, considera implementar Ros2_lingua en tu proyecto para mejorar la seguridad y la estabilidad de la interacción entre los LLMs y los robots.

```bash
ros2_lingua_cpp (para obtener más información sobre las C++ bindings)
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/ros2-lingua-a-runtime-capability-registration-layer-so-llms-only-call-actions-that-actually-exist/56628](https://discourse.openrobotics.org/t/ros2-lingua-a-runtime-capability-registration-layer-so-llms-only-call-actions-that-actually-exist/56628)
