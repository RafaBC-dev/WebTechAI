# Mejora de soporte para Raspberry Pi 5 en el kernel Linux

**Fecha:** 2026-07-13
**Categoría:** linux
**Tags:** robotica, linux, embebidos
**Título original:** Raspberry Pi 5 IOMMU Driver Being Worked On For The Mainline Linux Kernel

---

## Introducción

Después de más de dos años y medio desde su lanzamiento, el soporte para el Raspberry Pi 5 en el kernel Linux sigue mejorando. La última noticia es que se está trabajando en la integración del driver IOMMU para este dispositivo.

## ¿Qué es?

El driver IOMMU es un componente crucial para la gestión de la memoria gráfica en el Raspberry Pi 5. Su función es permitir la asignación eficiente de recursos de memoria para la aceleración gráfica. El driver se está adaptando desde el código de Raspberry Pi para ser compatible con el kernel Linux principal.

## ¿Cómo funciona?

El driver IOMMU utiliza la arquitectura de la placa para asignar eficientemente la memoria gráfica. Se utiliza la función generic_pt para la gestión de las tablas de páginas y se implementan las propiedades DT estándar-compliant para la compatibilidad con el firmware existente. El driver también se ha simplificado y se han realizado mejoras para una mayor eficiencia.

## ¿Por qué importa?

La integración del driver IOMMU en el kernel Linux principal mejorará significativamente el soporte para el Raspberry Pi 5. Esto permitirá a los usuarios aprovechar al máximo las capacidades de aceleración gráfica de la placa y mejorar la experiencia general de usuario.

## Consejo técnico

Si estás trabajando con el Raspberry Pi 5 y quieres aprovechar al máximo su capacidad de aceleración gráfica, asegúrate de compilar el kernel Linux con la opción PAGE_SIZE=4KB. Esto permitirá que el driver IOMMU funcione correctamente y te permitirá aprovechar al máximo las capacidades de la placa.

```bash
make menuconfig && make defconfig && make
```

---

**Fuente original:** [https://www.phoronix.com/news/Raspberry-Pi-5-IOMMU-Driver](https://www.phoronix.com/news/Raspberry-Pi-5-IOMMU-Driver)
