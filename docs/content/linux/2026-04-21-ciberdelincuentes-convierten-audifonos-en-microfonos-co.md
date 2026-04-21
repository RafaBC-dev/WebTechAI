# Ciberdelincuentes convierten audífonos en micrófonos con vulnerabilidades de software

**Fecha:** 2026-04-21
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Turning speakers to microphones by hackers

---

## Introducción

Un grupo de investigadores ha descubierto que audífonos y altavoces pueden ser hackeados para convertirse en micrófonos, lo que permite a los ciberdelincuentes escuchar conversaciones privadas sin que se den cuenta.

## ¿Qué es?

Un grupo de investigadores de la Universidad Ben-Gurión de Negev ha descubierto una vulnerabilidad en los audio chipsets que permite a los ciberdelincuentes convertir audífonos y altavoces en micrófonos mediante software malicioso. Esto se logra mediante la técnica de 'jack retasking', que permite reconfigurar los puertos de audio para que funcionen como entradas de micrófono.

## ¿Cómo funciona?

La vulnerabilidad se aprovecha mediante el uso de malware como SPEAKE(a)R, que puede reconfigurar los puertos de audio para que funcionen como entradas de micrófono. Esto permite a los ciberdelincuentes escuchar conversaciones privadas sin que se den cuenta, incluso si el micrófono está deshabilitado o no está presente.

## ¿Por qué importa?

Esta vulnerabilidad es importante porque permite a los ciberdelincuentes escuchar conversaciones privadas sin que se den cuenta, lo que puede ser utilizado para robar información confidencial o para realizar actividades maliciosas. Además, la mayoría de los audífonos y altavoces modernos están afectados por esta vulnerabilidad, lo que hace que sea un problema generalizado.

## Consejo técnico

Para protegerse de esta vulnerabilidad, es recomendable deshabilitar los codecs de audio en la BIOS/UEFI y configurar las políticas de kernel driver de manera estricta. También se puede utilizar software de detección de jack retasking para identificar y prevenir esta vulnerabilidad.

```bash
sudo modprobe -r snd_hda_intel
```

---

**Fuente original:** [https://blog.adafruit.com/2026/04/20/turning-speakers-to-microphones-by-hackers/](https://blog.adafruit.com/2026/04/20/turning-speakers-to-microphones-by-hackers/)
