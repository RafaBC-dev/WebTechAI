# Actualización de firmware en robots de flota sin dañarlos

**Fecha:** 2026-07-30
**Categoría:** embebidos
**Tags:** robotica, linux, embebidos
**Título original:** How are you handling firmware updates on fleet robots without bricking one?

---

## Introducción

Un equipo de robots de flota pequeña enfrenta problemas con las actualizaciones de firmware, lo que puede llevar a dañar algunos de ellos. ¿Cómo pueden abordar este desafío?

## ¿Qué es?

Un equipo de robots de flota utiliza una pequeña flota de robots AMR (Autonomous Mobile Robots) con ROS 2 Humble en Jetson Orins y microcontroladores STM32 para controlar los motores y seguridad. La actualización de firmware es un proceso complicado que puede llevar a dañar algunos robots.

## ¿Cómo funciona?

El equipo utiliza una actualización de firmware sobre la red (OTA) para actualizar el software en los robots, pero el proceso de actualización en el nivel de microcontrolador es complicado y requiere una conexión física. Están explorando diferentes opciones para simplificar este proceso, como utilizar un bootloader en el STM32 que recupere el firmware firmado del Jetson a través de UART o utilizar Mender para la actualización del Jetson.

## ¿Por qué importa?

La actualización de firmware es un problema crítico en la robótica, ya que puede llevar a dañar los robots y afectar la seguridad y la eficiencia del sistema. La solución a este problema puede ayudar a mejorar la disponibilidad y la confiabilidad de los robots de flota.

## Consejo técnico

Consideren utilizar un bootloader en el microcontrolador que permita la actualización de firmware sobre la red (OTA) y utilicen una arquitectura de partición A/B para permitir la actualización sin interrupir la operación del robot.

```bash
Utilicen un bootloader como MCUboot que permita la actualización de firmware OTA y utilicen una arquitectura de partición A/B para permitir la actualización sin interrupir la operación del robot.
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/how-are-you-handling-firmware-updates-on-fleet-robots-without-bricking-one/57050](https://discourse.openrobotics.org/t/how-are-you-handling-firmware-updates-on-fleet-robots-without-bricking-one/57050)
