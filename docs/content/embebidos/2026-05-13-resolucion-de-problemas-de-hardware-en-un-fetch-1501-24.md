# Resolución de problemas de hardware en un Fetch 1501: 24V Rail no activado

**Fecha:** 2026-05-13
**Categoría:** embebidos
**Tags:** robotica, hardware, electronica
**Título original:** Hardware Troubleshooting: Fetch 1501 Main Board - 24V Rail Not Activating

---

## Introducción

Un propietario de un Fetch 1501 está experimentando problemas con el rail de 24V, que no se activa a pesar de tener una entrada de 48V. El propietario busca ayuda para diagnosticar y resolver el problema.

## ¿Qué es?

El Fetch 1501 es un robot industrial que utiliza un sistema de distribución de poder propietario. El sistema de poder incluye una entrada de 48V y un rail de 24V que se utiliza para alimentar el robot.

## ¿Cómo funciona?

El Fetch 1501 utiliza un controlador STM32 para gestionar el sistema de poder. El controlador recibe la entrada de 48V y la utiliza para alimentar el rail de 24V. Sin embargo, en este caso, el rail de 24V no se está activando a pesar de que la entrada de 48V está presente.

## ¿Por qué importa?

El problema del rail de 24V no activado puede ser un problema crítico para el funcionamiento del robot. Si no se resuelve, puede provocar problemas de seguridad y daños al equipo.

## Consejo técnico

Para diagnosticar el problema, es recomendable verificar la presencia de una señal de enable en el pin 4 del chip PS2492. También es importante comprobar la limpieza de la área donde se encuentra el chip U9 y verificar la presencia de una señal de 24V en el rail de salida.

```bash
Verificar la presencia de una señal de enable en el pin 4 del chip PS2492 utilizando un multímetro o un osciloscopio.
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/hardware-troubleshooting-fetch-1501-main-board-24v-rail-not-activating/54764](https://discourse.openrobotics.org/t/hardware-troubleshooting-fetch-1501-main-board-24v-rail-not-activating/54764)
