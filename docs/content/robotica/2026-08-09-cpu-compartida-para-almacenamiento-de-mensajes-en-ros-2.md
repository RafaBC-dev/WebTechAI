# CPU compartida para almacenamiento de mensajes en ROS 2

**Fecha:** 2026-08-09
**Categoría:** robotica
**Tags:** robotica, linux, codigo
**Título original:** Has a CPU shared-memory backend for rosidl::Buffer been explored?

---

## Introducción

Los desarrolladores de ROS 2 están explorando la posibilidad de implementar un backend de memoria compartida en el CPU para almacenar mensajes de gran tamaño, como imágenes y nubes de puntos.

## ¿Qué es?

rosidl::Buffer es una capa de abstracción que permite almacenar mensajes en memoria compartida, lo que permite evitar copias de los datos y mejorar el rendimiento. Un backend de memoria compartida en el CPU sería una implementación específica de esta capa que aprovecharía la memoria compartida del procesador para almacenar los mensajes.

## ¿Cómo funciona?

La idea es que el backend de memoria compartida en el CPU permita almacenar los mensajes en memoria compartida del procesador, lo que permitiría evitar copias de los datos y mejorar el rendimiento. Esto se lograría mediante la creación de un descriptor o referencia que se utilizaría para transportar los mensajes entre procesos.

## ¿Por qué importa?

Un backend de memoria compartida en el CPU podría mejorar significativamente el rendimiento de ROS 2, especialmente en aplicaciones que manejan grandes cantidades de datos, como la visión por computadora y la procesamiento de señales.

## Consejo técnico

Si estás desarrollando aplicaciones con ROS 2 y manejas grandes cantidades de datos, considera investigar sobre la implementación de un backend de memoria compartida en el CPU para mejorar el rendimiento de tus aplicaciones.

```bash
ros2_cuda_ipc: Zero-copy GPU data sharing between ROS 2 processes
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/has-a-cpu-shared-memory-backend-for-rosidl-buffer-been-explored/57240](https://discourse.openrobotics.org/t/has-a-cpu-shared-memory-backend-for-rosidl-buffer-been-explored/57240)
