# Controlador de LED NeoPixels abiertamente disponible para instalaciones de iluminación

**Fecha:** 2026-05-27
**Categoría:** embebidos
**Tags:** esp32, robotica, microcontroladores
**Título original:** LichtBit’s open-source ESP32 Art-Net/sACN NeoPixels controller can drive up to 2,720 RGB LEDs

---

## Introducción

LichtBit ha lanzado un controlador de LED NeoPixels basado en ESP32 que puede manejar hasta 2.720 LEDs RGB. Este dispositivo está diseñado para instalaciones de iluminación de gran escala y diseño de escenario personalizado.

## ¿Qué es?

El controlador de LED NeoPixels de LichtBit es un dispositivo de hardware basado en ESP32 que permite controlar hasta 16 universos de LEDs addressables a través de 4 salidas dedicadas. Soporta protocolos de comunicación como Art-Net y sACN, y puede conectarse a la red a través de Ethernet o Wi-Fi.

## ¿Cómo funciona?

El controlador utiliza la biblioteca I2SClocklessLedDriver para manejar la renderización de píxeles, liberando los núcleos del procesador ESP32 para procesar paquetes de red de software complejo. Cuenta con una pantalla OLED de 128x32 para mostrar configuraciones y estados en tiempo real.

## ¿Por qué importa?

Este controlador es relevante para la industria de eventos y espectáculos, ya que conecta la tecnología de iluminación digital con software de alto rendimiento como Resolume Arena y MadMapper. Permite a los diseñadores de iluminación crear instalaciones de gran escala con una mayor flexibilidad y control.

## Consejo técnico

Si deseas empezar a trabajar con el controlador de LED NeoPixels de LichtBit, asegúrate de instalar la biblioteca I2SClocklessLedDriver en tu proyecto y configurar el protocolo de comunicación adecuado según tus necesidades.

---

**Fuente original:** [https://www.cnx-software.com/2026/05/27/lichtbit-open-source-esp32-art-net-sacn-neopixels-controller-can-drive-up-to-2720-rgb-leds/](https://www.cnx-software.com/2026/05/27/lichtbit-open-source-esp32-art-net-sacn-neopixels-controller-can-drive-up-to-2720-rgb-leds/)
