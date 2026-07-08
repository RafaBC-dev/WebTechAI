# Un dispositivo de radar aéreo personalizado con ESP32

**Fecha:** 2026-07-08
**Categoría:** embebidos
**Tags:** esp32, robotica, microcontroladores
**Título original:** ESP32 Keeps Tabs on Your Local Airspace

---

## Introducción

Mateusz Juszczyk ha creado un dispositivo de radar aéreo personalizado que utiliza la tecnología ESP32 para mostrar la ubicación de aviones cercanos en tiempo real. Este dispositivo es una excelente demostración de la capacidad de la tecnología ESP32 para realizar tareas complejas de procesamiento de datos.

## ¿Qué es?

El dispositivo de radar aéreo personalizado de Mateusz Juszczyk es un sistema que utiliza la tecnología ESP32 para recibir datos de localización de aviones cercanos a través de la red Wi-Fi y mostrarlos en una pantalla circular. El dispositivo utiliza la API de ADS-B (Automatic Dependent Surveillance-Broadcast) para obtener los datos de localización de los aviones.

## ¿Cómo funciona?

El dispositivo de radar aéreo personalizado funciona conectándose a la red Wi-Fi y solicitando los datos de localización de aviones cercanos a través de la API de ADS-B. Los datos de localización se reciben y se procesan en el ESP32, que luego los envía a la pantalla circular para ser visualizados. El dispositivo también ofrece una interfaz web para configurar los parámetros del dispositivo.

## ¿Por qué importa?

Este dispositivo de radar aéreo personalizado es importante porque ofrece una forma sencilla y accesible de visualizar la ubicación de aviones cercanos en tiempo real. Esto puede ser útil para pilotos, aeropuertos y otras entidades que necesitan monitorear el tráfico aéreo.

## Consejo técnico

Si deseas crear un dispositivo de radar aéreo personalizado similar, puedes utilizar la biblioteca de ESP32 para conectarte a la red Wi-Fi y solicitar los datos de localización de aviones cercanos a través de la API de ADS-B. Puedes utilizar la API de adsb.fi para obtener los datos de localización y mostrarlos en una pantalla circular.

```bash
utiliza la biblioteca de ESP32 para conectarte a la red Wi-Fi y solicitar los datos de localización de aviones cercanos a través de la API de ADS-B: `esp32.connect('adsb.fi', 8080)`
```

---

**Fuente original:** [https://hackaday.com/2026/07/08/esp32-keeps-tabs-on-your-local-airspace/](https://hackaday.com/2026/07/08/esp32-keeps-tabs-on-your-local-airspace/)
