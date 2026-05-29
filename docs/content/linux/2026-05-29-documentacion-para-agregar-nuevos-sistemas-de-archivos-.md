# Documentación para agregar nuevos sistemas de archivos a Linux

**Fecha:** 2026-05-29
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** [$] Policies for merging new filesystems

---

## Introducción

En el marco del Linux Storage, Filesystem, Memory Management y BPF Summit, Amir Goldstein presentó una propuesta para documentar la adición de nuevos sistemas de archivos al núcleo de Linux. Esto busca evitar que se agreguen sistemas de archivos que aumenten la carga de trabajo para los desarrolladores de VFS.

## ¿Qué es?

La propuesta de Goldstein consiste en crear una documentación que establezca políticas claras para la adición de nuevos sistemas de archivos al núcleo de Linux. Esto busca evitar que se agreguen sistemas de archivos que sean difíciles de mantener y no sean compatibles con las últimas tecnologías de Linux, como la API de montaje 'nueva' y los folios.

## ¿Cómo funciona?

La documentación propuesta por Goldstein busca establecer criterios para evaluar la viabilidad de agregar nuevos sistemas de archivos al núcleo de Linux. Esto incluye la evaluación de la complejidad del sistema de archivos, su compatibilidad con las últimas tecnologías de Linux y su mantenimiento futuro.

## ¿Por qué importa?

La adición de nuevos sistemas de archivos al núcleo de Linux puede tener un impacto significativo en la estabilidad y la seguridad del sistema operativo. La documentación propuesta por Goldstein busca evitar que se agreguen sistemas de archivos que aumenten la carga de trabajo para los desarrolladores de VFS y que puedan comprometer la estabilidad y la seguridad de Linux.

## Consejo técnico

Si estás desarrollando un nuevo sistema de archivos para Linux, asegúrate de revisar la documentación propuesta por Goldstein y evalúa si tu sistema de archivos cumple con los criterios establecidos. Esto te ayudará a evitar problemas de compatibilidad y mantenimiento en el futuro.

---

**Fuente original:** [https://lwn.net/Articles/1074557/](https://lwn.net/Articles/1074557/)
