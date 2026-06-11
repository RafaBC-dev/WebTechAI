# EpisodeVault: Herramienta para depurar problemas de modelos de LeRobot

**Fecha:** 2026-06-11
**Categoría:** ia
**Tags:** robotica, ia-local, herramientas
**Título original:** EpisodeVault: open source tool to debug why your LeRobot model regressed

---

## Introducción

Si has trabajado con LeRobot v3 y has experimentado regresiones en tus modelos, sabrás que puede ser difícil identificar la causa raíz. EpisodeVault es una herramienta open source diseñada para ayudarte a depurar estos problemas.

## ¿Qué es?

EpisodeVault es una herramienta open source que permite a los desarrolladores de LeRobot depurar problemas de regresión en sus modelos. Ofrece una forma sencilla de identificar qué tareas han cambiado o qué episodios han empeorado entre versiones de dataset.

## ¿Cómo funciona?

EpisodeVault funciona mediante cuatro comandos simples: `episodevault track`, `episodevault commit`, `episodevault diff` y `episodevault blame`. Estos comandos te permiten rastrear cambios en tus datasets, identificar tareas que han empeorado y determinar la versión de dataset que entrenó un modelo específico.

## ¿Por qué importa?

EpisodeVault es importante porque resuelve un problema común en la comunidad de LeRobot: la falta de herramientas para depurar regresiones en modelos. Con EpisodeVault, los desarrolladores pueden identificar y corregir problemas de regresión de manera más eficiente.

## Consejo técnico

Si estás experimentando regresiones en tus modelos de LeRobot, prueba EpisodeVault para identificar la causa raíz de los problemas. Puedes instalarla mediante `pip install episodevault` y comenzar a utilizarla de inmediato.

```bash
episodevault track ./my_dataset
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/episodevault-open-source-tool-to-debug-why-your-lerobot-model-regressed/55401](https://discourse.openrobotics.org/t/episodevault-open-source-tool-to-debug-why-your-lerobot-model-regressed/55401)
