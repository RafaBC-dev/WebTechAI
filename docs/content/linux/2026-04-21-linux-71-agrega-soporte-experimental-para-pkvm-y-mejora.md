# Linux 7.1 agrega soporte experimental para pKVM y mejoras en KVM

**Fecha:** 2026-04-21
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Linux 7.1 KVM Adds "Very Experimental" Support For pKVM Protected Guests

---

## Introducción

La versión 7.1 de Linux ha sido actualizada con cambios importantes en el Kernel-based Virtual Machine (KVM), una tecnología clave para la virtualización en Linux. Entre las mejoras, se encuentra el soporte experimental para pKVM, que permite una mayor aislación de los invitados en el anfitrión.

## ¿Qué es?

KVM es un proyecto de software libre que permite la creación de máquinas virtuales en Linux. Permite ejecutar múltiples sistemas operativos en un solo equipo, cada uno en su propia máquina virtual. Esto permite una mayor flexibilidad y seguridad en la gestión de sistemas y aplicaciones.

## ¿Cómo funciona?

El soporte para pKVM en KVM permite que las páginas de memoria sean desmappeadas del anfitrión cuando se cargan en el invitado. Esto se logra mediante llamadas de hipervisor pKVM. El anfitrión no tiene acceso a la memoria del invitado, lo que proporciona una mayor aislación y seguridad.

## ¿Por qué importa?

El soporte para pKVM es importante porque permite una mayor seguridad y aislación de los invitados en el anfitrión. Esto es especialmente relevante en entornos de servidor, donde la seguridad y la confiabilidad son fundamentales.

## Consejo técnico

Si deseas probar el soporte para pKVM en Linux 7.1, asegúrate de compilar el kernel con la opción CONFIG_ARM_PVKM_GUEST habilitada y de lanzar la máquina virtual con la opción kvm-arm.mode=protected.

```bash
kvm-arm.mode=protected
```

---

**Fuente original:** [https://www.phoronix.com/news/Linux-7.1-KVM](https://www.phoronix.com/news/Linux-7.1-KVM)
