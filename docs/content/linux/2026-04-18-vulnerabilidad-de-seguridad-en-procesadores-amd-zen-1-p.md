# Vulnerabilidad de seguridad en procesadores AMD Zen 1: patch en Linux

**Fecha:** 2026-04-18
**Categoría:** linux
**Tags:** linux, seguridad, cpu
**Título original:** AMD FP-DSS Security Bug For Zen 1 CPUs Made Public, Linux Kernel Patched

---

## Introducción

La compañía AMD ha hecho público un problema de seguridad en sus procesadores Zen 1, que pueden permitir a un atacante privilegiado acceder a datos sensibles. La vulnerabilidad afecta solo a los procesadores Zen 1 y Zen 1+, y no a las versiones más recientes.

## ¿Qué es?

La vulnerabilidad de seguridad se conoce como Floating Point Divider State Sampling (FP-DSS) y afecta a los procesadores Zen 1 y Zen 1+. Se trata de una vulnerabilidad de ejecución transitoria que puede permitir a un atacante privilegiado acceder a datos sensibles a través de las unidades de división de punto flotante.

## ¿Cómo funciona?

La vulnerabilidad se produce cuando el procesador intenta dividir un número en punto flotante, lo que puede permitir a un atacante privilegiado acceder a datos sensibles. La Linux kernel ha implementado un parche para mitigar esta vulnerabilidad, que consiste en establecer un bit en la MSR C001_1028.

## ¿Por qué importa?

La vulnerabilidad de seguridad en los procesadores Zen 1 puede permitir a un atacante privilegiado acceder a datos sensibles, lo que puede tener graves consecuencias. Sin embargo, AMD cree que el riesgo de pérdida de datos es bajo, ya que las operaciones de punto flotante en código de privilegio no son comunes.

## Consejo técnico

Para mitigar esta vulnerabilidad, es importante actualizar el kernel de Linux a la versión más reciente, que ya incluye el parche para la vulnerabilidad de FP-DSS. También es importante establecer el bit en la MSR C001_1028 para asegurarse de que la vulnerabilidad esté mitigada.

```bash
echo 1 > /dev/cpu/0/msr/c001_1028
```

---

**Fuente original:** [https://www.phoronix.com/news/AMD-FP-DSS-Zen-1-Bug](https://www.phoronix.com/news/AMD-FP-DSS-Zen-1-Bug)
