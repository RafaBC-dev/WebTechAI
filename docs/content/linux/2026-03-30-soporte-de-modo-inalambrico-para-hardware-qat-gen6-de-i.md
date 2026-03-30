# Soporte de modo inalámbrico para hardware QAT Gen6 de Intel

**Fecha:** 2026-03-30
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Intel Prepares Wireless Mode Support For QAT Gen6 Hardware

---

## Introducción

La empresa Intel está trabajando en la implementación de un modo inalámbrico para su hardware QAT Gen6, que permitirá acelerar tareas de criptografía inalámbrica en Linux.

## ¿Qué es?

El hardware QAT Gen6 es una tecnología de Intel diseñada para acelerar tareas de criptografía y otras operaciones en Linux. El modo inalámbrico es una característica adicional que permitirá a los usuarios aprovechar al máximo la potencia de este hardware para tareas de criptografía inalámbrica.

## ¿Cómo funciona?

El modo inalámbrico se implementará mediante un driver Linux que permitirá a los usuarios cargar un firmware específico para el hardware QAT Gen6. Este firmware estará diseñado para acelerar algoritmos de criptografía inalámbrica como ZUC-256 y 5G. El driver también permitirá a los usuarios configurar watchdog timers para monitorear el rendimiento del hardware.

## ¿Por qué importa?

La implementación de un modo inalámbrico para el hardware QAT Gen6 es importante porque permitirá a los usuarios acelerar tareas de criptografía inalámbrica en Linux, lo que es crucial para aplicaciones como la seguridad de redes y la autenticación de usuarios.

## Consejo técnico

Si deseas aprovechar al máximo el hardware QAT Gen6 para tareas de criptografía inalámbrica, asegúrate de configurar correctamente el driver Linux y cargar el firmware específico para el modo inalámbrico.

```bash
cfg_services sysfs attribute
```

---

**Fuente original:** [https://www.phoronix.com/news/Intel-QAT-Gen6-Wireless-Mode](https://www.phoronix.com/news/Intel-QAT-Gen6-Wireless-Mode)
