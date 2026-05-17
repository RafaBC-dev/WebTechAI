# Claude Desktop Buddy: un compañero de escritorio interactivo con IA

**Fecha:** 2026-05-17
**Categoría:** ia
**Tags:** ia-local, robotica, esp32
**Título original:** Anthropic’s open-source Claude Desktop Buddy turns ESP32-S3 devices into interactive AI desk companions

---

## Introducción

Anthropic ha liberado un proyecto de código abierto llamado Claude Desktop Buddy, que convierte dispositivos ESP32-S3 en compañeros de escritorio interactivos con IA. Esto permite a los usuarios interactuar con el agente de IA Claude de manera más rápida y conveniente.

## ¿Qué es?

El Claude Desktop Buddy es un dispositivo de hardware que se conecta a la aplicación de escritorio Claude a través de Bluetooth Low Energy (BLE). Se diseñó como un compañero físico para Claude Cowork y Claude Code en macOS y Windows, y proporciona actualizaciones en tiempo real sobre la actividad del agente de IA. También permite a los usuarios responder a solicitudes de permiso directamente utilizando botones, lo que hace que la interacción con el agente de IA sea más rápida y conveniente.

## ¿Cómo funciona?

El Claude Desktop Buddy se basa en el ESP32-S3 y utiliza la API de Claude Hardware Interface (Bluetooth API) para conectarse a la aplicación de escritorio Claude. El dispositivo utiliza botones físicos para permitir a los usuarios interactuar con el agente de IA, y proporciona visualización animada y retroalimentación en tiempo real.

## ¿Por qué importa?

El Claude Desktop Buddy resuelve un problema clave de aprobaciones de usuario frecuentes que otros sistemas de IA similares no abordan. Al permitir a los usuarios interactuar con el agente de IA de manera más rápida y conveniente, el dispositivo mejora la experiencia de usuario y reduce la necesidad de cambiar entre pantallas.

## Consejo técnico

Si deseas crear tu propio dispositivo de Claude Desktop Buddy, puedes utilizar el código abierto de la referencia del proyecto y la API de Claude Hardware Interface para conectarte a la aplicación de escritorio Claude. No olvides verificar la compatibilidad con tu dispositivo ESP32-S3 y configurar la API de BLE correctamente.

```bash
npm install @anthropic/claude-hardware-interface
```

---

**Fuente original:** [https://www.cnx-software.com/2026/05/16/anthropics-open-source-claude-desktop-buddy-turns-esp32-s3-devices-into-interactive-ai-desk-companions/](https://www.cnx-software.com/2026/05/16/anthropics-open-source-claude-desktop-buddy-turns-esp32-s3-devices-into-interactive-ai-desk-companions/)
