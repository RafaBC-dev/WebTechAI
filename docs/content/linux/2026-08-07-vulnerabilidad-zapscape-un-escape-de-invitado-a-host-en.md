# Vulnerabilidad Zapscape: un escape de invitado a host en Linux KVM

**Fecha:** 2026-08-07
**Categoría:** linux
**Tags:** linux, kvm, seguridad
**Título original:** Zapscape Is The Latest Linux Vulnerability For KVM Guest-To-Host Escape, LPE

---

## Introducción

La comunidad de Linux ha descubierto una nueva vulnerabilidad que permite a un atacante escapar de un invitado a host en KVM, lo que podría tener graves consecuencias en la seguridad de los sistemas virtuales.

## ¿Qué es?

Zapscape es una vulnerabilidad de escape de invitado a host en Linux KVM que permite a un atacante escapar de un sistema virtual a un sistema físico y ejecutar comandos con privilegios de superusuario. Esto se debe a una vulnerabilidad de uso después de liberación en el código de emulación de la MMU de KVM.

## ¿Cómo funciona?

La vulnerabilidad se produce cuando un atacante explota la vulnerabilidad de uso después de liberación en el código de emulación de la MMU de KVM, lo que permite acceder a la memoria del sistema físico y ejecutar comandos con privilegios de superusuario. Esto se puede hacer utilizando la herramienta /dev/kvm, que es world-writable en algunas distribuciones de Linux como RHEL.

## ¿Por qué importa?

Esta vulnerabilidad es importante porque permite a un atacante escapar de un sistema virtual a un sistema físico y ejecutar comandos con privilegios de superusuario, lo que podría tener graves consecuencias en la seguridad de los sistemas virtuales. Además, esta vulnerabilidad se ha estado explotando desde 2020, por lo que es importante que los administradores de sistemas tomen medidas para corregirla lo antes posible.

## Consejo técnico

Los administradores de sistemas deben verificar si su versión de Linux está afectada y aplicar la actualización de seguridad disponible para corregir la vulnerabilidad. Además, es recomendable cambiar la configuración de /dev/kvm para que no sea world-writable.

```bash
sudo apt-get update && sudo apt-get install linux-kvm | sudo chmod 0600 /dev/kvm
```

---

**Fuente original:** [https://www.phoronix.com/news/Linux-Zapscape-Vulnerability](https://www.phoronix.com/news/Linux-Zapscape-Vulnerability)
