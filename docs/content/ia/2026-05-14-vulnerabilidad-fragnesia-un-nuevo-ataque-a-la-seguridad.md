# Vulnerabilidad Fragnesia: un nuevo ataque a la seguridad de Linux

**Fecha:** 2026-05-14
**Categoría:** ia
**Tags:** linux, seguridad, vulnerabilidad
**Título original:** Yet another Dirty Frag type vulnerability: Fragnesia

---

## Introducción

Un investigador ha descubierto una nueva vulnerabilidad en Linux que permite el escalado de privilegios locales. Esta vulnerabilidad, llamada Fragnesia, se encuentra en el mismo sistema que la vulnerabilidad Dirty Frag y requiere una lógica de bug en el sub-sistema XFRM ESP-in-TCP.

## ¿Qué es?

Fragnesia es una vulnerabilidad de escalado de privilegios locales en Linux que permite a un atacante escribir bytes arbitrarios en el caché de páginas de kernel de archivos de solo lectura sin necesidad de una condición de carrera.

## ¿Cómo funciona?

La vulnerabilidad se produce debido a un bug de lógica en el sub-sistema XFRM ESP-in-TCP de Linux, lo que permite a un atacante escribir bytes arbitrarios en el caché de páginas de kernel de archivos de solo lectura.

## ¿Por qué importa?

Esta vulnerabilidad es importante porque permite a un atacante escalarse de privilegios locales y acceder a información confidencial en un sistema Linux.

## Consejo técnico

Si estás utilizando Linux, asegúrate de actualizar tu sistema con el último parche disponible para evitar esta vulnerabilidad. Puedes verificar la versión de tu kernel ejecutando el comando `uname -a` y verificando si hay actualizaciones disponibles en el sitio web de Linux.

```bash
uname -a
```

---

**Fuente original:** [https://lwn.net/Articles/1072647/](https://lwn.net/Articles/1072647/)
