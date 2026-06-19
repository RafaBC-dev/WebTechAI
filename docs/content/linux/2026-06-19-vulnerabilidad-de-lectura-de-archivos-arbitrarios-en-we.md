# Vulnerabilidad de lectura de archivos arbitrarios en WebsocketServer

**Fecha:** 2026-06-19
**Categoría:** linux
**Tags:** robotica, linux, seguridad
**Título original:** Security Advisory: Arbitrary File Read Vulnerability in WebsocketServer (Issue gz-sim#3589)

---

## Introducción

Una vulnerabilidad de seguridad ha sido identificada en el plugin WebsocketServer de Gazebo, que permite la lectura de archivos arbitrarios en el sistema host. Esto puede ser explotado por cualquier cliente en la red que pueda alcanzar el puerto WebSocket (9002 por defecto).

## ¿Qué es?

Gazebo es un entorno de simulación de realidad virtual que utiliza el plugin WebsocketServer para permitir la comunicación en tiempo real entre el cliente y el servidor. El plugin WebsocketServer es responsable de manejar las solicitudes de recursos del cliente.

## ¿Cómo funciona?

El plugin WebsocketServer utiliza el método OnAsset para leer recursos del sistema host. Sin embargo, este método no validaba suficientemente las rutas de los archivos, lo que permitía la lectura de archivos arbitrarios en el sistema host. El sistema fallaba en canonicalizar las rutas o confinarlas a un directorio base.

## ¿Por qué importa?

Esta vulnerabilidad puede ser explotada para acceder a archivos sensibles en el sistema host, lo que puede ser un problema de seguridad significativo. Es importante actualizar a las versiones parcheadas para evitar este tipo de ataques.

## Consejo técnico

Si no puedes actualizar inmediatamente, puedes mitigar esta vulnerabilidad configurando una clave de autorización en el plugin WebsocketServer o asegurando que el puerto 9002 esté estrictamente bloqueado desde el acceso a la red no confiable.

---

**Fuente original:** [https://discourse.openrobotics.org/t/security-advisory-arbitrary-file-read-vulnerability-in-websocketserver-issue-gz-sim-3589/55558](https://discourse.openrobotics.org/t/security-advisory-arbitrary-file-read-vulnerability-in-websocketserver-issue-gz-sim-3589/55558)
