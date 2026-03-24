# KUKA LBRs ahora disponibles en RoboStack

**Fecha:** 2026-03-24
**Categoría:** robotica
**Tags:** robotica, linux, codigo
**Título original:** KUKA LBRs (iiwa and med) now on RoboStack

---

## Introducción

La noticia es que los robots KUKA iiwa y med ahora pueden ser instalados fácilmente en sistemas Linux gracias a RoboStack. Esto abre nuevas posibilidades para la robótica y la automatización en diversas industrias.

## ¿Qué es?

RoboStack es una herramienta de gestión de paquetes para Linux que permite instalar y configurar fácilmente herramientas y paquetes relacionados con la robótica y la automatización. Los KUKA LBRs son robots industriales de alta precisión diseñados para realizar tareas complejas en entornos de producción.

## ¿Cómo funciona?

Los drivers para los KUKA LBRs pueden ser instalados en RoboStack mediante el comando `pixi add` y especificando los paquetes necesarios. Esto incluye la instalación de la biblioteca FRI (Flexible Robot Interface) y la configuración de los robots en el entorno de trabajo.

## ¿Por qué importa?

La disponibilidad de los KUKA LBRs en RoboStack permite a los desarrolladores y usuarios de Linux aprovechar la potencia de estos robots industriales en sus proyectos de automatización y robótica. Esto puede ser especialmente útil en industrias como la manufactura, la logística y la medicina.

## Consejo técnico

Si deseas instalar los KUKA LBRs en tu sistema Linux, asegúrate de tener instalado RoboStack y ejecuta el comando `pixi add lbr-fri-client-sdk=1.x ros-jazzy-desktop ros-jazzy-lbr-fri-ros2-stack ros-jazzy-med7-moveit-config ros-jazzy-med14-moveit-config ros-jazzy-iiwa7-moveit-config ros-jazzy-iiwa14-moveit-config` para instalar los paquetes necesarios.

```bash
pixi add lbr-fri-client-sdk=1.x ros-jazzy-desktop ros-jazzy-lbr-fri-ros2-stack ros-jazzy-med7-moveit-config ros-jazzy-med14-moveit-config ros-jazzy-iiwa7-moveit-config ros-jazzy-iiwa14-moveit-config
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/kuka-lbrs-iiwa-and-med-now-on-robostack/53471](https://discourse.openrobotics.org/t/kuka-lbrs-iiwa-and-med-now-on-robostack/53471)
