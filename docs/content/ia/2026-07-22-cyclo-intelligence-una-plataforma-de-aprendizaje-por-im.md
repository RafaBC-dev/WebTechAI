# Cyclo Intelligence: una plataforma de aprendizaje por imitación para robótica

**Fecha:** 2026-07-22
**Categoría:** ia
**Tags:** robotica, ia-local, linux
**Título original:** Guide to Imitation Learning with Cyclo Intelligence

---

## Introducción

La ROBOTIS Humanoid Division ha lanzado Cyclo Intelligence, una plataforma de aprendizaje por imitación para robótica que simplifica el proceso de aprendizaje de robots humanoides. Esta herramienta es fundamental para desarrollar inteligencia artificial física y manipulación robótica.

## ¿Qué es?

Cyclo Intelligence es una plataforma de aprendizaje por imitación que permite a los robots humanoides aprender de la experiencia humana. Utiliza datos de teleoperación para entrenar modelos que puedan realizar tareas complejas de manera autónoma.

## ¿Cómo funciona?

Cyclo Intelligence integra la recopilación de datos de teleoperación, la conversión de datos, el entrenamiento de modelos y la inferencia en tiempo real en un pipeline end-to-end. Soporta ROS 2 Zenoh RMW, ejecución en contenedores Docker y una interfaz web intuitiva.

## ¿Por qué importa?

Cyclo Intelligence es esencial para desarrollar inteligencia artificial física y manipulación robótica. Permite a los robots humanoides aprender de la experiencia humana y realizar tareas complejas de manera autónoma, lo que puede mejorar la eficiencia y la precisión en diversas aplicaciones.

## Consejo técnico

Si deseas explorar Cyclo Intelligence, puedes comenzar descargando el código de GitHub y configurando un entorno de desarrollo con Docker. Asegúrate de revisar la documentación oficial para obtener instrucciones detalladas sobre la instalación y el uso de la plataforma.

```bash
docker run -it --rm -v $PWD:/app robotis/cyclo_intelligence:latest
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/guide-to-imitation-learning-with-cyclo-intelligence/56851](https://discourse.openrobotics.org/t/guide-to-imitation-learning-with-cyclo-intelligence/56851)
