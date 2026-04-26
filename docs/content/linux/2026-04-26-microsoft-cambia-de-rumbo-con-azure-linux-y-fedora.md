# Microsoft cambia de rumbo con Azure Linux y Fedora

**Fecha:** 2026-04-26
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Microsoft Reportedly Looking At Rebasing Azure Linux On Fedora

---

## Introducción

Microsoft está considerando cambiar la base de su sistema operativo Azure Linux a Fedora, lo que podría mejorar su rendimiento y flexibilidad. Esta decisión podría tener un impacto significativo en la comunidad de Linux y en la forma en que se utilizan los sistemas operativos en la nube.

## ¿Qué es?

Azure Linux es un sistema operativo basado en Linux que utiliza Microsoft para sus servicios en la nube, incluyendo Azure y WSL. Es un sistema operativo RPM que se utiliza para satisfacer las necesidades de Linux de Microsoft. Fedora es una distribución de Linux popular y estable que se utiliza en entornos de desarrollo y producción.

## ¿Cómo funciona?

La propuesta de cambiar la base de Azure Linux a Fedora implica utilizar la arquitectura de Fedora como base para crear un nuevo sistema operativo. Esto permitiría a Microsoft aprovechar las características y mejoras de Fedora, como la compatibilidad con x86_64-v3, para mejorar el rendimiento y la flexibilidad de Azure Linux. La implementación de x86-64-v3 en Fedora permitiría a Microsoft utilizar recursos de cómputo más eficientes y mejorar la compatibilidad con aplicaciones y herramientas de terceros.

## ¿Por qué importa?

Esta decisión importa porque podría mejorar la eficiencia y la flexibilidad de los sistemas operativos en la nube de Microsoft, lo que podría tener un impacto positivo en la forma en que se utilizan los servicios en la nube y en la forma en que se desarrollan aplicaciones. También podría tener un impacto en la comunidad de Linux, ya que podría influir en la forma en que se utilizan y se desarrollan las distribuciones de Linux en el futuro.

## Consejo técnico

Si estás utilizando Azure Linux o Fedora, considera verificar la compatibilidad de tus aplicaciones y herramientas con la arquitectura de x86-64-v3. Puedes verificar la compatibilidad utilizando herramientas como `rpm` y `yum` para verificar la versión de tu sistema operativo y las dependencias de tus aplicaciones.

```bash
rpm -qa | grep x86_64-v3
```

---

**Fuente original:** [https://www.phoronix.com/news/MS-Azure-Linux-Fedora-Based](https://www.phoronix.com/news/MS-Azure-Linux-Fedora-Based)
