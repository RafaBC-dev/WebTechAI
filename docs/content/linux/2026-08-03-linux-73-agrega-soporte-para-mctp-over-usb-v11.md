# Linux 7.3 agrega soporte para MCTP-Over-USB v1.1

**Fecha:** 2026-08-03
**Categoría:** linux
**Tags:** linux, mctp, usb
**Título original:** Linux 7.3 Adding Support For MCTP-Over-USB v1.1

---

## Introducción

La versión 7.3 de Linux está a punto de incluir soporte para la versión 1.1 del estándar MCTP-Over-USB, lo que permitirá enviar paquetes de protocolo de transporte de componentes de gestión (MCTP) sobre USB de manera más eficiente.

## ¿Qué es?

MCTP-Over-USB es un estándar que permite enviar paquetes de MCTP sobre USB para tareas como dumps de crash, registro y actualizaciones de firmware. La versión 1.1 de este estándar incluye mejoras en la resiliencia de errores y la capacidad de enviar paquetes de MCTP más grandes.

## ¿Cómo funciona?

La implementación de MCTP-Over-USB v1.1 en Linux 7.3 utiliza un nuevo conjunto de bibliotecas llamado 'mctp-usblib' que permite enviar paquetes de MCTP de manera más eficiente sobre USB. Esto se logra mediante la capacidad de enviar paquetes de MCTP más grandes y la implementación de un nuevo modo de empaquetado de paquetes.

## ¿Por qué importa?

La inclusión de MCTP-Over-USB v1.1 en Linux 7.3 permitirá a los desarrolladores enviar paquetes de MCTP de manera más eficiente y segura, lo que puede ser beneficioso para aplicaciones que requieren la transferencia de grandes cantidades de datos sobre USB.

## Consejo técnico

Si estás desarrollando aplicaciones que requieren la transferencia de grandes cantidades de datos sobre USB, considera utilizar la biblioteca 'mctp-usblib' para aprovechar las mejoras de eficiencia y resiliencia de errores de MCTP-Over-USB v1.1.

```bash
git merge <hash del commit que incluye la implementación de MCTP-Over-USB v1.1>
```

---

**Fuente original:** [https://www.phoronix.com/news/Linux-7.3-MCTP-Over-USB-1.1](https://www.phoronix.com/news/Linux-7.3-MCTP-Over-USB-1.1)
