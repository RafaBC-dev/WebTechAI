# Hostilidad hacia systemd: un proyecto de código abierto bajo ataque

**Fecha:** 2026-04-01
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** [$] Objections to systemd age-attestation changes go overboard

---

## Introducción

El proyecto systemd, un conjunto de herramientas de código abierto para administrar sistemas Linux, ha sido objeto de una campaña de odio y desinformación después de que se propusiera una actualización para facilitar la cumplimiento de leyes de verificación de edad. El desarrollador detrás de la actualización ha recibido amenazas de muerte y ha sido doxxado.

## ¿Qué es?

Systemd es un conjunto de herramientas de código abierto para administrar sistemas Linux, incluyendo la gestión de usuarios y servicios. Se utiliza en muchos sistemas Linux y es conocido por su capacidad para simplificar la administración de sistemas.

## ¿Cómo funciona?

Systemd utiliza un archivo de configuración JSON para almacenar información sobre los usuarios, incluyendo su fecha de nacimiento. La actualización propuesta agregaría un campo para almacenar esta información de manera explícita, lo que facilitaría el cumplimiento de leyes de verificación de edad.

## ¿Por qué importa?

La actualización propuesta es importante porque permite a los desarrolladores de aplicaciones almacenar la fecha de nacimiento de los usuarios de manera segura y eficiente, lo que es esencial para cumplir con leyes de verificación de edad. Esto tiene implicaciones para la privacidad y la seguridad de los usuarios.

## Consejo técnico

Si estás trabajando con systemd y necesitas almacenar información de usuarios, considera utilizar la herramienta `systemd-userdb` para crear y gestionar archivos de configuración JSON. Esto te permitirá almacenar información de manera segura y eficiente.

```bash
systemd-userdb
```

---

**Fuente original:** [https://lwn.net/Articles/1064706/](https://lwn.net/Articles/1064706/)
