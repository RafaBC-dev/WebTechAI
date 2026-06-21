# KUnit de Linux ahora soporta JUnit para mejorar la interoperabilidad

**Fecha:** 2026-06-21
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Linux's KUnit Finally Supporting JUnit Output

---

## Introducción

La herramienta de pruebas unitarias KUnit de Linux ha agregado soporte para la salida en formato JUnit, lo que mejorará la interoperabilidad con sistemas de integración continua como Jenkins.

## ¿Qué es?

KUnit es una herramienta de pruebas unitarias para el núcleo de Linux que se inspiró en parte en Java's JUnit. Fue propuesta hace casi una década y se fusionó en el kernel 5.5 en 2020.

## ¿Cómo funciona?

KUnit ahora puede generar archivos en formato JUnit XML utilizando el argumento `--junit`. Esto permite una mayor interoperabilidad con sistemas de integración continua que utilizan este formato.

## ¿Por qué importa?

El soporte para JUnit es importante porque permite a los desarrolladores de Linux utilizar herramientas de integración continua como Jenkins de manera más sencilla y eficiente.

## Consejo técnico

Para utilizar el soporte de JUnit en KUnit, ejecuta el comando `make KUNIT_JUNIT=1` en el directorio del kernel y luego ejecuta `make KUNIT_JUNIT=1 test` para generar los archivos de pruebas en formato JUnit.

```bash
make KUNIT_JUNIT=1
```

---

**Fuente original:** [https://www.phoronix.com/news/Linux-KUnit-JUnit](https://www.phoronix.com/news/Linux-KUnit-JUnit)
