# Repo-Semantic-Memory: un sistema de contexto para codificadores en ROS 2

**Fecha:** 2026-06-19
**Categoría:** linux
**Tags:** robotica, python, librerias, herramientas
**Título original:** Dogfooding a local MCP context server for coding agents on a ROS 2 Python repo

---

## Introducción

Repo-Semantic-Memory (RSM) es una herramienta que ayuda a los desarrolladores de ROS 2 a encontrar y acceder a la información relevante de un proyecto, reduciendo el tiempo y la complejidad en la codificación.

## ¿Qué es?

RSM es un sistema de contexto que indexa un repositorio local y proporciona herramientas para encontrar archivos, pruebas y documentación relacionados con un proyecto. Se puede utilizar con codificadores para preparar un contexto enfocado antes de comenzar a editar.

## ¿Cómo funciona?

RSM se integra con el framework de ciclo de vida de ROS 2 (lifecore_ros2) y utiliza un servidor de MCP (Multi-Context Protocol) local para proporcionar acceso a la información relevante. Los codificadores pueden utilizar comandos como rsm_search, rsm_find_related y rsm_prepare_context para encontrar y acceder a la información necesaria.

## ¿Por qué importa?

RSM es importante para los desarrolladores de ROS 2 que trabajan en proyectos complejos y necesitan acceder rápidamente a la información relevante. Reduce el tiempo y la complejidad en la codificación, permitiendo a los desarrolladores enfocarse en la lógica del proyecto en lugar de buscar información.

## Consejo técnico

Si estás trabajando en un proyecto de ROS 2 y necesitas acceder rápidamente a la información relevante, prueba RSM. Puedes utilizar el comando `uv run rsm mcp serve --repo /path/to/repo --db /path/to/index.sqlite` para exponer el servidor de MCP local y acceder a la información necesaria.

```bash
uv run rsm mcp serve --repo /path/to/repo --db /path/to/index.sqlite
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/dogfooding-a-local-mcp-context-server-for-coding-agents-on-a-ros-2-python-repo/55556](https://discourse.openrobotics.org/t/dogfooding-a-local-mcp-context-server-for-coding-agents-on-a-ros-2-python-repo/55556)
