# Robótica: Auto-recharge desplegado en robots descomisionados

**Fecha:** 2026-03-13
**Categoría:** robotica
**Tags:** python, librerias, herramientas
**Título original:** Auto-recharge task dispatched to decommissioned robot with `idle_behavior=false`

---

## Introducción

Un usuario ha descubierto un comportamiento inesperado en robots descomisionados con ROS2 Jazzy. A pesar de estar descomisionados, estos robots siguen recibiendo tareas de recarga automática si su batería está por debajo de un umbral determinado.

## ¿Qué es?

Un robot descomisionado es un robot que ya no está activo y no está realizando tareas. Sin embargo, en este caso, la descomisión no impide que el robot reciba tareas de recarga automática si su batería está por debajo de un umbral determinado.

## ¿Cómo funciona?

La descomisión de un robot se realiza mediante una solicitud POST a la API, especificando que el robot no debe realizar tareas ni recibir tareas nuevas. Sin embargo, si la batería del robot está por debajo de un umbral determinado (recharge_threshold), el sistema enviará una tarea de recarga automática al robot.

## ¿Por qué importa?

Este comportamiento es importante porque puede tener implicaciones en la gestión de la energía y la vida útil de los robots. Si un robot está descomisionado pero sigue recibiendo tareas de recarga automática, puede llevar a una sobrecarga de la batería y reducir la vida útil del robot.

## Consejo técnico

Si se desea evitar que un robot descomisionado reciba tareas de recarga automática, es necesario especificar un umbral de batería más alto o establecer un valor de recharge_threshold más alto en la configuración del robot.

```bash
POST /fleets/<nombre_fleeta>/decommission?robot_name=<nombre_robot>&reassign_tasks=false&allow_idle_behavior=false
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/auto-recharge-task-dispatched-to-decommissioned-robot-with-idle-behavior-false/53190](https://discourse.openrobotics.org/t/auto-recharge-task-dispatched-to-decommissioned-robot-with-idle-behavior-false/53190)
