# Moral Execution Guard para robots humanoides: un paso hacia la seguridad ética

**Fecha:** 2026-08-05
**Categoría:** robotica
**Tags:** robotica, ia-local, linux
**Título original:** QERRA-v2 Demo 3: Moral Execution Guard for Humanoid AMRs (PAL Robotics TIAGo in Webots)

---

## Introducción

En la robótica, la seguridad física es fundamental, pero en la interacción con humanos, la seguridad moral es igualmente importante. Un robot que ejecuta órdenes sin considerar las implicaciones éticas puede generar consecuencias legales y operativas graves.

## ¿Qué es?

QERRA-v2 es un sistema de evaluación ética para robots humanoides que evalúa las órdenes recibidas y rechaza aquellas que violen la autonomía o manipulen la información de manera cognitiva. Utiliza una arquitectura de dos capas para monitorear la seguridad física y evaluar la semántica de las órdenes.

## ¿Cómo funciona?

La capa inferior (QERRA-HSR) monitorea la seguridad física en tiempo real, mientras que la capa superior (SEMEV-12) evalúa la semántica de las órdenes utilizando un patrón de coincidencia pronombre-guardada. Si una orden es rechazada, el robot se detiene inmediatamente y registra un mensaje de rechazo.

## ¿Por qué importa?

Este sistema es importante porque permite a los robots humanoides interactuar con humanos de manera segura y ética, evitando consecuencias legales y operativas graves. También proporciona una forma de recuperación dinámica cuando una orden es redefinida de manera ética.

## Consejo técnico

Si deseas implementar un sistema de evaluación ética en tu proyecto de robótica, puedes utilizar la arquitectura de dos capas de QERRA-v2 y la librería PyTrees para crear un comportamiento de árbol de decisiones.

```bash
pip install PyTrees
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/qerra-v2-demo-3-moral-execution-guard-for-humanoid-amrs-pal-robotics-tiago-in-webots/57159](https://discourse.openrobotics.org/t/qerra-v2-demo-3-moral-execution-guard-for-humanoid-amrs-pal-robotics-tiago-in-webots/57159)
