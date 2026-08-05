# AMD Presenta Propuesta para Subsistema eSPI en Linux

**Fecha:** 2026-08-05
**Categoría:** linux
**Tags:** linux, microcontroladores, embebidos
**Título original:** AMD Posts Proposal & Linux Patches For eSPI Subsystem

---

## Introducción

AMD ha presentado una propuesta para agregar un nuevo subsistema al kernel de Linux para manejar la interfaz de comunicación eSPI. Esta tecnología, originalmente desarrollada por Intel, se utiliza para enlazar con el BIOS, controladores de sistema y otros periféricos. Con AMD empezando a utilizar eSPI, es hora de que Linux la soporte.

## ¿Qué es?

eSPI es una interfaz de comunicación que permite enlazar con el BIOS, controladores de sistema y otros periféricos. Fue originalmente desarrollada por Intel como una alternativa a la interfaz LPC, SPI tradicional y otros sistemas de señalización lateral. Con AMD empezando a utilizar eSPI, es hora de que Linux la soporte.

## ¿Cómo funciona?

La propuesta de AMD incluye un nuevo driver para manejar la interfaz eSPI en Linux. El nuevo subsistema se basa en el modelo de bus de Linux y utiliza la ACPI para configurar los dispositivos. El driver de AMD ha sido probado y validado en una plataforma AMDI0070 y funciona correctamente.

## ¿Por qué importa?

La adición de eSPI a Linux es importante porque permite a los usuarios de AMD aprovechar al máximo la tecnología eSPI en sus sistemas. Esto incluye la capacidad de enlazar con el BIOS, controladores de sistema y otros periféricos de manera más eficiente.

## Consejo técnico

Si estás interesado en probar la propuesta de AMD, puedes encontrar los parches en la lista de correo electrónico del kernel de Linux. Recuerda que los parches aún están en desarrollo y pueden tener limitaciones, como la falta de soporte para la tabla de dispositivos.

---

**Fuente original:** [https://www.phoronix.com/news/AMD-eSPI-Linux-Patches](https://www.phoronix.com/news/AMD-eSPI-Linux-Patches)
