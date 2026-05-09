# ros2_lingua: un motor de grounding seguro para LLMs en robótica

**Fecha:** 2026-05-09
**Categoría:** ia
**Tags:** robotica, llms, python
**Título original:** ros2_lingua: A safe, dependency-aware grounding engine for LLMs

---

## Introducción

Un desarrollador ha creado un proyecto llamado ros2_lingua para solucionar problemas comunes al integrar LLMs con robots. Estos problemas incluyen la tendencia de los LLMs a 'hallucinar' acciones y asumir requisitos no cumplidos.

## ¿Qué es?

ros2_lingua es un motor de grounding que introduce un contrato estructurado entre nodos de ROS 2 y LLMs. Esto permite a los LLMs producir planes basados en capacidades explícitamente registradas y utiliza un planificador de retroceso para inyectar pasos faltantes de manera automática.

## ¿Cómo funciona?

ros2_lingua funciona mediante la publicación de capacidades por parte de los nodos de ROS 2, que definen su nombre, acción o servicio, parámetros, precondiciones y postcondiciones. Luego, el motor de grounding utiliza un planificador de retroceso para verificar el estado actual del robot y agregar pasos necesarios antes de ejecutar el plan.

## ¿Por qué importa?

ros2_lingua resuelve problemas comunes al integrar LLMs con robots, como la tendencia a 'hallucinar' acciones y asumir requisitos no cumplidos. Esto permite a los desarrolladores crear sistemas de control de robots más seguros y fiables.

## Consejo técnico

Si estás desarrollando un sistema de control de robot con LLMs, considera utilizar ros2_lingua para introducir un contrato estructurado entre tus nodos de ROS 2 y LLMs. Esto te permitirá producir planes más seguros y fiables y reducir el riesgo de 'hallucinaciones' de acciones.

```bash
ros2_lingua_core
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/ros2-lingua-a-safe-dependency-aware-grounding-engine-for-llms/54645](https://discourse.openrobotics.org/t/ros2-lingua-a-safe-dependency-aware-grounding-engine-for-llms/54645)
