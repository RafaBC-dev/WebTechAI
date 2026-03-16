# Rewire: una herramienta para visualizar temas ROS 2 con cero dependencias

**Fecha:** 2026-03-16
**Categoría:** linux
**Tags:** robotica, linux, codigo
**Título original:** Rewire — stream ROS 2 topics to Rerun with zero ROS 2 build dependencies

---

## Introducción

Una nueva herramienta llamada Rewire permite visualizar temas ROS 2 en tiempo real sin necesidad de instalar dependencias adicionales. Esto puede ser especialmente útil para desarrolladores de robótica que buscan simplificar su proceso de visualización.

## ¿Qué es?

Rewire es una herramienta de código abierto que se ejecuta como un solo archivo binario en Rust. Actúa como un observador pasivo que streamea temas ROS 2 a Rerun, una herramienta de visualización en tiempo real. No requiere instalación de ROS 2 ni configuración de middleware.

## ¿Cómo funciona?

Rewire habla directamente con los protocolos de cable de DDS y Zenoh, y utiliza un archivo de configuración JSON5 para mapear tipos de mensajes ROS 2 a arquetipos de Rerun. Puede visualizar temas de sensores, geometría, navegación, transformaciones, visión y más.

## ¿Por qué importa?

Rewire resuelve problemas comunes en la visualización de temas ROS 2, como la necesidad de instalar dependencias adicionales y configurar middleware. Esto permite a los desarrolladores de robótica enfocarse en su trabajo sin tener que preocuparse por la complejidad de la visualización.

## Consejo técnico

Si deseas utilizar Rewire, puedes instalarlo ejecutando el comando `curl -fsSL https://rewire.run/install.sh | sh` y luego utilizar el comando `rewire record -a` para subscribirte a todos los temas.

```bash
curl -fsSL https://rewire.run/install.sh | sh
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/rewire-stream-ros-2-topics-to-rerun-with-zero-ros-2-build-dependencies/53233](https://discourse.openrobotics.org/t/rewire-stream-ros-2-topics-to-rerun-with-zero-ros-2-build-dependencies/53233)
