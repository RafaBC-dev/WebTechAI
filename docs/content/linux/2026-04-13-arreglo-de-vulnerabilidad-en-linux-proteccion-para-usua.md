# Arreglo de vulnerabilidad en Linux: protección para usuarios no privilegiados

**Fecha:** 2026-04-13
**Categoría:** linux
**Tags:** linux, seguridad, vulnerabilidad
**Título original:** Linux Out-Of-Bounds Access Fixed For Unprivileged Users With Specially Crafted Certs

---

## Introducción

La comunidad de desarrolladores de Linux ha encontrado y arreglado una vulnerabilidad crítica en el kernel que permitía a usuarios no privilegiados acceder a memoria no válida. La vulnerabilidad se podía explotar mediante certificados X.509 especialmente diseñados.

## ¿Qué es?

La vulnerabilidad se debía a un acceso a memoria no válida en el código de certificados X.509. Un usuario no privilegiado podía enviar un certificado especialmente diseñado a través de la API de keyrings del kernel, lo que provocaba el acceso a memoria no válida.

## ¿Cómo funciona?

El acceso a memoria no válida se producía al leer el primer byte de una extensión de certificado antes de comprobar su longitud. El desarrollador Lukas Wunner ha agregado comprobaciones condicionales para solucionar el problema.

## ¿Por qué importa?

Esta vulnerabilidad era particularmente peligrosa porque podía ser explotada por usuarios no privilegiados, lo que podría provocar una escalada de privilegios, pérdida de información, ejecución de código arbitrario o incluso un pánico del kernel.

## Consejo técnico

Si estás utilizando un sistema Linux, asegúrate de actualizar tu kernel a la versión más reciente para evitar esta vulnerabilidad. Puedes verificar la versión de tu kernel con el comando `uname -r` y actualizarlo con `sudo apt-get update && sudo apt-get upgrade` (o el equivalente en tu distribución Linux).

```bash
uname -r
```

---

**Fuente original:** [https://www.phoronix.com/news/Linux-OOB-Special-Certificate](https://www.phoronix.com/news/Linux-OOB-Special-Certificate)
