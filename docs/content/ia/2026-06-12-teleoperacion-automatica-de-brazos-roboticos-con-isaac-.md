# Teleoperación automática de brazos robóticos con Isaac Lab

**Fecha:** 2026-06-12
**Categoría:** ia
**Tags:** robotica, ia-local, linux
**Título original:** Isaac Lab Teleoperation & Data Collection 2.0: Automated Block Stacking Dataset Generation with AgileX PiPER and NERO

---

## Introducción

La teleoperación es una técnica efectiva para recopilar demostraciones expertas, pero escalar datasets a través de operaciones manuales se vuelve tedioso y difícil de mantener. Ahora, se ha desarrollado un marco de generación de datos de estantería automática que puede completar tareas de manipulación de manera autónoma y exportar demostraciones exitosas de manera continua.

## ¿Qué es?

El proyecto Isaac Lab Teleoperation & Data Collection 2.0 es una extensión del pipeline original de teleoperación que introduce un marco de generación de datos de estantería automática. Este marco puede completar tareas de manipulación de manera autónoma y exportar demostraciones exitosas de manera continua. El objetivo es crear un pipeline de generación de datos escalable para flujos de aprendizaje de robots.

## ¿Cómo funciona?

El pipeline se compone de varias etapas, incluyendo detección de posición de cubos, planificación de trayectoria, control de IK de pila, movimiento del robot y exportación de datos a HDF5. El controlador genera movimientos de pose cartesiana, mientras que el módulo de IK de Isaac Lab maneja la computación de kinemática inversa internamente. El pipeline es capaz de completar secuencias de estantería completas de manera autónoma.

## ¿Por qué importa?

Este proyecto es importante porque permite la creación de datasets de estantería escalables y autónomos, lo que es esencial para flujos de aprendizaje de robots. Esto puede mejorar la capacidad de los robots para aprender y adaptarse a nuevas situaciones.

## Consejo técnico

Si deseas implementar un pipeline de generación de datos de estantería automática, puedes comenzar por utilizar el script `record_ik_stack.py` que se proporciona en el repositorio. Este script ejecuta una secuencia de estantería completa de manera autónoma y exporta demostraciones exitosas a HDF5.

```bash
record_ik_stack.py
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/isaac-lab-teleoperation-data-collection-2-0-automated-block-stacking-dataset-generation-with-agilex-piper-and-nero/55439](https://discourse.openrobotics.org/t/isaac-lab-teleoperation-data-collection-2-0-automated-block-stacking-dataset-generation-with-agilex-piper-and-nero/55439)
