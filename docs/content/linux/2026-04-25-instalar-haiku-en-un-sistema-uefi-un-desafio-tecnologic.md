# Instalar Haiku en un sistema UEFI: un desafío tecnológico

**Fecha:** 2026-04-25
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** How to Install Haiku on a UEFI-Only Modern System

---

## Introducción

Haiku, un sistema operativo que busca ser un reemplazo para macOS y Windows, ha sido objeto de atención reciente debido a su proximidad a ser un sistema operativo diario. Sin embargo, todavía existen varios obstáculos antes de que pueda ser utilizado como tal. Un video reciente muestra cómo instalar Haiku en un MiniPC con procesador Ryzen 3 que solo admite UEFI boot.

## ¿Qué es?

Haiku es un sistema operativo que busca ser un reemplazo para macOS y Windows. Es un proyecto que busca ser un sistema operativo diario, es decir, que pueda ser utilizado para realizar tareas cotidianas como trabajar, jugar y ver películas. Haiku se basa en el núcleo de BeOS y busca ser un sistema operativo más rápido y eficiente que los sistemas operativos actuales.

## ¿Cómo funciona?

Para instalar Haiku en un sistema UEFI, es necesario crear una partición de UEFI boot y otra para la partición del sistema operativo. Luego, se debe copiar el bootloader en la partición de UEFI boot. Una vez que se haya instalado Haiku, se puede instalar junto a otros sistemas operativos como Windows y Linux. Sin embargo, todavía existen algunos obstáculos, como la falta de soporte para la iGPU Vega.

## ¿Por qué importa?

Haiku es importante porque busca ser un sistema operativo diario que pueda ser utilizado para realizar tareas cotidianas. También es importante porque busca ser un sistema operativo más rápido y eficiente que los sistemas operativos actuales. Además, Haiku es fácil de portar software de Linux, lo que significa que puede ser utilizado para ejecutar aplicaciones Linux.

## Consejo técnico

Si deseas instalar Haiku en un sistema UEFI, asegúrate de crear una partición de UEFI boot y otra para la partición del sistema operativo. Luego, copia el bootloader en la partición de UEFI boot. Recuerda que la falta de soporte para la iGPU Vega puede ser un obstáculo.

```bash
fdisk -l /dev/sda (para verificar la partición del disco duro)
```

---

**Fuente original:** [https://hackaday.com/2026/04/24/how-to-install-haiku-on-a-uefi-only-modern-system/](https://hackaday.com/2026/04/24/how-to-install-haiku-on-a-uefi-only-modern-system/)
