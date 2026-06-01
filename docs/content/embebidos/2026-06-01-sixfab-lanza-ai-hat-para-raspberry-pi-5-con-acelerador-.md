# Sixfab lanza AI HAT+ para Raspberry Pi 5 con acelerador AI DEEPX DX-M1

**Fecha:** 2026-06-01
**Categoría:** embebidos
**Tags:** ia-local, robotica, raspberry-pi
**Título original:** Sixfab AI HAT+ for Raspberry Pi 5 integrates DEEPX DX-M1 AI accelerator

---

## Introducción

Sixfab ha lanzado el AI HAT+ para Raspberry Pi 5, un módulo de expansión que integra un acelerador AI llamado DEEPX DX-M1. Este acelerador es similar al utilizado en otros dispositivos como el ALPON X5 y el Mini DX-M1 SoM. El AI HAT+ es diseñado para realizar tareas de visión AI localmente en el Raspberry Pi 5, como la detección de objetos y la segmentación de imágenes.

## ¿Qué es?

El AI HAT+ es un módulo de expansión para Raspberry Pi 5 que integra un acelerador AI llamado DEEPX DX-M1. Este acelerador es un procesador dedicado a realizar tareas de visión AI, como la detección de objetos y la segmentación de imágenes. El AI HAT+ se conecta al Raspberry Pi 5 a través de un cable PCIe y recibe poder a través de la conexión GPIO del 40-pines.

## ¿Cómo funciona?

El AI HAT+ utiliza el acelerador DEEPX DX-M1 para realizar tareas de visión AI localmente en el Raspberry Pi 5. El acelerador se conecta al Raspberry Pi 5 a través de un cable PCIe y recibe poder a través de la conexión GPIO del 40-pines. El AI HAT+ también incluye un conector para un ventilador que puede ser utilizado para enfriar el acelerador en caso de que se necesite.

## ¿Por qué importa?

El AI HAT+ es importante porque permite a los desarrolladores de Raspberry Pi realizar tareas de visión AI localmente en su dispositivo, sin necesidad de enviar los datos a un servidor remoto. Esto puede ser útil en aplicaciones como la detección de objetos en tiempo real, la segmentación de imágenes y la reconocimiento de patrones.

## Consejo técnico

Si deseas utilizar el AI HAT+ con tu Raspberry Pi 5, asegúrate de instalar el paquete dxrt-runtime desde la repositorio de Sixfab. Esto incluye el driver y la runtime necesarios para utilizar el acelerador DEEPX DX-M1.

```bash
sudo apt-get install dxrt-runtime
```

---

**Fuente original:** [https://www.cnx-software.com/2026/06/01/sixfab-ai-hat-for-raspberry-pi-5-integrates-deepx-dx-m1-ai-accelerator/](https://www.cnx-software.com/2026/06/01/sixfab-ai-hat-for-raspberry-pi-5-integrates-deepx-dx-m1-ai-accelerator/)
