# Ruta más corta con Raspberry Pi Pico y Dijkstra's algoritmo

**Fecha:** 2026-08-10
**Categoría:** robotica
**Tags:** robotica, python, linux
**Título original:** Build a Raspberry Pi Pico route finder using Dijkstra’s algorithm

---

## Introducción

El satnav y los robots también usan algoritmos para encontrar la ruta más corta. Descubre cómo funcionan y cómo crear uno con Raspberry Pi Pico.

## ¿Qué es?

Dijkstra's algoritmo es una técnica para encontrar la ruta más corta entre dos puntos en un mapa. Consiste en crear un gráfico de nodos conectados y usar la información para calcular la distancia y la ruta más eficiente.

## ¿Cómo funciona?

El algoritmo de Dijkstra funciona siguiendo tres reglas: mantener un registro de la distancia a cada nodo, siempre elegir la ruta más corta y mantener un registro de los nodos visitados. Esto se implementa en Python y se ejecuta en un Raspberry Pi Pico.

## ¿Por qué importa?

Este algoritmo es crucial en la navegación y la comunicación de redes. Los satnav y los robots lo usan para encontrar la ruta más corta y evitar obstáculos.

## Consejo técnico

Prueba a implementar Dijkstra's algoritmo en un proyecto de robótica o navegación usando la librería MicroPython en Raspberry Pi Pico.

```bash
from machine import Pin
import time
import math
# Implementación de Dijkstra's algoritmo
```

---

**Fuente original:** [https://www.raspberrypi.com/news/build-a-raspberry-pi-pico-route-finder-using-dijkstras-algorithm/](https://www.raspberrypi.com/news/build-a-raspberry-pi-pico-route-finder-using-dijkstras-algorithm/)
