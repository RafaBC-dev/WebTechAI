# Crear un servicio personalizado en Flowstate para AIC Phase 1

**Fecha:** 2026-06-21
**Categoría:** ia
**Tags:** ia-local, robotica, linux
**Título original:** AIC Phase 1: How to run custom aic_model service in Flowstate with AIC_ROUTER_ADDR?

---

## Introducción

El equipo de AIC ha lanzado una nueva fase de su proyecto, que requiere la creación de un servicio personalizado en Flowstate. Este servicio debe ser capaz de interactuar con el router de AIC y ejecutar ciertas acciones. Sin embargo, la documentación proporcionada no es clara sobre cómo configurar correctamente el servicio.

## ¿Qué es?

AIC Phase 1 es una fase del proyecto AIC que requiere la creación de un servicio personalizado en Flowstate. Este servicio debe ser capaz de interactuar con el router de AIC y ejecutar ciertas acciones. El servicio se llama 'aic_model' y debe ser creado utilizando el comando 'inctl service add'.

## ¿Cómo funciona?

Para crear el servicio personalizado, se debe utilizar el comando 'inctl service add' y proporcionar la versión del servicio y el nombre del servicio. El servicio también requiere la configuración de variables de entorno, como 'AIC_ROUTER_ADDR' y 'AIC_MODEL_PASSWD'. Estas variables deben ser proporcionadas de manera segura para evitar la exposición de secretos.

## ¿Por qué importa?

Crear un servicio personalizado en Flowstate para AIC Phase 1 es importante porque permite a los desarrolladores interactuar con el router de AIC y ejecutar acciones específicas. Esto abre nuevas posibilidades para la creación de soluciones personalizadas y automatizadas.

## Consejo técnico

Si estás creando un servicio personalizado en Flowstate para AIC Phase 1, asegúrate de utilizar el comando 'inctl service add' y proporcionar la versión del servicio y el nombre del servicio. También asegúrate de configurar las variables de entorno de manera segura para evitar la exposición de secretos.

```bash
inctl service add <service_asset_id_version> --cluster ... --name aic_model
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/aic-phase-1-how-to-run-custom-aic-model-service-in-flowstate-with-aic-router-addr/55595](https://discourse.openrobotics.org/t/aic-phase-1-how-to-run-custom-aic-model-service-in-flowstate-with-aic-router-addr/55595)
