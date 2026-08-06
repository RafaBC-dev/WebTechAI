# Acceder a namespaces de red diferentes con BPF

**Fecha:** 2026-08-06
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** [$] Examining other network namespaces using BPF

---

## Introducción

Jordan Rife, experto en BPF, busca permitir a los programas BPF iterar a través de los sockets de un namespace de red diferente. Esto podría ser útil en entornos de Kubernetes.

## ¿Qué es?

BPF (Berkeley Packet Filter) es una tecnología de software que permite a los programas ejecutarse en el kernel de Linux. Los namespaces de red son una forma de aislamiento de red en Linux que permite a los procesos tener su propia red virtual.

## ¿Cómo funciona?

Los programas BPF pueden ser escritos para interactuar con los namespaces de red diferentes utilizando la función `bpf_iterate` que permite iterar a través de los sockets de un namespace de red específico. Esto requiere permisos adecuados para acceder a los sockets del namespace de red diferente.

## ¿Por qué importa?

Esta funcionalidad podría ser útil en entornos de Kubernetes donde los namespaces de red son comunes. Permite a los programas BPF acceder a los sockets de otros namespaces de red, lo que podría ser útil para la gestión de la red y la seguridad.

## Consejo técnico

Si estás trabajando con BPF en un entorno de Kubernetes, considera utilizar la función `bpf_iterate` para acceder a los sockets de otros namespaces de red. Puedes encontrar más información sobre esta función en la documentación de BPF.

```bash
bpf_iterate
```

---

**Fuente original:** [https://lwn.net/Articles/1085896/](https://lwn.net/Articles/1085896/)
