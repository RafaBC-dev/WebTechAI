# Cómo excluir plataformas al liberar un paquete en Linux

**Fecha:** 2026-04-11
**Categoría:** linux
**Tags:** robotica, linux, codigo
**Título original:** Exclude platforms when releasing a package

---

## Introducción

Un desarrollador de ROS (Robot Operating System) se enfrenta a problemas de compilación en Fedora debido a la falta de dependencias. Esto genera errores en la CI (Integración Continua) diarios. ¿Cómo evitar esto?

## ¿Qué es?

ROS es un sistema operativo para robots que permite a los desarrolladores crear aplicaciones y herramientas de forma sencilla. Un paquete es una unidad de software que contiene código y dependencias. La CI es un proceso automático que verifica la compilación y ejecución de código.

## ¿Cómo funciona?

La liberación de un paquete en ROS implica crear un paquete que pueda ser instalado en diferentes plataformas. Sin embargo, si una plataforma no tiene las dependencias necesarias, la compilación falla. En este caso, el desarrollador quiere excluir la plataforma Fedora de la liberación.

## ¿Por qué importa?

Excluir plataformas innecesarias en la liberación de un paquete ayuda a evitar errores en la CI y a ahorrar tiempo y recursos. Esto es especialmente importante en proyectos de software complejos como ROS.

## Consejo técnico

Para excluir la plataforma Fedora de la liberación de un paquete en ROS, puedes utilizar la opción `--exclude-platforms` en el comando `bloom-release`. Por ejemplo: `bloom-release --exclude-platforms fedora`.

```bash
bloom-release --exclude-platforms fedora
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/exclude-platforms-when-releasing-a-package/53939](https://discourse.openrobotics.org/t/exclude-platforms-when-releasing-a-package/53939)
