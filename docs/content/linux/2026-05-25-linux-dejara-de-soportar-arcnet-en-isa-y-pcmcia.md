# Linux dejará de soportar ARCnet en ISA y PCMCIA

**Fecha:** 2026-05-25
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Linux To Drop ARCnet Support For Old ISA & PCMCIA Hardware

---

## Introducción

La comunidad de Linux ha decidido eliminar el soporte para ARCnet en ISA y PCMCIA en la próxima versión del kernel, lo que afectará a aquellos que siguen utilizando esta tecnología de red antigua.

## ¿Qué es?

ARCnet es una tecnología de red que se utilizó en la década de 1980 y 1990, antes de la popularización de Ethernet. Se utilizaba en entornos industriales, de automatización y de edificios. Aunque sigue siendo utilizada en algunos entornos, la mayoría de los dispositivos que la soportaban han sido reemplazados por tecnologías más modernas.

## ¿Cómo funciona?

La eliminación del soporte para ARCnet en ISA y PCMCIA se logrará eliminando los drivers y la documentación relacionados con estos dispositivos. Los desarrolladores de Linux están actualizando las instrucciones para cargar módulos y pasar parámetros para que funcionen en kernels modernos y con el driver com20020_pci.

## ¿Por qué importa?

La eliminación del soporte para ARCnet en ISA y PCMCIA no afectará a aquellos que siguen utilizando esta tecnología en entornos industriales o de automatización, ya que los desarrolladores de Linux han decidido mantener el soporte para ARCnet en otros dispositivos. Sin embargo, aquellos que siguen utilizando ISA y PCMCIA en su equipo deberán actualizar a una versión más moderna del kernel o utilizar una versión LTS de Linux.

## Consejo técnico

Si estás utilizando ISA y PCMCIA en tu equipo y necesitas soporte para ARCnet, considera actualizar a una versión más moderna del kernel o utilizar una versión LTS de Linux, que seguirá soportando esta tecnología.

```bash
Para verificar si tu equipo soporta ARCnet, puedes utilizar el comando `modprobe -l arcnet` y verificar si el módulo está cargado. Si no está cargado, puedes intentar cargarlo manualmente con `modprobe arcnet`.
```

---

**Fuente original:** [https://www.phoronix.com/news/Linux-To-Drop-ARCnet-ISA-PCMCIA](https://www.phoronix.com/news/Linux-To-Drop-ARCnet-ISA-PCMCIA)
