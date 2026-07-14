# Mejoras en el manejo de dispositivos de intercambio en Linux

**Fecha:** 2026-07-14
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** New Linux Patches Aim To Better Handle Multiple Swap Devices

---

## Introducción

Un conjunto de parches recientes para el núcleo de Linux busca mejorar la gestión de dispositivos de intercambio múltiples en sistemas Linux, especialmente en entornos de servidor complejos.

## ¿Qué es?

Los dispositivos de intercambio son áreas de almacenamiento en memoria RAM que permiten al sistema Linux utilizar espacio en disco cuando la memoria RAM está llena. Los parches recientes buscan mejorar la distribución de I/O a múltiples dispositivos de intercambio, lo que es especialmente útil en entornos de servidor que utilizan tecnologías de intercambio en capas o de intercambio jerárquico.

## ¿Cómo funciona?

El nuevo diseño utiliza una cola de prioridad por lector por CPU para distribuir I/O de manera equitativa entre los dispositivos de intercambio. Además, se ha eliminado la caché de cluster mutable y la bloqueo global, lo que permite una asignación y rotación más libres. La gestión de dispositivos de intercambio ahora utiliza un semáforo de lectura/escritura por CPU para mejorar la escalabilidad y la futura resistencia a cambios.

## ¿Por qué importa?

Estas mejoras son importantes para sistemas Linux que utilizan múltiples dispositivos de intercambio, ya que pueden mejorar el rendimiento y la eficiencia en la gestión de memoria. Esto puede ser especialmente útil en entornos de servidor que requieren una gestión de memoria dinámica y flexible.

## Consejo técnico

Si estás utilizando múltiples dispositivos de intercambio en tu sistema Linux, puedes probar utilizar la cola de prioridad por lector por CPU para mejorar la distribución de I/O y mejorar el rendimiento de tu sistema.

```bash
echo 'vm.swappiness = 60' > /etc/sysctl.conf
```

---

**Fuente original:** [https://www.phoronix.com/news/Linux-Improve-Multi-Swap-Device](https://www.phoronix.com/news/Linux-Improve-Multi-Swap-Device)
