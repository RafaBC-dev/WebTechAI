# Mejora en Linux 7.2 para comunicar comportamiento de archivos

**Fecha:** 2026-06-15
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Linux 7.2 To Better Communicate File-System Casefolding For Helping Windows NFS & More

---

## Introducción

La versión en desarrollo de Linux 7.2 ha incorporado una mejora importante para la comunicación de comportamiento de archivos entre sistemas Linux y Windows. Esto permitirá a los servidores de archivos Linux informar a los clientes de Windows sobre la insensibilidad a mayúsculas y minúsculas de los archivos, lo que mejorará la compatibilidad y la eficiencia en la búsqueda de archivos.

## ¿Qué es?

La mejora consiste en exponer la información sobre el comportamiento de archivos de los sistemas de archivos locales a través de nuevas banderas de atributos de archivo (file_kattr). Esto permite a los servidores de archivos Linux, como NFSD y KSMBD, informar a los clientes sobre la insensibilidad a mayúsculas y minúsculas de los archivos, lo que es esencial para la compatibilidad con los clientes de Windows.

## ¿Cómo funciona?

Los sistemas de archivos locales, como FAT, EXFAT, NTFS3, HFS, HFS+, XFS, CIFS, NFS, VBOXSF y ISOFS, ahora reportan su comportamiento de archivo a través de las nuevas banderas de atributos de archivo. Esto permite a los servidores de archivos Linux informar a los clientes sobre la insensibilidad a mayúsculas y minúsculas de los archivos, lo que es esencial para la compatibilidad con los clientes de Windows.

## ¿Por qué importa?

Esta mejora es importante porque permite a los clientes de Windows funcionar correctamente con los servidores de archivos Linux, lo que mejora la compatibilidad y la eficiencia en la búsqueda de archivos. Además, permite a los servidores de archivos Linux informar a los clientes sobre la insensibilidad a mayúsculas y minúsculas de los archivos, lo que es esencial para la compatibilidad con los clientes de Windows.

## Consejo técnico

Si estás trabajando con servidores de archivos Linux y clientes de Windows, asegúrate de actualizar tu versión de Linux a 7.2 para aprovechar esta mejora. También es importante verificar la configuración de tus sistemas de archivos locales para asegurarte de que estén configurados correctamente para reportar su comportamiento de archivo.

```bash
No aplica
```

---

**Fuente original:** [https://www.phoronix.com/news/Linux-7.2-Casefolding](https://www.phoronix.com/news/Linux-7.2-Casefolding)
