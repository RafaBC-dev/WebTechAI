# Vulnerabilidad Dirty Frag: acceso root en todas las distribuciones de Linux

**Fecha:** 2026-05-08
**Categoría:** ia
**Tags:** linux, codigo, seguridad
**Título original:** Dirty Frag Vulnerability Made Public Early: Root Privilege On All Distributions

---

## Introducción

Una nueva vulnerabilidad en Linux ha sido revelada, permitiendo a los usuarios locales elevar su privilegio a root en todas las distribuciones principales. Aunque no hay parches disponibles, hay una solución temporal para proteger a los sistemas.

## ¿Qué es?

La vulnerabilidad Dirty Frag es un bug de escalada de privilegios local que afecta a las distribuciones de Linux. Se encuentra en el código del kernel en las rutas de encriptación rápida de esp4, esp6 y rxrpc.

## ¿Cómo funciona?

La vulnerabilidad se aprovecha de la forma en que el kernel maneja las rutas de encriptación rápida, permitiendo a los usuarios locales acceder a la configuración del kernel y elevar su privilegio a root.

## ¿Por qué importa?

La vulnerabilidad Dirty Frag es importante porque permite a los usuarios locales acceder a la configuración del kernel y elevar su privilegio a root en todas las distribuciones de Linux. Esto puede ser utilizado para realizar acciones maliciosas y comprometer la seguridad del sistema.

## Consejo técnico

Para proteger a su sistema, puede utilizar la solución temporal de eliminar los módulos esp4, esp6 y rxrpc. Esto se puede hacer ejecutando el comando `sh -c 'printf 'install esp4 /bin/false
install esp6 /bin/false
install rxrpc /bin/false
' > /etc/modprobe.d/dirtyfrag.conf; rmmod esp4 esp6 rxrpc 2>/dev/null; true'`

```bash
sh -c 'printf 'install esp4 /bin/false
install esp6 /bin/false
install rxrpc /bin/false
' > /etc/modprobe.d/dirtyfrag.conf; rmmod esp4 esp6 rxrpc 2>/dev/null; true'
```

---

**Fuente original:** [https://www.phoronix.com/news/Dirty-Frag-Linux](https://www.phoronix.com/news/Dirty-Frag-Linux)
