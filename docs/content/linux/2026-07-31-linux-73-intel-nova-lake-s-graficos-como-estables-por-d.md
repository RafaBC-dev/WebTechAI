# Linux 7.3: Intel Nova Lake S Gráficos como Estables por Defecto

**Fecha:** 2026-07-31
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Linux 7.3 Will Treat Intel Nova Lake S Graphics As Stable

---

## Introducción

La próxima versión del kernel Linux, 7.3, incluirá soporte estable para los gráficos integrados de los procesadores Intel Nova Lake S. Esto significa que los usuarios podrán utilizar estos gráficos sin necesidad de configuraciones adicionales.

## ¿Qué es?

Los procesadores Intel Nova Lake S son una serie de procesadores que incluyen gráficos integrados Xe3P. Estos gráficos han estado disponibles en el kernel Linux desde hace tiempo, pero con una configuración experimental que requería la utilización de un parámetro de módulo específico.

## ¿Cómo funciona?

La actualización del kernel Linux 7.3 incluye un parche que elimina la necesidad de utilizar el parámetro 'force_probe' para habilitar el soporte de gráficos integrados en los procesadores Intel Nova Lake S. Esto se debe a que los ingenieros de software de Intel han considerado que los gráficos son lo suficientemente estables como para ser habilitados por defecto.

## ¿Por qué importa?

La inclusión de soporte estable para los gráficos integrados de los procesadores Intel Nova Lake S en el kernel Linux 7.3 es importante porque permite a los usuarios aprovechar al máximo la potencia de estos procesadores sin necesidad de configuraciones adicionales. Esto también facilita la integración de estos procesadores en sistemas Linux.

## Consejo técnico

Si estás planificando utilizar un procesador Intel Nova Lake S en un sistema Linux, asegúrate de actualizar tu kernel a la versión 7.3 o superior para aprovechar el soporte estable de gráficos integrados.

```bash
sudo apt-get update && sudo apt-get install linux-image-7.3
```

---

**Fuente original:** [https://www.phoronix.com/news/Linux-7.3-Intel-NVL-S-Stable](https://www.phoronix.com/news/Linux-7.3-Intel-NVL-S-Stable)
