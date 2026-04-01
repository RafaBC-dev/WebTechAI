# Llamadas a revisar parches con inteligencia artificial en el kernel de Linux

**Fecha:** 2026-04-01
**Categoría:** ia
**Tags:** llms, linux, codigo
**Título original:** [$] The role of LLMs in patch review

---

## Introducción

El mantenimiento del kernel de Linux ha sido complicado por una serie de cambios en un parche de gestión de memoria que se extendieron más allá de lo inicialmente planeado. La discusión sobre cómo y cuándo adoptar Sashiko, un sistema de revisión de parches basado en LLM, podría tener implicaciones para otras partes del kernel.

## ¿Qué es?

Sashiko es un sistema de revisión de parches basado en LLM (Modelos de Lenguaje de Línea de Mando) que se utiliza para revisar parches en el kernel de Linux. Los LLM son modelos de inteligencia artificial que pueden analizar y generar texto, lo que los hace útiles para la revisión de parches, que a menudo involucra la lectura y comprensión de código complejo.

## ¿Cómo funciona?

Sashiko utiliza un LLM para analizar los parches y proporcionar retroalimentación a los autores de los parches. El sistema puede identificar problemas potenciales y sugerir cambios para mejorar la calidad del parche. El mantenimiento del kernel de Linux ha propuesto utilizar Sashiko para revisar parches, pero otros mantenedores han expresado objeciones.

## ¿Por qué importa?

La adopción de Sashiko podría mejorar la calidad y la eficiencia de la revisión de parches en el kernel de Linux, lo que podría llevar a una mayor estabilidad y seguridad del sistema operativo. Además, la discusión sobre la adopción de Sashiko podría tener implicaciones para otras partes del kernel y la comunidad de desarrolladores de Linux.

## Consejo técnico

Si deseas aprender más sobre Sashiko y cómo funciona, puedes revisar el código fuente en GitHub y explorar la documentación oficial. También puedes probar utilizar Sashiko para revisar parches en tu propio proyecto de Linux.

```bash
git clone https://github.com/linux-sashiko/sashiko.git
```

---

**Fuente original:** [https://lwn.net/Articles/1064830/](https://lwn.net/Articles/1064830/)
