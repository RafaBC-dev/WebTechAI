# KASAN para código BPF compilado en tiempo justo

**Fecha:** 2026-06-24
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** [$] KASAN for JIT-compiled BPF code

---

## Introducción

El proyecto KASAN se ha expandido para incluir código BPF compilado en tiempo justo, lo que ayudará a detectar errores en el compilador JIT. Esto es especialmente importante para garantizar la seguridad y estabilidad del kernel Linux.

## ¿Qué es?

KASAN es un sistema de verificación de memoria del kernel Linux que ayuda a detectar problemas de gestión de memoria. El código BPF (Berkeley Packet Filter) es un lenguaje de programación utilizado para filtrar y procesar paquetes de red en tiempo real. El compilador JIT (Just-In-Time) es una técnica que compila código en tiempo de ejecución para mejorar el rendimiento.

## ¿Cómo funciona?

KASAN utiliza un sistema de marcadores de memoria para rastrear la memoria asignada a cada proceso. Cuando se detecta un error de memoria, KASAN genera un informe que ayuda a los desarrolladores a identificar y corregir el problema. El soporte para código BPF compilado en tiempo justo permite a KASAN rastrear la memoria asignada a estos programas y detectar errores en el compilador JIT.

## ¿Por qué importa?

La adición de soporte para código BPF compilado en tiempo justo en KASAN es importante porque ayuda a garantizar la seguridad y estabilidad del kernel Linux. Esto se debe a que el compilador JIT puede generar código que no es seguro o que puede causar errores de memoria. Con KASAN, los desarrolladores pueden detectar estos errores y corregirlos antes de que causen problemas en el sistema.

## Consejo técnico

Para empezar a utilizar KASAN con código BPF compilado en tiempo justo, puedes utilizar la herramienta `bpftrace` para crear un programa de seguimiento que utilice KASAN. Por ejemplo, puedes utilizar el comando `bpftrace -e 'kasan:enable'` para habilitar KASAN en tu sistema.

```bash
bpftrace -e 'kasan:enable'
```

---

**Fuente original:** [https://lwn.net/Articles/1077740/](https://lwn.net/Articles/1077740/)
