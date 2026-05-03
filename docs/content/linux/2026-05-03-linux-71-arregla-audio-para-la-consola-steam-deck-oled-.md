# Linux 7.1 arregla audio para la consola Steam Deck OLED después de 2 años

**Fecha:** 2026-05-03
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Linux 7.1 Fixes Audio For The Steam Deck OLED After Being Broken 2 Years On The Upstream Kernel

---

## Introducción

La consola de juegos Steam Deck OLED ha sufrido un problema con el soporte de audio desde una actualización en 2023. Aunque Valve había implementado una solución en su kernel personalizado, ahora se ha encontrado una solución en la versión 7.1 del kernel Linux.

## ¿Qué es?

Linux 7.1 es una versión del kernel Linux que incluye una solución para el problema de audio en la consola Steam Deck OLED. Este problema se debió a un cambio en el código del kernel que afectó la topología de audio de la consola. La solución se basa en una quirk de DMI (Device Management Interface) que permite al kernel detectar la consola y ajustar la configuración de audio en consecuencia.

## ¿Cómo funciona?

La solución se implementa mediante un cambio en el código del kernel que permite al kernel detectar la consola Steam Deck OLED y ajustar la configuración de audio en consecuencia. La quirk de DMI se utiliza para identificar la consola y aplicar la solución adecuada. Esto permite que el audio funcione correctamente en la consola sin afectar a otras plataformas.

## ¿Por qué importa?

Esta solución es importante porque permite que la consola Steam Deck OLED funcione correctamente con el audio, lo que es esencial para los jugadores que utilizan la consola. Además, esta solución se puede aplicar a otras plataformas que utilicen el kernel Linux, lo que puede ayudar a resolver problemas de audio similares.

## Consejo técnico

Si estás utilizando la consola Steam Deck OLED y tienes problemas de audio, puedes intentar actualizar tu kernel a la versión 7.1 y ver si la solución funciona. También puedes investigar sobre la quirk de DMI y cómo se utiliza para ajustar la configuración de audio en tu consola.

```bash
Para actualizar tu kernel a la versión 7.1, puedes utilizar el comando `sudo apt-get update && sudo apt-get install linux-image-7.1` en un terminal de Linux.
```

---

**Fuente original:** [https://www.phoronix.com/news/Steam-Deck-OLED-Audio-Fix](https://www.phoronix.com/news/Steam-Deck-OLED-Audio-Fix)
