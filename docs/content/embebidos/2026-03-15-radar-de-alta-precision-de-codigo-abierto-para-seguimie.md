# Radar de alta precisión de código abierto para seguimiento de objetos a 20km

**Fecha:** 2026-03-15
**Categoría:** embebidos
**Tags:** ia-local, python, herramientas
**Título original:** AERIS-10 open-source hardware radar can track multiple objects up to 20km away

---

## Introducción

Un equipo de desarrolladores ha lanzado un sistema de radar de código abierto llamado AERIS-10, capaz de seguir múltiples objetos a una distancia de hasta 20km. Este proyecto es relevante debido a su potencial para ser utilizado en aplicaciones de seguridad, investigación y desarrollo de tecnologías de vanguardia.

## ¿Qué es?

El AERIS-10 es un sistema de radar de alta precisión basado en hardware de código abierto, que utiliza una frecuencia de 10.5 GHz y una modulación de frecuencia lineal (LFM) para generar pulsos de radar. Se compone de una placa principal con un procesador de campo programable (FPGA) AMD Artix-7 y un microcontrolador ST STM32F746xx.

## ¿Cómo funciona?

El sistema de radar funciona generando pulsos de radar a través del DAC y leyendo datos de ADC. El FPGA realiza procesamiento de señal, incluyendo corrección de ganancia automática, conversión de baseband a I/Q, decimación, filtrado y procesamiento de Doppler, MTI y CFAR. El sistema también incluye una interfaz USB y una serie de sensores y actuadores para controlar la configuración y el funcionamiento del sistema.

## ¿Por qué importa?

El AERIS-10 es importante debido a su capacidad para seguir múltiples objetos a largas distancias, lo que lo hace útil para aplicaciones de seguridad, investigación y desarrollo de tecnologías de vanguardia. También es un ejemplo de cómo la tecnología de código abierto puede ser utilizada para crear sistemas de alta precisión y complejidad.

## Consejo técnico

Si estás interesado en desarrollar un sistema de radar propio, considera utilizar el AERIS-10 como punto de partida y modificarlo para adaptarlo a tus necesidades específicas. Puedes encontrar todos los recursos necesarios en el repositorio de GitHub de NawfalMotii79.

```bash
python
```

---

**Fuente original:** [https://www.cnx-software.com/2026/03/15/aeris-10-open-source-hardware-radar-can-track-multiple-objects-up-to-20km-away/](https://www.cnx-software.com/2026/03/15/aeris-10-open-source-hardware-radar-can-track-multiple-objects-up-to-20km-away/)
