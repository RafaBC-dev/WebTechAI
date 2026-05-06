# Interfaz de hardware para Gazebo Harmonic sin necesidad de DDS

**Fecha:** 2026-05-06
**Categoría:** robotica
**Tags:** robotica, linux, codigo
**Título original:** [Release] emcon_gz_hardware_interface: A DDS-bypassing hardware interface for Gazebo Harmonic

---

## Introducción

Un desarrollador ha creado una interfaz de hardware para Gazebo Harmonic que permite evitar el uso de DDS, lo que puede ser un problema para la escalabilidad y la seguridad en simulaciones de robots y estimadores de estado aislados.

## ¿Qué es?

La interfaz de hardware emcon_gz_hardware_interface es un sistema de interfaz de hardware que actúa como un 'diodo de datos' y se conecta directamente a los temas nativos de transporte de Gazebo, evitando el uso de DDS y garantizando la seguridad y la escalabilidad.

## ¿Cómo funciona?

La interfaz de hardware emcon_gz_hardware_interface utiliza el protocolo de transporte nativo de Gazebo y se conecta directamente a los temas de transporte, evitando el uso de DDS y garantizando la seguridad y la escalabilidad. También utiliza un buffer de tiempo real para asegurar que el bucle de control nunca se bloquee.

## ¿Por qué importa?

Esta interfaz de hardware es importante porque permite a los desarrolladores de robots y simulaciones evitar el uso de DDS, lo que puede ser un problema para la escalabilidad y la seguridad. También permite la creación de simulaciones de robots y estimadores de estado aislados de manera más segura y escalable.

## Consejo técnico

Si estás trabajando con simulaciones de robots y estimadores de estado aislados, considera utilizar la interfaz de hardware emcon_gz_hardware_interface para evitar el uso de DDS y garantizar la seguridad y la escalabilidad.

```bash
Para instalar la interfaz de hardware emcon_gz_hardware_interface, puedes utilizar el comando `git clone https://github.com/yenode/emcon_gz_hardware_interface.git` y luego seguir las instrucciones de instalación en el repositorio.
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/release-emcon-gz-hardware-interface-a-dds-bypassing-hardware-interface-for-gazebo-harmonic/54549](https://discourse.openrobotics.org/t/release-emcon-gz-hardware-interface-a-dds-bypassing-hardware-interface-for-gazebo-harmonic/54549)
