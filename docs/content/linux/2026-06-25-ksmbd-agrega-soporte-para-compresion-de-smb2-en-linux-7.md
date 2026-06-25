# KSMBD agrega soporte para compresión de SMB2 en Linux 7.2

**Fecha:** 2026-06-25
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** KSMBD Adds SMB2 Compression Support In Linux 7.2

---

## Introducción

El proyecto KSMBD, un servidor de archivos SMB3 en kernel, ha recibido una actualización importante con la adición de soporte para compresión de SMB2 en Linux 7.2. Esto permitirá a los usuarios aprovechar la compresión de datos en tiempo de transmisión, lo que puede acelerar la copia de archivos. La actualización también incluye correcciones de errores para mejorar la estabilidad del servidor.

## ¿Qué es?

KSMBD es un servidor de archivos SMB3 en kernel que permite a los usuarios compartir archivos entre sistemas operativos Windows y Linux. El proyecto se enfoca en proporcionar una implementación de SMB3 en kernel que sea rápida, segura y fácil de usar.

## ¿Cómo funciona?

La compresión de SMB2 en KSMBD se basa en el algoritmo LZ77, que comprime los datos en tiempo de transmisión para reducir el tamaño de los paquetes y mejorar la velocidad de transferencia. El servidor también puede negociar la compresión con el cliente y advertir las capacidades de compresión necesarias.

## ¿Por qué importa?

La adición de soporte para compresión de SMB2 en KSMBD es importante porque permite a los usuarios aprovechar la compresión de datos en tiempo de transmisión, lo que puede acelerar la copia de archivos y mejorar la eficiencia de la red. Esto es especialmente útil para usuarios que necesitan transferir grandes cantidades de datos entre sistemas operativos.

## Consejo técnico

Si deseas aprovechar la compresión de SMB2 en KSMBD, asegúrate de que tu sistema operativo Linux esté actualizado a la versión 7.2 y que el servidor KSMBD esté configurado para negociar la compresión con el cliente.

```bash
sudo modprobe ksmbd
```

---

**Fuente original:** [https://www.phoronix.com/news/Linux-7.2-KSMBD](https://www.phoronix.com/news/Linux-7.2-KSMBD)
