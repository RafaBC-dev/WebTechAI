# LSEP v0.2: una implementación de referencia de ROS 2 para robótica

**Fecha:** 2026-06-14
**Categoría:** robotica
**Tags:** robotica, linux, codigo
**Título original:** LSEP v0.2 — now a buildable ROS 2 reference implementation: typed lsep_msgs + managed lifecycle node, green CI

---

## Introducción

La comunidad de robótica ha recibido una actualización importante con la versión 0.2 de LSEP (Layered State Estimation Protocol), un protocolo de estimación de estados jerárquico para robótica. Esta versión incluye una implementación de referencia de ROS 2 (Robot Operating System 2) que puede ser construida y ejecutada en minutos.

## ¿Qué es?

LSEP es un protocolo de estimación de estados jerárquico para robótica que permite a los sistemas de robótica gestionar estados complejos de manera eficiente. La versión 0.2 de LSEP incluye una implementación de referencia de ROS 2 que permite a los desarrolladores construir y ejecutar sistemas de robótica de manera sencilla.

## ¿Cómo funciona?

La implementación de referencia de ROS 2 de LSEP v0.2 incluye mensajes tipo (lsep_msgs) que permiten a los sistemas de robótica comunicarse de manera eficiente. También incluye un nodo de ciclo de vida gestionado (lsep_node) que permite a los sistemas de robótica gestionar estados de manera determinista. Además, la versión 2.1 del motor de LSEP incluye mejoras en la escalada y desescalada de estados.

## ¿Por qué importa?

La versión 0.2 de LSEP es importante porque proporciona una implementación de referencia de ROS 2 que puede ser construida y ejecutada en minutos, lo que facilita la creación de sistemas de robótica. También incluye mejoras en la escalada y desescalada de estados que permiten a los sistemas de robótica gestionar estados complejos de manera eficiente.

## Consejo técnico

Si deseas construir un sistema de robótica con LSEP, puedes utilizar la herramienta Colcon para construir y ejecutar la implementación de referencia de ROS 2. También puedes utilizar la herramienta CI (Continuous Integration) para probar y verificar la implementación de LSEP.

```bash
colcon build
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/lsep-v0-2-now-a-buildable-ros-2-reference-implementation-typed-lsep-msgs-managed-lifecycle-node-green-ci/55466](https://discourse.openrobotics.org/t/lsep-v0-2-now-a-buildable-ros-2-reference-implementation-typed-lsep-msgs-managed-lifecycle-node-green-ci/55466)
