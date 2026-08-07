# ROS 2: Herramienta de monitoreo de rendimiento para bibliotecas de clientes

**Fecha:** 2026-08-07
**Categoría:** linux
**Tags:** robotica, linux, codigo
**Título original:** [GSoC 2026] ROS 2 Client Library Performance Monitoring: Midterm Progress Update

---

## Introducción

La Organización de Software de Robótica (OSRF) ha estado trabajando en una herramienta para monitorear el rendimiento de las bibliotecas de clientes de ROS 2. Esta herramienta permitirá a los desarrolladores comparar y entender mejor los resultados de las pruebas de rendimiento.

## ¿Qué es?

La herramienta de monitoreo de rendimiento de ROS 2 es un proyecto que conecta la ejecución de pruebas de rendimiento, el procesamiento de resultados y la visualización. Su objetivo es hacer que los resultados sean más fáciles de reproducir, comparar y entender.

## ¿Cómo funciona?

La herramienta proporciona un flujo de trabajo de línea de comandos para ejecutar una matriz reducida de pruebas de rendimiento de rclcpp. Cubre la comunicación publica/suscripción, llamadas de cliente/servicio, tamaños de mensajes múltiples, implementaciones de middleware, modos de comunicación y diseños de proceso único/múltiple.

## ¿Por qué importa?

La herramienta de monitoreo de rendimiento de ROS 2 es importante porque permite a los desarrolladores comparar y entender mejor los resultados de las pruebas de rendimiento. Esto es especialmente útil en robots que tienen diferentes necesidades y requieren diferentes configuraciones.

## Consejo técnico

Para empezar a utilizar la herramienta de monitoreo de rendimiento de ROS 2, ejecuta el comando `ros2-performance-monitoring run` para ejecutar la matriz reducida de pruebas de rendimiento de rclcpp.

```bash
ros2-performance-monitoring run
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/gsoc-2026-ros-2-client-library-performance-monitoring-midterm-progress-update/57204](https://discourse.openrobotics.org/t/gsoc-2026-ros-2-client-library-performance-monitoring-midterm-progress-update/57204)
