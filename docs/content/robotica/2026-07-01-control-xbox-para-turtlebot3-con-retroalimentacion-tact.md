# Control Xbox para TurtleBot3 con retroalimentación táctil y freno

**Fecha:** 2026-07-01
**Categoría:** robotica
**Tags:** robotica, ia-local, linux
**Título original:** Xbox controller teleop for TurtleBot3, with a brake and haptic feedback (sim + real robot)

---

## Introducción

Un desarrollador ha creado un paquete ROS 2 para controlar un TurtleBot3 con un controlador Xbox Bluetooth, añadiendo retroalimentación táctil y freno. Esto permite una experiencia de conducción más realista y segura.

## ¿Qué es?

El paquete, llamado tb3_xbox_teleop, es una herramienta para controlar un TurtleBot3 utilizando un controlador Xbox Bluetooth. Permite que el usuario controle el robot con un joystick en el que la parte izquierda se utiliza para avanzar y la parte derecha para girar.

## ¿Cómo funciona?

El paquete utiliza la biblioteca joy para enviar señales de retroalimentación táctil al controlador Xbox. La velocidad del robot se utiliza para determinar la intensidad de la retroalimentación. Además, se puede activar una advertencia de proximidad utilizando el lidar del robot.

## ¿Por qué importa?

Esta herramienta es importante porque permite una experiencia de conducción más realista y segura para los usuarios de TurtleBot3. También puede ser útil para fines de investigación y desarrollo en robótica.

## Consejo técnico

Si deseas probar el paquete tb3_xbox_teleop, asegúrate de instalar la biblioteca joy y configurar correctamente el controlador Xbox. Puedes encontrar más información en el repositorio de GitHub del proyecto.

```bash
ros2 run tb3_xbox_teleop
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/xbox-controller-teleop-for-turtlebot3-with-a-brake-and-haptic-feedback-sim-real-robot/55978](https://discourse.openrobotics.org/t/xbox-controller-teleop-for-turtlebot3-with-a-brake-and-haptic-feedback-sim-real-robot/55978)
