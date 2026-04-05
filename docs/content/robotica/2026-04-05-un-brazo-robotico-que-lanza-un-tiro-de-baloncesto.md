# Un brazo robótico que lanza un tiro de baloncesto

**Fecha:** 2026-04-05
**Categoría:** robotica
**Tags:** robotica, ia-local, python
**Título original:** A Robot that Slam Dunks

---

## Introducción

Un ingeniero ha creado un brazo robótico capaz de detectar, coger y lanzar un balón de baloncesto hacia una canasta. Esta innovación podría tener aplicaciones en la automatización de tareas y la mejora de la precisión en la industria.

## ¿Qué es?

El proyecto consiste en un brazo robótico llamado myCobot 280, fabricado por Elephant Robotics, que ha sido entrenado para detectar y coger un balón de baloncesto. El robot utiliza una visión artificial para reconocer el balón en tiempo real y reaccionar accordingly.

## ¿Cómo funciona?

Para lograr esto, el ingeniero entrenó un modelo de visión artificial en Edge Impulse utilizando un conjunto de datos gratuito de VisionDatasets.com. El modelo permite al robot entender su entorno y reconocer el balón en tiempo real. El robot luego utiliza un mecanismo de lanzamiento para enviar el balón hacia la canasta.

## ¿Por qué importa?

Esta innovación podría tener aplicaciones en la automatización de tareas y la mejora de la precisión en la industria. El uso de visión artificial y robots podría permitir a las empresas realizar tareas más complejas y precisas, lo que podría aumentar la eficiencia y la productividad.

## Consejo técnico

Si deseas crear un proyecto similar, puedes utilizar Edge Impulse para entrenar un modelo de visión artificial y luego integrarlo con un brazo robótico como el myCobot 280. Recuerda que es importante seleccionar un conjunto de datos adecuado para entrenar tu modelo.

```bash
edge impulse train --dataset visiondatasets.com --model mycobot_280
```

---

**Fuente original:** [https://blog.adafruit.com/2026/04/04/a-robot-that-slam-dunks/](https://blog.adafruit.com/2026/04/04/a-robot-that-slam-dunks/)
