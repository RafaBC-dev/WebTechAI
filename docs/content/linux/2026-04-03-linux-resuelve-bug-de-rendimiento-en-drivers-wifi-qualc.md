# Linux resuelve bug de rendimiento en drivers WiFi Qualcomm

**Fecha:** 2026-04-03
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Linux Fixes Performance Bug Affecting Qualcomm Ath11k & Ath12k WiFi Drivers

---

## Introducción

El kernel Linux 7.0 ha recibido actualizaciones para los drivers WiFi Qualcomm Ath11k y Ath12k, que resuelven un problema de rendimiento que afectaba a estos dispositivos desde su integración en 2019 y 2022, respectivamente.

## ¿Qué es?

Los drivers WiFi Qualcomm Ath11k y Ath12k son componentes del kernel Linux que permiten la comunicación inalámbrica con dispositivos WiFi basados en la tecnología 802.11ax. El bug de rendimiento afectaba a la capacidad de estos dispositivos para manejar tráfico de red de manera eficiente.

## ¿Cómo funciona?

El bug se debía a que el driver WiFi incorrectamente paraba la sesión de agregación (AMPDU) para un ID de flujo (TID) incorrecto, lo que provocaba una degradación del rendimiento. Las actualizaciones resuelven este problema pasando el ID de flujo correcto al método que actualiza el estado de la sesión de recepción.

## ¿Por qué importa?

La resolución de este bug es importante porque afecta a la capacidad de los dispositivos WiFi basados en Qualcomm para manejar tráfico de red de manera eficiente, lo que puede provocar problemas de rendimiento en aplicaciones que dependen de la conectividad inalámbrica.

## Consejo técnico

Si estás utilizando un dispositivo WiFi basado en Qualcomm, te recomendamos verificar la versión actual del kernel Linux y aplicar las actualizaciones disponibles para asegurarte de que estás utilizando la versión más reciente de los drivers WiFi.

---

**Fuente original:** [https://www.phoronix.com/news/Linux-7.0-rc7-Networking-Fixes](https://www.phoronix.com/news/Linux-7.0-rc7-Networking-Fixes)
