# Intel Presenta USB4STREAM: Un Protocolo para Transferir Datos con USB4 sin Red

**Fecha:** 2026-05-25
**Categoría:** linux
**Tags:** linux, usb4, thunderbolt
**Título original:** Intel Introducing USB4STREAM Protocol For Linux - Opening Up Some Nifty Uses For USB4

---

## Introducción

Intel ha presentado un nuevo protocolo llamado USB4STREAM para la transferencia de datos con USB4/Thunderbolt. Este protocolo permite transferir datos directamente entre dos host conectados por cable USB4/Thunderbolt, sin necesidad de pasar por la red. Esto puede ser útil para transferir datos rápidamente entre sistemas, compartir cámaras web o otros periféricos, o en entornos donde no haya red disponible.

## ¿Qué es?

El protocolo USB4STREAM es una forma de transferir datos directamente entre dos host conectados por cable USB4/Thunderbolt. Esto se logra a través de un dispositivo de característica llamado /dev/tbstreamX, que se expone en cada host conectado. El protocolo permite transferir datos de manera bidireccional, es decir, desde un host a otro y viceversa.

## ¿Cómo funciona?

El protocolo USB4STREAM funciona a través de un dispositivo de característica llamado /dev/tbstreamX, que se configura a través de la interfaz ConfigFS. Una vez configurado, se puede transferir datos entre los hosts conectados mediante comandos de sistema como dd o cat. El protocolo utiliza un túnel dentro del fabricio Thunderbolt/USB4 para transferir los datos.

## ¿Por qué importa?

El protocolo USB4STREAM es importante porque permite transferir datos directamente entre dos host conectados por cable USB4/Thunderbolt, sin necesidad de pasar por la red. Esto puede ser útil para transferir datos rápidamente entre sistemas, compartir cámaras web o otros periféricos, o en entornos donde no haya red disponible.

## Consejo técnico

Para aprovechar el protocolo USB4STREAM, puedes utilizar el comando dd para transferir datos entre hosts conectados. Por ejemplo, puedes utilizar dd para transferir un archivo de un host a otro, simplemente conectando los hosts con un cable USB4/Thunderbolt y ejecutando el comando dd desde un terminal.

```bash
dd
```

---

**Fuente original:** [https://www.phoronix.com/news/Intel-Linux-USB4STREAM](https://www.phoronix.com/news/Intel-Linux-USB4STREAM)
