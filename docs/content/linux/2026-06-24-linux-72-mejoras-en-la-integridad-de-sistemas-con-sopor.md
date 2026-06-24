# Linux 7.2: Mejoras en la integridad de sistemas con soporte post-cuántico

**Fecha:** 2026-06-24
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Linux 7.2 Ready With IMA and EVM Post-Quantum ML-DSA Signature Support

---

## Introducción

La versión 7.2 del kernel Linux ha sido lanzada con importantes mejoras en la integridad de sistemas, incluyendo el soporte post-cuántico para firmas de ML-DSA. Esto significa que los sistemas Linux pueden ahora validar firmas de manera más segura y futura.

## ¿Qué es?

La Integridad de Medición de Linux (IMA) y el Módulo de Verificación Extendida (EVM) son subsistemas que verifican la integridad de archivos y sistemas. La firma de ML-DSA es un tipo de firma digital que utiliza algoritmos post-cuánticos para garantizar la autenticidad de los datos.

## ¿Cómo funciona?

La IMA y el EVM ahora pueden validar firmas de ML-DSA, lo que proporciona una mayor seguridad y futuribilidad. Además, se ha introducido la capacidad de eliminar registros de la lista de medición almacenados en memoria del kernel, lo que reduce el consumo de recursos en sistemas con limitaciones.

## ¿Por qué importa?

Estas mejoras son importantes porque protegen a los sistemas Linux contra ataques cuánticos futuros. También mejoran la seguridad y eficiencia de la verificación de firmas en sistemas con limitaciones de recursos.

## Consejo técnico

Si estás utilizando Linux 7.2, puedes utilizar el comando `ima_stat` para verificar la integridad de tus sistemas y `evm_stat` para verificar la integridad de tus archivos.

```bash
ima_stat, evm_stat
```

---

**Fuente original:** [https://www.phoronix.com/news/Linux-7.2-Integrity](https://www.phoronix.com/news/Linux-7.2-Integrity)
