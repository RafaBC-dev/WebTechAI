# Dispositivo de autenticación de huella dactilar inalámbrico para Linux y Mac

**Fecha:** 2026-07-04
**Categoría:** linux
**Tags:** robotica, microcontroladores, software y Linux
**Título original:** Building A Wireless Fingerprint Authorization Device

---

## Introducción

Después de la popularidad de la autenticación de huella dactilar en laptops y ordenadores de escritorio, [superdog] decidió crear un dispositivo similar para Linux y Mac. Este proyecto, llamado immurok, tiene como objetivo facilitar la autenticación en máquinas que utilizan teclados externos y realizan trabajo en terminal.

## ¿Qué es?

El dispositivo immurok es una herramienta de autenticación de huella dactilar inalámbrico diseñada para personas que utilizan teclados externos y realizan trabajo en terminal en máquinas Mac y Linux. Utiliza un microcontrolador WCH CH592F con conectividad Bluetooth y un sensor de huella dactilar R559S capacitivo.

## ¿Cómo funciona?

El dispositivo immurok se conecta a la máquina objetivo mediante Bluetooth, anunciándose como un dispositivo de teclado HID estándar. El sensor de huella dactilar verifica la huella localmente, sin enviar datos biométricos. En la máquina, Linux utiliza una aplicación CLI/TUI integrada con PAM para manejar la autorización de inicio de sesión y sudo en terminal, mientras que en Mac se utiliza una aplicación de barra de menús con integración de PAM para peticiones de administrador.

## ¿Por qué importa?

Este dispositivo resuelve el problema de la autenticación de huella dactilar inalámbrico en máquinas que utilizan teclados externos y realizan trabajo en terminal, facilitando la autenticación y evitando la necesidad de ingresar la contraseña repetidamente.

## Consejo técnico

Para implementar un sistema de autenticación de huella dactilar inalámbrico similar, puedes utilizar el microcontrolador WCH CH592F y el sensor de huella dactilar R559S capacitivo, y configurar la aplicación CLI/TUI en Linux o la aplicación de barra de menús en Mac con integración de PAM.

```bash
sudo apt-get install libpam-dev para instalar las herramientas de desarrollo de PAM en Linux
```

---

**Fuente original:** [https://hackaday.com/2026/07/03/building-a-wireless-fingerprint-authorization-device/](https://hackaday.com/2026/07/03/building-a-wireless-fingerprint-authorization-device/)
