# Detectar colapso de ejecución antes del E-stop: ros2_kinematic_guard

**Fecha:** 2026-05-19
**Categoría:** robotica
**Tags:** robotica, linux, codigo
**Título original:** Detecting execution collapse before hard E-stop: ros2_kinematic_guard for ROS 2 AMR/AGV

---

## Introducción

Un nuevo paquete de ROS 2 llamado ros2_kinematic_guard busca detectar colapso de ejecución en sistemas de robots móviles antes de que el sistema de seguridad intervenga. Esto puede evitar paradas bruscas y mejorar la disponibilidad del sistema.

## ¿Qué es?

ros2_kinematic_guard es un paquete de ROS 2 que actúa como un filtro de temas para detectar colapso de ejecución en sistemas de robots móviles. Monitorea el movimiento del robot y emite un mensaje de estado kinemático compacto cuando detecta inconsistencias en el movimiento. Puede también aplicar frenos o limitar la velocidad del robot en caso de detectar problemas.

## ¿Cómo funciona?

El paquete ros2_kinematic_guard funciona como un filtro de temas en ROS 2, monitoreando el tema /cmd_vel y el tema /odom. Cuando detecta inconsistencias en el movimiento del robot, emite un mensaje de estado kinemático compacto y puede aplicar frenos o limitar la velocidad del robot. Funciona en tres modos: observación pasiva, prueba de cableado y modo de guardia activo.

## ¿Por qué importa?

Detectar colapso de ejecución antes del E-stop puede evitar paradas bruscas y mejorar la disponibilidad del sistema. Esto puede reducir el tiempo de recuperación manual, la interrupción de la producción y la inestabilidad de la carga. Además, puede ayudar a identificar la causa raíz de los problemas durante la depuración posterior a incidentes.

## Consejo técnico

Para implementar ros2_kinematic_guard en tu sistema de robot móvil, puedes agregar el paquete a tu árbol de trabajo de ROS 2 y configurarlo para funcionar en el modo de guardia activo. Esto te permitirá detectar colapso de ejecución y aplicar frenos o limitar la velocidad del robot en caso de detectar problemas.

```bash
ros2 run ros2_kinematic_guard <nombre_de_la_nodo>
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/detecting-execution-collapse-before-hard-e-stop-ros2-kinematic-guard-for-ros-2-amr-agv/54944](https://discourse.openrobotics.org/t/detecting-execution-collapse-before-hard-e-stop-ros2-kinematic-guard-for-ros-2-amr-agv/54944)
