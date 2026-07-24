# Barrera de carga de trabajo de navegación abierta para robots

**Fecha:** 2026-07-24
**Categoría:** robotica
**Tags:** robotica, ia-local, benchmarks
**Título original:** [Nav2] Open Navigation's Robotics Workload Benchmark Release

---

## Introducción

La comunidad de robótica acaba de recibir una herramienta valiosa para evaluar la capacidad de procesamiento de diferentes plataformas. La barra de carga de trabajo de navegación abierta es un conjunto de pruebas que simula la ejecución de un sistema de autonomía completo en un entorno de fábrica.

## ¿Qué es?

La barra de carga de trabajo de navegación abierta es un conjunto de pruebas que evalúa la capacidad de procesamiento de diferentes plataformas para ejecutar un sistema de autonomía completo. Este sistema incluye la gestión de 9 flujos de datos de sensores, como LIDAR y cámaras de profundidad, en un entorno de fábrica de 180.000 metros cuadrados.

## ¿Cómo funciona?

La barra de carga de trabajo se ejecuta en un entorno Dockerizado y puede ser ejecutada en cualquier hardware. La prueba simula la ejecución de un sistema de autonomía completo en un entorno de fábrica, incluyendo la gestión de sensores y la toma de decisiones. La prueba se puede ejecutar en diferentes plataformas, como AMD Strix Halo, NVIDIA Jetson Thor y Orin AGX.

## ¿Por qué importa?

Esta herramienta es importante porque permite a los desarrolladores de robótica evaluar la capacidad de procesamiento de diferentes plataformas de manera más realista. Esto puede ayudar a tomar decisiones informadas sobre la elección de la plataforma adecuada para un proyecto de robótica.

## Consejo técnico

Si deseas ejecutar la barra de carga de trabajo de navegación abierta en tu propio hardware, asegúrate de instalar Docker en tu sistema y seguir las instrucciones en la página de GitHub de Open Navigation.

```bash
docker run -it --rm open-navigation/benchmark
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/nav2-open-navigations-robotics-workload-benchmark-release/56909](https://discourse.openrobotics.org/t/nav2-open-navigations-robotics-workload-benchmark-release/56909)
