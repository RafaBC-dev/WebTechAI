# PyPI rechaza nuevos archivos después de 14 días para evitar ataques

**Fecha:** 2026-07-23
**Categoría:** linux
**Tags:** python, librerias, herramientas
**Título original:** PyPI now rejects new files after 14 days

---

## Introducción

La Python Software Foundation ha implementado un cambio en el Python Package Index para evitar que proyectos comprometidos contaminen versiones antiguas. Esto se debe a que dos proyectos populares, LiteLLM y Telnyx, fueron comprometidos recientemente.

## ¿Qué es?

El Python Package Index (PyPI) es un repositorio de paquetes de Python que permite a los desarrolladores compartir y utilizar código. Es una herramienta fundamental para la comunidad de Python.

## ¿Cómo funciona?

PyPI permite a los desarrolladores subir nuevos archivos a versiones existentes de un proyecto. Sin embargo, a partir de ahora, PyPI rechazará nuevos archivos que sean subidos a versiones que tienen más de 14 días de antigüedad. Esto se hace para evitar que proyectos comprometidos contaminen versiones antiguas.

## ¿Por qué importa?

Este cambio es importante porque previene que proyectos comprometidos contaminen versiones antiguas de otros proyectos. Esto podría tener consecuencias graves, como la pérdida de confianza en la comunidad de Python.

## Consejo técnico

Si eres un desarrollador de Python, asegúrate de actualizar tus herramientas y workflows para evitar que tus proyectos se vean afectados por este cambio. Puedes hacer esto consultando la documentación de PyPI y actualizando tus scripts y herramientas para que se ajusten a las nuevas reglas.

```bash
pip install --upgrade pip
```

---

**Fuente original:** [https://lwn.net/Articles/1084218/](https://lwn.net/Articles/1084218/)
