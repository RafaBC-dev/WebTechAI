# Linux 7.2 apoyará Ethernet USB 10GbE con RTL8159 de Realtek

**Fecha:** 2026-05-08
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Linux 7.2 To Support Realtek RTL8159 10GbE USB Ethernet

---

## Introducción

La próxima versión del kernel Linux 7.2 incluirá soporte para el chipset RTL8159 de Realtek, utilizado en adaptadores de red USB 10GbE. Esto permitirá a los usuarios aprovechar la velocidad de 10 Gbps en sus dispositivos Linux.

## ¿Qué es?

El RTL8159 es un chipset de Ethernet USB 10GbE desarrollado por Realtek. Se utiliza en adaptadores de red USB que ofrecen velocidades de hasta 10 Gbps. El soporte para este chipset se ha estado trabajando en el kernel Linux para mejorar la compatibilidad y la estabilidad de los dispositivos Linux que utilizan esta tecnología.

## ¿Cómo funciona?

El soporte para el RTL8159 se ha implementado en el driver r8152 del kernel Linux. El driver utiliza el mecanismo de carga de firmware existente para cargar el firmware necesario para el PHY del chipset. Esto permite a los usuarios aprovechar la velocidad de 10 Gbps en sus dispositivos Linux.

## ¿Por qué importa?

El soporte para el RTL8159 en Linux 7.2 es importante porque permite a los usuarios aprovechar la velocidad de 10 Gbps en sus dispositivos Linux. Esto es especialmente relevante para usuarios que necesitan transferir grandes cantidades de datos a través de la red, como en aplicaciones de almacenamiento en red y de procesamiento de datos en tiempo real.

## Consejo técnico

Si planea utilizar un adaptador de red USB 10GbE con el chipset RTL8159, asegúrese de que su sistema Linux esté actualizado a la versión 7.2 o superior antes de instalar el dispositivo. Además, es importante verificar que el firmware necesario esté disponible en la rama linux-firmware.git.

```bash
sudo apt-get update && sudo apt-get install linux-image-7.2
```

---

**Fuente original:** [https://www.phoronix.com/news/Realtek-RTL8159-Linux-7.2](https://www.phoronix.com/news/Realtek-RTL8159-Linux-7.2)
