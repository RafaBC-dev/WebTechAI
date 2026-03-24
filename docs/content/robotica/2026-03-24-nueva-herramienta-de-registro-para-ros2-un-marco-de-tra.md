# Nueva herramienta de registro para ROS2: un marco de trabajo compuesto para C++

**Fecha:** 2026-03-24
**Categoría:** robotica
**Tags:** robotica, codigo, linux
**Título original:** Compositional C++ log framework for ROS2

---

## Introducción

Después de sentirse abrumado por la verbosidad de los macros de registro de ROS2, un desarrollador ha creado una alternativa más concisa y compuesta basada en flujos de C++.

## ¿Qué es?

La herramienta de registro es una clase de plantilla llamada 'log' que encapsula un flujo de cadena de caracteres y pasa la información de registro a un objeto de registro llamado 'Logger' cuando se destruye. El Logger puede ser reemplazado por un objeto de registro que implemente un registro con retardo.

## ¿Cómo funciona?

La clase 'log' tiene dos parámetros: el nivel de severidad y un objeto de registro callable. La clase encapsula un flujo de cadena de caracteres y pasa la información de registro a un objeto de registro cuando se destruye. El objeto de registro puede ser reemplazado por un objeto de registro que implemente un registro con retardo.

## ¿Por qué importa?

Esta herramienta de registro es importante porque proporciona una forma más concisa y compuesta de registrar información en ROS2, lo que puede ser útil para desarrolladores que buscan mejorar la legibilidad y la mantenibilidad de su código.

## Consejo técnico

Si estás trabajando con ROS2, considera utilizar esta herramienta de registro para mejorar la concisión y la composicionalidad de tus macros de registro.

```bash
No aplica
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/compositional-c-log-framework-for-ros2/53472](https://discourse.openrobotics.org/t/compositional-c-log-framework-for-ros2/53472)
