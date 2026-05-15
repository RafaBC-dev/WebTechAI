# CLIM: una solución para garantizar la integridad del comando y la confiabilidad en la robótica

**Fecha:** 2026-05-15
**Categoría:** linux
**Tags:** robotica, linux, codigo
**Título original:** [PoC] CLIM: Open-RMF-style Delay Advisory and Evidence Windows for command-feedback integrity

---

## Introducción

La comunidad de Open-RMF ha desarrollado una herramienta llamada CLIM, que permite a los robots reportar no solo retrasos, sino también por qué la ventana de ejecución del comando y la retroalimentación ya no es confiable. Esto es especialmente importante en entornos de robótica donde la seguridad y la precisión son fundamentales.

## ¿Qué es?

CLIM (Causal Link Integrity Middleware) es un middleware que explora la posibilidad de que un robot pueda reportar no solo que está retrasado, sino también por qué la ventana de ejecución del comando y la retroalimentación ya no es confiable. Esto se logra mediante la emisión de señales estructuradas en formato JSON que pueden ser mapeadas por un Plan Executor o un adaptador de flota a futuras interfaces de retraso y progreso de Open-RMF.

## ¿Cómo funciona?

CLIM funciona emitiendo señales de integridad de comando y señales de advertencia de retraso. La señal de integridad de comando pregunta si el Plan Executor puede seguir confiando en la ejecución del comando, mientras que la señal de advertencia de retraso informa al Plan Executor que el robot puede necesitar reportar un retraso o detener el progreso cerca de un punto de progreso específico.

## ¿Por qué importa?

CLIM es importante porque permite a los robots reportar de manera precisa y confiable su estado de ejecución, lo que es fundamental en entornos de robótica donde la seguridad y la precisión son fundamentales. Esto puede ayudar a prevenir accidentes y mejorar la eficiencia de los sistemas de robótica.

## Consejo técnico

Si estás trabajando con robots y quieres implementar CLIM en tu sistema, puedes empezar por investigar la documentación de Open-RMF y aprender a crear señales de integridad de comando y señales de advertencia de retraso utilizando herramientas como JSON y Plan Executor.

---

**Fuente original:** [https://discourse.openrobotics.org/t/poc-clim-open-rmf-style-delay-advisory-and-evidence-windows-for-command-feedback-integrity/54853](https://discourse.openrobotics.org/t/poc-clim-open-rmf-style-delay-advisory-and-evidence-windows-for-command-feedback-integrity/54853)
