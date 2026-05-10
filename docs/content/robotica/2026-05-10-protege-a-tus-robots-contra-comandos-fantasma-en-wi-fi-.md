# Protege a tus robots contra comandos fantasma en Wi-Fi inestable

**Fecha:** 2026-05-10
**Categoría:** robotica
**Tags:** robotica, linux, codigo
**Título original:** Stop “Ghost Commands” on Bad Wi-Fi: ros2_kinematic_guard for `/cmd_vel` safety

---

## Introducción

¿Has experimentado comandos fantasma en tus robots móviles después de una caída de Wi-Fi o 5G? Un desarrollador ha creado una solución para proteger a tus robots contra este problema común.

## ¿Qué es?

ros2_kinematic_guard es un proyecto de ROS 2 que se encarga de proteger a los robots móviles contra comandos fantasma que pueden ocurrir debido a la inestabilidad del Wi-Fi o 5G. Esto se logra evaluando una ventana local de comandos y odometría para detectar inconsistencias y tomar medidas de seguridad.

## ¿Cómo funciona?

El proyecto ros2_kinematic_guard funciona mediante un guardián que se sitúa entre el flujo de comandos y el controlador del robot. Evalúa una ventana local de comandos y odometría para detectar inconsistencias y tomar medidas de seguridad. Si se detecta una inconsistencia, el guardián entra en un estado determinista que corta la movilidad, elimina los comandos dañados y espera a que se recupere la estabilidad.

## ¿Por qué importa?

Este proyecto es importante porque protege a los robots móviles contra comandos fantasma que pueden ocurrir debido a la inestabilidad del Wi-Fi o 5G. Esto puede evitar daños a los robots y garantizar su seguridad y estabilidad en entornos inestables.

## Consejo técnico

Prueba el proyecto ros2_kinematic_guard en tu entorno de desarrollo y configura el guardián para que se adapte a tus necesidades específicas. Puedes utilizar el código proporcionado en el repositorio para crear un entorno de prueba y evaluar la efectividad del proyecto.

```bash
ros2_kinematic_guard
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/stop-ghost-commands-on-bad-wi-fi-ros2-kinematic-guard-for-cmd-vel-safety/54681](https://discourse.openrobotics.org/t/stop-ghost-commands-on-bad-wi-fi-ros2-kinematic-guard-for-cmd-vel-safety/54681)
