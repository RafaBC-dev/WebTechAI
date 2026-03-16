# Radar abiertamente disponible para rastrear objetos a 20km de distancia

**Fecha:** 2026-03-16
**Categoría:** embebidos
**Tags:** robotica, electronica, linux
**Título original:** AERIS-10 open-source hardware radar can track multiple objects up to 20km away

---

## Introducción

Un equipo de desarrolladores ha creado un sistema de radar de alta precisión y bajo costo, basado en tecnología de código abierto. Este sistema puede rastrear múltiples objetos a una distancia de hasta 20km y tiene aplicaciones en campos como la seguridad, la investigación científica y la industria.

## ¿Qué es?

El AERIS-10 es un sistema de radar de 10.5 GHz que utiliza una matriz de antenas de 32x16 para detectar y rastrear objetos en un radio de hasta 20km. El sistema se basa en un procesador de campo-programable (FPGA) AMD Artix-7 y utiliza una modulación de frecuencia lineal (LFM) para generar señales de radar.

## ¿Cómo funciona?

El AERIS-10 funciona generando señales de radar mediante el procesador FPGA, que luego se envían a través de la matriz de antenas. Las señales reflejadas por los objetos se capturan y procesan mediante el FPGA, que utiliza algoritmos de procesamiento de señales para detectar y rastrear los objetos. El sistema también incluye un microcontrolador STM32 para gestionar la comunicación con el usuario y controlar el sistema.

## ¿Por qué importa?

El AERIS-10 tiene aplicaciones en campos como la seguridad, la investigación científica y la industria. Puede ser utilizado para detectar y rastrear objetos en áreas de alta seguridad, como aeropuertos y centros de investigación. También puede ser utilizado en aplicaciones de monitoreo ambiental y de seguimiento de vehículos.

## Consejo técnico

Si deseas implementar un sistema de radar similar, puedes empezar investigando sobre la documentación del AERIS-10 y utilizando herramientas como el software de simulación de radar de Python, que se proporciona en la documentación del proyecto.

```bash
python -m radar_simulator
```

---

**Fuente original:** [https://www.cnx-software.com/2026/03/15/aeris-10-open-source-hardware-radar-can-track-multiple-objects-up-to-20km-away/](https://www.cnx-software.com/2026/03/15/aeris-10-open-source-hardware-radar-can-track-multiple-objects-up-to-20km-away/)
