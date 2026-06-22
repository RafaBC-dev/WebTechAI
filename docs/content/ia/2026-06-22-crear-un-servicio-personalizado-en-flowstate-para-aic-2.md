# Crear un servicio personalizado en Flowstate para AIC Phase 1

**Fecha:** 2026-06-22
**Categoría:** ia
**Tags:** ia-local, robotica, linux
**Título original:** AIC Phase 1: How to run custom aic_model service in Flowstate with AIC_ROUTER_ADDR?

---

## Introducción

El equipo de AIC ha lanzado una nueva fase de su proyecto, que requiere la creación de un servicio personalizado en Flowstate. Este servicio debe ser capaz de interactuar con el router de AIC y ejecutar ciertas acciones. Sin embargo, la documentación proporcionada no es clara sobre cómo configurar el router y proporcionar credenciales de seguridad.

## ¿Qué es?

Flowstate es un entorno de desarrollo para la creación de aplicaciones de inteligencia artificial. AIC Phase 1 es una fase del proyecto AIC que requiere la creación de un servicio personalizado en Flowstate. Este servicio debe ser capaz de interactuar con el router de AIC y ejecutar ciertas acciones.

## ¿Cómo funciona?

Para crear un servicio personalizado en Flowstate, se debe utilizar el comando `inctl asset install` para instalar el paquete del servicio y luego `inctl service add` para agregar el servicio al entorno de Flowstate. El servicio debe ser configurado para interactuar con el router de AIC y ejecutar las acciones necesarias. El router de AIC requiere la dirección `AIC_ROUTER_ADDR` y, en algunos casos, la contraseña `AIC_MODEL_PASSWD` para autenticarse.

## ¿Por qué importa?

La creación de un servicio personalizado en Flowstate es importante para la fase AIC Phase 1, ya que permite a los desarrolladores interactuar con el router de AIC y ejecutar acciones específicas. Esto puede ayudar a mejorar la eficiencia y la precisión de la inteligencia artificial en el proyecto AIC.

## Consejo técnico

Si estás intentando crear un servicio personalizado en Flowstate para AIC Phase 1, asegúrate de utilizar el comando correcto para instalar el paquete del servicio y agregarlo al entorno de Flowstate. Utiliza `inctl asset install <bundle.tar> --org ... --cluster ...` y luego `inctl service add <service_asset_id_version> --cluster ... --name aic_model`.

```bash
inctl asset install <bundle.tar> --org ... --cluster ...; inctl service add <service_asset_id_version> --cluster ... --name aic_model
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/aic-phase-1-how-to-run-custom-aic-model-service-in-flowstate-with-aic-router-addr/55595](https://discourse.openrobotics.org/t/aic-phase-1-how-to-run-custom-aic-model-service-in-flowstate-with-aic-router-addr/55595)
