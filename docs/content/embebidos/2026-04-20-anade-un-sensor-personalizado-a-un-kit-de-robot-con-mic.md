# Añade un sensor personalizado a un kit de robot con MicroPython

**Fecha:** 2026-04-20
**Categoría:** embebidos
**Tags:** robotica, microcontroladores, python
**Título original:** Use MicroPython to Add a Custom Sensor to a Robot Kit

---

## Introducción

El proyecto consiste en agregar un sensor de audio a un kit de robot Otto, permitiendo que el robot detecte sonidos y se gire hacia ellos. Esto es posible gracias a la plataforma MicroPython y la herramienta Thonny.

## ¿Qué es?

El kit de robot Otto es una plataforma de educación que permite a los usuarios diseñar y programar sus propios robots. Está equipado con un microcontrolador ESP32-WROOM y tiene conexiones para motores, sensores y una batería recargable. Sin embargo, el kit no incluye un cuerpo de robot, lo que permite a los usuarios diseñar y imprimir sus propios componentes.

## ¿Cómo funciona?

Para agregar un sensor de audio al kit de robot, se diseñaron y imprimieron partes personalizadas en 3D. Luego, se utilizó MicroPython y la herramienta Thonny para programar el microcontrolador y conectar el sensor de audio. El sensor detecta sonidos y envía señales al microcontrolador, que a su vez gira el robot hacia la fuente del sonido.

## ¿Por qué importa?

Este proyecto es importante porque demuestra la capacidad de personalizar y ampliar la funcionalidad de un kit de robot. También muestra cómo la plataforma MicroPython y la herramienta Thonny pueden ser utilizadas para crear sensores y dispositivos personalizados.

## Consejo técnico

Si deseas agregar un sensor de audio a tu propio kit de robot, puedes utilizar la herramienta Thonny para programar el microcontrolador y conectar el sensor. Recuerda que debes diseñar y imprimir partes personalizadas en 3D para adaptar el sensor a tu kit de robot.

```bash
python -m thonny <ruta_al_codigo>
```

---

**Fuente original:** [https://blog.adafruit.com/2026/04/19/use-micropython-to-add-a-custom-sensor-to-a-robot-kit/](https://blog.adafruit.com/2026/04/19/use-micropython-to-add-a-custom-sensor-to-a-robot-kit/)
