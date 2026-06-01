# Actualización de Ubuntu 26.04 afecta a robot Lyrical-Dave

**Fecha:** 2026-06-01
**Categoría:** linux
**Tags:** robotica, linux, python
**Título original:** Upgrading to Ubuntu 26.04 (Python 3.14) Made Robot Lyrical-Dave's Life Messy

---

## Introducción

Un usuario ha experimentado problemas con su robot Lyrical-Dave después de actualizar a Ubuntu 26.04, debido a cambios en la versión de Python 3.14. Este incidente resalta la importancia de probar y validar las actualizaciones antes de implementarlas en entornos críticos.

## ¿Qué es?

Ubuntu 26.04 es una versión actualizada del sistema operativo Ubuntu, que incluye la versión 3.14 de Python. Lyrical-Dave es un robot controlado por ROS 2 (Robot Operating System 2) y utiliza la plataforma GoPiGo3. El robot es una implementación de una entidad digital llamada 'tt', que ha sido registrada desde 2014.

## ¿Cómo funciona?

La actualización a Ubuntu 26.04 incluyó cambios en la versión de Python 3.14, que afectaron a la compatibilidad de Lyrical-Dave. El robot utiliza ROS 2 para controlar sus acciones y la plataforma GoPiGo3 para interactuar con el entorno. La versión 3.14 de Python introdujo cambios en la sintaxis y la compatibilidad con bibliotecas, lo que causó problemas en el funcionamiento del robot.

## ¿Por qué importa?

Este incidente es importante porque resalta la necesidad de probar y validar las actualizaciones antes de implementarlas en entornos críticos. La actualización a Ubuntu 26.04 y la versión 3.14 de Python puede afectar a otros robots y sistemas que utilicen ROS 2 y GoPiGo3.

## Consejo técnico

Si estás utilizando ROS 2 y GoPiGo3, asegúrate de probar y validar la compatibilidad de tu sistema con la versión 3.14 de Python antes de actualizar a Ubuntu 26.04.

```bash
python3.14 -c 'import sys; print(sys.version)'
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/upgrading-to-ubuntu-26-04-python-3-14-made-robot-lyrical-daves-life-messy/55186](https://discourse.openrobotics.org/t/upgrading-to-ubuntu-26-04-python-3-14-made-robot-lyrical-daves-life-messy/55186)
