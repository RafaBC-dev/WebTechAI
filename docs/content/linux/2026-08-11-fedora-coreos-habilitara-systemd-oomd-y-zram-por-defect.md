# Fedora CoreOS habilitará systemd-oomd y zRAM por defecto

**Fecha:** 2026-08-11
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Fedora CoreOS To Enable systemd-oomd & zRAM Swap By Default

---

## Introducción

Fedora CoreOS, el sistema operativo optimizado para contenedores de Fedora, está cambiando sus configuraciones por defecto. A partir de la versión 45, systemd-oomd y la swap en zRAM estarán habilitados de manera predeterminada.

## ¿Qué es?

Fedora CoreOS es un sistema operativo diseñado para ejecutar contenedores de manera eficiente. Es una variante de Fedora que se enfoca en la virtualización y la automatización. systemd-oomd es un servicio que monitorea y gestiona el uso de memoria en el sistema, mientras que zRAM es una técnica que utiliza la memoria RAM para crear un espacio de intercambio.

## ¿Cómo funciona?

systemd-oomd funciona monitoreando el uso de memoria en el sistema y tomando medidas para evitar que se sobrecargue. En caso de que la memoria esté agotada, systemd-oomd puede eliminar procesos no esenciales para liberar espacio. zRAM, por otro lado, utiliza la memoria RAM para crear un espacio de intercambio que se puede utilizar en lugar del disco duro.

## ¿Por qué importa?

La habilitación de systemd-oomd y zRAM por defecto en Fedora CoreOS es importante porque mejora la estabilidad y el rendimiento del sistema. Esto se debe a que systemd-oomd puede prevenir que el sistema se sobrecargue y zRAM puede reducir la carga en el disco duro, lo que puede mejorar la velocidad de respuesta del sistema.

## Consejo técnico

Si estás utilizando Fedora CoreOS, puedes verificar si systemd-oomd y zRAM están habilitados ejecutando el comando `systemctl status systemd-oomd` y `cat /proc/sys/vm/swappiness`.

```bash
systemctl status systemd-oomd; cat /proc/sys/vm/swappiness
```

---

**Fuente original:** [https://www.phoronix.com/news/Fedora-CoreOS-OOMD-zRAM-Swap](https://www.phoronix.com/news/Fedora-CoreOS-OOMD-zRAM-Swap)
