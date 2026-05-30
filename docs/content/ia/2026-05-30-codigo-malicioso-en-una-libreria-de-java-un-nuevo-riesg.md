# Código malicioso en una librería de Java: un nuevo riesgo en la cadena de suministro

**Fecha:** 2026-05-30
**Categoría:** ia
**Tags:** librerias, herramientas, linux
**Título original:** Nesbitt: Protestware for coding agents

---

## Introducción

Un desarrollador de Java ha descubierto un código malicioso en la librería jqwik, que intenta eliminar pruebas y código existentes. Este incidente destaca un nuevo riesgo en la cadena de suministro que no es detectado por los escáneres de seguridad.

## ¿Qué es?

jqwik es una librería de Java para pruebas de propiedad, que ayuda a los desarrolladores a escribir pruebas de manera más eficiente. La librería jqwik es utilizada por muchos proyectos de Java para realizar pruebas de propiedad.

## ¿Cómo funciona?

La librería jqwik funciona creando pruebas de propiedad que se ejecutan en un entorno de prueba. El código malicioso se encuentra en la versión 1.10.0 de la librería, que fue lanzada el 25 de mayo. El código intenta eliminar pruebas y código existentes mediante un comando System.out.print de 68 bytes de ASCII.

## ¿Por qué importa?

Este incidente es importante porque destaca un nuevo riesgo en la cadena de suministro que no es detectado por los escáneres de seguridad. Los escáneres de seguridad suelen buscar instalaciones de hooks, llamadas de red, escrituras en el sistema de archivos, cadenas obfuscadas y similares. Sin embargo, el código malicioso en jqwik no se ajusta a estos patrones y, por lo tanto, no es detectado.

## Consejo técnico

Si estás utilizando jqwik en tu proyecto de Java, te recomendamos verificar la versión de la librería y actualizarla a la versión más reciente. Además, es importante revisar el código de la librería y asegurarte de que no haya código malicioso.

```bash
No aplica
```

---

**Fuente original:** [https://lwn.net/Articles/1075315/](https://lwn.net/Articles/1075315/)
