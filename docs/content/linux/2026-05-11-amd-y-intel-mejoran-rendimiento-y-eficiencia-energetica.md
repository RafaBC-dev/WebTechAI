# AMD y Intel mejoran rendimiento y eficiencia energética en Linux 7.2

**Fecha:** 2026-05-11
**Categoría:** linux
**Tags:** ia-local, linux, herramientas
**Título original:** AMD Ryzen AI & Intel NPU Drivers Adding New Power Features With Linux 7.2

---

## Introducción

Las empresas AMD e Intel están trabajando en mejorar la eficiencia energética de sus procesadores de NPU (Neural Processing Unit) en la próxima versión de Linux, Linux 7.2. Esto se logrará mediante la adición de nuevas características de gestión de poder en los controladores de Ryzen AI y NPU de Intel.

## ¿Qué es?

Los procesadores de NPU son componentes especializados para procesar tareas de inteligencia artificial y aprendizaje automático. Los controladores de Ryzen AI y NPU de Intel son software que permite a los sistemas operativos Linux interactuar con estos procesadores de NPU.

## ¿Cómo funciona?

Los nuevos controladores de Ryzen AI y NPU de Intel incluirán características de gestión de poder que permitirán a los sistemas reducir su consumo de energía. Por ejemplo, el controlador de Ryzen AI permitirá establecer modos de poder 'bajo' y 'medio', que reducirán el consumo de energía al minimizar la frecuencia de reloj y la gestión dinámica de poder. El controlador de NPU de Intel permitirá limitar artificialmente la frecuencia del procesador para reducir su consumo de energía.

## ¿Por qué importa?

Estas mejoras en la eficiencia energética son importantes porque permitirán a los sistemas reducir su consumo de energía y prolongar la vida útil de sus componentes. Además, esto también permitirá a los desarrolladores crear aplicaciones más eficientes y sostenibles.

## Consejo técnico

Si deseas aprovechar estas características en tu sistema Linux, asegúrate de actualizar a Linux 7.2 y verificar que tus controladores de Ryzen AI y NPU de Intel estén actualizados. Puedes verificar la versión de tus controladores mediante el comando `lsmod` y actualizarlos mediante el comando `modprobe`.

```bash
lsmod, modprobe
```

---

**Fuente original:** [https://www.phoronix.com/news/AMD-Intel-NPU-Drivers-Power-7.2](https://www.phoronix.com/news/AMD-Intel-NPU-Drivers-Power-7.2)
