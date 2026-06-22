# Systemd v261: una actualización significativa para sistemas Linux

**Fecha:** 2026-06-22
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Systemd v261 released

---

## Introducción

La versión 261 de Systemd ha sido lanzada con una larga lista de cambios, incluyendo una nueva función de 'boot secret' para sistemas que carecen de un TPM físico. Esto significa que los sistemas pueden ahora generar y utilizar claves de inicio de sesión seguras sin necesidad de un dispositivo de seguridad físico.

## ¿Qué es?

Systemd es un conjunto de herramientas y servicios para administrar y automatizar el arranque y funcionamiento de sistemas Linux. Su objetivo es proporcionar una experiencia de usuario más fluida y segura para los administradores de sistemas y usuarios finales.

## ¿Cómo funciona?

La nueva función 'boot secret' utiliza el algoritmo de generación de claves de inicio de sesión de Systemd para crear claves seguras que se almacenan en la memoria del sistema. Estas claves se utilizan para autenticar el arranque del sistema y se eliminan automáticamente después de cada arranque.

## ¿Por qué importa?

Esta actualización es importante porque permite a los sistemas Linux utilizar claves de inicio de sesión seguras sin necesidad de un dispositivo de seguridad físico. Esto es especialmente útil para sistemas que carecen de un TPM físico o que requieren una mayor flexibilidad en la configuración de la seguridad.

## Consejo técnico

Si deseas aprovechar la función 'boot secret' en tu sistema Linux, asegúrate de configurar el parámetro `BootSecret=auto` en el archivo `/etc/systemd/system.conf` y reinicia el sistema para aplicar los cambios.

```bash
systemctl restart systemd
```

---

**Fuente original:** [https://lwn.net/Articles/1078708/](https://lwn.net/Articles/1078708/)
