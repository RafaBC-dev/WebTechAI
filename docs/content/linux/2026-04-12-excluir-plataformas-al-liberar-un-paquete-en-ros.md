# Excluir plataformas al liberar un paquete en ROS

**Fecha:** 2026-04-12
**Categoría:** linux
**Tags:** robotica, linux, codigo
**Título original:** Exclude platforms when releasing a package

---

## Introducción

Un desarrollador de ROS ha enfrentado problemas con la integración continua (CI) después de liberar un paquete debido a dependencias no disponibles en Fedora. Esto ha generado correos electrónicos diarios con errores de compilación en máquinas de Fedora.

## ¿Qué es?

ROS (Robot Operating System) es un framework de software de código abierto para la robótica. Un paquete es una unidad de software que se puede liberar y compartir con la comunidad de ROS.

## ¿Cómo funciona?

La integración continua (CI) es un proceso automatizado que se ejecuta después de liberar un paquete para verificar su funcionalidad y compatibilidad con diferentes plataformas. En este caso, la CI ha fallado en máquinas de Fedora debido a la falta de dependencias necesarias.

## ¿Por qué importa?

Excluir plataformas al liberar un paquete es importante para evitar errores de compilación y asegurar que el paquete se libere correctamente. Esto es especialmente relevante en entornos de CI, donde la automatización es crucial para la eficiencia y la precisión.

## Consejo técnico

Para excluir plataformas al liberar un paquete en ROS, puedes utilizar la opción `--exclude-platforms` en el comando `bloom-release`. Por ejemplo: `bloom-release --exclude-platforms Fedora`.

```bash
bloom-release --exclude-platforms Fedora
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/exclude-platforms-when-releasing-a-package/53939](https://discourse.openrobotics.org/t/exclude-platforms-when-releasing-a-package/53939)
