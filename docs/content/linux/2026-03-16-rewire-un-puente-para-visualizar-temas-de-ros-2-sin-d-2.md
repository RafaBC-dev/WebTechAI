# Rewire: un puente para visualizar temas de ROS 2 sin dependencias

**Fecha:** 2026-03-16
**Categoría:** linux
**Tags:** robotica, linux, codigo
**Título original:** Rewire — stream ROS 2 topics to Rerun with zero ROS 2 build dependencies

---

## Introducción

Un desarrollador ha creado Rewire, un puente que permite visualizar temas de ROS 2 sin necesidad de instalar dependencias adicionales. Esto simplifica la configuración de herramientas de visualización en entornos de ROS 2.

## ¿Qué es?

Rewire es un puente de código Rust que habla protocolos de cable de DDS y Zenoh directamente. No es un nodo de ROS 2, por lo que no se une al grafo de ROS ni requiere instalación de ROS 2. Actúa como un observador pasivo. Rewire se ejecuta como un solo archivo binario y puede conectarse a una red de DDS/Zenoh para visualizar temas en tiempo real.

## ¿Cómo funciona?

Rewire utiliza un archivo de configuración JSON5 para mapear tipos de mensajes de ROS 2 a arquetipos de Rerun. Esto permite visualizar mensajes personalizados sin necesidad de recompilar el código. El puente también puede cargar URDF, visualizar árboles de transformaciones y mostrar diagnósticos de temas.

## ¿Por qué importa?

Rewire resuelve el problema de la configuración de herramientas de visualización en ROS 2, que a menudo implica instalar dependencias y configurar middleware. Esto permite a los desarrolladores enfocarse en la programación y la experimentación, en lugar de la configuración.

## Consejo técnico

Si deseas probar Rewire, ejecuta el comando `curl -fsSL https://rewire.run/install.sh | sh` para instalar el puente, y luego ejecuta `rewire record -a` para suscribirte a todos los temas.

```bash
curl -fsSL https://rewire.run/install.sh | sh
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/rewire-stream-ros-2-topics-to-rerun-with-zero-ros-2-build-dependencies/53233](https://discourse.openrobotics.org/t/rewire-stream-ros-2-topics-to-rerun-with-zero-ros-2-build-dependencies/53233)
