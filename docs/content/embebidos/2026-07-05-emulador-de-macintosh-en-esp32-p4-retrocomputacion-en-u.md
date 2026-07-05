# Emulador de Macintosh en ESP32-P4: retrocomputación en un dispositivo portátil

**Fecha:** 2026-07-05
**Categoría:** embebidos
**Tags:** robotica, embebidos, linux
**Título original:** Macintosh emulator works on ESP32-P4 display devkits from M5Stack and Waveshare

---

## Introducción

Austin McChord ha logrado emular un Macintosh en un dispositivo ESP32-P4, permitiendo a los usuarios disfrutar de la experiencia de retrocomputación en un dispositivo portátil. Esto es posible gracias a la capacidad del ESP32-P4 para emular un Motorola 68040 y otros componentes del sistema.

## ¿Qué es?

El proyecto consiste en una emulación completa de un Macintosh 68k, incluyendo el sistema operativo Mac OS (desde System 7.x hasta Mac OS 8.1). Esto se logra mediante la utilización de un emulador llamado BasiliskII, que se ha portado a un dispositivo ESP32-P4. El dispositivo emulado es capaz de ejecutar aplicaciones y juegos de la época, y cuenta con características como una pantalla táctil, soporte para USB y conexión a Internet a través de WiFi.

## ¿Cómo funciona?

La emulación se logra mediante la utilización de dos núcleos (CORE 0 y CORE 1) en el dispositivo ESP32-P4. El CORE 0 se encarga de la renderización de video y la gestión de entrada/salida, mientras que el CORE 1 se encarga de la emulación del CPU Motorola 68040. La emulación se realiza mediante la utilización de un pipeline óptimizado que incluye escritura en tiempo real de seguimiento de suciedad, DMA doble-buferrado y renderizado basado en mosaicos.

## ¿Por qué importa?

Esta emulación es importante porque permite a los usuarios disfrutar de la experiencia de retrocomputación en un dispositivo portátil. Esto es especialmente relevante para aquellos que desean experimentar la tecnología de la época sin necesidad de utilizar un dispositivo físico antiguo. Además, la emulación es compatible con una variedad de sistemas operativos y aplicaciones, lo que la hace una herramienta versátil para los entusiastas de la retrocomputación.

## Consejo técnico

Si deseas probar la emulación, puedes descargar el código fuente y la documentación del proyecto desde su repositorio en GitHub. Asegúrate de tener un dispositivo ESP32-P4 compatible y de seguir las instrucciones de configuración para asegurarte de que todo funcione correctamente.

---

**Fuente original:** [https://www.cnx-software.com/2026/07/05/macintosh-emulator-works-on-esp32-p4-display-devkits-from-m5stack-and-waveshare/](https://www.cnx-software.com/2026/07/05/macintosh-emulator-works-on-esp32-p4-display-devkits-from-m5stack-and-waveshare/)
