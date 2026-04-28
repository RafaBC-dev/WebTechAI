# Actualización de pip 26.1: archivos de bloqueo y cooldown de dependencias

**Fecha:** 2026-04-28
**Categoría:** ia
**Tags:** python, librerias, herramientas
**Título original:** What's new in pip 26.1 - lockfiles and dependency cooldowns!

---

## Introducción

La versión 26.1 de pip, la herramienta de instalación de dependencias de Python por defecto, ha sido actualizada con nuevas funcionalidades. Entre ellas, la creación de archivos de bloqueo y la implementación de cooldown de dependencias. Esto significa que los desarrolladores pueden asegurarse de que sus proyectos se mantengan actualizados y seguros.

## ¿Qué es?

pip es la herramienta de instalación de dependencias de Python por defecto. Su función es instalar y gestionar las dependencias de un proyecto Python. La versión 26.1 de pip ha sido actualizada con nuevas funcionalidades para mejorar la seguridad y la gestión de dependencias.

## ¿Cómo funciona?

La versión 26.1 de pip crea archivos de bloqueo (pylock.toml) que contienen la lista de dependencias instaladas en un proyecto. Además, introduce la función de cooldown de dependencias, que permite a los desarrolladores especificar un plazo de tiempo después de que una dependencia haya sido actualizada para que no se instale una versión más reciente. Esto se puede hacer mediante la opción --uploaded-prior-to PXXD, donde X es el número de días.

## ¿Por qué importa?

La actualización de pip 26.1 es importante porque proporciona una forma más segura y eficiente de gestionar las dependencias de los proyectos Python. Los desarrolladores pueden asegurarse de que sus proyectos se mantengan actualizados y seguros, lo que reduce el riesgo de ataques de seguridad y errores de configuración.

## Consejo técnico

Si deseas aprovechar las nuevas funcionalidades de pip 26.1, prueba la opción --uploaded-prior-to PXXD para especificar un plazo de tiempo después de que una dependencia haya sido actualizada. Por ejemplo, puedes instalar la versión 0.30 de LLM mediante el comando `pip install llm --uploaded-prior-to P4D`.

```bash
pip install llm --uploaded-prior-to P4D
```

---

**Fuente original:** [https://simonwillison.net/2026/Apr/28/pip-261/#atom-everything](https://simonwillison.net/2026/Apr/28/pip-261/#atom-everything)
