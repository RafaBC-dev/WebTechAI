# Proxmox VE ahora oficialmente soporta 64-bit Arm (Aarch64)

**Fecha:** 2026-08-07
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Proxmox VE now officially supports 64-bit Arm (Aarch64) targets

---

## Introducción

Proxmox ha anunciado la primera versión oficial de Proxmox Virtual Environment (VE) con soporte para 64-bit Arm (arm64/aarch64). Esto significa que los usuarios de hardware Arm pueden utilizar la popular solución de virtualización.

## ¿Qué es?

Proxmox VE es una solución de virtualización que permite crear y gestionar máquinas virtuales en un solo entorno. Ahora, está disponible para hardware Arm, lo que ofrece más opciones para los usuarios de este tipo de hardware.

## ¿Cómo funciona?

Proxmox VE para Arm se basa en Debian 13.5 "Trixie" con Linux 7.0 y utiliza la misma configuración, herramientas y documentación que la versión para x86-64, excepto por algunas diferencias específicas del hardware Arm.

## ¿Por qué importa?

El soporte para Arm es importante porque permite a los usuarios de hardware Arm aprovechar las características de la solución de virtualización de Proxmox, lo que puede mejorar la eficiencia y la escalabilidad de sus sistemas.

## Consejo técnico

Si deseas instalar Proxmox VE en un Raspberry Pi 4 o 5, asegúrate de utilizar la versión UEFI+ACPI y de desactivar NetworkManager y cloud-init para evitar problemas de configuración.

```bash
sudo apt-get install proxmox-ve
```

---

**Fuente original:** [https://www.cnx-software.com/2026/08/07/proxmox-ve-now-officially-supports-64-bit-arm-aarch64-targets/](https://www.cnx-software.com/2026/08/07/proxmox-ve-now-officially-supports-64-bit-arm-aarch64-targets/)
