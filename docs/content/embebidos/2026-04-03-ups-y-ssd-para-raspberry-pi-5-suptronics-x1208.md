# UPS y SSD para Raspberry Pi 5: SupTronics X1208

**Fecha:** 2026-04-03
**Categoría:** embebidos
**Tags:** robotica, raspberry-pi, embebidos
**Título original:** SupTronics X1208 – A UPS + M.2 NVMe SSD HAT for the Raspberry Pi 5

---

## Introducción

La empresa SupTronics ha lanzado un nuevo dispositivo llamado X1208, que combina una batería de iones de litio con una ranura para SSD M.2 NVMe. Este dispositivo está diseñado para proteger el sistema en caso de apagones y ofrecer almacenamiento rápido para aplicaciones de Edge Computing y NAS.

## ¿Qué es?

El SupTronics X1208 es un dispositivo de alimentación ininterrumpida (UPS) y una ranura para SSD M.2 NVMe diseñado para Raspberry Pi 5. Ofrece almacenamiento rápido y protege el sistema en caso de apagones para aplicaciones de Edge Computing, NAS, registro de datos y otros sistemas siempre encendidos.

## ¿Cómo funciona?

El X1208 utiliza una pila de iones de litio de 21700 que se carga a través de un puerto USB-C. La batería alimenta el Raspberry Pi 5 a través de un conector GPIO de 40 pines, eliminando la necesidad de cables adicionales. La ranura M.2 M-key admite SSDs NVMe de hasta 4TB con velocidades de PCIe 2.0 y 3.0. El dispositivo también incluye un chip de medición de la batería Maxim para monitorear la tensión y la capacidad de la batería.

## ¿Por qué importa?

El X1208 es importante para aplicaciones que requieren almacenamiento rápido y protección en caso de apagones. Puede ser utilizado en Edge Computing, NAS, registro de datos y otros sistemas siempre encendidos. También es útil para proyectos que requieren una fuente de alimentación ininterrumpida y almacenamiento rápido.

## Consejo técnico

Si estás utilizando el X1208 con Raspberry Pi 5, asegúrate de configurar el PSU_MAX_CURRENT a 5000 en el archivo de configuración del Pi para aprovechar al máximo la capacidad de la batería.

```bash
PSU_MAX_CURRENT=5000
```

---

**Fuente original:** [https://www.cnx-software.com/2026/04/03/suptronics-x1208-a-ups-m-2-nvme-ssd-hat-for-the-raspberry-pi-5/](https://www.cnx-software.com/2026/04/03/suptronics-x1208-a-ups-m-2-nvme-ssd-hat-for-the-raspberry-pi-5/)
