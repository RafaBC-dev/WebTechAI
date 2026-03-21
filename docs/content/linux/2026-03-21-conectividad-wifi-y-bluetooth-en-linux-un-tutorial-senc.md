# Conectividad WiFi y Bluetooth en Linux: un tutorial sencillo

**Fecha:** 2026-03-21
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Enabling MediaTek M7902 WiFi and Bluetooth drivers on Ubuntu 24.04 the easy way

---

## Introducción

Después de casi dos años de espera, los usuarios de Linux pueden disfrutar de la conectividad WiFi y Bluetooth en sus dispositivos gracias a la inclusión de los drivers MediaTek M7902 en el kernel Linux. En este tutorial, aprenderás a instalar y configurar estos drivers en Ubuntu 24.04 de manera sencilla.

## ¿Qué es?

Los drivers MediaTek M7902 son una implementación de los chips WiFi y Bluetooth MediaTek MT7902, que se utilizan en muchos portátiles Windows. Estos chips ofrecen conectividad WiFi 6E y Bluetooth 5.x, y ahora están disponibles en el kernel Linux gracias a la contribución de un desarrollador que los portó a versiones anteriores del kernel.

## ¿Cómo funciona?

Para instalar los drivers, debes clonar el repositorio de GitHub de hmtheboy154 y seguir los pasos de compilación y instalación. Una vez instalados, debes cargar el módulo del kernel y configurar la conectividad WiFi y Bluetooth. El proceso es sencillo y no requiere conocimientos avanzados de Linux.

## ¿Por qué importa?

La inclusión de los drivers MediaTek M7902 en el kernel Linux es importante porque permite a los usuarios de Linux disfrutar de la conectividad WiFi y Bluetooth en sus dispositivos. Esto es especialmente útil para aquellos que utilizan dispositivos con chips MediaTek MT7902, como los portátiles ASUS Vivobook 16.

## Consejo técnico

Si deseas instalar los drivers MediaTek M7902 en tu dispositivo, asegúrate de utilizar el comando `git clone https://github.com/hmtheboy154/mt7902` para clonar el repositorio de GitHub. Luego, sigue los pasos de compilación y instalación descritos en el tutorial.

```bash
git clone https://github.com/hmtheboy154/mt7902
```

---

**Fuente original:** [https://www.cnx-software.com/2026/03/20/enabling-mediatek-m7902-wifi-and-bluetooth-drivers-on-ubuntu-24-04-the-easy-way/](https://www.cnx-software.com/2026/03/20/enabling-mediatek-m7902-wifi-and-bluetooth-drivers-on-ubuntu-24-04-the-easy-way/)
