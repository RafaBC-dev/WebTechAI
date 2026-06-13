# ROS2: comunicación multi-máquina entre WSL2 y Linux

**Fecha:** 2026-06-13
**Categoría:** robotica
**Tags:** robotica, linux, codigo
**Título original:** ROS2 multi-machine with WSL2 + Linux (NVIDIA Jetson Orin Nano)

---

## Introducción

Un usuario de ROS2 está intentando establecer comunicación entre su máquina local con WSL2 (Ubuntu 22.04) y una plataforma Linux nativa, específicamente la NVIDIA Jetson Orin Nano. Sin embargo, está experimentando problemas para que las dos máquinas puedan ver los temas y nodos respectivos.

## ¿Qué es?

ROS2 (Robot Operating System 2) es una plataforma de software de código abierto para la robótica que permite a los desarrolladores crear y desplegar sistemas de control de robots de manera eficiente. La comunicación multi-máquina es una característica clave de ROS2 que permite a los robots y los sistemas de control comunicarse entre sí de manera segura y eficiente.

## ¿Cómo funciona?

Para establecer comunicación entre WSL2 y la NVIDIA Jetson Orin Nano, el usuario debe configurar la red de manera que las dos máquinas puedan comunicarse entre sí. Esto se puede lograr activando el modo de red de reflejo en WSL2 utilizando la bandera `networkingMode=mirrored`. Además, se pueden utilizar herramientas como Cyclone y FastDDS para configurar la comunicación entre las dos máquinas.

## ¿Por qué importa?

La comunicación multi-máquina es fundamental en la robótica para permitir a los robots y los sistemas de control compartir información y coordinar sus acciones de manera eficiente. En este caso, la comunicación entre WSL2 y la NVIDIA Jetson Orin Nano permite al usuario generar datos en una máquina y procesarlos en la otra, lo que puede ser útil en aplicaciones como la visión artificial y la control de robots.

## Consejo técnico

Si estás experimentando problemas para establecer comunicación entre WSL2 y una plataforma Linux nativa, asegúrate de activar el modo de red de reflejo en WSL2 y de configurar la comunicación utilizando herramientas como Cyclone y FastDDS. También es importante verificar que las dos máquinas estén conectadas a la misma red y que no haya problemas de configuración en el sistema de red.

```bash
wsl --set-default-version 2 && wsl --install -d Ubuntu-22.04 && wsl --import Ubuntu-22.04 <nombre_de_la_maquina> <ruta_de_la_maquina>
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/ros2-multi-machine-with-wsl2-linux-nvidia-jetson-orin-nano/55452](https://discourse.openrobotics.org/t/ros2-multi-machine-with-wsl2-linux-nvidia-jetson-orin-nano/55452)
