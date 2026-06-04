# Microsoft lanza Coreutils para Windows, herramientas Unix en el sistema operativo

**Fecha:** 2026-06-04
**Categoría:** linux
**Tags:** linux, herramientas, codigo
**Título original:** Microsoft introduces Coreutils for Windows, bringing familiar Unix-style command-line tools to Windows without requiring WSL

---

## Introducción

Microsoft ha lanzado Coreutils para Windows, un conjunto de herramientas de línea de comandos Unix que se ejecutan nativamente en Windows sin necesidad de WSL. Esto significa que desarrolladores pueden utilizar comandos y flujos de trabajo comunes en Linux, macOS, WSL, contenedores y entornos en la nube en Windows.

## ¿Qué es?

Coreutils para Windows es un conjunto de herramientas de línea de comandos Unix mantenidas por Microsoft que se ejecutan nativamente en Windows. Está basado en el proyecto uutils, una implementación en Rust de GNU Coreutils. Incluye herramientas como cp, ls, mv, rm y sleep.

## ¿Cómo funciona?

La herramienta se distribuye como un solo archivo binario multi-calle y se puede instalar mediante WinGet. Requiere PowerShell 7.4 o posterior. La implementación se basa en la versión uutils/coreutils del proyecto uutils.

## ¿Por qué importa?

Esta herramienta reduce la fricción para desarrolladores que utilizan herramientas de línea de comandos Unix en diferentes plataformas. Ahora pueden utilizar comandos y flujos de trabajo comunes en Windows sin necesidad de WSL o capas de compatibilidad adicionales.

## Consejo técnico

Si deseas utilizar Coreutils para Windows, asegúrate de instalar PowerShell 7.4 o posterior y utiliza WinGet para instalar la herramienta. Ten en cuenta que algunos comandos pueden conflictuar con los comandos integrados o alias de PowerShell.

```bash
winget install uutils/coreutils
```

---

**Fuente original:** [https://blog.adafruit.com/2026/06/03/microsoft-introduces-coreutils-for-windows-bringing-familiar-unix-style-command-line-tools-to-windows-without-requiring-wsl/](https://blog.adafruit.com/2026/06/03/microsoft-introduces-coreutils-for-windows-bringing-familiar-unix-style-command-line-tools-to-windows-without-requiring-wsl/)
