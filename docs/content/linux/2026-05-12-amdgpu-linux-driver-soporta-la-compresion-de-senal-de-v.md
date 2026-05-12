# AMDGPU Linux Driver soporta la compresión de señal de video HDMI 2.1

**Fecha:** 2026-05-12
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** HDMI 2.1 Display Stream Compression "DSC" Also Ready For AMDGPU Linux Driver

---

## Introducción

La empresa AMD ha publicado parches para su driver AMDGPU Linux que permiten la compresión de señal de video HDMI 2.1, lo que permite una mayor eficiencia de banda y una mayor velocidad de refresco en pantallas de alta resolución.

## ¿Qué es?

La compresión de señal de video HDMI 2.1, también conocida como Display Stream Compression (DSC), es una tecnología que comprime la señal de video para reducir la cantidad de datos necesarios para transmitirla. Esto permite una mayor eficiencia de banda y una mayor velocidad de refresco en pantallas de alta resolución, como 4K@240Hz y 8K@120Hz.

## ¿Cómo funciona?

La compresión de señal de video HDMI 2.1 utiliza un algoritmo de compresión que reduce la cantidad de datos necesarios para transmitir la señal de video. Esto se logra mediante la eliminación de información redundante y la compresión de los datos restantes. El driver AMDGPU Linux utiliza esta tecnología para comprimir la señal de video y enviarla a la pantalla de alta resolución.

## ¿Por qué importa?

La compresión de señal de video HDMI 2.1 es importante porque permite una mayor eficiencia de banda y una mayor velocidad de refresco en pantallas de alta resolución. Esto es especialmente útil en aplicaciones que requieren una gran cantidad de datos, como juegos y películas de alta calidad.

## Consejo técnico

Si deseas aprovechar la compresión de señal de video HDMI 2.1 en tu sistema Linux, asegúrate de que tu driver AMDGPU esté actualizado y que tu pantalla de alta resolución esté configurada correctamente. Puedes verificar la versión de tu driver AMDGPU ejecutando el comando `sudo apt-get update && sudo apt-get install amdgpu` en tu terminal Linux.

```bash
sudo apt-get update && sudo apt-get install amdgpu
```

---

**Fuente original:** [https://www.phoronix.com/news/HDMI-2.1-DSC-AMDGPU-FRL](https://www.phoronix.com/news/HDMI-2.1-DSC-AMDGPU-FRL)
