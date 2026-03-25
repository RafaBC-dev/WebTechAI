# LiteLLM en PyPI comprometido: una amenaza para la seguridad

**Fecha:** 2026-03-25
**Categoría:** ia
**Tags:** ia-local, python, librerias
**Título original:** LiteLLM on PyPI is compromised

---

## Introducción

LiteLLM, una biblioteca de inteligencia artificial, ha sido comprometida en la tienda de paquetes PyPI. Esto significa que cualquier persona que haya instalado la versión 1.82.8 del paquete puede haber sido víctima de un ataque de robo de credenciales.

## ¿Qué es?

LiteLLM es una biblioteca de inteligencia artificial desarrollada en Python que permite a los desarrolladores crear modelos de lenguaje y agentes de inteligencia artificial. Sin embargo, la versión 1.82.8 de la biblioteca ha sido comprometida con un archivo malicioso que recopila y envía información confidencial a los atacantes.

## ¿Cómo funciona?

El archivo malicioso, llamado litellm_init.pth, se ejecuta automáticamente cuando se instala la biblioteca en el entorno de Python. Esto significa que cualquier persona que haya instalado la biblioteca en su sistema puede haber sido afectada por el ataque.

## ¿Por qué importa?

La comprometida de LiteLLM es una amenaza importante para la seguridad de los desarrolladores y usuarios de la biblioteca. Puede haber permitido a los atacantes acceder a credenciales de SSH, servicios en la nube, monederos criptográficos y otros datos confidenciales.

## Consejo técnico

Si has instalado la versión 1.82.8 de LiteLLM en tu sistema, debes actualizar a la versión más reciente y eliminar cualquier archivo o configuración relacionada con la biblioteca comprometida. Además, debes cambiar cualquier credencial o contraseña que haya sido comprometida.

```bash
pip uninstall litellm --force
```

---

**Fuente original:** [https://lwn.net/Articles/1064479/](https://lwn.net/Articles/1064479/)
