# Cryptsetup 2.8.7: una actualización para superar la deprecación de AF_ALG

**Fecha:** 2026-07-22
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Cryptsetup 2.8.7 Released To Deal With Fallout Of Linux's Rushed AF_ALG Deprecation

---

## Introducción

La comunidad de Linux ha lanzado una actualización de Cryptsetup para abordar los problemas causados por la deprecación de la interfaz AF_ALG. Esta interfaz ha sido eliminada por razones de seguridad, lo que ha dejado a aplicaciones como Cryptsetup sin acceso a ciertas funcionalidades.

## ¿Qué es?

Cryptsetup es una herramienta de Linux que se utiliza para configurar y administrar dispositivos de almacenamiento criptografiados. AF_ALG es una interfaz del kernel de Linux que proporciona acceso a la API de criptografía del kernel desde el espacio de usuario.

## ¿Cómo funciona?

Cryptsetup utiliza AF_ALG para acceder a la API de criptografía del kernel y realizar operaciones de criptografía en el espacio de usuario. Sin embargo, la eliminación de AF_ALG ha dejado a Cryptsetup sin acceso a ciertas funcionalidades, lo que ha llevado a la actualización de Cryptsetup 2.8.7.

## ¿Por qué importa?

La actualización de Cryptsetup 2.8.7 es importante porque permite a las aplicaciones como Cryptsetup seguir funcionando correctamente incluso después de la eliminación de AF_ALG. Esto es especialmente importante para los usuarios que dependen de Cryptsetup para la seguridad de sus datos.

## Consejo técnico

Si estás utilizando Cryptsetup y te encuentras con problemas después de la actualización de AF_ALG, puedes intentar utilizar la opción de fallback a una biblioteca de criptografía del espacio de usuario. Puedes hacer esto ejecutando el comando `cryptsetup --fallback-userspace`.

```bash
cryptsetup --fallback-userspace
```

---

**Fuente original:** [https://www.phoronix.com/news/Cryptsetup-2.8.7-Released](https://www.phoronix.com/news/Cryptsetup-2.8.7-Released)
