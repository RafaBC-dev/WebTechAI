# BPF programas pueden suspenderse y reanudarse, facilitando tareas largas

**Fecha:** 2026-06-20
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** [$] Suspending and resuming BPF programs

---

## Introducción

El desarrollo de BPF programas en Linux ha permitido extender muchas funcionalidades del kernel, pero ha tenido un inconveniente: debían completarse en el mismo contexto en el que comenzaron. Esto ha limitado su utilidad para tareas largas. Sin embargo, un nuevo avance promete cambiar esto.

## ¿Qué es?

BPF (Berkeley Packet Filter) es una tecnología que permite a los desarrolladores crear programas que se ejecutan en el kernel de Linux. Estos programas pueden ser utilizados para realizar tareas como la monitorización de redes, la gestión de memoria y la optimización de rendimiento. Sin embargo, hasta ahora, estos programas debían completarse en el mismo contexto en el que comenzaron, lo que limitaba su capacidad para realizar tareas largas.

## ¿Cómo funciona?

El nuevo avance, obra de Kumar Kartikeya Dwivedi, permite a los BPF programas ser expresados como corutinas. Esto significa que pueden suspenderse y reanudarse en diferentes puntos, lo que les permite realizar tareas largas de manera más eficiente. Las corutinas son una forma de programación que permite a los programas suspenderse y reanudarse en diferentes puntos, lo que les permite aprovechar al máximo los recursos del sistema.

## ¿Por qué importa?

Este avance es importante porque permite a los desarrolladores crear BPF programas que puedan realizar tareas largas de manera más eficiente. Esto puede ser útil para aplicaciones que requieren realizar tareas de monitorización, gestión de memoria o optimización de rendimiento durante períodos prolongados de tiempo.

## Consejo técnico

Si deseas aprovechar al máximo los beneficios de los BPF programas suspendidos y reanudados, puedes comenzar investigando sobre la implementación de corutinas en tu proyecto. Puedes utilizar la herramienta `bpftrace` para crear y depurar tus BPF programas, y la herramienta `libbpf` para crear y compilar tus programas de forma eficiente.

```bash
bpftrace
```

---

**Fuente original:** [https://lwn.net/Articles/1076210/](https://lwn.net/Articles/1076210/)
