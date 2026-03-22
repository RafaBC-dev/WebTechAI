# Conecta tu laptop con WiFi y Bluetooth en Ubuntu 24.04

**Fecha:** 2026-03-22
**Categoría:** linux
**Tags:** robotica, linux, codigo
**Título original:** Enabling MediaTek M7902 WiFi and Bluetooth drivers on Ubuntu 24.04 the easy way

---

## Introducción

Después de dos años de espera, los usuarios de Linux pueden disfrutar de la conectividad WiFi y Bluetooth en sus laptops con chipsets MediaTek MT7902. Un desarrollador ha creado un método sencillo para instalar los drivers en Ubuntu 24.04.

## ¿Qué es?

El MediaTek MT7902 es un chipset de WiFi 6E y Bluetooth 5.x utilizado en muchos laptops Windows. Los usuarios de Linux han estado esperando la disponibilidad de los drivers para este chipset durante casi dos años. Finalmente, un desarrollador ha creado un método para instalar los drivers en Linux 6.6 a 6.19, lo que permite a los usuarios de Ubuntu 24.04 disfrutar de la conectividad WiFi y Bluetooth.

## ¿Cómo funciona?

Para instalar los drivers, se deben seguir cuatro pasos: clonar el repositorio de GitHub de hmtheboy154, compilar y instalar los drivers, instalar el firmware opcional y cargar el módulo del kernel con el comando `sudo modprobe mt7902e`. Esto permite a los usuarios de Ubuntu 24.04 conectar sus laptops a una red WiFi y utilizar la función de Bluetooth.

## ¿Por qué importa?

La disponibilidad de los drivers para el MediaTek MT7902 es importante para los usuarios de Linux que desean disfrutar de la conectividad WiFi y Bluetooth en sus laptops. Esto permite a los usuarios conectarse a redes WiFi y utilizar dispositivos Bluetooth, lo que es especialmente útil en entornos de trabajo o estudio.

## Consejo técnico

Si tienes un laptop con chipset MediaTek MT7902 y Ubuntu 24.04, puedes instalar los drivers siguiendo los pasos descritos en este artículo. Recuerda clonar el repositorio de GitHub de hmtheboy154 y compilar los drivers con el comando `make -j8`. Luego, instala el firmware opcional con `sudo make install_fw` y carga el módulo del kernel con `sudo modprobe mt7902e`.

```bash
git clone https://github.com/hmtheboy154/mt7902; cd mt7902; make -j8; sudo make install; sudo make install_fw; sudo modprobe mt7902e
```

---

**Fuente original:** [https://www.cnx-software.com/2026/03/20/enabling-mediatek-m7902-wifi-and-bluetooth-drivers-on-ubuntu-24-04-the-easy-way/](https://www.cnx-software.com/2026/03/20/enabling-mediatek-m7902-wifi-and-bluetooth-drivers-on-ubuntu-24-04-the-easy-way/)
