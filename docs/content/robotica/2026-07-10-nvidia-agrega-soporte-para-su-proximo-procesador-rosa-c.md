# NVIDIA agrega soporte para su próximo procesador Rosa con el núcleo Rigel

**Fecha:** 2026-07-10
**Categoría:** robotica
**Tags:** linux, codigo, herramientas
**Título original:** LLVM Clang Merges Initial Support For NVIDIA Rigel Core With Next-Gen Rosa CPU

---

## Introducción

NVIDIA ha confirmado detalles sobre su próximo procesador Rosa, que sucederá a Vera. El nuevo procesador contará con un núcleo Rigel, basado en el diseño Olympus. Esto es importante porque marca un paso importante en la integración de NVIDIA en la comunidad de código abierto.

## ¿Qué es?

El núcleo Rigel es un procesador de 64 bits basado en la arquitectura Armv9.2-A, diseñado por NVIDIA. Es una iteración del núcleo Olympus y forma parte del procesador Rosa, que será el sucesor de Vera.

## ¿Cómo funciona?

El soporte para el núcleo Rigel se ha agregado al compilador LLVM Clang a través de la opción -mcpu=rigel. Esto permite a los desarrolladores utilizar el compilador con el núcleo Rigel y aprovechar sus capacidades. El soporte inicial incluye la detección del núcleo y la configuración básica, pero no incluye ajustes especializados o tablas de costos.

## ¿Por qué importa?

La adición de soporte para el núcleo Rigel es importante porque permite a los desarrolladores aprovechar las capacidades del procesador Rosa, que será lanzado en el futuro. Esto también marca un paso importante en la integración de NVIDIA en la comunidad de código abierto.

## Consejo técnico

Si estás interesado en utilizar el núcleo Rigel, puedes probar el compilador LLVM Clang con la opción -mcpu=rigel y ver cómo funciona. También puedes investigar sobre la arquitectura Armv9.2-A y cómo se diferencia de otras arquitecturas.

```bash
-mcpu=rigel
```

---

**Fuente original:** [https://www.phoronix.com/news/LLVM-Clang-NVIDIA-Rosa-Rigel](https://www.phoronix.com/news/LLVM-Clang-NVIDIA-Rosa-Rigel)
