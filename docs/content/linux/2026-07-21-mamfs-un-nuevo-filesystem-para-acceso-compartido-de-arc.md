# Mamfs: un nuevo filesystem para acceso compartido de archivos en memoria

**Fecha:** 2026-07-21
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** [$] Merging famfs?

---

## Introducción

El filesystem mamfs, diseñado para proporcionar acceso compartido a archivos enormes en memoria, ha regresado al Linux Storage, Filesystem, Memory Management, and BPF Summit (LSFMM+BPF) en 2026. Aunque fue discutido en 2024 y 2025, aún no ha sido incluido en el kernel. ¿Qué problemas resuelve este nuevo filesystem?

## ¿Qué es?

El filesystem mamfs es un sistema de archivos diseñado para proporcionar acceso compartido a archivos enormes que se almacenan en memoria. Esto permite a múltiples procesos acceder y manipular estos archivos de manera simultánea, lo que es especialmente útil en entornos de alta performance y escalabilidad.

## ¿Cómo funciona?

El mamfs utiliza la tecnología CXL (Compute Express Link) para acceder a dispositivos de almacenamiento en memoria. Al hacerlo, permite a los procesos acceder a archivos enormes de manera eficiente y segura, utilizando una arquitectura de capas que separa la lógica de acceso del almacenamiento en sí.

## ¿Por qué importa?

El mamfs es importante porque resuelve problemas de escalabilidad y rendimiento en entornos de alta demanda. Al permitir el acceso compartido a archivos enormes, reduce la carga de trabajo en los sistemas de archivos y mejora la eficiencia de las aplicaciones que los utilizan.

## Consejo técnico

Si deseas probar el mamfs en tu sistema, puedes compilar el código fuente y configurarlo en tu kernel. Recuerda que el mamfs aún no está incluido en el kernel oficial, por lo que debes compilarlo manualmente utilizando el comando `make` en la carpeta del proyecto.

```bash
make
```

---

**Fuente original:** [https://lwn.net/Articles/1082687/](https://lwn.net/Articles/1082687/)
