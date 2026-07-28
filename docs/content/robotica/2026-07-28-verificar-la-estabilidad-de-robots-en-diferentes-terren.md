# Verificar la estabilidad de robots en diferentes terrenos

**Fecha:** 2026-07-28
**Categoría:** robotica
**Tags:** robotica, linux, codigo
**Título original:** False-green mobility on firm soil — Dual check on your URDF (PASS or FAIL both count)

---

## Introducción

Un desarrollador ha creado un proyecto para evaluar la estabilidad de robots en diferentes tipos de terrenos, como suelo firme o suelo blando, antes de realizar pruebas en campo. Esto puede evitar daños en el hardware y mejorar la precisión de los robots.

## ¿Qué es?

El proyecto consiste en un software llamado 'ha-dual-socket' que verifica la estabilidad de un robot en diferentes terrenos a través de un archivo de configuración en formato JSON. El software utiliza un algoritmo de verificación para determinar si el robot puede moverse de manera segura en cada tipo de terreno.

## ¿Cómo funciona?

El software 'ha-dual-socket' utiliza un archivo de configuración en formato JSON que contiene la descripción del robot y los parámetros de cada tipo de terreno. Luego, el software aplica un algoritmo de verificación que evalúa la estabilidad del robot en cada tipo de terreno y devuelve un resultado de 'seguro' o 'no seguro'.

## ¿Por qué importa?

Este proyecto es importante porque permite a los desarrolladores evaluar la estabilidad de sus robots en diferentes tipos de terrenos antes de realizar pruebas en campo, lo que puede evitar daños en el hardware y mejorar la precisión de los robots.

## Consejo técnico

Si deseas utilizar este proyecto, puedes descargar el software 'ha-dual-socket' y seguir las instrucciones para configurar el archivo de configuración en formato JSON. Luego, puedes utilizar el comando `ha-dual-socket --urdf your_robot.urdf --kind wheeled_base --soils your_safe_hostile.json` para verificar la estabilidad de tu robot en diferentes tipos de terrenos.

```bash
ha-dual-socket --urdf your_robot.urdf --kind wheeled_base --soils your_safe_hostile.json
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/false-green-mobility-on-firm-soil-dual-check-on-your-urdf-pass-or-fail-both-count/57009](https://discourse.openrobotics.org/t/false-green-mobility-on-firm-soil-dual-check-on-your-urdf-pass-or-fail-both-count/57009)
