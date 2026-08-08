# Raspberry Pi Pico: un rutafinder con Dijkstra's algoritmo

**Fecha:** 2026-08-08
**Categoría:** robotica
**Tags:** robotica, microcontroladores, python
**Título original:** Build a Raspberry Pi Pico route finder using Dijkstra’s algorithm

---

## Introducción

¿Cómo funciona tu satnav o cómo deciden las redes qué ruta tomar? La respuesta es gracias a algoritmos como Dijkstra's, que ahora se puede implementar en un Raspberry Pi Pico.

## ¿Qué es?

Dijkstra's es un algoritmo de ruta-finding desarrollado por Edsger Dijkstra en los años 50. Consiste en crear un grafo de nodos conectados y usar el algoritmo para encontrar la ruta más barata entre ellos. En este caso, se aplica a un proyecto de rutafinder con un Raspberry Pi Pico.

## ¿Cómo funciona?

El algoritmo funciona según tres reglas: mantener un registro de los costos de llegar a cada lugar, siempre usar la ruta más barata y mantener un registro de los lugares visitados. En el proyecto, se utiliza un MicroPython programado en un Raspberry Pi Pico para crear un rutafinder que muestra la distancia y la ruta entre diferentes lugares en el Reino Unido.

## ¿Por qué importa?

Este proyecto es importante porque demuestra cómo se pueden aplicar algoritmos de ruta-finding en proyectos de robótica y electrónica, y cómo se pueden utilizar para resolver problemas de navegación y optimización.

## Consejo técnico

Si deseas implementar Dijkstra's en tu propio proyecto, puedes utilizar la librería de MicroPython para crear un rutafinder similar. Recuerda que debes mantener un registro de los costos y utilizar la ruta más barata.

```bash
from machine import Pin, ADC
from utime import sleep_ms
# Código para leer sensores y calcular costos
```

---

**Fuente original:** [https://www.raspberrypi.com/news/build-a-raspberry-pi-pico-route-finder-using-dijkstras-algorithm/](https://www.raspberrypi.com/news/build-a-raspberry-pi-pico-route-finder-using-dijkstras-algorithm/)
