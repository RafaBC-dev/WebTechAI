# Fusión de tecnologías de navegación robótica con rtabmap_ros

**Fecha:** 2026-05-20
**Categoría:** robotica
**Tags:** robotica, linux, codigo
**Título original:** FusionCore + icp_odometry feedback loop merged into rtabmap_ros

---

## Introducción

La comunidad de robótica ha logrado un avance significativo en la navegación de robots con la fusión de tecnologías de navegación robótica en el proyecto rtabmap_ros. Esta integración permite a los robots navegar de manera más precisa y eficiente en entornos complejos.

## ¿Qué es?

rtabmap_ros es un proyecto de software de navegación robótica que utiliza tecnologías de visión computacional y sensoriamento para permitir a los robots navegar en entornos desconocidos. La integración de FusionCore y icp_odometry en rtabmap_ros permite a los robots utilizar información de sensores de inercia y ruedas para mejorar la precisión de la navegación.

## ¿Cómo funciona?

La integración de FusionCore y icp_odometry en rtabmap_ros funciona de la siguiente manera: FusionCore utiliza información de sensores de inercia y ruedas para estimar la posición y velocidad del robot, mientras que icp_odometry utiliza información de visión computacional para mejorar la precisión de la navegación. La información de icp_odometry se utiliza como retroalimentación para mejorar la precisión de la estimación de FusionCore.

## ¿Por qué importa?

Esta integración es importante porque permite a los robots navegar de manera más precisa y eficiente en entornos complejos, lo que es esencial para aplicaciones como la exploración de entornos desconocidos, la búsqueda y rescate, y la navegación en entornos urbanos.

## Consejo técnico

Si deseas implementar esta tecnología en tu propio proyecto de robótica, puedes empezar por instalar los paquetes necesarios con el comando `sudo apt install ros-jazzy-fusioncore-ros ros-jazzy-rtabmap-ros` y luego lanzar el demo con el comando `ros2 launch rtabmap_demos turtlebot3_sim_fusioncore_icp_demo.launch.py`.

```bash
sudo apt install ros-jazzy-fusioncore-ros ros-jazzy-rtabmap-ros ros-jazzy-turtlebot3-gazebo ros-jazzy-nav2-bringup
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/fusioncore-icp-odometry-feedback-loop-merged-into-rtabmap-ros/54963](https://discourse.openrobotics.org/t/fusioncore-icp-odometry-feedback-loop-merged-into-rtabmap-ros/54963)
