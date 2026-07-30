# NightRun: un proyecto que ejecuta LLMs locales sin OS en Raspberry Pi y PCs x86

**Fecha:** 2026-07-30
**Categoría:** ia
**Tags:** llms, ia-local, robotica
**Título original:** NightRun UEFI application boots a local LLM on Raspberry Pi 5 and x86 PCs without an OS

---

## Introducción

NightRun es un proyecto experimental de código abierto que permite ejecutar modelos de lenguaje de inteligencia artificial (LLMs) locales en dispositivos sin sistema operativo, como Raspberry Pi y PCs x86, sin necesidad de cargar un OS convencional.

## ¿Qué es?

NightRun es una aplicación UEFI que se ejecuta directamente desde una unidad de almacenamiento USB o tarjeta microSD, sin cargar un OS convencional, y permite ejecutar LLMs locales con mayor eficiencia en términos de memoria y velocidad de procesamiento.

## ¿Cómo funciona?

NightRun utiliza la API de UEFI para acceder a los servicios de arranque y manejo de dispositivo, y carga el modelo de LLM en la memoria RAM, donde se ejecuta utilizando kernels de AVX2/FMA/F16C en x86 y NEON en Raspberry Pi. El modelo se ejecuta directamente desde la memoria RAM sin necesidad de desquantizar.

## ¿Por qué importa?

NightRun es importante porque permite ejecutar LLMs locales de manera eficiente y segura, sin necesidad de cargar un OS convencional, lo que reduce el consumo de memoria y mejora la velocidad de procesamiento. Esto tiene aplicaciones en diversas áreas, como la automatización y la inteligencia artificial.

## Consejo técnico

Si deseas probar NightRun en tu Raspberry Pi o PC x86, asegúrate de tener un modelo de LLM compatible y una tarjeta microSD o unidad de almacenamiento USB con suficiente espacio para cargar el modelo.

---

**Fuente original:** [https://www.cnx-software.com/2026/07/30/nightrun-uefi-application-boots-a-local-llm-on-raspberry-pi-5-and-x86-pcs-without-an-os/](https://www.cnx-software.com/2026/07/30/nightrun-uefi-application-boots-a-local-llm-on-raspberry-pi-5-and-x86-pcs-without-an-os/)
