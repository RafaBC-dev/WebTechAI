# Nueva función de THP para combinar el mejor de HugeTLB y THP en Linux

**Fecha:** 2026-06-28
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Reserved THP Feature Proposed For Linux To Combine The Best Of HugeTLB & THP

---

## Introducción

El desarrollador de Linux Qi Zheng ha presentado una nueva función llamada Reserved THP, que combina las ventajas de HugeTLB y THP para mejorar la gestión de memoria en Linux. Esta función podría resolver problemas de reserva de memoria en escenarios de actualización caliente.

## ¿Qué es?

Reserved THP es una nueva función de Linux que permite reservar páginas de memoria gigantes (THP) para uso específico, combinando las ventajas de HugeTLB y THP. Esto permite reservar memoria sin garantizar su asignación, pero con la capacidad de manejar intercambio de memoria (swap).

## ¿Cómo funciona?

Reserved THP funciona reservando páginas de memoria gigantes (THP) para uso específico, lo que permite a los desarrolladores reservar memoria sin garantizar su asignación. Esto se logra mediante la función madvise(), que permite a los desarrolladores indicar a Linux que reserve memoria específica para uso futuro. La función también permite el intercambio de memoria (swap), lo que permite a Linux liberar memoria cuando no se utiliza.

## ¿Por qué importa?

Esta función es importante porque resuelve problemas de reserva de memoria en escenarios de actualización caliente, donde se requiere memoria adicional para realizar la actualización. También permite a los desarrolladores reservar memoria sin garantizar su asignación, lo que puede ser útil en escenarios donde la memoria es limitada.

## Consejo técnico

Si estás trabajando con escenarios de actualización caliente y necesitas reservar memoria para uso futuro, considera utilizar la función Reserved THP en Linux. Puedes empezar configurando la función madvise() para reservar memoria específica y luego utilizar la función Reserved THP para asignar la memoria reservada.

```bash
madvise()
```

---

**Fuente original:** [https://www.phoronix.com/news/Reserved-THP-Linux](https://www.phoronix.com/news/Reserved-THP-Linux)
