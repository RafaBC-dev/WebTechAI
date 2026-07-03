# EFS File-System se eliminará de Linux 7.3 después de 20+ años sin mantenimiento

**Fecha:** 2026-07-03
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** EFS File-System Slated For Removal With Linux 7.3 After 20+ Years Unmaintained

---

## Introducción

Después de 20 años sin ser actualizado, el EFS file-system se eliminará de Linux 7.3. Este cambio afectará a usuarios de sistemas de archivo específicos, pero no tendrá un impacto significativo en la mayoría de los usuarios de Linux.

## ¿Qué es?

El EFS file-system es un sistema de archivos que se utilizaba en sistemas de CD-ROM y particiones de disco en SGI IRIX. Fue reemplazado por XFS en IRIX 6.0 y ha estado sin mantenimiento en el kernel de Linux desde entonces.

## ¿Cómo funciona?

El EFS file-system se implementó en el kernel de Linux como un driver de sistema de archivos en lectura solo. Sin embargo, nunca se actualizó y no ha sido utilizado en años. Los usuarios que necesitan acceder a sistemas de archivo EFS pueden utilizar herramientas de usuario como efsextract.

## ¿Por qué importa?

La eliminación del EFS file-system no tendrá un impacto significativo en la mayoría de los usuarios de Linux, ya que no se utiliza comúnmente. Sin embargo, puede afectar a usuarios de sistemas de archivo específicos que dependen de este sistema de archivos.

## Consejo técnico

Si necesitas acceder a sistemas de archivo EFS, puedes utilizar la herramienta efsextract de GitHub, que te permite extraer archivos de sistemas de archivo EFS.

```bash
efsextract -h
```

---

**Fuente original:** [https://www.phoronix.com/news/EFS-File-System-Removal-Coming](https://www.phoronix.com/news/EFS-File-System-Removal-Coming)
