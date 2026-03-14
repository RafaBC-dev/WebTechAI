# Descomisión de robots con auto-recarga: una sorpresa en ROS2 Jazzy

**Fecha:** 2026-03-14
**Categoría:** robotica
**Tags:** ia-local, python, librerias
**Título original:** Auto-recharge task dispatched to decommissioned robot with `idle_behavior=false`

---

## Introducción

Un usuario ha descubierto que cuando se descomisiona un robot con la configuración de auto-recarga activada, el sistema aún envía una tarea de recarga automática si la batería está por debajo de un umbral determinado. Esto podría ser un problema si se busca detener completamente el robot.

## ¿Qué es?

Un robot descomisionado es un robot que ya no está en uso y no realiza tareas. Sin embargo, en ROS2 Jazzy, se ha descubierto que si se descomisiona un robot con la configuración de auto-recarga activada, el sistema aún envía una tarea de recarga automática si la batería está por debajo de un umbral determinado.

## ¿Cómo funciona?

La configuración de auto-recarga se establece en el archivo tinyRobot_config.yaml, donde se especifica el umbral de recarga y la acción a realizar cuando la batería esté por debajo de ese umbral. Cuando se descomisiona el robot, el sistema verifica si la batería está por debajo de ese umbral y, si es así, envía una tarea de recarga automática.

## ¿Por qué importa?

Este problema importa porque podría ser un problema de seguridad si se busca detener completamente el robot. Si el robot sigue realizando tareas de recarga automática, podría seguir funcionando de manera inesperada y potencialmente causar problemas.

## Consejo técnico

Si se busca detener completamente un robot, es recomendable descomisionarlo con la configuración de auto-recarga desactivada y verificar que no queden tareas pendientes de recarga automática.

```bash
POST /fleets/tinyRobot/decommission?robot_name=tinyRobot2&reassign_tasks=false&allow_idle_behavior=false
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/auto-recharge-task-dispatched-to-decommissioned-robot-with-idle-behavior-false/53190](https://discourse.openrobotics.org/t/auto-recharge-task-dispatched-to-decommissioned-robot-with-idle-behavior-false/53190)
