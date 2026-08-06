# Linux 7.3: un paso importante para el controlador Steam original

**Fecha:** 2026-08-06
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Linux 7.3 To Fix Longstanding Gap In The Native Driver For Original Steam Controller

---

## Introducción

La versión 7.3 del kernel Linux está a punto de llegar con una mejora significativa para el controlador Steam original. Hasta ahora, este controlador no tenía soporte para eventos de sensor, lo que limitaba su funcionalidad. Ahora, gracias a un parche reciente, se puede aprovechar al máximo este dispositivo.

## ¿Qué es?

El controlador Steam original es un dispositivo de juego diseñado por Valve que permite controlar juegos de manera más natural. Sin embargo, hasta ahora, no tenía soporte para eventos de sensor, lo que limitaba su funcionalidad. Los eventos de sensor permiten que el controlador detecte movimientos y acciones del jugador, lo que puede ser utilizado para activar acciones en los juegos sin necesidad de presionar botones físicos.

## ¿Cómo funciona?

El parche reciente agrega soporte para eventos de sensor al controlador Steam original. Esto se logra mediante la adición de 200 líneas de código a la driver hid-steam del kernel Linux. La nueva función permite que el controlador detecte eventos de sensor, como acelerómetros, giroscopio, palancas de tacto y más.

## ¿Por qué importa?

Esta mejora es importante porque permite que los jugadores aprovechen al máximo el controlador Steam original. Ahora pueden utilizar eventos de sensor para activar acciones en los juegos, lo que puede mejorar la experiencia de juego. Además, esta mejora se alinea con la funcionalidad del controlador Steam en la aplicación Steam y la biblioteca SDL.

## Consejo técnico

Si deseas aprovechar al máximo el controlador Steam original con Linux 7.3, asegúrate de actualizar tu kernel a la versión 7.3 y verificar que el driver hid-steam esté configurado correctamente.

```bash
sudo apt update && sudo apt upgrade -y && sudo modprobe hid-steam
```

---

**Fuente original:** [https://www.phoronix.com/news/Linux-7.3-Steam-Controller](https://www.phoronix.com/news/Linux-7.3-Steam-Controller)
