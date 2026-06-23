# Linux 7.2 reduce overhead en RISC-V y soporta Eswin SoC por defecto

**Fecha:** 2026-06-23
**Categoría:** linux
**Tags:** linux, risc-v, embebidos
**Título original:** Linux 7.2 RISC-V Reduces Kernel Startup Overhead, Eswin SoC Support By Default

---

## Introducción

La versión 7.2 del kernel Linux para arquitectura RISC-V ha sido actualizada con mejoras significativas. Ahora reduce el overhead en el arranque del kernel y soporta por defecto la Eswin SoC, popular en la placa de desarrollo SiFive HiFive Premier P550.

## ¿Qué es?

Linux es un sistema operativo de código abierto que se utiliza en una amplia variedad de dispositivos, desde servidores hasta dispositivos embebidos. La versión 7.2 es una actualización del kernel Linux que se enfoca en mejorar el rendimiento y la estabilidad en la arquitectura RISC-V.

## ¿Cómo funciona?

La actualización del kernel RISC-V reduce el overhead en el arranque del kernel mediante la optimización de la inicialización de ftrace. Además, se ha agregado soporte por defecto para la Eswin SoC, lo que permite que los desarrolladores utilicen la placa de desarrollo SiFive HiFive Premier P550 sin necesidad de configuraciones adicionales.

## ¿Por qué importa?

Estas mejoras son importantes para los desarrolladores que trabajan con la arquitectura RISC-V, ya que permiten una mayor eficiencia y estabilidad en sus proyectos. Además, el soporte por defecto para la Eswin SoC facilita el desarrollo de aplicaciones en la placa de desarrollo SiFive HiFive Premier P550.

## Consejo técnico

Si estás trabajando con la arquitectura RISC-V y la placa de desarrollo SiFive HiFive Premier P550, actualiza tu kernel Linux a la versión 7.2 para aprovechar las mejoras en el rendimiento y la estabilidad.

```bash
Para actualizar tu kernel Linux a la versión 7.2, ejecuta el comando `git pull origin master` y luego `make oldconfig` para configurar el kernel según tus necesidades.
```

---

**Fuente original:** [https://www.phoronix.com/news/Linux-7.2-RISC-V](https://www.phoronix.com/news/Linux-7.2-RISC-V)
