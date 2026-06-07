# Docker para microcontroladores: AkiraOS combina Zephyr RTOS con WASM

**Fecha:** 2026-06-07
**Categoría:** embebidos
**Tags:** embebidos, linux, ia-local
**Título original:** Docker for Microcontrollers? AkiraOS combines Zephyr RTOS with WebAssembly (WASM) applications

---

## Introducción

AkiraOS es un sistema operativo para microcontroladores que permite ejecutar aplicaciones WebAssembly de manera sandboxed, similar a Docker. Esto permite a los usuarios actualizar y gestionar aplicaciones sin necesidad de reflotar el firmware.

## ¿Qué es?

AkiraOS es un sistema operativo basado en Zephyr RTOS que ejecuta aplicaciones WebAssembly de manera sandboxed en microcontroladores. Esto significa que el firmware permanece estable mientras que las aplicaciones son independientes y se pueden actualizar de manera OTA sin reflotar.

## ¿Cómo funciona?

AkiraOS utiliza WebAssembly para ejecutar aplicaciones de manera sandboxed en microcontroladores. Las aplicaciones se pueden instalar y actualizar de manera independiente, lo que permite a los usuarios mantener el firmware estable mientras que las aplicaciones se actualizan. El sistema utiliza un runtime personalizado para WebAssembly y un sistema de gestión de aplicaciones para permitir la instalación y actualización de aplicaciones.

## ¿Por qué importa?

AkiraOS es importante porque permite a los usuarios actualizar y gestionar aplicaciones en microcontroladores de manera más fácil y eficiente. Esto se logra mediante la ejecución de aplicaciones WebAssembly de manera sandboxed, lo que permite a los usuarios mantener el firmware estable mientras que las aplicaciones se actualizan.

## Consejo técnico

Si deseas empezar a trabajar con AkiraOS, puedes descargar el código fuente y las instrucciones para empezar desde el repositorio de GitHub. También puedes utilizar la herramienta de desarrollo de aplicaciones de AkiraOS para crear y depurar aplicaciones.

```bash
git clone https://github.com/akiraos/akiraos.git
```

---

**Fuente original:** [https://www.cnx-software.com/2026/06/06/docker-for-microcontrollers-akiraos-combines-zephyr-rtos-with-webassembly-wasm-applications/](https://www.cnx-software.com/2026/06/06/docker-for-microcontrollers-akiraos-combines-zephyr-rtos-with-webassembly-wasm-applications/)
