# Linux 7.1 elimina drivers PCMCIA obsoletos

**Fecha:** 2026-04-24
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Linux 7.1 Removes Some Obsolete PCMCIA Drivers That Likely Haven't Been Used In Years

---

## Introducción

La versión 7.1 del kernel Linux ha eliminado algunos drivers PCMCIA obsoletos que probablemente no se han utilizado en años. Esta decisión forma parte de un esfuerzo más amplio para eliminar el soporte de PCMCIA del kernel.

## ¿Qué es?

Los drivers PCMCIA son componentes del kernel Linux que permiten la comunicación con tarjetas PCMCIA, una tecnología de tarjetas de expansión que se utilizó en ordenadores portátiles y otros dispositivos en la década de 1990 y principios de la década de 2000. Sin embargo, esta tecnología ha sido prácticamente eliminada de la industria de la informática y ya no se utiliza en dispositivos modernos.

## ¿Cómo funciona?

La eliminación de los drivers PCMCIA obsoletos se ha realizado mediante la remoción de los módulos del kernel correspondientes, que son el I82092, el I82365 y el TCIC. Estos drivers se habían mantenido en el kernel por razones históricas, pero no se han actualizado ni se han utilizado en años. La eliminación de estos drivers no afecta a la funcionalidad del kernel en dispositivos modernos, ya que no se utilizan en la práctica.

## ¿Por qué importa?

La eliminación de los drivers PCMCIA obsoletos es importante porque reduce la complejidad del kernel y elimina la posibilidad de errores y vulnerabilidades en estos componentes. Además, esta decisión forma parte de un esfuerzo más amplio para eliminar el soporte de tecnologías obsoletas del kernel y mejorar la seguridad y la estabilidad del sistema operativo.

## Consejo técnico

Si estás utilizando un dispositivo que todavía utiliza tarjetas PCMCIA, es posible que debas actualizar tu sistema operativo a una versión que no tenga soporte para estas tarjetas. Puedes verificar si tu sistema operativo tiene soporte para PCMCIA utilizando el comando `lsmod | grep pcmcia` en un terminal.

```bash
lsmod | grep pcmcia
```

---

**Fuente original:** [https://www.phoronix.com/news/Linux-7.1-Drops-Old-PCMCIA-Code](https://www.phoronix.com/news/Linux-7.1-Drops-Old-PCMCIA-Code)
