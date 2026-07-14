# IoTLabs wM-Bus Gateway: un dispositivo para Home Assistant con conectividad inalámbrica

**Fecha:** 2026-07-14
**Categoría:** embebidos
**Tags:** robotica, microcontroladores, software-y-linux
**Título original:** IoTLabs wM-Bus gateway – An ESP32 device with Wireless M-Bus connectivity for Home Assistant

---

## Introducción

IoTLabs ha lanzado un dispositivo llamado wM-Bus Gateway, que permite a los usuarios de Home Assistant conectar dispositivos de medición y sensores inalámbricos a su sistema de automatización doméstica. Este dispositivo es especialmente útil para aquellos que desean monitorear y controlar su consumo de energía, agua y gas de manera remota.

## ¿Qué es?

El wM-Bus Gateway es un dispositivo basado en el microcontrolador ESP32, que soporta la norma de comunicación inalámbrica wM-Bus (Wireless Meter Bus) para recibir datos de dispositivos de medición y sensores compatibles. Este dispositivo está diseñado para trabajar en estrecha colaboración con Home Assistant, permitiendo a los usuarios integrar fácilmente sus dispositivos de medición y sensores en su sistema de automatización doméstica.

## ¿Cómo funciona?

El wM-Bus Gateway utiliza el protocolo wM-Bus para recibir datos de dispositivos de medición y sensores inalámbricos. Estos datos se reciben a través de una antena SMA externa, que debe ser conectada antes de encender el dispositivo para evitar daños. El dispositivo también cuenta con una pantalla OLED de 1,3 pulgadas para mostrar información en vivo y actualizada, como las mediciones recibidas de los dispositivos de medición y el estado del dispositivo.

## ¿Por qué importa?

El wM-Bus Gateway es importante porque permite a los usuarios de Home Assistant monitorear y controlar su consumo de energía, agua y gas de manera remota. Esto puede ayudar a reducir el consumo de recursos y a identificar posibles problemas de eficiencia en el hogar. Además, el dispositivo puede ser configurado para enviar datos a un servidor de MQTT, lo que permite a los usuarios analizar y visualizar los datos en tiempo real.

## Consejo técnico

Si deseas integrar dispositivos de medición y sensores inalámbricos en tu sistema de automatización doméstica con Home Assistant, asegúrate de utilizar el wM-Bus Gateway y la biblioteca wmbusmeters para recibir y procesar los datos de los dispositivos de medición.

```bash
git clone https://github.com/IoTLabs/wM-Bus-Gateway.git
```

---

**Fuente original:** [https://www.cnx-software.com/2026/07/14/iotlabs-wm-bus-gateway-an-esp32-device-with-wireless-m-bus-connectivity-for-home-assistant/](https://www.cnx-software.com/2026/07/14/iotlabs-wm-bus-gateway-an-esp32-device-with-wireless-m-bus-connectivity-for-home-assistant/)
