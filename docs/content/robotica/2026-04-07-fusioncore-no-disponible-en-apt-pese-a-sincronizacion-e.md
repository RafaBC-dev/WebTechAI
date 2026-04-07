# FusionCore no disponible en apt pese a sincronización exitosa

**Fecha:** 2026-04-07
**Categoría:** robotica
**Tags:** robotica, linux, codigo
**Título original:** Ros-jazzy-fusioncore-ros not available via apt despite build farm showing SYNC

---

## Introducción

La biblioteca FusionCore, que se ha integrado en rosdistro, no se encuentra disponible en apt a pesar de haber sido sincronizada con éxito. Esto ha llevado a una pregunta sobre qué pasos se deben seguir para que se publique en apt.

## ¿Qué es?

FusionCore es una biblioteca de software que se ha integrado en rosdistro, un sistema de gestión de paquetes para ROS (Robot Operating System). Permite la creación de aplicaciones de robótica de manera más sencilla y eficiente.

## ¿Cómo funciona?

La biblioteca FusionCore se ha integrado en rosdistro a través de un pull request (PR) #50462. El build farm de rosdistro ha sincronizado con éxito los paquetes fusioncore_core, fusioncore_ros, fusioncore_gazebo y compass_msgs. Sin embargo, el paquete ros-jazzy-fusioncore-ros no se encuentra disponible en apt.

## ¿Por qué importa?

La disponibilidad de FusionCore en apt es importante para los desarrolladores de aplicaciones de robótica, ya que les permite instalar y utilizar la biblioteca de manera fácil y sencilla. Esto puede ayudar a acelerar el desarrollo de aplicaciones de robótica y mejorar su calidad.

## Consejo técnico

Para verificar la disponibilidad de FusionCore en apt, puedes utilizar el comando `sudo apt install ros-jazzy-fusioncore-ros` y verificar si se encuentra disponible. Si no está disponible, puedes intentar sincronizar manualmente los paquetes con el comando `sudo apt update` y luego `sudo apt install ros-jazzy-fusioncore-ros`.

```bash
sudo apt install ros-jazzy-fusioncore-ros
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/ros-jazzy-fusioncore-ros-not-available-via-apt-despite-build-farm-showing-sync/53841](https://discourse.openrobotics.org/t/ros-jazzy-fusioncore-ros-not-available-via-apt-despite-build-farm-showing-sync/53841)
