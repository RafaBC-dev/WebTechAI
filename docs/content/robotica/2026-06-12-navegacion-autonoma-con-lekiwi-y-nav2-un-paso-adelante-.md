# Navegación autónoma con LeKiwi y Nav2: un paso adelante en robótica

**Fecha:** 2026-06-12
**Categoría:** robotica
**Tags:** robotica, linux, python
**Título original:** Autonomous Navigation with LeKiwi and Nav2

---

## Introducción

Foxglove ha colaborado con Aditya Kamath para integrar Nav2 en su robot holónico LeKiwi. Este proyecto muestra cómo combinar tecnologías como ros2_control, localización, SLAM y navegación autónoma.

## ¿Qué es?

LeKiwi es un robot holónico que utiliza Nav2 para navegar de manera autónoma. Nav2 es un sistema de navegación autónoma que permite a los robots moverse de manera segura y eficiente en entornos desconocidos. La integración de ros2_control, localización y SLAM permite a LeKiwi mapear su entorno y ajustar su ruta en tiempo real.

## ¿Cómo funciona?

La integración de Nav2 en LeKiwi implica la combinación de varios componentes clave. El sistema de localización utiliza sensores como GPS y odómetros para determinar la posición y velocidad del robot. El sistema de SLAM mapea el entorno utilizando información de los sensores y la navegación autónoma utiliza algoritmos de planificación de rutas para determinar la mejor ruta a seguir. ros2_control se encarga de controlar los movimientos del robot.

## ¿Por qué importa?

Este proyecto es importante porque muestra cómo los robots pueden navegar de manera autónoma en entornos desconocidos. La integración de Nav2 y ros2_control permite a los robots adaptarse a cambios en su entorno y mejorar su eficiencia. Esto tiene aplicaciones en diversas áreas, como la exploración espacial, la robótica industrial y la asistencia a la personas con discapacidad.

## Consejo técnico

Si deseas implementar navegación autónoma en tu propio proyecto, considera utilizar Nav2 y ros2_control. Puedes empezar por instalar Nav2 en tu sistema de control y configurar los parámetros de navegación. Luego, puedes integrar ros2_control para controlar los movimientos del robot.

```bash
ros2 run nav2_bringup nav2_bringup --ros-args --params-file nav2_params.yaml
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/autonomous-navigation-with-lekiwi-and-nav2/55440](https://discourse.openrobotics.org/t/autonomous-navigation-with-lekiwi-and-nav2/55440)
