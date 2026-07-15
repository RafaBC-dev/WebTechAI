# Apple M1/M2 con Asahi Linux y Rusticl: Primera implementación conformante de OpenCL 3.1

**Fecha:** 2026-07-15
**Categoría:** linux
**Tags:** ia-local, linux, codigo
**Título original:** Khronos Lists First Conformant OpenCL 3.1 Implementation: Apple M1/M2 On Asahi Linux With Rusticl

---

## Introducción

La comunidad de Linux ha logrado una gran hazaña: la primera implementación conformante de OpenCL 3.1 se ha logrado en Apple Silicon M1/M2 con Asahi Linux y el driver Rusticl. Esto significa que se ha demostrado la capacidad de ejecutar OpenCL 3.1 en hardware de Apple en un entorno de Linux.

## ¿Qué es?

OpenCL es una API para programación paralela que permite aprovechar la potencia de los procesadores gráficos y los procesadores centrales para realizar tareas computacionales intensivas. La versión 3.1 de OpenCL se centra en aplicaciones de inteligencia artificial y cálculo de alto rendimiento.

## ¿Cómo funciona?

La implementación conformante de OpenCL 3.1 se logró utilizando el driver Rusticl, que es una implementación genérica de OpenCL para los drivers Gallium3D de Mesa. El driver Rusticl se ejecuta en el hardware de Apple Silicon M1/M2, que se ejecuta en Asahi Linux.

## ¿Por qué importa?

Esta implementación importa porque demuestra la capacidad de ejecutar OpenCL 3.1 en hardware de Apple en un entorno de Linux, lo que abre nuevas posibilidades para la programación paralela en Linux. Esto también muestra la capacidad de la comunidad de Linux para reverse-engineer el hardware de Apple y crear implementaciones de software para él.

## Consejo técnico

Si deseas probar la implementación conformante de OpenCL 3.1 en tu máquina con Asahi Linux y Rusticl, asegúrate de instalar el driver Rusticl y configurar tu sistema para ejecutar OpenCL 3.1. Puedes hacer esto siguiendo las instrucciones en el repositorio de Rusticl en GitHub.

```bash
git clone https://github.com/rusticl/rusticl.git && cd rusticl && ./configure && make && sudo make install
```

---

**Fuente original:** [https://www.phoronix.com/news/OpenCL-3.1-Conformance-Apple](https://www.phoronix.com/news/OpenCL-3.1-Conformance-Apple)
