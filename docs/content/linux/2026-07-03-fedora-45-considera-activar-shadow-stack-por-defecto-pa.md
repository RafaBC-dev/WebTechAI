# Fedora 45 considera activar Shadow Stack por defecto para mejorar la seguridad

**Fecha:** 2026-07-03
**Categoría:** linux
**Tags:** linux, seguridad, fedora
**Título original:** Fedora 45 Considering x86_64 Shadow Stack Usage By Default

---

## Introducción

La distribución Linux Fedora 45 podría incluir un cambio importante en la seguridad de sus sistemas. La propuesta de cambio busca activar por defecto la tecnología Shadow Stack en los sistemas x86_64, lo que ayudaría a proteger contra ataques de programación orientada a retorno (ROP).

## ¿Qué es?

Shadow Stack es una tecnología de seguridad que utiliza la arquitectura de los procesadores Intel y AMD para proteger contra ataques de ROP. Funciona activando un stack de seguridad que ayuda a prevenir que los atacantes accedan a la memoria del sistema.

## ¿Cómo funciona?

La tecnología Shadow Stack se activa automáticamente en los procesadores que la soportan, utilizando la arquitectura Intel CET. El enlazador dinámico o las rutinas de inicio del sistema activan la tecnología para cualquier proceso que tenga dependencias de bibliotecas compiladas con soporte para Shadow Stack.

## ¿Por qué importa?

La activación de Shadow Stack por defecto en Fedora 45 ayudaría a proteger contra ataques de ROP, que pueden ser peligrosos para la seguridad de los sistemas. Además, la tecnología es compatible con la mayoría de los binarios existentes, lo que minimiza el impacto en la compatibilidad.

## Consejo técnico

Si estás utilizando Fedora 45, puedes comprobar si tu sistema soporta Shadow Stack ejecutando el comando `getconf LONG_BIT` y verificando si el resultado es 64. Si es así, puedes activar la tecnología ejecutando el comando `echo 'enable_shadow_stack=1' >> /etc/sysctl.conf` y reiniciando el sistema.

```bash
getconf LONG_BIT
```

---

**Fuente original:** [https://www.phoronix.com/news/Fedora-45-Consider-Shadow-Stack](https://www.phoronix.com/news/Fedora-45-Consider-Shadow-Stack)
