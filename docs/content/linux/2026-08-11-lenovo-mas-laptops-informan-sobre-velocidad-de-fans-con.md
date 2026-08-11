# Lenovo: más laptops informan sobre velocidad de fans con Linux 7.3

**Fecha:** 2026-08-11
**Categoría:** linux
**Tags:** linux, robotica, embebidos
**Título original:** Five More Lenovo Laptops To Report Fan Sensors With Linux 7.3

---

## Introducción

La próxima versión de Linux, 7.3, incluirá soporte para más modelos de laptops Lenovo, lo que permitirá que los usuarios monitoreen la velocidad de sus ventiladores. Esto es posible gracias a la extensión del driver Yogafan.

## ¿Qué es?

El driver Yogafan es una herramienta que permite monitorizar la velocidad de los ventiladores en laptops Lenovo. Se ha extendido para incluir más modelos, lo que facilitará a los usuarios la gestión de la temperatura de sus dispositivos.

## ¿Cómo funciona?

El driver Yogafan utiliza la información de la tabla de identificación de dispositivos (DMI) para detectar y monitorear la velocidad de los ventiladores en los laptops Lenovo. La información se almacena en la base de datos del kernel de Linux.

## ¿Por qué importa?

La inclusión de más modelos de laptops Lenovo en el driver Yogafan permite a los usuarios monitorear la temperatura de sus dispositivos de manera más precisa. Esto es especialmente importante para evitar daños a los componentes electrónicos debido a sobrecalentamiento.

## Consejo técnico

Si tienes un laptop Lenovo y deseas monitorear la velocidad de tus ventiladores, asegúrate de actualizar tu kernel de Linux a la versión 7.3 y verificar que el driver Yogafan esté habilitado.

```bash
sudo apt-get update && sudo apt-get install linux-image-7.3
```

---

**Fuente original:** [https://www.phoronix.com/news/Linux-7.3-Yogafan-Driver](https://www.phoronix.com/news/Linux-7.3-Yogafan-Driver)
