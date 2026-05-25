# QERRA-v2: Evaluación ética para sistemas autónomos y robóticos

**Fecha:** 2026-05-25
**Categoría:** robotica
**Tags:** robotica, ia-local, linux
**Título original:** QERRA-v2 Classical: Practical integration as a Behavior Tree Condition node?

---

## Introducción

Marussa Metocharaki, investigadora griega, ha lanzado la versión 1.8.8 de QERRA-v2 Classical, un motor de evaluación ética explicable para sistemas autónomos y robóticos. Este sistema utiliza el marco SEMEV-12 y devuelve un puntaje transparente con razonamiento. Se busca integrar QERRA como nodo de condición en un árbol de comportamiento.

## ¿Qué es?

QERRA-v2 Classical es un motor de evaluación ética diseñado para sistemas autónomos y robóticos. Utiliza el marco SEMEV-12, que evalúa 12 vectores éticos, y devuelve un puntaje transparente con razonamiento. No utiliza redes neuronales, lo que lo hace completamente clásico.

## ¿Cómo funciona?

QERRA-v2 Classical utiliza el marco SEMEV-12 para evaluar 12 vectores éticos, incluyendo seguridad, privacidad y responsabilidad. El sistema devuelve un puntaje transparente con razonamiento, lo que permite a los desarrolladores entender las razones detrás de la evaluación. La versión 1.8.8 incluye todas las 12 vectores activas.

## ¿Por qué importa?

QERRA-v2 Classical importa porque proporciona una evaluación ética transparente y explicable para sistemas autónomos y robóticos. Esto permite a los desarrolladores crear sistemas que sean más responsables y seguros, y que cumplan con las normas éticas. La integración de QERRA como nodo de condición en un árbol de comportamiento permitirá a los sistemas tomar decisiones más informadas y éticas.

## Consejo técnico

Si deseas integrar QERRA-v2 Classical como nodo de condición en un árbol de comportamiento en ROS 2, puedes utilizar la API pública de Hugging Face para obtener la versión 1.8.8 del motor. Luego, puedes utilizar el archivo QERRA_FOR_ROBOTICS.md para obtener información sobre la integración y los patrones comunes.

```bash
huggingface api get /qerra-v2-classical/1.8.8
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/qerra-v2-classical-practical-integration-as-a-behavior-tree-condition-node/55065](https://discourse.openrobotics.org/t/qerra-v2-classical-practical-integration-as-a-behavior-tree-condition-node/55065)
