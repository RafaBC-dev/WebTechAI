# Pakete de AUR de Arch Linux comprometidos por atacante malicioso

**Fecha:** 2026-06-15
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Hundreds of AUR packages compromised

---

## Introducción

Un atacante ha comprometido cientos de paquetes abandonados en el Arch User Repository (AUR), lo que podría permitir la extracción de datos sensibles. Los usuarios de Arch Linux y distribuciones basadas en él deben verificar si han instalado actualizaciones comprometidas.

## ¿Qué es?

El AUR es un repositorio de paquetes de software para Arch Linux, donde los usuarios pueden compartir y colaborar en la creación de paquetes. Es un lugar donde los desarrolladores pueden compartir sus proyectos y permitir a otros usuarios instalarlos fácilmente.

## ¿Cómo funciona?

Los paquetes en el AUR se crean y mantienen por voluntarios, que los suben al repositorio y los mantienen actualizados. Sin embargo, en este caso, un atacante ha comprometido cientos de paquetes abandonados, agregando un paquete malicioso llamado 'atomic-lockfile' que puede exfiltrar datos sensibles.

## ¿Por qué importa?

La seguridad de los paquetes en el AUR es crucial para los usuarios de Arch Linux y distribuciones basadas en él, ya que pueden instalar actualizaciones comprometidas sin saberlo. Esto puede permitir a los atacantes acceder a datos sensibles y comprometer la seguridad de los sistemas.

## Consejo técnico

Los usuarios de Arch Linux y distribuciones basadas en él deben verificar si han instalado actualizaciones comprometidas utilizando el comando 'pacman -Q' para listar los paquetes instalados y buscar el paquete 'atomic-lockfile'. Si lo encuentran, deben eliminarlo inmediatamente.

```bash
pacman -Q
```

---

**Fuente original:** [https://lwn.net/Articles/1077718/](https://lwn.net/Articles/1077718/)
