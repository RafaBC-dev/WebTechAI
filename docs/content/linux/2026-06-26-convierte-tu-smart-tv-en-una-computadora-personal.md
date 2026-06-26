# Convierte tu Smart TV en una computadora personal

**Fecha:** 2026-06-26
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Make That Smart TV into a Computer

---

## Introducción

Una guía reciente muestra cómo transformar una Smart TV en una computadora personal, liberando su potencial de software. Esto podría ser especialmente útil para aquellos que buscan una forma económica de acceder a una computadora básica.

## ¿Qué es?

La guía describe cómo convertir una Smart TV en una computadora personal utilizando Android Debug Bridge (ADB), Shizuku y Termux. Se instala una versión convencional de Linux con el gestor de ventanas Openbox, permitiendo al usuario acceder a una interfaz de usuario más tradicional.

## ¿Cómo funciona?

El proceso comienza estableciendo una conexión ADB, obteniendo acceso raíz con Shizuku y luego instalando Linux con Openbox a través de Termux. Se deben realizar algunas configuraciones específicas para manejar los ciclos de poder de la TV.

## ¿Por qué importa?

Esta guía puede ser especialmente útil para aquellos que buscan una forma económica de acceder a una computadora básica. Además, permite a los usuarios liberar el potencial de software de sus Smart TVs, convirtiéndolos en dispositivos de entretenimiento más flexibles.

## Consejo técnico

Si deseas seguir esta guía, asegúrate de tener instalado Termux en tu Smart TV y de conocer los comandos básicos de ADB y Shizuku. También es importante tener en cuenta que la versión de Linux instalada puede ser antigua, lo que puede causar problemas de estabilidad.

```bash
adb connect <dirección_IP_de_la_TV>; shizuku install; termux install openbox
```

---

**Fuente original:** [https://hackaday.com/2026/06/25/make-that-smart-tv-into-a-computer/](https://hackaday.com/2026/06/25/make-that-smart-tv-into-a-computer/)
