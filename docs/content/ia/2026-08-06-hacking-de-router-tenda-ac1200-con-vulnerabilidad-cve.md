# Hacking de router Tenda AC1200 con vulnerabilidad CVE

**Fecha:** 2026-08-06
**Categoría:** ia
**Tags:** robotica, linux, codigo
**Título original:** Hacking a Tenda AC1200 Wi-Fi Router with a CVE Combo

---

## Introducción

Un investigador ha descubierto una vulnerabilidad en un router Tenda AC1200 que permite acceder a la consola del dispositivo. La vulnerabilidad se debe a una combinación de dos CVE (Common Vulnerabilities and Exposures) que permiten al atacante acceder a la consola del router y obtener acceso root.

## ¿Qué es?

Un CVE es una vulnerabilidad conocida en un software o hardware que puede ser explotada por un atacante. En este caso, la vulnerabilidad se debe a una combinación de dos CVE: CVE-2026-11405 y CVE-2025-52054. La primera vulnerabilidad permite acceder a la consola del router, mientras que la segunda permite obtener acceso root.

## ¿Cómo funciona?

El investigador descubrió que la vulnerabilidad se debía a una combinación de dos CVE. Primero, utilizó la herramienta binwalk para analizar el firmware del router y descubrir la vulnerabilidad CVE-2026-11405. Luego, utilizó la herramienta Ghidra para analizar el código del firmware y descubrir la vulnerabilidad CVE-2025-52054. Finalmente, utilizó la herramienta Telnet para acceder a la consola del router y obtener acceso root.

## ¿Por qué importa?

Esta vulnerabilidad es importante porque permite al atacante acceder a la consola del router y obtener acceso root, lo que puede ser utilizado para realizar ataques maliciosos en la red.

## Consejo técnico

Si tienes un router Tenda AC1200, es importante actualizar su firmware a la versión más reciente para evitar esta vulnerabilidad. Además, es recomendable utilizar una contraseña segura y única para la consola del router.

```bash
binwalk -e firmware_image.bin
```

---

**Fuente original:** [https://hackaday.com/2026/08/05/hacking-a-tenda-ac1200-wi-fi-router-with-a-cve-combo/](https://hackaday.com/2026/08/05/hacking-a-tenda-ac1200-wi-fi-router-with-a-cve-combo/)
