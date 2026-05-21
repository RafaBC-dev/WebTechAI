# Protocolo SpatialDDS para compartir datos espaciales en tiempo real

**Fecha:** 2026-05-21
**Categoría:** robotica
**Tags:** robotica, linux, ia-local
**Título original:** SpatialDDS — open spatial computing protocol with ROS 2 bridge

---

## Introducción

La comunidad de robótica y sistemas embebidos acaba de recibir un regalo importante: SpatialDDS, un protocolo de cómputo espacial abierto que permite compartir datos espaciales en tiempo real entre diferentes dominios, incluyendo robots, vehículos autónomos, IoT y más.

## ¿Qué es?

SpatialDDS es un protocolo de cómputo espacial que se basa en DDS (Data Distribution Service) para compartir datos espaciales, como detecciones, posiciones y mapas, entre diferentes operadores y sistemas. Define mensajes tipo (detecciones 3D, posiciones fraccionadas, etc.) y permite la descubierta espacial y la asignación de nombres de operador.

## ¿Cómo funciona?

El protocolo SpatialDDS se implementa mediante un puente con ROS 2 (Robot Operating System 2), que permite la comunicación con robots y sistemas embebidos. Además, hay puentes para MCAP, MQTT y WebSocket, lo que facilita la integración con otros sistemas y aplicaciones. La demostración de fusión de operadores se puede ejecutar mediante el comando `docker compose up`.

## ¿Por qué importa?

SpatialDDS es importante porque permite a diferentes operadores y sistemas compartir datos espaciales en tiempo real, lo que puede mejorar la precisión y la eficiencia en aplicaciones como la navegación autónoma, la detección de obstáculos y la visualización de entornos.

## Consejo técnico

Para empezar a trabajar con SpatialDDS, puedes descargar la demostración de fusión de operadores desde GitHub y ejecutarla utilizando `docker compose up`. Esto te permitirá experimentar con la comunicación entre diferentes operadores y sistemas.

```bash
docker compose up
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/spatialdds-open-spatial-computing-protocol-with-ros-2-bridge/54988](https://discourse.openrobotics.org/t/spatialdds-open-spatial-computing-protocol-with-ros-2-bridge/54988)
