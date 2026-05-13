# Huge Pages Transparentes: un salto hacia 1GB de memoria

**Fecha:** 2026-05-13
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** [$] Scaling transparent huge pages to 1GB

---

## Introducción

Los desarrolladores de Linux han estado trabajando en mejorar la gestión de la memoria en sistemas operativos. Un paso importante en este sentido es la implementación de huge pages transparentes, que permiten a los procesos acceder a bloques de memoria mucho más grandes de lo habitual. Esto puede mejorar significativamente el rendimiento de aplicaciones que requieren grandes cantidades de memoria.

## ¿Qué es?

Los huge pages transparentes (THPs) son una tecnología que permite a los procesos acceder a bloques de memoria de hasta 1GB de tamaño sin necesidad de configuración adicional. Esto se logra a través de la creación de páginas de memoria de tamaño 1GB, que se pueden asignar a los procesos de manera transparente.

## ¿Cómo funciona?

La implementación de THPs implica la creación de páginas de memoria de tamaño 1GB y la asignación de estas páginas a los procesos de manera transparente. Esto se logra a través de la modificación del kernel de Linux para que pueda crear y gestionar páginas de memoria de tamaño 1GB. Los desarrolladores también deben configurar el sistema para que utilice THPs de manera predeterminada.

## ¿Por qué importa?

La implementación de THPs puede mejorar significativamente el rendimiento de aplicaciones que requieren grandes cantidades de memoria. Esto se debe a que los procesos pueden acceder a bloques de memoria de tamaño 1GB de manera más eficiente, lo que reduce la latencia y mejora la velocidad de respuesta. Esto puede ser especialmente beneficioso para aplicaciones como bases de datos, sistemas de archivo y simulaciones científicas.

## Consejo técnico

Si deseas probar THPs en tu sistema, puedes utilizar el comando `echo 1 > /sys/kernel/mm/transparent_hugepage/enabled` para habilitarlos. Luego, puedes verificar si THPs están habilitados utilizando el comando `cat /sys/kernel/mm/transparent_hugepage/enabled`. Recuerda que THPs solo están disponibles en sistemas x86.

```bash
echo 1 > /sys/kernel/mm/transparent_hugepage/enabled
```

---

**Fuente original:** [https://lwn.net/Articles/1071716/](https://lwn.net/Articles/1071716/)
