# AMD P-State Driver: Nuevas características en Linux 7.1

**Fecha:** 2026-04-03
**Categoría:** linux
**Tags:** robotica, linux, ia-local
**Título original:** AMD P-State Driver Introducing New Features With Linux 7.1

---

## Introducción

El driver AMD P-State para Linux 7.1 ha recibido una actualización importante con nuevas características que mejoran la gestión de frecuencia y energía de los procesadores AMD Ryzen y EPYC. Estas mejoras son especialmente relevantes para usuarios de laptops Ryzen que buscan optimizar el rendimiento y la eficiencia energética.

## ¿Qué es?

El driver AMD P-State es un componente del kernel de Linux que se encarga de gestionar la frecuencia y el consumo de energía de los procesadores AMD Ryzen y EPYC. Su objetivo es optimizar el rendimiento y la eficiencia energética de los sistemas basados en estos procesadores.

## ¿Cómo funciona?

El driver AMD P-State utiliza la tecnología CPPC (Collaborative Processor Performance Control) para permitir a los usuarios asignar diferentes niveles de rendimiento a diferentes núcleos del procesador. También introduce la característica EPP (Energy Performance Preference) que permite cambiar el perfil de rendimiento y energía dependiendo de si el sistema está conectado a corriente alterna (AC) o directa (DC). Además, se ha agregado la característica Raw EPP que permite especificar un valor de rendimiento y energía personalizado entre 0 y 255.

## ¿Por qué importa?

Estas mejoras son importantes para los usuarios de laptops Ryzen que buscan optimizar el rendimiento y la eficiencia energética de sus sistemas. También son relevantes para los desarrolladores que buscan aprovechar al máximo las capacidades de los procesadores AMD Ryzen y EPYC.

## Consejo técnico

Si estás utilizando un laptop Ryzen, puedes probar la característica EPP para ver si puedes mejorar el rendimiento y la eficiencia energética de tu sistema. Puedes hacerlo mediante la herramienta sysfs, especificando el valor de EPP que deseas utilizar.

```bash
echo 128 > /sys/devices/system/cpu/cpu0/cpufreq/epp
```

---

**Fuente original:** [https://www.phoronix.com/news/AMD-P-State-Linux-7.1](https://www.phoronix.com/news/AMD-P-State-Linux-7.1)
