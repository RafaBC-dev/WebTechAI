# Soporte abierto para la GPU Mali G1 Pro en Linux

**Fecha:** 2026-05-14
**Categoría:** robotica
**Tags:** linux, codigo, herramientas
**Título original:** Arm Mali G1 Pro Now Working With Open-Source PanVK & Panfrost Drivers

---

## Introducción

La comunidad de Linux ha logrado soportar la GPU Mali G1 Pro, una de las últimas generaciones de hardware gráfico de ARM. Esto significa que los desarrolladores pueden utilizar esta GPU en sus proyectos de código abierto.

## ¿Qué es?

La GPU Mali G1 Pro es una de las últimas generaciones de hardware gráfico de ARM, diseñada para ofrecer una experiencia de visualización de alta calidad en dispositivos móviles y embebidos. La PanVK y Panfrost son dos drivers de código abierto que permiten utilizar esta GPU en Linux.

## ¿Cómo funciona?

La PanVK es un driver de Vulkan que permite utilizar la GPU Mali G1 Pro en aplicaciones que requieren gráficos acelerados. La Panfrost es un driver Gallium3D que proporciona soporte para la GPU Mali G1 Pro en Linux. Estos drivers se han integrado en la versión 26.2 de Mesa, que se espera que sea lanzada en agosto.

## ¿Por qué importa?

El soporte abierto para la GPU Mali G1 Pro es importante porque permite a los desarrolladores utilizar esta GPU en sus proyectos de código abierto. Esto puede ser especialmente útil para aquellos que desean crear aplicaciones que requieren gráficos acelerados, como juegos o simulaciones.

## Consejo técnico

Si deseas utilizar la PanVK y Panfrost en tu proyecto, asegúrate de configurar el entorno de compilación con la variable de entorno PAN_I_WANT_A_BROKEN_VULKAN_DRIVER=1. Esto te permitirá habilitar el soporte para la GPU Mali G1 Pro.

```bash
PAN_I_WANT_A_BROKEN_VULKAN_DRIVER=1
```

---

**Fuente original:** [https://www.phoronix.com/news/Arm-Mali-G1-Pro-Mesa-26.2](https://www.phoronix.com/news/Arm-Mali-G1-Pro-Mesa-26.2)
