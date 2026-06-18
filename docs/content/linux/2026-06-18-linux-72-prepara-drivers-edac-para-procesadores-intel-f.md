# Linux 7.2 prepara drivers EDAC para procesadores Intel futuros

**Fecha:** 2026-06-18
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Linux 7.2 EDAC Drivers Prep For Diamond Rapids, Nova Lake H

---

## Introducción

La versión 7.2 de Linux está trabajando en mejorar los drivers EDAC para prepararse para la llegada de nuevos procesadores Intel, como Diamond Rapids y Nova Lake H. Esto permitirá una mayor detección y corrección de errores en la memoria.

## ¿Qué es?

Los drivers EDAC (Error Detection And Correction) son componentes del sistema operativo Linux que se encargan de detectar y corregir errores en la memoria, lo que ayuda a prevenir problemas de estabilidad y seguridad. Estos drivers están especialmente diseñados para trabajar con memoria ECC (Error-Correcting Code), que es una tecnología que permite detectar y corregir errores en la información almacenada en la memoria.

## ¿Cómo funciona?

Los drivers EDAC en Linux 7.2 están siendo actualizados para agregar soporte para los procesadores Intel Diamond Rapids y Nova Lake H. Esto incluye la adición de funcionalidades como la detección de errores en subcanales de memoria y la lógica de reintento de errores en rango de rango. Además, se están consolidando los ayudantes de acceso a registros de controlador de memoria en código compartido, lo que mejora la eficiencia y la escalabilidad de los drivers.

## ¿Por qué importa?

La mejora de los drivers EDAC en Linux 7.2 es importante porque permitirá una mayor detección y corrección de errores en la memoria, lo que ayudará a prevenir problemas de estabilidad y seguridad en los sistemas que utilicen estos procesadores. Esto es especialmente relevante en entornos de alta disponibilidad y seguridad, donde la detección y corrección de errores en la memoria es crucial para mantener la integridad de la información.

## Consejo técnico

Si estás trabajando con Linux y deseas aprovechar las mejoras de los drivers EDAC en Linux 7.2, puedes probar actualizando tus drivers EDAC a la versión más reciente utilizando el comando `sudo apt-get update && sudo apt-get install linux-edac` en sistemas Ubuntu o Debian.

```bash
sudo apt-get update && sudo apt-get install linux-edac
```

---

**Fuente original:** [https://www.phoronix.com/news/Linux-7.2-EDAC](https://www.phoronix.com/news/Linux-7.2-EDAC)
