# Programe BPF como coroutines: un cambio revolucionario en Linux

**Fecha:** 2026-06-22
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** [$] Suspending and resuming BPF programs

---

## Introducción

Los BPF programs son una herramienta poderosa para extender el kernel de Linux, pero hasta ahora, debían ejecutarse hasta su finalización en el mismo contexto en que comenzaron. Sin embargo, gracias al trabajo de Kumar Kartikeya Dwivedi, esto está a punto de cambiar.

## ¿Qué es?

Un BPF program es un programa de software que se ejecuta dentro del kernel de Linux. Estos programas pueden ser utilizados para extender muchas facetas del kernel, como la gestión de memoria o la seguridad. Sin embargo, hasta ahora, estos programas debían ejecutarse hasta su finalización en el mismo contexto en que comenzaron, lo que limitaba su capacidad para realizar tareas largas.

## ¿Cómo funciona?

El cambio propuesto por Kumar Kartikeya Dwivedi permite a los BPF programas ser expresados como coroutines, lo que les permite ejecutarse en diferentes contextos y finalizar en cualquier momento. Esto se logra mediante la utilización de la tecnología de coroutines, que permite a los programas suspender y reanudar su ejecución en diferentes momentos.

## ¿Por qué importa?

Este cambio revolucionario permitirá a los desarrolladores crear BPF programas más complejos y eficientes, capaces de realizar tareas largas y complejas en el kernel de Linux. Esto abrirá nuevas posibilidades para la creación de software en Linux, especialmente en áreas como la seguridad y la gestión de redes.

## Consejo técnico

Si deseas aprovechar este cambio, puedes empezar a investigar sobre la implementación de coroutines en Linux y cómo pueden ser utilizadas para crear BPF programas más eficientes. Puedes empezar por leer la documentación oficial de Linux sobre coroutines y BPF programs.

```bash
bpf
```

---

**Fuente original:** [https://lwn.net/Articles/1076210/](https://lwn.net/Articles/1076210/)
