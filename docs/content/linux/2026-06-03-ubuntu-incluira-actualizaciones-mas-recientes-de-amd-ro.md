# Ubuntu incluirá actualizaciones más recientes de AMD ROCm

**Fecha:** 2026-06-03
**Categoría:** linux
**Tags:** ia-local, linux, codigo
**Título original:** Ubuntu To Ship Newer AMD ROCm Updates Via SRUs

---

## Introducción

Ubuntu planea mejorar su soporte para la computación de GPU de AMD, permitiendo a los usuarios obtener actualizaciones más recientes de AMD ROCm sin tener que esperar a una nueva versión de Ubuntu. Esto es especialmente importante para la comunidad de inteligencia artificial, ya que ROCm es una herramienta crucial para el desarrollo de modelos de IA.

## ¿Qué es?

AMD ROCm es una plataforma de computación de GPU abierta que permite a los desarrolladores crear aplicaciones de alta performance para procesamiento de datos y aprendizaje automático. Se basa en el lenguaje de programación OpenCL y ofrece una API para acceder a las capacidades de GPU de los dispositivos AMD.

## ¿Cómo funciona?

Para aprovechar las actualizaciones más recientes de ROCm, los usuarios de Ubuntu pueden utilizar el comando `apt install rocm` para instalar la plataforma. Sin embargo, hasta ahora, Ubuntu ha estado utilizando una versión de ROCm que es meses más antigua que la versión más reciente disponible. Para mejorar esto, Canonical, el equipo detrás de Ubuntu, planea utilizar la técnica de actualizaciones de liberación estable (SRU) para proporcionar actualizaciones más recientes de ROCm a los usuarios.

## ¿Por qué importa?

Las actualizaciones más recientes de ROCm ofrecen mejoras significativas en rendimiento y funcionalidad, lo que es especialmente importante para la comunidad de inteligencia artificial. Algunas de las mejoras incluyen soporte para nuevas características de hardware de AMD y mejoras en la compatibilidad con aplicaciones de IA.

## Consejo técnico

Si estás utilizando Ubuntu y necesitas actualizaciones más recientes de ROCm, puedes verificar si hay actualizaciones disponibles ejecutando el comando `apt list --upgradable` y luego instalando las actualizaciones con `apt install <paquete>`. También es recomendable seguir las instrucciones de Canonical para asegurarte de que las actualizaciones se instalen de manera segura.

```bash
apt install rocm
```

---

**Fuente original:** [https://www.phoronix.com/news/Ubuntu-Newer-ROCm-SRUs](https://www.phoronix.com/news/Ubuntu-Newer-ROCm-SRUs)
