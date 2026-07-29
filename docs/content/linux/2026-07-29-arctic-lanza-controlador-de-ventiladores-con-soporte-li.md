# ARCTIC lanza controlador de ventiladores con soporte Linux desde el inicio

**Fecha:** 2026-07-29
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** ARCTIC Launches Its New Fan Controller That Already Has Mainline Linux Support

---

## Introducción

La empresa ARCTIC ha lanzado un nuevo controlador de ventiladores que ya cuenta con soporte en el núcleo de Linux, lo que lo hace muy interesante para los usuarios de este sistema operativo.

## ¿Qué es?

El controlador de ventiladores ARCTIC es un dispositivo que permite controlar y monitorear hasta 10 ventiladores en un sistema. Se conecta a la placa base mediante un puerto USB y utiliza un driver open-source para interactuar con el sistema operativo.

## ¿Cómo funciona?

El driver del controlador de ventiladores ARCTIC se ha integrado en el núcleo de Linux desde la versión 7.2, lo que significa que los usuarios pueden configurarlo y utilizarlo sin necesidad de instalar software adicional. El controlador utiliza la interfaz HWMON de Linux para controlar y monitorear los ventiladores.

## ¿Por qué importa?

Este controlador de ventiladores es importante porque es uno de los primeros en ofrecer soporte en el núcleo de Linux desde el inicio. Esto significa que los usuarios de Linux pueden utilizarlo sin necesidad de realizar modificaciones o instalar software adicional.

## Consejo técnico

Si deseas utilizar el controlador de ventiladores ARCTIC con Linux, asegúrate de instalar el driver en tu sistema operativo utilizando el comando `sudo apt-get install arctic-fan-controller` o `sudo dnf install arctic-fan-controller` dependiendo de tu distribución de Linux.

```bash
sudo apt-get install arctic-fan-controller
```

---

**Fuente original:** [https://www.phoronix.com/news/ARCTIC-Fan-Controller-Launches](https://www.phoronix.com/news/ARCTIC-Fan-Controller-Launches)
