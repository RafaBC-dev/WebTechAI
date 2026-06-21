# Programas BPF pueden suspenderse y reanudarse: un cambio importante

**Fecha:** 2026-06-21
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** [$] Suspending and resuming BPF programs

---

## Introducción

Los programas BPF son una herramienta poderosa para extender el kernel de Linux, pero hasta ahora han tenido una limitación importante: debían terminar en el mismo contexto en que comenzaron. Esto puede cambiar pronto gracias a un trabajo en curso que permite expresar programas BPF como coroutines, lo que hará que tareas largas sean más fáciles de escribir.

## ¿Qué es?

Los programas BPF (Berkeley Packet Filter) son una herramienta del kernel de Linux que permite extender la funcionalidad del sistema operativo. Pueden ser utilizados para realizar tareas como la medición de rendimiento, la seguridad y la gestión de recursos. Sin embargo, hasta ahora han tenido la limitación de que debían terminar en el mismo contexto en que comenzaron.

## ¿Cómo funciona?

El trabajo en curso de Kumar Kartikeya Dwivedi permite expresar programas BPF como coroutines, lo que significa que pueden suspenderse y reanudarse en diferentes puntos. Esto se logra mediante la creación de un mecanismo que permite la pausa y reanudación de los programas BPF en el contexto de la coroutine. Esto permite que los programas BPF puedan realizar tareas largas sin tener que terminar en el mismo contexto en que comenzaron.

## ¿Por qué importa?

Este cambio es importante porque permite que los programas BPF puedan realizar tareas largas de manera más fácil y eficiente. Esto puede ser especialmente útil en aplicaciones que requieren la medición de rendimiento o la gestión de recursos en tiempo real. Además, permite que los desarrolladores puedan escribir programas BPF más complejos y escalables.

## Consejo técnico

Si deseas aprovechar este cambio, puedes empezar a investigar sobre las herramientas y librerías disponibles para trabajar con coroutines en Linux. Puedes comenzar con la documentación de la API de coroutines en Linux y explorar las herramientas como `liburcu` que permiten la implementación de coroutines en el kernel de Linux.

```bash
`git clone https://github.com/kartikeyadwivedi/liburcu.git`
```

---

**Fuente original:** [https://lwn.net/Articles/1076210/](https://lwn.net/Articles/1076210/)
