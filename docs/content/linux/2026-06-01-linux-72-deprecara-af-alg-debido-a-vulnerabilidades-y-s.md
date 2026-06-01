# Linux 7.2 deprecará AF_ALG debido a vulnerabilidades y superficie de ataque

**Fecha:** 2026-06-01
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Linux 7.2 Proceeding To Deprecate AF_ALG Due To "Massive Attack Surface", Drops Offloading

---

## Introducción

La versión 7.2 del kernel de Linux está a punto de deprecar la interfaz AF_ALG debido a una gran cantidad de vulnerabilidades que han sido descubiertas recientemente. Esta medida se debe a que la interfaz expone una superficie de ataque masiva que no ha podido ser protegida con herramientas de descubrimiento de vulnerabilidades modernas.

## ¿Qué es?

AF_ALG es una interfaz del kernel de Linux que permite a las aplicaciones de usuario acceder directamente al motor de criptografía integrado del kernel. Sin embargo, esta interfaz ha demostrado ser una superficie de ataque masiva que no ha podido ser protegida con herramientas de descubrimiento de vulnerabilidades modernas.

## ¿Cómo funciona?

AF_ALG permite a las aplicaciones de usuario acceder directamente al motor de criptografía integrado del kernel, lo que puede ser útil para ciertas aplicaciones que requieren criptografía en tiempo real. Sin embargo, esta interfaz también expone una superficie de ataque masiva que puede ser explotada por atacantes.

## ¿Por qué importa?

La deprecación de AF_ALG es importante porque elimina una superficie de ataque masiva que ha sido explotada recientemente. Además, esta medida también elimina la capacidad de utilizar offloading de criptografía en AF_ALG, lo que puede ser un problema para ciertas aplicaciones que requieren criptografía en tiempo real.

## Consejo técnico

Si estás utilizando AF_ALG en tu aplicación, debes considerar migrar a una interfaz de criptografía más segura, como la interfaz de criptografía de usuario. Puedes utilizar la herramienta `cryptodev` para verificar la seguridad de tu aplicación y migrar a una interfaz más segura si es necesario.

```bash
cryptodev
```

---

**Fuente original:** [https://www.phoronix.com/news/Linux-AF-ALG-Deprecation](https://www.phoronix.com/news/Linux-AF-ALG-Deprecation)
