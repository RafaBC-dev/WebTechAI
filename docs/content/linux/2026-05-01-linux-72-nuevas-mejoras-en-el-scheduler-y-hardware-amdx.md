# Linux 7.2: Nuevas mejoras en el scheduler y hardware AMDXDNA

**Fecha:** 2026-05-01
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Linux 7.2 To Set Default DRM Scheduler Priority To "Fair", New AIE4 Hardware In AMDXDNA

---

## Introducción

La versión 7.2 del kernel de Linux está en camino y trae consigo varias mejoras importantes. Una de ellas es el cambio en la política de scheduler por defecto, que pasará de FIFO a 'fair'. Esto debería mejorar la experiencia de usuario, especialmente en cargas de trabajo interactivas. Además, se han agregado nuevas características en el driver de AMDXDNA, que incluyen soporte para nuevos dispositivos AIE4.

## ¿Qué es?

El scheduler es un componente clave del kernel de Linux que se encarga de asignar recursos a los procesos en ejecución. La política de scheduler determina cómo se asignan estos recursos. La política 'fair' es una mejora sobre la política FIFO, ya que asigna recursos de manera más justa y eficiente. El driver de AMDXDNA es responsable de controlar la acceleración de procesamiento de AMD Ryzen AI NPUs.

## ¿Cómo funciona?

La política de scheduler 'fair' funciona asignando recursos de manera que cada proceso reciba una cantidad igual de tiempo de procesamiento. Esto se logra mediante un algoritmo que ajusta la asignación de recursos en función de la carga de trabajo actual. En cuanto al driver de AMDXDNA, se ha agregado soporte para nuevos dispositivos AIE4, que incluyen mejoras en la aceleración de procesamiento.

## ¿Por qué importa?

Estas mejoras son importantes porque mejorarán la experiencia de usuario en cargas de trabajo interactivas y proporcionarán una mayor eficiencia en la asignación de recursos. Además, el soporte para nuevos dispositivos AIE4 permitirá aprovechar al máximo la potencia de los procesadores AMD Ryzen AI NPUs.

## Consejo técnico

Si estás utilizando un sistema con kernel de Linux, puedes probar la política de scheduler 'fair' mediante la ejecución del comando `echo fair > /sys/block/sda/queue/scheduler` en la terminal. Esto cambiará la política de scheduler por defecto a 'fair' para el dispositivo de almacenamiento `/dev/sda`.

```bash
echo fair > /sys/block/sda/queue/scheduler
```

---

**Fuente original:** [https://www.phoronix.com/news/Linux-7.2-Initial-DRM-Misc-Next](https://www.phoronix.com/news/Linux-7.2-Initial-DRM-Misc-Next)
