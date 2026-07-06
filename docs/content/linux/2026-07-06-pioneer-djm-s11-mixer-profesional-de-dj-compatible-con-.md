# Pioneer DJM-S11: mixer profesional de DJ compatible con Linux 7.3

**Fecha:** 2026-07-06
**Categoría:** linux
**Tags:** linux, robotica, herramientas
**Título original:** Pioneer DJM-S11 Professional DJ Mixer To Be Supported By Linux 7.3

---

## Introducción

La empresa Pioneer ha anunciado que su mixer profesional de DJ, el DJM-S11, será compatible con Linux 7.3 gracias a un parche de código de 87 líneas. Esto permitirá a los DJs utilizar este equipo en entornos Linux, lo que es una gran noticia para la comunidad de Linux.

## ¿Qué es?

El Pioneer DJM-S11 es un mixer profesional de DJ de dos canales diseñado para clubes, conciertos, estudios de música y eventos en vivo. Se caracteriza por su amplia gama de características y su precio de $2,269 USD.

## ¿Cómo funciona?

El DJM-S11 utiliza descriptores de clase USB específicos del fabricante y trucos de mezclador personalizados. Para hacer que funcione en Linux, se han agregado varios trucos de mezclador USB al kernel de Linux. Sin embargo, la pantalla táctil del dispositivo no está aún compatible con Linux.

## ¿Por qué importa?

La compatibilidad del DJM-S11 con Linux es importante porque permite a los DJs utilizar este equipo en entornos Linux, lo que es una gran ventaja para la comunidad de Linux. Además, esto muestra la voluntad de la empresa Pioneer de apoyar a la comunidad de Linux.

## Consejo técnico

Si deseas utilizar el DJM-S11 en un entorno Linux, asegúrate de instalar el parche de código de 87 líneas que agrega la compatibilidad con Linux 7.3. Puedes encontrar este parche en el repositorio 'for-next' de Git de la rama de sonido de Linux.

```bash
git checkout -b linux-7.3-branch && git merge -t for-next linux-7.3-patch
```

---

**Fuente original:** [https://www.phoronix.com/news/Pioneer-DJ-DJM-S11-Linux](https://www.phoronix.com/news/Pioneer-DJ-DJM-S11-Linux)
