# Ubuntu ARM64: un paso hacia la igualdad con las arquitecturas x86

**Fecha:** 2026-07-06
**Categoría:** linux
**Tags:** linux, ubuntu, arm64
**Título original:** Canonical On Making Ubuntu For ARM64 "Truly A First-Class Architecture"

---

## Introducción

Canonical, el proveedor de Ubuntu, ha estado trabajando durante un año para hacer que Ubuntu en ARM64 sea una arquitectura de primera clase. Esto significa que los usuarios de ARM64 tendrán acceso a los mismos paquetes y funcionalidades que los usuarios de x86.

## ¿Qué es?

Ubuntu en ARM64 es una versión de la distribución Linux Ubuntu que se ejecuta en procesadores ARM64. Esto permite a los usuarios de dispositivos ARM64 como los Snapdragon X Elite y otros dispositivos con procesadores ARM64 ejecutar Ubuntu de manera nativa.

## ¿Cómo funciona?

Para hacer que Ubuntu en ARM64 sea una arquitectura de primera clase, Canonical ha estado trabajando en varios aspectos. Por un lado, han movido los paquetes ARM64 a la archive principal de Ubuntu, en lugar de mantenerlos en el repositorio de Ports. Además, han comenzado a apoyar la actualización en vivo del kernel en ARM64, lo que permite a los usuarios actualizar el kernel sin tener que reiniciar el sistema.

## ¿Por qué importa?

Esta actualización es importante porque permite a los usuarios de ARM64 tener acceso a los mismos paquetes y funcionalidades que los usuarios de x86. Esto significa que podrán ejecutar aplicaciones como Steam y Chrome de manera nativa, y que tendrán acceso a las últimas actualizaciones de seguridad y funcionalidades de Ubuntu.

## Consejo técnico

Si estás utilizando Ubuntu en ARM64, puedes verificar si tienes acceso a los paquetes ARM64 ejecutando el comando `apt update` y luego `apt search <paquete>`. Si el paquete no está disponible, puedes intentar instalarlo desde el repositorio de Ports.

```bash
apt update && apt search <paquete>
```

---

**Fuente original:** [https://www.phoronix.com/news/Ubuntu-ARM64-2026](https://www.phoronix.com/news/Ubuntu-ARM64-2026)
