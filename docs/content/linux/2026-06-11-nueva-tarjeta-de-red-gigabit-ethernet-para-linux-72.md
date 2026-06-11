# Nueva tarjeta de red Gigabit Ethernet para Linux 7.2

**Fecha:** 2026-06-11
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Airoha AN8801R Gigabit Ethernet PHY Driver Coming To Linux 7.2

---

## Introducción

La comunidad de Linux ha estado trabajando en la implementación de una nueva tarjeta de red Gigabit Ethernet, la Airoha AN8801R, que se espera que esté disponible en la versión 7.2 del kernel Linux. Esta tarjeta es ideal para dispositivos que requieren una conexión de red rápida y eficiente.

## ¿Qué es?

La Airoha AN8801R es una tarjeta de red Gigabit Ethernet que ofrece una conexión de red rápida y eficiente. Es una tarjeta de un solo puerto que se utiliza en dispositivos como Ethernet switches, routers, set top boxes, smart TVs y game consoles. La tarjeta es promovida por Airoha como una opción de bajo consumo y altamente integrada.

## ¿Cómo funciona?

La tarjeta de red Airoha AN8801R se conecta a la placa base del dispositivo y utiliza una interfaz de comunicación para enviar y recibir datos. La tarjeta utiliza un driver de Linux para interactuar con el sistema operativo y proporcionar una conexión de red segura y estable. El driver de Linux es desarrollado por la comunidad de Linux y se basa en un driver de kernel desarrollado por Airoha.

## ¿Por qué importa?

La implementación de la tarjeta de red Airoha AN8801R en Linux 7.2 es importante porque proporciona una conexión de red rápida y eficiente para dispositivos que requieren una alta velocidad de transferencia de datos. Esto es especialmente útil para dispositivos que requieren una conexión de red constante, como routers y switches de red.

## Consejo técnico

Si deseas probar la tarjeta de red Airoha AN8801R en tu sistema Linux, asegúrate de habilitar la opción de configuración AIR_AN8801_PHY en el archivo de configuración de Linux. Esto te permitirá utilizar la tarjeta de red y aprovechar sus características de alta velocidad y eficiencia.

```bash
echo 'CONFIG_AIR_AN8801_PHY=y' >> .config
```

---

**Fuente original:** [https://www.phoronix.com/news/Airoha-N8801R-Linux-7.2](https://www.phoronix.com/news/Airoha-N8801R-Linux-7.2)
