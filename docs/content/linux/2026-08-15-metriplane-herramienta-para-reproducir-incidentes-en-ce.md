# Metriplane: herramienta para reproducir incidentes en celdas de trabajo

**Fecha:** 2026-08-15
**Categoría:** linux
**Tags:** robotica, python, linux
**Título original:** Metriplane v0.3.0: turn recorded workcell incidents into repeatable regression tests

---

## Introducción

Metriplane es una herramienta de código abierto que permite reproducir incidentes en celdas de trabajo de robots y simular su comportamiento. Esto se logra mediante la creación de un informe de incidente claro, un conjunto de evidencia verificada y un test de regresión que puede ser ejecutado nuevamente después de cambios.

## ¿Qué es?

Metriplane es una herramienta de código abierto que se enfoca en la observabilidad física de celdas de trabajo de robots. Permite reproducir incidentes y simular el comportamiento de los robots de manera determinista. Esto se logra mediante la creación de un informe de incidente claro, un conjunto de evidencia verificada y un test de regresión que puede ser ejecutado nuevamente después de cambios.

## ¿Cómo funciona?

Metriplane utiliza un enfoque de ingeniería inversa para analizar los registros de trabajo de los robots y reconstruir el estado de la celda de trabajo en un momento específico. Luego, utiliza un motor de test de regresión para ejecutar un test que reproduce el incidente y verificar que el resultado sea el mismo que en la primera vez que se ejecutó.

## ¿Por qué importa?

Metriplane es importante porque permite a los desarrolladores y ingenieros de sistemas reproducir incidentes en celdas de trabajo de robots de manera fiable y determinista. Esto les permite identificar y solucionar problemas de manera más eficiente y efectiva.

## Consejo técnico

Si deseas reproducir incidentes en celdas de trabajo de robots, puedes utilizar Metriplane para crear un informe de incidente claro y un test de regresión que pueda ser ejecutado nuevamente después de cambios. Comienza por instalar Metriplane utilizando el comando `python -m pip install metriplane==0.3.0` y luego ejecuta el demo utilizando `metriplane demo --open`.

```bash
python -m pip install metriplane==0.3.0
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/metriplane-v0-3-0-turn-recorded-workcell-incidents-into-repeatable-regression-tests/57409](https://discourse.openrobotics.org/t/metriplane-v0-3-0-turn-recorded-workcell-incidents-into-repeatable-regression-tests/57409)
