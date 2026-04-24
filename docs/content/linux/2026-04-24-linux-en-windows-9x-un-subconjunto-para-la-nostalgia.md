# Linux en Windows 9x: un subconjunto para la nostalgia

**Fecha:** 2026-04-24
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** WSL9x: Add a Linux Subsystem to Your Windows 9x

---

## Introducción

Los entusiastas de la nostalgia de la era de los 90 pueden celebrar: ahora es posible ejecutar Linux dentro de Windows 9x, gracias a un proyecto llamado WSL9x. Esta herramienta permite a los usuarios correr Linux y Windows 9x de manera cooperativa, lo que abre nuevas posibilidades para la emulación y el desarrollo de software.

## ¿Qué es?

WSL9x es un proyecto que permite ejecutar Linux dentro de Windows 9x, aprovechando la arquitectura de subconjuntos de Windows. Se basa en un kernel de Linux modificado que llama a las API del kernel de Windows 9x en lugar de las API POSIX. Esto permite a los usuarios correr Linux y Windows 9x de manera cooperativa.

## ¿Cómo funciona?

Para utilizar WSL9x, es necesario construir un kernel de Linux modificado y crear una imagen de disco con una copia instalada de Windows 9x. Luego, se puede cargar WSL9x con el comando `wsl` y comenzar a correr Linux y Windows 9x de manera cooperativa. El kernel de Linux se basa en la tecnología de Linux en modo usuario, lo que permite a los usuarios correr Linux sin necesidad de modificar el kernel de Windows 9x.

## ¿Por qué importa?

WSL9x es importante porque permite a los usuarios correr Linux y Windows 9x de manera cooperativa, lo que abre nuevas posibilidades para la emulación y el desarrollo de software. Esto puede ser útil para desarrolladores que necesitan emular entornos de desarrollo antiguos o para usuarios que quieren correr aplicaciones de Linux en un entorno Windows 9x.

## Consejo técnico

Si deseas utilizar WSL9x, asegúrate de construir el kernel de Linux modificado correctamente y de crear una imagen de disco con una copia instalada de Windows 9x. También es importante tener en cuenta que WSL9x es un proyecto experimental y puede tener problemas de estabilidad.

```bash
wsl
```

---

**Fuente original:** [https://hackaday.com/2026/04/23/wsl9x-add-an-entire-windows-9x-subsystem-to-your-linux/](https://hackaday.com/2026/04/23/wsl9x-add-an-entire-windows-9x-subsystem-to-your-linux/)
