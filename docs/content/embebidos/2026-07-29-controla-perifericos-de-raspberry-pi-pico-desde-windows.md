# Controla periféricos de Raspberry Pi Pico desde Windows

**Fecha:** 2026-07-29
**Categoría:** embebidos
**Tags:** robotica, embebidos, linux
**Título original:** PicoJig: control peripherals (GPIO, ADC, UART, SPI, I2C, PWM) of a Raspberry Pi Pico / Pico W from a Windows PC via USB or WiFi  @raspberry_pi

---

## Introducción

¿Quieres controlar tus proyectos de Raspberry Pi Pico desde tu computadora de escritorio? Ahora es posible gracias a PicoJig, una herramienta que te permite controlar los periféricos de tu microcontrolador desde Windows

## ¿Qué es?

PicoJig es una herramienta que consiste en firmware, una aplicación para PC y una biblioteca que te permite controlar los periféricos de un Raspberry Pi Pico o Pico W desde una computadora de escritorio. Esto incluye GPIO, ADC, UART, SPI, I2C y PWM

## ¿Cómo funciona?

PicoJig funciona mediante conexión USB o WiFi. En modo USB, se utiliza una puerta virtual COM para controlar el Pico, mientras que en modo WiFi, se utiliza una comunicación TCP/IP para controlar el Pico W de forma remota

## ¿Por qué importa?

PicoJig es importante porque te permite controlar tus proyectos de Raspberry Pi Pico de forma más cómoda y eficiente, sin necesidad de conectar un monitor o teclado a tu microcontrolador

## Consejo técnico

Para empezar a usar PicoJig, descarga el firmware y la aplicación para PC desde GitHub y sigue las instrucciones para configurar tu conexión USB o WiFi

```bash
git clone https://github.com/raspberrypi/picojig
```

---

**Fuente original:** [https://blog.adafruit.com/2026/07/28/picojig-control-peripherals-gpio-adc-uart-spi-i2c-pwm-of-a-raspberry-pi-pico-pico-w-from-a-windows-pc-via-usb-or-wifi-raspberry_pi/](https://blog.adafruit.com/2026/07/28/picojig-control-peripherals-gpio-adc-uart-spi-i2c-pwm-of-a-raspberry-pi-pico-pico-w-from-a-windows-pc-via-usb-or-wifi-raspberry_pi/)
