# AMD prepara solución para el Apple Studio Display en Linux

**Fecha:** 2026-07-19
**Categoría:** linux
**Tags:** linux, robotica, codigo
**Título original:** AMD Linux Graphics Driver Preps Fix For Apple Studio Display

---

## Introducción

La comunidad de desarrolladores de AMD ha estado trabajando en mejorar la compatibilidad del Apple Studio Display con los gráficos Radeon en Linux. Después de varios intentos fallidos, parece que finalmente se ha encontrado la solución.

## ¿Qué es?

El Apple Studio Display es una pantalla de 27 pulgadas de alta resolución que utiliza DisplayPort. Sin embargo, su manejo de DisplayPort por parte del driver AMDGPU DC es insuficiente, lo que provoca problemas con la configuración de la pantalla en Linux.

## ¿Cómo funciona?

El nuevo parche de AMDGPU DC esconde/disconecta el segundo enlace de DisplayPort para evitar que el sistema operativo Linux lo utilice de manera innecesaria. Esto permite que la pantalla se configure correctamente en modo 5K.

## ¿Por qué importa?

Esta solución es importante porque permite a los usuarios de Linux con gráficos Radeon utilizar el Apple Studio Display sin problemas. Además, también se han realizado mejoras en la compatibilidad con otros dispositivos y se han agregado nuevas características como la escalado de YUV422.

## Consejo técnico

Si estás utilizando un Apple Studio Display con gráficos Radeon en Linux, asegúrate de actualizar tu driver AMDGPU DC a la versión más reciente para aprovechar la solución de este problema.

```bash
sudo apt-get update && sudo apt-get install linux-headers-$(uname -r) && sudo apt-get install amd-gpu-dkms
```

---

**Fuente original:** [https://www.phoronix.com/news/AMDGPU-DC-Apple-Studio-Display](https://www.phoronix.com/news/AMDGPU-DC-Apple-Studio-Display)
