# Herramienta de pruebas automatizadas para pila de autonomía de ROS 2

**Fecha:** 2026-05-18
**Categoría:** robotica
**Tags:** robotica, linux, codigo
**Título original:** Title: Would your team use an open-loop regression testing tool for ROS 2 autonomy stacks?

---

## Introducción

Los equipos de robótica enfrentan desafíos en la pruebas de autonomía de sus sistemas. Una herramienta de pruebas automatizadas podría mejorar la eficiencia y reducir errores.

## ¿Qué es?

La herramienta de pruebas automatizadas es un sistema que reproduce escenarios de pruebas en un entorno de autonomía de ROS 2, utilizando registros de logs de MCAP/rosbag y Docker.

## ¿Cómo funciona?

La herramienta funciona restando un registro de log, ejecutando la pila de autonomía en un entorno de Docker, observando los temas de salida seleccionados y evaluando las reglas de paso/fallo.

## ¿Por qué importa?

Esta herramienta importa porque permite a los equipos de robótica automatizar la pruebas de autonomía, reducir errores y mejorar la eficiencia en la entrega de actualizaciones de autonomía.

## Consejo técnico

Utiliza Docker para crear un entorno de pruebas de autonomía y automatiza la reproducción de escenarios de pruebas utilizando la herramienta de pruebas automatizadas.

```bash
docker run -it --rm -v $(pwd):/app <imagen-de-autonomia>
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/title-would-your-team-use-an-open-loop-regression-testing-tool-for-ros-2-autonomy-stacks/54919](https://discourse.openrobotics.org/t/title-would-your-team-use-an-open-loop-regression-testing-tool-for-ros-2-autonomy-stacks/54919)
