# Robot Autónomo Abierto con Navegación, Visión y Asistencia por Voz

**Fecha:** 2026-06-07
**Categoría:** robotica
**Tags:** robotica, ia-local, linux
**Título original:** Introducing an Open-Source Autonomous Navigation & Interactive Robot

---

## Introducción

Un desarrollador está creando un robot autónomo abierto que combina navegación, visión por computadora, interacción por voz y asistencia por inteligencia artificial. Este proyecto busca proporcionar una plataforma para la investigación y el desarrollo de robots autónomos.

## ¿Qué es?

El robot autónomo es una plataforma abierta que utiliza tecnologías como ROS2, MediaPipe y RTAB-Map para navegar y interactuar con su entorno. Está equipado con sensores como LiDAR, cámaras y sensores de voz, lo que le permite detectar obstáculos, reconocer rostros y gestos, y responder a comandos por voz.

## ¿Cómo funciona?

El robot utiliza un sistema de control motorizado para moverse por el entorno, mientras que la tecnología LiDAR proporciona información sobre la topografía del entorno. La cámara y la tecnología de visión por computadora permiten al robot reconocer objetos y personas, y la asistencia por voz se realiza mediante la integración de un asistente de voz como Whisper. El robot también utiliza la tecnología de Docker para contener y ejecutar aplicaciones en tiempo real.

## ¿Por qué importa?

Este proyecto es importante porque proporciona una plataforma abierta para la investigación y el desarrollo de robots autónomos. También permite a los desarrolladores experimentar con tecnologías como la navegación autónoma, la visión por computadora y la asistencia por voz en un entorno realista.

## Consejo técnico

Si deseas experimentar con la tecnología de ROS2, puedes comenzar creando un proyecto de navegación autónoma utilizando el paquete de navegación de ROS2. Puedes utilizar el comando `ros2 launch` para iniciar un proyecto de navegación y configurar la ruta de navegación utilizando el archivo `nav2_config.yaml`.

```bash
ros2 launch
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/introducing-an-open-source-autonomous-navigation-interactive-robot/55286](https://discourse.openrobotics.org/t/introducing-an-open-source-autonomous-navigation-interactive-robot/55286)
