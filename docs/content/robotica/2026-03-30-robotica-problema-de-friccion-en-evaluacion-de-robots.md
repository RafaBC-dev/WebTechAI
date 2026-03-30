# Robótica: Problema de Fricción en Evaluación de Robots

**Fecha:** 2026-03-30
**Categoría:** robotica
**Tags:** robotica, gazebo, linux
**Título original:** AIC - Gazebo Friction During Evaluation

---

## Introducción

Un usuario de Gazebo ha reportado un problema común en la evaluación de robots: la fricción entre el cable y los NUC boxes hace que el robot se atasque. ¿Es este comportamiento intencionado o se puede reducir la fricción?

## ¿Qué es?

Gazebo es una simulación de realidad virtual para la robótica y la automatización. Permite a los desarrolladores probar y evaluar sus robots en un entorno virtual antes de implementarlos en la vida real.

## ¿Cómo funciona?

La simulación de Gazebo utiliza un modelo de física para simular el comportamiento de los robots en un entorno virtual. El usuario puede configurar la simulación para incluir elementos como la fricción, la gravedad y la resistencia del aire.

## ¿Por qué importa?

Este problema de fricción es importante porque puede afectar la precisión y la estabilidad de la simulación. Si la fricción es demasiado alta, el robot puede no funcionar correctamente o incluso fallar en la evaluación.

## Consejo técnico

Para reducir la fricción en la evaluación de robots con Gazebo, puedes ajustar la configuración de la simulación para reducir la fricción entre el cable y los NUC boxes. Puedes hacer esto ajustando la propiedad 'friction' en el archivo de configuración de la simulación.

```bash
gazebo --verbose --config=friction=0.5
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/aic-gazebo-friction-during-evaluation/53640](https://discourse.openrobotics.org/t/aic-gazebo-friction-during-evaluation/53640)
