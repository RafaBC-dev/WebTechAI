# AMD limpia BUG()s en su driver de gráficos Linux

**Fecha:** 2026-07-08
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** AMD Linux Graphics Driver Working To Clear Out All Of Its BUG()s

---

## Introducción

La empresa AMD está trabajando en eliminar el uso de la macro BUG() en su driver de gráficos Linux, lo que podría evitar problemas de seguridad y mejorar la estabilidad del sistema.

## ¿Qué es?

La macro BUG() es un mecanismo de crash que se utiliza en el kernel de Linux para detener la ejecución del sistema en caso de condiciones irreversibles. Sin embargo, su uso puede llevar a problemas de seguridad y estabilidad.

## ¿Cómo funciona?

El mantenedor del driver AMDGPU, Alex Deucher, ha enviado un conjunto de 30 parches para cambiar el código y eliminar el uso de BUG() en situaciones en las que no es necesario. En algunos casos, se reducirá el nivel de error a advertencia o se emitirá un error sin detener la ejecución del sistema.

## ¿Por qué importa?

La eliminación de BUG() en el driver de gráficos AMD puede mejorar la estabilidad del sistema y evitar problemas de seguridad, como ataques de denegación de servicio. Además, permitirá que el sistema continúe funcionando en caso de errores específicos del driver.

## Consejo técnico

Si estás utilizando el driver de gráficos AMD en tu sistema Linux, es recomendable revisar los parches enviados por Alex Deucher y aplicarlos para aprovechar las mejoras en estabilidad y seguridad.

```bash
No aplica
```

---

**Fuente original:** [https://www.phoronix.com/news/AMDGPU-Clearing-Out-BUGs](https://www.phoronix.com/news/AMDGPU-Clearing-Out-BUGs)
