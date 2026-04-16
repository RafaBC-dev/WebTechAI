# AMD mejora el control de energía en Linux con el módulo de poder

**Fecha:** 2026-04-16
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** AMD Linux Graphics Driver Introducing "Power Module" To Better Match Windows Behavior

---

## Introducción

AMD ha presentado un conjunto de parches para el driver de gráficos AMDGPU que incluye un módulo de poder para mejorar el control de energía en Linux. Esto permitirá una experiencia de ahorro de energía más uniforme en comparación con Windows.

## ¿Qué es?

El módulo de poder es una característica que permite al driver de gráficos controlar el consumo de energía de la pantalla, incluyendo la iluminación del panel y la función de autorefresh. Esto se inspira en la forma en que Windows gestiona estas características.

## ¿Cómo funciona?

El módulo de poder se conecta al código de la Display Core (DC) para gestionar las características de ahorro de energía. Esto incluye la implementación de eventos para habilitar/deshabilitar la función de autorefresh y la iluminación del panel, así como la refacción del control de la iluminación del panel para utilizar el módulo de poder.

## ¿Por qué importa?

Esta mejora permitirá una experiencia de ahorro de energía más uniforme en comparación con Windows, lo que es especialmente importante para dispositivos móviles como laptops. Además, esta característica se inspira en la forma en que Windows gestiona estas características, lo que podría ayudar a reducir los problemas específicos de Linux.

## Consejo técnico

Para aprovechar esta característica, es recomendable verificar la documentación del driver de gráficos AMDGPU para conocer los pasos necesarios para habilitar el módulo de poder y configurarlo según las necesidades de tu dispositivo.

```bash
Para obtener más información sobre el driver de gráficos AMDGPU y el módulo de poder, puedes consultar la documentación oficial de AMD o buscar en línea recursos relacionados con la configuración y el uso de esta característica.
```

---

**Fuente original:** [https://www.phoronix.com/news/AMDGPU-DC-Power-Module](https://www.phoronix.com/news/AMDGPU-DC-Power-Module)
