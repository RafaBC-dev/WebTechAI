# ros_tap: un telemetría sin configuración para robots ROS

**Fecha:** 2026-06-09
**Categoría:** robotica
**Tags:** robotica, python, librerias
**Título original:** ros_tap: zero config telemetry tap for any ROS robot

---

## Introducción

Un desarrollador de ROS 2 necesitaba una herramienta para registrar datos de su robot sin tener que configurar nada cada vez que cambiaba el código. Así que creó ros_tap, un telemetría que se conecta automáticamente a la red DDS y registra todos los datos del robot.

## ¿Qué es?

ros_tap es una herramienta de telemetría que se conecta a la red DDS de un robot ROS y registra todos los datos publicados por el robot. No necesita ser configurada ni reconfigurada cada vez que se cambia el código del robot. Puede escribir los datos a un archivo local, subirlos a S3 o enviarlos a la salida estándar.

## ¿Cómo funciona?

ros_tap utiliza CycloneDDS para conectarse a la red DDS del robot y descubrir todos los nodos y temas publicados. Luego, registra todos los datos publicados por el robot en formato JSONL. Puede ser instalada mediante pip y se puede ejecutar desde cualquier máquina que tenga acceso a la red DDS del robot.

## ¿Por qué importa?

ros_tap es importante porque resuelve el problema de la configuración y la reconfiguración de la telemetría cada vez que se cambia el código del robot. Además, es una herramienta flexible que puede ser utilizada en diferentes entornos y con diferentes tipos de robots.

## Consejo técnico

Si estás trabajando con robots ROS, considera instalar ros_tap y utilizarla para registrar datos de tu robot. Puedes instalarla mediante pip con el comando `pip install ros_tap` y luego ejecutarla con el comando `ros_tap record -o ./data` para escribir los datos a un archivo local.

```bash
ros_tap record -o ./data
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/ros-tap-zero-config-telemetry-tap-for-any-ros-robot/55363](https://discourse.openrobotics.org/t/ros-tap-zero-config-telemetry-tap-for-any-ros-robot/55363)
