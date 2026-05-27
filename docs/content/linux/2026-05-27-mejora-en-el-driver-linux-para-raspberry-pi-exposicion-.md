# Mejora en el driver Linux para Raspberry Pi: exposición de voltajes

**Fecha:** 2026-05-27
**Categoría:** linux
**Tags:** linux, raspberry-pi, embebidos
**Título original:** Linux Driver To Expose Voltage Inputs For Raspberry Pi SBCs

---

## Introducción

La comunidad de Raspberry Pi ha recibido una actualización importante en el driver de hardware de Linux, que permite la exposición de mediciones de voltaje en estas computadoras de placa única ARM. Esto significa que los usuarios podrán acceder a información detallada sobre la salud y el rendimiento de sus dispositivos.

## ¿Qué es?

El driver 'RASPBERRYPI-HWMON' es un componente del kernel de Linux que se encarga de monitorear y controlar la temperatura, la voltaje y otros parámetros de los dispositivos de Raspberry Pi. La actualización permite que las mediciones de voltaje sean accesibles desde el espacio de usuario, lo que facilita la depuración y el monitoreo de los dispositivos.

## ¿Cómo funciona?

La actualización del driver utiliza la información proporcionada por el firmware de Raspberry Pi, que incluye mediciones de voltaje para el núcleo y varias tensiones de memoria SDRAM. Estas mediciones se propagan al espacio de usuario a través de las interfaces de sysfs convencionales, lo que permite a los usuarios acceder a la información de voltaje utilizando comandos como 'cat /sys/class/hwmon/hwmon0/in0_input'.

## ¿Por qué importa?

Esta actualización es importante porque permite a los usuarios de Raspberry Pi tener una visión más detallada de la salud y el rendimiento de sus dispositivos. Esto puede ayudar a identificar problemas de configuración o hardware, y a tomar medidas correctivas para mejorar el rendimiento y la estabilidad de los dispositivos.

## Consejo técnico

Si deseas aprovechar esta actualización, asegúrate de revisar la documentación de sysfs y aprender a leer las mediciones de voltaje utilizando comandos como 'cat /sys/class/hwmon/hwmon0/in0_input'. Esto te permitirá monitorear la salud de tu dispositivo y tomar medidas correctivas si es necesario.

```bash
cat /sys/class/hwmon/hwmon0/in0_input
```

---

**Fuente original:** [https://www.phoronix.com/news/Raspberry-Pi-Voltage-Inputs](https://www.phoronix.com/news/Raspberry-Pi-Voltage-Inputs)
