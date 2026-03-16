# Rewire: un puente para visualizar temas de ROS 2 sin dependencias

**Fecha:** 2026-03-16
**Categoría:** linux
**Tags:** robotica, linux, codigo
**Título original:** Rewire — stream ROS 2 topics to Rerun with zero ROS 2 build dependencies

---

## Introducción

Desarrolladores de ROS 2, ahora podéis visualizar temas de vuestros proyectos sin necesidad de instalar herramientas adicionales. Rewire es el nombre de este puente que os permite ver en tiempo real lo que está sucediendo en vuestros proyectos.

## ¿Qué es?

Rewire es un puente que permite visualizar temas de ROS 2 en tiempo real sin necesidad de instalar dependencias adicionales. Es un binario de Rust que habla directamente con los protocolos de cable de DDS y Zenoh, y no requiere la instalación de ROS 2 ni la creación de nodos.

## ¿Cómo funciona?

Rewire funciona como un observador pasivo que se conecta a una red de DDS/Zenoh y comienza a visualizar los temas en tiempo real. Puedes utilizar el comando `rewire record -a` para suscribirte a todos los temas y visualizarlos en tiempo real.

## ¿Por qué importa?

Rewire es importante porque resuelve un problema común en la visualización de temas de ROS 2: la necesidad de instalar dependencias adicionales y configurar middleware. Ahora, puedes visualizar tus temas en tiempo real sin necesidad de hacer esto.

## Consejo técnico

Si deseas empezar a utilizar Rewire, te recomiendo que primero te asegures de que tengas instalado Rust en tu sistema. Luego, puedes instalar Rewire utilizando el comando `curl -fsSL https://rewire.run/install.sh | sh`.

```bash
curl -fsSL https://rewire.run/install.sh | sh
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/rewire-stream-ros-2-topics-to-rerun-with-zero-ros-2-build-dependencies/53233](https://discourse.openrobotics.org/t/rewire-stream-ros-2-topics-to-rerun-with-zero-ros-2-build-dependencies/53233)
