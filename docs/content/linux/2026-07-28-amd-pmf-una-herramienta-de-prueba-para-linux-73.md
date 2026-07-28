# AMD PMF: una herramienta de prueba para Linux 7.3

**Fecha:** 2026-07-28
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** AMD PMF Testing Tool Slated For Linux 7.3

---

## Introducción

La compañía AMD ha anunciado la inclusión de una herramienta de prueba para el marco de gestión de plataforma AMD (AMD PMF) en la versión 7.3 de Linux. Esta herramienta permitirá a los desarrolladores y usuarios testear y analizar los datos de sistema. La herramienta se espera que sea incluida en la versión 7.3 de Linux en las próximas semanas.

## ¿Qué es?

La herramienta de prueba AMD PMF es un pequeño programa que se ejecuta en el espacio de usuario y se conecta a la interfaz /dev/amdpmf_interface para leer y analizar datos de sistema. Estos datos incluyen la fuente de alimentación, la temperatura del procesador, el estado de la batería, la posición del teclado y otros parámetros.

## ¿Cómo funciona?

La herramienta de prueba AMD PMF se conecta a la interfaz /dev/amdpmf_interface y lee los datos de sistema. Luego, imprime estos datos en la consola para que los desarrolladores y usuarios puedan analizarlos. La herramienta es similar a otras herramientas como Turbostat y se espera que sea incluida en la versión 7.3 de Linux.

## ¿Por qué importa?

La herramienta de prueba AMD PMF es importante porque permite a los desarrolladores y usuarios testear y analizar los datos de sistema de los ordenadores con procesadores AMD. Esto puede ayudar a identificar problemas de rendimiento y temperatura, y a optimizar el funcionamiento del sistema.

## Consejo técnico

Para probar la herramienta de prueba AMD PMF, los usuarios deben asegurarse de que estén ejecutando la versión 7.3 de Linux y que tengan acceso a la interfaz /dev/amdpmf_interface. Luego, pueden ejecutar la herramienta en la consola y analizar los datos de sistema que se impriman.

```bash
/dev/amdpmf_interface
```

---

**Fuente original:** [https://www.phoronix.com/news/AMD-PMF-Testing-Tool-Linux-7.3](https://www.phoronix.com/news/AMD-PMF-Testing-Tool-Linux-7.3)
