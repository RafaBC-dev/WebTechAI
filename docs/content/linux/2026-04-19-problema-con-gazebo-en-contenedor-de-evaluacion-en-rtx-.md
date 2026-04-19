# Problema con Gazebo en contenedor de evaluación en RTX 5090

**Fecha:** 2026-04-19
**Categoría:** linux
**Tags:** robotica, linux, codigo
**Título original:** Gazebo failing to create OpenGL context in eval container on RTX 5090/ NVIDIA driver 575

---

## Introducción

Un usuario ha reportado problemas al intentar ejecutar Gazebo en un contenedor de evaluación en una tarjeta gráfica NVIDIA RTX 5090 con el driver 575.57.08. El error ocurre al intentar crear un contexto OpenGL.

## ¿Qué es?

Gazebo es un simulador de robótica en 3D que permite simular y visualizar entornos y robots en un entorno virtual. Es una herramienta popular en la comunidad de robótica y IA.

## ¿Cómo funciona?

Gazebo utiliza OpenGL para renderizar gráficos en 3D y permitir la visualización de entornos y robots. Sin embargo, en este caso, el contexto OpenGL no se puede crear correctamente en el contenedor de evaluación.

## ¿Por qué importa?

Este problema puede afectar a desarrolladores de robótica y IA que dependen de Gazebo para simular y visualizar sus entornos y robots. Puede retrasar o impedir el desarrollo de proyectos que utilizan Gazebo.

## Consejo técnico

Si estás experimentando este problema, intenta actualizar el driver de la tarjeta gráfica NVIDIA a una versión más reciente. También puedes intentar utilizar una versión diferente de Gazebo o ajustar las configuraciones del contenedor de evaluación.

```bash
/entrypoint.sh ground_truth:=false start_aic_engine:=true
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/gazebo-failing-to-create-opengl-context-in-eval-container-on-rtx-5090-nvidia-driver-575/54140](https://discourse.openrobotics.org/t/gazebo-failing-to-create-opengl-context-in-eval-container-on-rtx-5090-nvidia-driver-575/54140)
