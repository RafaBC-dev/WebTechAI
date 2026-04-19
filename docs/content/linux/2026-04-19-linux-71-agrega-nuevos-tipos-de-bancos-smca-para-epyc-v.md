# Linux 7.1 agrega nuevos tipos de bancos SMCA para EPYC Venice

**Fecha:** 2026-04-19
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Linux 7.1 Adds New AMD SMCA Bank Types, Presumably For Upcoming EPYC Venice

---

## Introducción

La versión 7.1 de Linux ha sido actualizada con soporte para nuevos tipos de bancos SMCA, lo que sugiere que están destinados a la próxima generación de procesadores EPYC Venice de AMD. Esto es importante porque permitirá a los desarrolladores de software aprovechar al máximo las capacidades de estos nuevos procesadores.

## ¿Qué es?

Los bancos SMCA (Scalable Machine Check Architecture) son una arquitectura para representar diferentes unidades de hardware en los procesadores modernos de AMD. Se utilizan para identificar y manejar errores en el sistema. Los nuevos tipos de bancos SMCA incluyen Data Acceleration Back-end, Data Acceleration Front-end, eDDR5 CMN, AMD Root of Trust Microprocessor, AMD Secure Processor, AMD Secure Processor V2, Microprocessor Manageability Core, MP for RAS, SMCA_MPRAS y Die to Die Interconnect.

## ¿Cómo funciona?

Los patches para Linux 7.1 agregan soporte para estos nuevos tipos de bancos SMCA en el driver de errores de AMD. El driver utiliza la arquitectura SMCA para representar diferentes unidades de hardware en el procesador y manejar errores en el sistema. Los nuevos tipos de bancos SMCA se utilizan para representar unidades de hardware específicas, como la aceleración de datos y la seguridad.

## ¿Por qué importa?

Esto es importante porque permitirá a los desarrolladores de software aprovechar al máximo las capacidades de los nuevos procesadores EPYC Venice. Los nuevos tipos de bancos SMCA permitirán a los desarrolladores crear software más eficiente y seguro para estos procesadores.

## Consejo técnico

Si estás desarrollando software para procesadores EPYC Venice, asegúrate de verificar la documentación de Linux 7.1 para obtener más información sobre cómo utilizar los nuevos tipos de bancos SMCA.

```bash
Verifica la documentación de Linux 7.1 para obtener más información sobre cómo utilizar los nuevos tipos de bancos SMCA.
```

---

**Fuente original:** [https://www.phoronix.com/news/AMD-2026-New-SMCA-Bank-Types](https://www.phoronix.com/news/AMD-2026-New-SMCA-Bank-Types)
