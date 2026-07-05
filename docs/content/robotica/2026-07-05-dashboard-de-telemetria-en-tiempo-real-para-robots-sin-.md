# Dashboard de telemetría en tiempo real para robots sin servidor de visualización

**Fecha:** 2026-07-05
**Categoría:** robotica
**Tags:** robotica, linux, codigo
**Título original:** Real-time robot dashboards in React without a separate visualization server

---

## Introducción

Si has construido una interfaz de usuario para operadores o una estación terrestre en React, sabes que la visualización de telemetría en tiempo real es un desafío. Hasta ahora, las opciones eran usar Foxglove o Grafana como infraestructura separada o crear componentes de canvas desde cero. Ahora hay una solución mejor.

## ¿Qué es?

Altara es un conjunto de componentes de React para la visualización de telemetría en tiempo real, diseñado para vivir dentro de la aplicación que se está construyendo. Se puede conectar a un tema de sensor_msgs de ROS2 y mostrar la información en gráficos, indicadores de gauge o mapas de GPS.

## ¿Cómo funciona?

Altara utiliza un adaptador de rosbridge para conectar a los temas de sensor_msgs de ROS2 y mostrar la información en canvas utilizando requestAnimationFrame. Esto permite una visualización fluida y sin retrasos, incluso con flujos de datos de alta frecuencia.

## ¿Por qué importa?

Altara es importante porque resuelve el problema de la visualización de telemetría en tiempo real dentro de la aplicación, sin necesidad de un servidor de visualización separado. Esto permite a los desarrolladores de robots y sistemas embebidos crear interfaces de usuario más completas y eficientes.

## Consejo técnico

Si estás construyendo una interfaz de usuario para operadores en React, considera usar Altara para la visualización de telemetría en tiempo real. Puedes empezar con la documentación de Storybook y explorar los 41 componentes disponibles.

```bash
import { AltaraProvider, TimeSeries } from '@altara/core'; import { createRosbridgeAdapter } from '@altara/ros'; const imu = createRosbridgeAdapter({ url: 'ws://localhost:9090', topic: '/imu/data', messageType: 'sensor_msgs/Imu', }); <AltaraProvider theme='dark'> <TimeSeries dataSource={imu} height={240} /> </AltaraProvider>
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/real-time-robot-dashboards-in-react-without-a-separate-visualization-server/56132](https://discourse.openrobotics.org/t/real-time-robot-dashboards-in-react-without-a-separate-visualization-server/56132)
