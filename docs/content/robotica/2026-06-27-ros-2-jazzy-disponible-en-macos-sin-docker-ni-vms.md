# ROS 2 Jazzy disponible en macOS sin Docker ni VMs

**Fecha:** 2026-06-27
**Categoría:** robotica
**Tags:** robotica, linux, codigo
**Título original:** 🍺 ros2-jazzy is now available on Homebrew!

---

## Introducción

La comunidad de robótica y sistemas embebidos ha ganado un gran aliado con la llegada de ROS 2 Jazzy en macOS. Gracias a Homebrew, ahora es posible instalar este entorno de desarrollo de manera nativa en tu máquina macOS sin necesidad de utilizar Docker ni VMs.

## ¿Qué es?

ROS 2 Jazzy es una distribución de ROS 2, un framework de software de código abierto para la robótica y los sistemas embebidos. Permite la creación de aplicaciones de robótica y automatización de manera eficiente y escalable. Con ROS 2 Jazzy, puedes desarrollar y ejecutar aplicaciones de robótica en tu máquina macOS sin necesidad de utilizar Docker ni VMs.

## ¿Cómo funciona?

Para instalar ROS 2 Jazzy en macOS, debes agregar el repositorio de Homebrew para ROS 2 mediante el comando `brew tap idesign0/ros2` y luego instalar la distribución mediante `brew install ros2-jazzy`. Esto te permitirá acceder a una variedad de herramientas y librerías de robótica, incluyendo Gazebo, ros2_control, MoveIt 2 y Nav2.

## ¿Por qué importa?

La disponibilidad de ROS 2 Jazzy en macOS es importante porque permite a los desarrolladores de robótica y sistemas embebidos trabajar de manera nativa en su máquina macOS, lo que facilita la creación de aplicaciones de robótica y automatización. Además, la integración con Homebrew hace que sea fácil de instalar y mantener.

## Consejo técnico

Si estás interesado en probar ROS 2 Jazzy, te recomiendo comenzar con los tutoriales de MoveIt 2 y TurtleBot4 disponibles en el repositorio de Ros2_macos. Estos tutoriales te guiarán a través del proceso de configuración y ejecución de aplicaciones de robótica en macOS.

```bash
brew tap idesign0/ros2 && brew install ros2-jazzy
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/ros2-jazzy-is-now-available-on-homebrew/55737](https://discourse.openrobotics.org/t/ros2-jazzy-is-now-available-on-homebrew/55737)
