# El futuro de EFS: ¿un nuevo mantenedor o una eliminación?

**Fecha:** 2026-06-08
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Linux EFS File-System May Have New Maintainer - Or It Might Just Get Removed

---

## Introducción

La comunidad de Linux se debate sobre el mantenimiento de un antiguo driver de sistema de archivos, el EFS, que ya no es utilizado por nadie. ¿Qué pasa si alguien se ofrece a mantenerlo, aunque no lo use?

## ¿Qué es?

El EFS es un sistema de archivos de Linux que se utilizó en el pasado en los sistemas operativos de Silicon Graphics, IRIX, para leer sistemas de archivos en CD-ROM y discos duros. Fue reemplazado por XFS en la versión 6.0 de IRIX.

## ¿Cómo funciona?

El EFS es un driver de sistema de archivos que se encarga de leer y escribir en sistemas de archivos no ISO9660. Fue desarrollado por Silicon Graphics y se utilizó en la versión 5.x de IRIX. Aunque ya no es utilizado, alguien se ha ofrecido a mantenerlo y enviar correcciones para que funcione con versiones más recientes de GCC.

## ¿Por qué importa?

La decisión sobre el mantenimiento del EFS es importante porque puede afectar a aquellos que aún utilizan sistemas de archivos EFS para recuperar datos antiguos. Si se elimina, no habrá forma de acceder a esos datos en versiones más recientes de Linux.

## Consejo técnico

Si necesitas acceder a un sistema de archivos EFS, puedes intentar utilizar una versión más antigua de Linux, como una versión LTS, que todavía soporta este sistema de archivos.

---

**Fuente original:** [https://www.phoronix.com/news/Linux-EFS-File-System-2026](https://www.phoronix.com/news/Linux-EFS-File-System-2026)
