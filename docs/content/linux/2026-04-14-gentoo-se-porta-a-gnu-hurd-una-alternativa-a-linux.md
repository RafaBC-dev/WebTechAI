# Gentoo se porta a GNU Hurd: una alternativa a Linux

**Fecha:** 2026-04-14
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** They Weren’t Joking: Gentoo WAS ported to GNU Hurd

---

## Introducción

La distribución Gentoo Linux ha sido portada al kernel GNU Hurd, una alternativa a Linux con una arquitectura de microkernel. Esta noticia puede ser importante para los usuarios de Linux que buscan opciones más seguras y flexibles.

## ¿Qué es?

GNU Hurd es un kernel de microkernel que se basa en el kernel Mach. Se diferencia de Linux en que mantiene los drivers fuera del kernel, lo que reduce el riesgo de que un dispositivo malicioso cause problemas. Aunque todavía hay pocos drivers disponibles para Hurd, esta arquitectura puede ofrecer beneficios en cuanto a la seguridad y la escalabilidad.

## ¿Cómo funciona?

La portación de Gentoo a Hurd implica que el sistema operativo puede ejecutarse con el kernel Hurd en lugar del kernel Linux. Esto permite a los usuarios experimentar con la arquitectura de microkernel y aprovechar sus beneficios. La configuración de Hurd es similar a la de Linux, pero con algunas diferencias importantes en cuanto a la gestión de los drivers y la seguridad.

## ¿Por qué importa?

La disponibilidad de Gentoo en Hurd puede atraer a los usuarios de Linux que buscan opciones más seguras y flexibles. Además, la arquitectura de microkernel de Hurd puede ofrecer beneficios en cuanto a la escalabilidad y la gestión de recursos. Esto puede ser especialmente importante para los usuarios que necesitan ejecutar múltiples aplicaciones simultáneamente.

## Consejo técnico

Si estás interesado en probar Hurd, puedes instalar la versión de Gentoo con el kernel Hurd y experimentar con la arquitectura de microkernel. Recuerda que todavía hay pocos drivers disponibles para Hurd, por lo que es importante verificar la compatibilidad de tus dispositivos antes de hacer la transición.

```bash
sudo emerge -a gentoo-hurd
```

---

**Fuente original:** [https://hackaday.com/2026/04/13/they-werent-joking-gentoo-was-ported-to-gnu-hurd/](https://hackaday.com/2026/04/13/they-werent-joking-gentoo-was-ported-to-gnu-hurd/)
