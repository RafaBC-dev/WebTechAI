# Protoros2: un middleware para usar protobuf en ROS 2 sin compromisos

**Fecha:** 2026-08-04
**Categoría:** robotica
**Tags:** robotica, linux, codigo
**Título original:** Announcing protoros2: use protobuf in ros2 without compromise

---

## Introducción

La comunidad de ROS 2 ha demandado durante años la integración sin problemas de la serialización de protobuf. Ahora, protoros2 ofrece una solución que no compromete la velocidad ni la producción.

## ¿Qué es?

protoros2 es un middleware que actúa como un motor de orchestración tri-estado, uniendo fundamentos de código abierto en una arquitectura unificada. Permite utilizar protobuf en la pila sin compromisos.

## ¿Cómo funciona?

protoros2 no reemplaza la serialización existente, sino que la complementa con un canal de comunicación transparente que inspecciona el formato de serialización RMW en tiempo de ejecución. Si el RMW soporta protobuf nativamente, envía mensajes directamente. Si no, cae en el estándar CDR.

## ¿Por qué importa?

protoros2 importa porque ofrece una forma flexible de utilizar protobuf en ROS 2, soportando diferentes arquitecturas de Single Source of Truth (SSOT) y permitiendo la coexistencia con RMWs estándar o nativos de protobuf.

## Consejo técnico

Si estás utilizando ROS 2, considera utilizar protoros2 para aprovechar la serialización de protobuf y mejorar la velocidad y la producción de tu aplicación.

```bash
rclcpp::SerializedMessage
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/announcing-protoros2-use-protobuf-in-ros2-without-compromise/57152](https://discourse.openrobotics.org/t/announcing-protoros2-use-protobuf-in-ros2-without-compromise/57152)
