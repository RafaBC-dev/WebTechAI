# Configurando Robots Doble-Armado con Comunicación CAN

**Fecha:** 2026-07-02
**Categoría:** robotica
**Tags:** robotica, ia-local, linux
**Título original:** Mastering NERO | How to Configure CAN Master–Follower Linkage for Dual 7-DoF Robotic Arms

---

## Introducción

Los robots doble-armado están revolucionando la investigación en inteligencia artificial, teleoperación y aprendizaje por imitación. En este tutorial, aprenderás a configurar dos robots AgileX NERO 7-DOF en un setup maestro-sinónimo utilizando comunicación CAN.

## ¿Qué es?

Un robot doble-armado es un sistema robótico que consiste en dos brazos robóticos independientes que pueden moverse y interactuar con su entorno. En este caso, se utiliza la comunicación CAN para sincronizar los movimientos de los dos brazos.

## ¿Cómo funciona?

Para configurar el setup maestro-sinónimo, se conectan los cables CAN entre los dos robots. Luego, se asignan los roles de maestro y sinónimo, donde el maestro genera comandos de movimiento y el sinónimo replica los movimientos en tiempo real. La configuración se realiza utilizando el software de control NERO.

## ¿Por qué importa?

La configuración de robots doble-armado con comunicación CAN es importante para aplicaciones como la teleoperación, el aprendizaje por imitación y la manipulación colaborativa. Esto permite a los robots trabajar juntos de manera coordinada y eficiente.

## Consejo técnico

Antes de configurar el setup maestro-sinónimo, asegúrate de que los dos robots estén cerca de sus posiciones iniciales y que el entorno esté libre de obstáculos. Esto evitará accidentes y daños a los robots.

```bash
nero config maestro-sinonimo --can-h <id_maestro> --can-l <id_sinonimo>
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/mastering-nero-how-to-configure-can-master-follower-linkage-for-dual-7-dof-robotic-arms/56028](https://discourse.openrobotics.org/t/mastering-nero-how-to-configure-can-master-follower-linkage-for-dual-7-dof-robotic-arms/56028)
