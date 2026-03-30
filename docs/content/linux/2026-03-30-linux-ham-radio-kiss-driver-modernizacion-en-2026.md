# Linux Ham Radio KISS Driver: Modernización en 2026

**Fecha:** 2026-03-30
**Categoría:** linux
**Tags:** linux, robotica, codigo
**Título original:** Linux Ham Radio KISS Serial Driver Being Modernized In 2026

---

## Introducción

El driver de Linux para comunicaciones de radio amateur, KISS, está siendo actualizado después de más de dos décadas sin cambios significativos. Esta modernización busca mejorar la seguridad y la legibilidad del código.

## ¿Qué es?

El driver KISS es un protocolo serial para intercambiar datos entre una computadora y un terminal node computer para conexiones de radio amateur AX.25. Ha estado presente en el núcleo de Linux desde hace más de 20 años.

## ¿Cómo funciona?

El driver KISS utiliza el protocolo KISS para enviar y recibir datos a través de una conexión serial. El código ha sido actualizado para mejorar la seguridad y la legibilidad, incluyendo la eliminación de inicializaciones redundantes y la modernización del sistema de registro.

## ¿Por qué importa?

La modernización del driver KISS es importante porque mejorará la seguridad y la estabilidad de las conexiones de radio amateur en Linux. Esto beneficiará a los usuarios que dependen de estas conexiones para sus actividades de radio amateur.

## Consejo técnico

Si estás utilizando el driver KISS en tu proyecto de radio amateur, te recomendamos revisar el código actualizado y aplicar las mejoras para asegurarte de que estás utilizando la versión más segura y estable.

```bash
git pull https://git.kernel.org/pub/scm/linux/kernel/git/mashiro/linux.git mkiss-modernization
```

---

**Fuente original:** [https://www.phoronix.com/news/Linux-Ham-Radio-MKISS-2026](https://www.phoronix.com/news/Linux-Ham-Radio-MKISS-2026)
