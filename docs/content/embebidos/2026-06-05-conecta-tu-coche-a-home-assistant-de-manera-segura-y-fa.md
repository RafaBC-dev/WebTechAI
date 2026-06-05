# Conecta tu coche a Home Assistant de manera segura y fácil

**Fecha:** 2026-06-05
**Categoría:** embebidos
**Tags:** robotica, microcontroladores, software y linux
**Título original:** Connecting Your Car to Home Assistant

---

## Introducción

Conecta tu coche a tu hogar inteligente con Home Assistant y monitorea parámetros importantes de manera remota. Ahora es posible gracias a la creación de un widget que se conecta a la OBD-II del coche.

## ¿Qué es?

Home Assistant es una plataforma de automatización de hogares que permite controlar y monitorear dispositivos inteligentes de manera centralizada. El widget creado se conecta a la OBD-II del coche a través de un dongle ESP32-S3 llamado WiCAN, que se configura a través de Wi-Fi.

## ¿Cómo funciona?

El dongle WiCAN se conecta a la OBD-II del coche y se configura a través de Wi-Fi. Luego, se puede integrar con Home Assistant a través de la documentación proporcionada por MeatPi, la empresa que creó el dongle. La configuración puede requerir algunos ajustes para adaptarse a la ECU del coche específica.

## ¿Por qué importa?

Conectar tu coche a Home Assistant te permite monitorear parámetros importantes como nivel de combustible, días para el servicio y temperatura del refrigerante de manera remota. Esto puede ser especialmente útil para identificar problemas potenciales y realizar mantenimiento preventivo.

## Consejo técnico

Para configurar el dongle WiCAN, asegúrate de seguir la documentación proporcionada por MeatPi y ajustar la configuración según sea necesario para tu coche específico.

```bash
wicand -c /path/to/config.json
```

---

**Fuente original:** [https://hackaday.com/2026/06/04/connecting-your-car-to-home-assistant/](https://hackaday.com/2026/06/04/connecting-your-car-to-home-assistant/)
