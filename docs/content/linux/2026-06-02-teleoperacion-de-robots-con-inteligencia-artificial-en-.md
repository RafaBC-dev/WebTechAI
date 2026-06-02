# Teleoperación de Robots con Inteligencia Artificial en NVIDIA Isaac Sim

**Fecha:** 2026-06-02
**Categoría:** linux
**Tags:** robotica, ia-local, linux
**Título original:** ROBOTIS HAND VR Teleoperation in NVIDIA Isaac Sim - Real Control, Virtual Tasks

---

## Introducción

La empresa ROBOTIS ha lanzado un guía técnica y demostración sobre teleoperación de robots con inteligencia artificial en NVIDIA Isaac Sim. Esto permite a los desarrolladores probar tareas de manipulación móvil y recopilar datos de aprendizaje por imitación en simulación sin necesidad de hardware físico.

## ¿Qué es?

La teleoperación de robots con inteligencia artificial en NVIDIA Isaac Sim es una tecnología que permite a los desarrolladores controlar robots de manera remota utilizando herramientas de realidad virtual. Esto se logra mediante una conexión en tiempo real entre el controlador de movimiento del robot y el entorno de simulación de NVIDIA Isaac Sim.

## ¿Cómo funciona?

La tecnología utiliza una puente DDS (Data Distribution Service) basada en ROS 2 para conectar el controlador de movimiento del robot con el entorno de simulación. Esto permite a los desarrolladores probar tareas de manipulación móvil y recopilar datos de aprendizaje por imitación en simulación. La tecnología también incluye características como la simulación de fricción en los dedos del robot y la eliminación de colisiones entre los dedos y la base del robot.

## ¿Por qué importa?

Esta tecnología es importante porque permite a los desarrolladores probar y mejorar la inteligencia artificial de los robots de manera más eficiente y segura. También permite la recopilación de datos de aprendizaje por imitación en simulación, lo que puede acelerar el proceso de desarrollo de robots capaces de realizar tareas complejas.

## Consejo técnico

Si deseas probar la teleoperación de robots con inteligencia artificial en NVIDIA Isaac Sim, puedes descargar el código y la documentación desde el repositorio de GitHub de ROBOTIS y seguir las instrucciones para configurar el entorno de simulación y el controlador de movimiento del robot.

```bash
docker run -it --rm -v $PWD:/robotis_lab robotis/ai-worker-isaac-sim
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/robotis-hand-vr-teleoperation-in-nvidia-isaac-sim-real-control-virtual-tasks/55213](https://discourse.openrobotics.org/t/robotis-hand-vr-teleoperation-in-nvidia-isaac-sim-real-control-virtual-tasks/55213)
