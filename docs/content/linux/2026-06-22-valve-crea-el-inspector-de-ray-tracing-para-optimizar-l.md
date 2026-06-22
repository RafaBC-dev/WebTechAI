# Valve crea el Inspector de Ray-Tracing para optimizar los controladores de GPU de Linux

**Fecha:** 2026-06-22
**Categoría:** linux
**Tags:** linux, ray-tracing, gpu
**Título original:** Valve Creates The Ray-Tracing Inspector "RTI" To Help Further Optimize Linux GPU Drivers

---

## Introducción

Valve ha creado un nuevo herramienta llamada Ray-Tracing Inspector (RTI) para ayudar a optimizar los controladores de GPU de Linux. Esta herramienta es importante porque permitirá a los desarrolladores analizar y mejorar el rendimiento de la ray-tracing en los juegos de Steam Play para Linux.

## ¿Qué es?

El Ray-Tracing Inspector (RTI) es una herramienta de interfaz gráfica de usuario (GUI) diseñada para ayudar a los desarrolladores a analizar y optimizar el rendimiento de la ray-tracing en los juegos de Steam Play para Linux. Esta herramienta se basa en algunas de las características de depuración existentes del controlador de GPU Radeon RADV y utiliza la biblioteca ImGUI para crear la interfaz gráfica.

## ¿Cómo funciona?

El RTI se puede utilizar para analizar y optimizar el rendimiento de la ray-tracing en los juegos de Steam Play para Linux. Para utilizar la herramienta, los desarrolladores deben configurar el controlador de GPU Radeon RADV para dumpar los datos de la estructura de aceleración de rayos y la historia de rayos, y luego cargar estos datos en la herramienta RTI. La herramienta RTI también permite a los desarrolladores visualizar y analizar los datos de la estructura de aceleración de rayos y la historia de rayos.

## ¿Por qué importa?

El RTI importa porque permitirá a los desarrolladores mejorar el rendimiento de la ray-tracing en los juegos de Steam Play para Linux. Esto es importante porque la ray-tracing es una tecnología que requiere una gran cantidad de recursos de hardware y puede ser un obstáculo para los jugadores con hardware más modesto. Con el RTI, los desarrolladores pueden optimizar el rendimiento de la ray-tracing y hacer que los juegos sean más accesibles para un mayor número de jugadores.

## Consejo técnico

Para utilizar el RTI, los desarrolladores deben configurar el controlador de GPU Radeon RADV para dumpar los datos de la estructura de aceleración de rayos y la historia de rayos, y luego cargar estos datos en la herramienta RTI. Pueden hacer esto estableciendo la variable de entorno RADV_DEBUG=rti y luego ejecutando la herramienta RTI.

```bash
-D tools=rti Meson build option
```

---

**Fuente original:** [https://www.phoronix.com/news/Mesa-Ray-Tracing-Inspector-RTI](https://www.phoronix.com/news/Mesa-Ray-Tracing-Inspector-RTI)
