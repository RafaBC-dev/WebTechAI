# Limitar la frecuencia del NPU Intel para mejorar la gestión de potencia y calor

**Fecha:** 2026-04-10
**Categoría:** linux
**Tags:** ia-local, linux, codigo
**Título original:** Intel NPU Linux Driver To Allow Limiting Frequency For Power & Thermal Management

---

## Introducción

La Intel ha presentado un parche para el driver del NPU Linux que permite limitar la frecuencia del procesador para mejorar la gestión de potencia y calor. Esto es especialmente relevante para los SoCs Core Ultra que utilizan el NPU.

## ¿Qué es?

El NPU (Neural Processing Unit) es un procesador especializado en inteligencia artificial que se utiliza en los SoCs Core Ultra de Intel. El parche presentado permite limitar la frecuencia del NPU para mejorar la gestión de potencia y calor.

## ¿Cómo funciona?

El parche permite leer la frecuencia mínima y máxima del NPU, obtener la frecuencia óptima de funcionamiento y leer la frecuencia actual del NPU. Esto se puede hacer con el hardware Intel NPU 50XX+ y se aplica a los SoCs Intel Panther Lake y posteriores.

## ¿Por qué importa?

Limitar la frecuencia del NPU puede ayudar a mejorar la gestión de potencia y calor en los dispositivos que utilizan este procesador. Esto es especialmente importante para dispositivos que se utilizan en entornos de alta temperatura o que requieren una gran cantidad de energía.

## Consejo técnico

Si estás utilizando un dispositivo con un SoC Core Ultra de Intel, puedes probar limitar la frecuencia del NPU para mejorar la gestión de potencia y calor. Puedes hacer esto utilizando el comando `ivpu_freq` para leer la frecuencia actual del NPU y ajustarla según sea necesario.

```bash
ivpu_freq
```

---

**Fuente original:** [https://www.phoronix.com/news/Intel-NPU-Linux-Limit-Frequency](https://www.phoronix.com/news/Intel-NPU-Linux-Limit-Frequency)
