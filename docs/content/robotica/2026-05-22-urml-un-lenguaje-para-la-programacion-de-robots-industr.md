# URML: un lenguaje para la programación de robots industriales

**Fecha:** 2026-05-22
**Categoría:** robotica
**Tags:** robotica, linux, codigo
**Título original:** URML composition draft over ROS-Industrial drivers: does the manifest match?

---

## Introducción

Un equipo de desarrolladores ha creado URML, un lenguaje de programación para robots industriales que permite componer sobre pilas de robótica existentes, en lugar de reemplazarlas. Esto podría revolucionar la forma en que se programan los robots industriales.

## ¿Qué es?

URML (Universal Robot Language) es un lenguaje de programación Apache 2.0 que se enfoca en la programación de robots industriales. Permite componer sobre pilas de robótica existentes, en lugar de reemplazarlas. Esto significa que los desarrolladores pueden crear programas que se ejecuten en diferentes plataformas de robótica sin necesidad de reescribir el código.

## ¿Cómo funciona?

URML se basa en la idea de componer sobre pilas de robótica existentes, utilizando un patrón de composición que se encuentra en el archivo `urml_ros2_runtime.RclpyAdapter`. Esto permite a los desarrolladores crear programas que se ejecuten en diferentes plataformas de robótica, como ABB, FANUC, KUKA, etc. Sin embargo, esto requiere que los desarrolladores adapten su código para que se ajuste a la plataforma específica.

## ¿Por qué importa?

URML podría revolucionar la forma en que se programan los robots industriales, permitiendo a los desarrolladores crear programas que se ejecuten en diferentes plataformas de robótica sin necesidad de reescribir el código. Esto podría acelerar el desarrollo de aplicaciones de robótica y mejorar la eficiencia de la producción.

## Consejo técnico

Si deseas empezar a trabajar con URML, te recomendamos que revises el repositorio de GitHub de URML y explore los ejemplos de código disponibles. También es recomendable que revises la documentación de ROS-Industrial para entender mejor cómo funciona la composición de pilas de robótica.

---

**Fuente original:** [https://discourse.openrobotics.org/t/urml-composition-draft-over-ros-industrial-drivers-does-the-manifest-match/55010](https://discourse.openrobotics.org/t/urml-composition-draft-over-ros-industrial-drivers-does-the-manifest-match/55010)
