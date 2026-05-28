# Nuevos compiladores para gráficos en dispositivos ARM Mali

**Fecha:** 2026-05-28
**Categoría:** robotica
**Tags:** linux, codigo, herramientas
**Título original:** KRAID Being Developed As New Compiler For Modern Arm Mali Graphics

---

## Introducción

La comunidad de desarrollo de Mesa ha anunciado la creación de un nuevo compilador para gráficos en dispositivos ARM Mali, llamado KRAID. Este proyecto busca mejorar la eficiencia y el rendimiento de los gráficos en dispositivos móviles y de escritorio.

## ¿Qué es?

KRAID es un nuevo compilador escrito en Rust para gráficos en dispositivos ARM Mali, diseñado para procesadores gráficos Valhall y posteriores. Está inspirado en el compilador NAK de la NVIDIA NVK Vulkan driver.

## ¿Cómo funciona?

KRAID traduce código de alto nivel (NIR) a instrucciones de hardware específicas para los procesadores gráficos ARM Mali. Actualmente está en etapas de desarrollo y ha pasado su primer test de conformidad con dEQP.

## ¿Por qué importa?

KRAID puede mejorar significativamente el rendimiento y la eficiencia de los gráficos en dispositivos móviles y de escritorio, lo que es especialmente importante para aplicaciones que requieren gráficos intensivos, como juegos y simulaciones.

## Consejo técnico

Si deseas aprender más sobre KRAID, puedes revisar el código fuente y la documentación de la inicialización de merge request para Mesa.

---

**Fuente original:** [https://www.phoronix.com/news/Mesa-Arm-Mali-KRAID](https://www.phoronix.com/news/Mesa-Arm-Mali-KRAID)
