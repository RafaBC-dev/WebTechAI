# XFS ya no es experimental en Linux 7.2: mejora para dispositivos zonados

**Fecha:** 2026-06-16
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** XFS Zone Allocator No Longer Experimental With Linux 7.2

---

## Introducción

La versión 7.2 del kernel Linux incluye una actualización importante para el sistema de archivos XFS, que ahora ya no es experimental. Esto significa que los dispositivos zonados, como los discos duros de grabación en hilera (SMR) y los SSDs con espacio de nombres zonado (ZNS), pueden aprovechar al máximo las capacidades de XFS.

## ¿Qué es?

XFS es un sistema de archivos para Linux que permite gestionar dispositivos zonados, que requieren que las escrituras se realicen secuencialmente desde el principio hasta el final. Los dispositivos zonados son comunes en los discos duros de grabación en hilera (SMR) y los SSDs con espacio de nombres zonado (ZNS).

## ¿Cómo funciona?

El algoritmo de asignación de zonas de XFS es responsable de gestionar las zonas de escritura en los dispositivos zonados. Funciona asignando bloques de datos a zonas específicas del dispositivo, lo que permite que las escrituras se realicen de manera eficiente y segura. El algoritmo de asignación de zonas de XFS ha sido parte del kernel de Linux durante algún tiempo, pero ahora ya no es experimental.

## ¿Por qué importa?

La actualización de XFS en Linux 7.2 es importante porque permite que los dispositivos zonados aprovechen al máximo las capacidades de XFS. Esto significa que los usuarios pueden esperar una mejor rendimiento y una mayor confiabilidad en sus sistemas de archivos. Además, la actualización de XFS también incluye algunos ajustes menores y correcciones de errores.

## Consejo técnico

Si estás utilizando dispositivos zonados en tu sistema Linux, es recomendable actualizar a la versión 7.2 del kernel para aprovechar las mejoras de XFS. Puedes verificar la versión de tu kernel ejecutando el comando `uname -r` y actualizarlo ejecutando `sudo apt-get update && sudo apt-get upgrade` en sistemas Ubuntu o Debian.

```bash
uname -r
```

---

**Fuente original:** [https://www.phoronix.com/news/XFS-Zone-Allocator-Linux-7.2](https://www.phoronix.com/news/XFS-Zone-Allocator-Linux-7.2)
