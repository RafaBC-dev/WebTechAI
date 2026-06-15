# El bicho del año 2000 en BSD 2.11 que sobrevivió a 2000

**Fecha:** 2026-06-15
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** The Y2K Bug in BSD 2.11 that Survived 2000

---

## Introducción

Un año antes de la llegada del nuevo milenio, se predijo que el bicho del año 2000 paralizaría la sociedad moderna. Gracias a los esfuerzos de muchos ingenieros y desarrolladores, apenas hubo problemas. Sin embargo, un bug en BSD 2.11 ha sido descubierto recientemente.

## ¿Qué es?

El bicho del año 2000 fue un problema de software que se esperaba que causara problemas significativos al pasar del año 1999 al 2000. Sin embargo, un bug en la versión 2.11 de BSD ha sido descubierto recientemente, que se debió a la utilización de números de año explícitos del siglo XX.

## ¿Cómo funciona?

El bug se produce en la versión 2.11 de BSD, que se ejecuta en un PDP-11/70 de 1975. El problema se produce cuando se utiliza un adaptador para recibir señales de tiempo de WWV/WWVH y se ejecuta el comando `ntpd -a any -d -d -d -d`. Esto produce un error de 'desplazamiento excesivo' en el registro.

## ¿Por qué importa?

Este bug es importante porque muestra que los problemas del año 2000 no se limitaron a los campos de años de dos dígitos, sino que también se debieron a atajos y suposiciones descuidadas al manejar años. Esto puede ser útil para evitar problemas similares en el futuro, como el problema del año 2038.

## Consejo técnico

Si estás trabajando con sistemas antiguos, asegúrate de revisar la documentación y los códigos para asegurarte de que no hay problemas de año similares. Puedes utilizar herramientas como `ntpd` para verificar el tiempo y evitar problemas de sincronización.

```bash
ntpd -a any -d -d -d -d
```

---

**Fuente original:** [https://hackaday.com/2026/06/15/the-y2k-bug-in-bsd-2-11-that-survived-2000/](https://hackaday.com/2026/06/15/the-y2k-bug-in-bsd-2-11-that-survived-2000/)
