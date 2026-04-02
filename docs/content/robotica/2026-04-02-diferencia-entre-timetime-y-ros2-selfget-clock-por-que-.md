# Diferencia entre time.time() y Ros2 self.get_clock(): ¿por qué importa?

**Fecha:** 2026-04-02
**Categoría:** robotica
**Tags:** robotica, linux, codigo
**Título original:** Difference between time.time() and Ros2 self.get_clock()

---

## Introducción

En el desarrollo de aplicaciones de robótica con ROS2, es común utilizar la función self.get_clock() para medir el tiempo. Sin embargo, ¿por qué no se utiliza la función time.time() en lugar de ella? En este artículo, exploraremos la diferencia entre estas dos funciones y por qué es importante elegir la correcta.

## ¿Qué es?

La función self.get_clock() es una herramienta de ROS2 que devuelve el tiempo actual en la simulación o en el sistema de computadora. Por otro lado, time.time() es una función de Python que devuelve el tiempo actual en segundos desde la época Unix. En el desarrollo de aplicaciones de robótica, es importante elegir la función correcta según el contexto.

## ¿Cómo funciona?

La función self.get_clock() funciona medir el tiempo en la simulación o en el sistema de computadora, dependiendo del contexto en el que se utilice. Por otro lado, time.time() devuelve el tiempo actual en segundos desde la época Unix. En el desarrollo de aplicaciones de robótica, es importante tener en cuenta la diferencia entre estas dos funciones para evitar errores en la medición del tiempo.

## ¿Por qué importa?

La diferencia entre self.get_clock() y time.time() es importante en el desarrollo de aplicaciones de robótica porque puede afectar la precisión y la consistencia de la medición del tiempo. Si se utiliza la función incorrecta, puede provocar errores en la simulación o en la ejecución del código.

## Consejo técnico

Si estás trabajando con ROS2, asegúrate de utilizar la función self.get_clock() para medir el tiempo en la simulación o en el sistema de computadora. Si necesitas medir el tiempo en segundos, utiliza la función time.time() en lugar de self.get_clock().

```bash
ros2 run my_package my_node
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/difference-between-time-time-and-ros2-self-get-clock/53722](https://discourse.openrobotics.org/t/difference-between-time-time-and-ros2-self-get-clock/53722)
