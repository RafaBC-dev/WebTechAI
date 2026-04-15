# Nueva tecnología para controlar robots con mayor precisión y estabilidad

**Fecha:** 2026-04-15
**Categoría:** robotica
**Tags:** robotica, linux, codigo
**Título original:** [Announcement] ROS2 Adaptive Admittance Controller

---

## Introducción

La comunidad de ROS (Robot Operating System) acaba de recibir una noticia emocionante: un nuevo controlador adaptativo de admisión que promete mejorar la precisión y estabilidad de los robots en aplicaciones de manipulación física.

## ¿Qué es?

El controlador adaptativo de admisión es un componente de software diseñado para trabajar en conjunto con otros controladores de robot, como el controlador de trayectoria de articulaciones. Su función principal es permitir que el robot se comporte de manera flexible y adaptable en situaciones de contacto físico, como la asamblea de piezas o la teleoperación avanzada.

## ¿Cómo funciona?

El controlador adaptativo de admisión utiliza un algoritmo de control de admisión que calcula una velocidad de giro (twist) basada en los parámetros de admisión (rigidez, amortiguación, masa, comando de momento, ejes activos y marco de complacencia) y los parámetros del herramienta (masa y centro de gravedad). También incluye un filtro de paso bajo para suavizar los valores de momento recibidos del sensor de fuerza y torque.

## ¿Por qué importa?

La capacidad de reconfigurar los parámetros de admisión de manera gradual y segura es fundamental en aplicaciones de manipulación física, donde la estabilidad del robot es crucial. Además, la capacidad de estimar y mitigar el sesgo del sensor de fuerza y torque mejora la calidad del comportamiento complaciente del robot.

## Consejo técnico

Si deseas implementar este controlador en tu proyecto de robot, asegúrate de utilizar la biblioteca de ROS2 Jazzy y de configurar correctamente los parámetros de admisión y herramienta. También es recomendable utilizar un filtro de paso bajo para suavizar los valores de momento recibidos del sensor de fuerza y torque.

```bash
ros2 run adaptive_admittance_controller
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/announcement-ros2-adaptive-admittance-controller/54027](https://discourse.openrobotics.org/t/announcement-ros2-adaptive-admittance-controller/54027)
