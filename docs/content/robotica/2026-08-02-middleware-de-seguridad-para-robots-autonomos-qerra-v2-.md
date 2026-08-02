# Middleware de seguridad para robots autónomos: QERRA-v2 Classical

**Fecha:** 2026-08-02
**Categoría:** robotica
**Tags:** robotica, ia-local, python
**Título original:** QERRA-v2 Classical: Two-Layer Moral & Physical Safety Middleware for ROS 2 & Behavior Trees

---

## Introducción

Un equipo de desarrolladores ha presentado QERRA-v2 Classical, un middleware de seguridad para robots autónomos que evalúa las acciones del robot antes de su ejecución. Este sistema es crucial para garantizar la seguridad y la ética en la robótica.

## ¿Qué es?

QERRA-v2 Classical es un middleware de seguridad abierto y explicable que evalúa las acciones de un robot autónomo antes de su ejecución. Utiliza una arquitectura de dos capas: QERRA-HSR (capa de seguridad física) y SEMEV-12 (motor de deliberación moral).

## ¿Cómo funciona?

La capa de seguridad física (QERRA-HSR) utiliza Python para evaluar la proximidad de peligros físicos y señales de estrés humano. La capa de deliberación moral (SEMEV-12) evalúa tareas naturales de lenguaje contra 12 dimensiones éticas humanas. El sistema se integra en pipelines de ROS 2 mediante servidores de acción y nodos de árboles de comportamiento.

## ¿Por qué importa?

QERRA-v2 Classical es importante porque resuelve problemas de seguridad y ética en la robótica. Permite evaluar las acciones de un robot antes de su ejecución, lo que reduce el riesgo de accidentes y violaciones de la ética.

## Consejo técnico

Si estás interesado en probar QERRA-v2 Classical, puedes descargar el código desde el repositorio de GitHub y seguir las instrucciones para integrarlo en tus proyectos de robótica.

```bash
git clone https://github.com/marunigno-ship-it/QERRA-v2-classical.git
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/qerra-v2-classical-two-layer-moral-physical-safety-middleware-for-ros-2-behavior-trees/57110](https://discourse.openrobotics.org/t/qerra-v2-classical-two-layer-moral-physical-safety-middleware-for-ros-2-behavior-trees/57110)
