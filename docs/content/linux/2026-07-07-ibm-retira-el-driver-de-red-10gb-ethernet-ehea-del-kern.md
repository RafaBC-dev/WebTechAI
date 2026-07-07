# IBM retira el driver de red 10Gb Ethernet EHEA del kernel Linux

**Fecha:** 2026-07-07
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** EHEA 10Gb Ethernet Driver Being Retired By IBM As A Relic Of Outdated POWER Hardware

---

## Introducción

La empresa IBM ha decidido retirar el driver de red 10Gb Ethernet EHEA del kernel Linux debido a que el hardware asociado ha sido obsoleto desde 2020. Esto no es sorprendente, ya que el kernel Linux ha estado eliminando drivers de hardware antiguo en los últimos años.

## ¿Qué es?

El driver EHEA es un controlador de red 10Gb Ethernet utilizado en servidores IBM POWER7. Fue creado para interactuar con la tarjeta de red eHEA, que se encuentra en servidores IBM pSeries y BladeCenter JS/PS.

## ¿Cómo funciona?

El driver EHEA se encarga de comunicarse con la tarjeta de red eHEA para enviar y recibir datos a través de la red. El driver utiliza la API de red del kernel Linux para interactuar con la tarjeta de red y realizar la transmisión de datos.

## ¿Por qué importa?

La retirada del driver EHEA no afectará directamente a los usuarios que no utilizan servidores IBM POWER7. Sin embargo, esta acción refleja el proceso de eliminación de hardware antiguo del kernel Linux, lo que puede llevar a una mayor estabilidad y seguridad en el sistema.

## Consejo técnico

Si estás utilizando un servidor IBM POWER7, es recomendable actualizar a un hardware más reciente para aprovechar las últimas características y seguridad del kernel Linux.

```bash
sudo apt-get update && sudo apt-get install linux-image-$(uname -r)
```

---

**Fuente original:** [https://www.phoronix.com/news/IBM-EHEA-Being-Retired](https://www.phoronix.com/news/IBM-EHEA-Being-Retired)
