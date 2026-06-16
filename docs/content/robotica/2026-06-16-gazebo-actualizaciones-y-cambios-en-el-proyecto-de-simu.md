# Gazebo: Actualizaciones y cambios en el proyecto de simulación de robótica

**Fecha:** 2026-06-16
**Categoría:** robotica
**Tags:** robotica, linux, codigo
**Título original:** Gazebo PMC Meeting Minutes 2026-06-15

---

## Introducción

La comunidad de Gazebo ha tenido una reunión para discutir y aprobar cambios importantes en el proyecto. Entre ellos, la adición de un nuevo miembro como comitente, la revisión de propuestas de financiación y la transición a una nueva biblioteca de carga de meshes.

## ¿Qué es?

Gazebo es un proyecto de simulación de robótica que permite a los desarrolladores crear y probar entornos virtuales para robots y sistemas embebidos. Es una herramienta fundamental para la investigación y el desarrollo de aplicaciones de robótica.

## ¿Cómo funciona?

Gazebo utiliza una arquitectura de simulación en tiempo real, que permite a los desarrolladores crear entornos virtuales que se comportan de manera similar a los reales. La simulación se basa en una serie de componentes, como la física, la gráfica y la interacción con el usuario.

## ¿Por qué importa?

Estos cambios en Gazebo son importantes porque permiten a los desarrolladores crear simulaciones más realistas y complejas, lo que a su vez facilita la investigación y el desarrollo de aplicaciones de robótica. Además, la transición a una nueva biblioteca de carga de meshes permitirá a los desarrolladores cargar y visualizar meshes de manera más eficiente.

## Consejo técnico

Si estás trabajando con Gazebo, te recomiendo probar la nueva biblioteca de carga de meshes Assimp, que se ha integrado en la última versión de Gazebo. Puedes hacerlo configurando la variable de entorno `GAZEBO_MODEL_PATH` con el directorio donde se encuentran tus meshes.

```bash
export GAZEBO_MODEL_PATH=/path/a/tus/meshes
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/gazebo-pmc-meeting-minutes-2026-06-15/55498](https://discourse.openrobotics.org/t/gazebo-pmc-meeting-minutes-2026-06-15/55498)
