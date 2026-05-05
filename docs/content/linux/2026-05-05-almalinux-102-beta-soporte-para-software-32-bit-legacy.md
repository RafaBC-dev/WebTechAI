# AlmaLinux 10.2 Beta: soporte para software 32-bit legacy

**Fecha:** 2026-05-05
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** AlmaLinux 10.2 Beta Released With Legacy 32-bit Software Support

---

## Introducción

AlmaLinux ha lanzado la versión beta de su sistema operativo 10.2, que incluye soporte para software 32-bit legacy, algo que no se encuentra en la versión upstream de Red Hat Enterprise Linux 10.2. Esto permitirá a los usuarios ejecutar software antiguo en sus máquinas x86_64.

## ¿Qué es?

AlmaLinux es un sistema operativo basado en Red Hat Enterprise Linux, diseñado para ser una alternativa gratuita y compatible con RHEL. Se enfoca en ser una plataforma estable y segura para servidores y aplicaciones empresariales.

## ¿Cómo funciona?

AlmaLinux 10.2 Beta incluye soporte para paquetes de usuario espacios i686, lo que significa que los usuarios pueden ejecutar software 32-bit legacy en sus máquinas x86_64. Esto se logra mediante la inclusión de paquetes de usuario espacios i686 en el sistema operativo. Además, la versión beta también incluye actualizaciones de paquetes como Python 3.14, PostgreSQL, Ruby 4.0 y PHP 8.4.

## ¿Por qué importa?

El soporte para software 32-bit legacy es importante para aquellos que necesitan ejecutar aplicaciones antiguas en sus máquinas x86_64. Esto puede ser especialmente útil para empresas que tienen aplicaciones legacy que no han sido actualizadas a versiones más recientes.

## Consejo técnico

Si necesitas ejecutar software 32-bit legacy en tu máquina x86_64, puedes instalar el paquete de usuario espacios i686 en AlmaLinux 10.2 Beta utilizando el comando `sudo dnf install libstdc++-devel.i686`. Esto te permitirá ejecutar software 32-bit legacy en tu máquina.

```bash
sudo dnf install libstdc++-devel.i686
```

---

**Fuente original:** [https://www.phoronix.com/news/AlmaLinux-10.2-Beta](https://www.phoronix.com/news/AlmaLinux-10.2-Beta)
