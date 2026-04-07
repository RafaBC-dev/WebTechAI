# Convierte un calibrador Bluetooth en un dispositivo de entrada para FreeCAD

**Fecha:** 2026-04-07
**Categoría:** linux
**Tags:** python, librerias, herramientas, linux
**Título original:** Turning a Bluetooth caliper into a FreeCAD input device

---

## Introducción

Un ingeniero ha encontrado una forma de aprovechar un calibrador Bluetooth para tomar medidas y sincronizarlas directamente con el software de diseño asistido por computadora (CAD) FreeCAD. Esto elimina la necesidad de transcribir manualmente las medidas y reduce errores.

## ¿Qué es?

El proyecto consiste en desarrollar una biblioteca de Python llamada sylvac-measure que lee medidas del calibrador Bluetooth Sylvac S_Cal EVO y una extensión de FreeCAD llamada InstrumentInput que permite tomar medidas con el calibrador y sincronizarlas en el software de CAD.

## ¿Cómo funciona?

La biblioteca sylvac-measure utiliza la conexión Bluetooth del calibrador para leer las medidas, que luego se envían a la extensión InstrumentInput de FreeCAD. Esta extensión permite seleccionar un campo de medida en el software de CAD y tomar la medida con el calibrador, que se sincroniza automáticamente en el campo seleccionado.

## ¿Por qué importa?

Esta solución es importante porque elimina la necesidad de transcribir manualmente las medidas, lo que reduce errores y aumenta la eficiencia en el proceso de diseño y modelado. También permite una mayor precisión y velocidad en la toma de medidas.

## Consejo técnico

Si deseas aprovechar este proyecto, puedes instalar la biblioteca sylvac-measure y la extensión InstrumentInput de FreeCAD, y luego configurar tu calibrador Bluetooth Sylvac S_Cal EVO para que se comunique con la biblioteca. Puedes encontrar instrucciones en el blog del ingeniero que desarrolló el proyecto.

```bash
pip install sylvac-measure
```

---

**Fuente original:** [https://blog.adafruit.com/2026/04/06/turning-a-bluetooth-caliper-into-a-freecad-input-device/](https://blog.adafruit.com/2026/04/06/turning-a-bluetooth-caliper-into-a-freecad-input-device/)
