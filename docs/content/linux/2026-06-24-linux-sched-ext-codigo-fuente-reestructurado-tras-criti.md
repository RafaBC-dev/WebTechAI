# Linux sched_ext: Código fuente reestructurado tras crítica de Linus Torvalds

**Fecha:** 2026-06-24
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** "Disgusting" Linux sched_ext Source Code Restructured Following Complaint By Linus Torvalds

---

## Introducción

Linus Torvalds, creador de Linux, ha criticado la forma en que se ha estructurado el código fuente del proyecto sched_ext. Ha sugerido que se utilice una estructura de directorios más organizada para evitar la proliferación de archivos con prefijos 'ext_'.

## ¿Qué es?

El proyecto sched_ext es un framework de programación en el núcleo de Linux que permite la creación de subprogramas de programación en el espacio de usuario (BPF) para controlar la planificación del procesador. Esto permite una mayor flexibilidad y personalización en la gestión del sistema.

## ¿Cómo funciona?

El framework sched_ext utiliza un conjunto de archivos C y cabecera para implementar la lógica de programación en el espacio de usuario. Sin embargo, Linus Torvalds ha criticado la forma en que se han creado estos archivos, sugiriendo que se utilice una estructura de directorios más organizada.

## ¿Por qué importa?

La reestructuración del código fuente de sched_ext es importante porque garantiza una mayor organización y mantenibilidad del código. Esto permite a los desarrolladores trabajar de manera más eficiente y evitar errores de configuración.

## Consejo técnico

Si estás trabajando con el proyecto sched_ext, es recomendable utilizar la herramienta 'git' para gestionar el código fuente y seguir las mejores prácticas de organización de directorios.

```bash
git add -A && git commit -m 'Reestructuración del código fuente de sched_ext'
```

---

**Fuente original:** [https://www.phoronix.com/news/Linux-Sched-Ext-Restructured](https://www.phoronix.com/news/Linux-Sched-Ext-Restructured)
