# Scry: una herramienta de depuración de robots ROS 2 con asistencia de IA

**Fecha:** 2026-06-21
**Categoría:** ia
**Tags:** robotica, ia-local, python, herramientas
**Título original:** Scry — debug your ROS 2 robot from your phone, with an AI assistant

---

## Introducción

Después de años de frustración con la depuración en campo, un desarrollador ha creado Scry, una herramienta de depuración de robots ROS 2 que utiliza una asistencia de IA para ayudar a los usuarios a identificar y solucionar problemas en tiempo real.

## ¿Qué es?

Scry es una herramienta de depuración de robots ROS 2 que permite a los usuarios acceder a la gráfica de ROS 2 de su robot desde su teléfono móvil. Utiliza una asistencia de IA para inspeccionar los temas, nodos, servicios, parámetros, ciclo de vida, TF y registros en tiempo real, y proporcionar el probable origen del problema. La herramienta es compatible con diferentes ROS 2 distros y permite a los usuarios realizar búsquedas y visualizaciones en tiempo real.

## ¿Cómo funciona?

Scry consta de dos componentes: scry-connect, un servidor Python que se ejecuta en el robot y utiliza rclpy para exponer la gráfica de ROS 2 del robot, y la aplicación Scry para Android, que ejecuta el ciclo de IA, renderiza los resultados y se comunica con el robot. Los usuarios pueden realizar preguntas en inglés para obtener respuestas sobre el problema del robot, y la herramienta proporciona visualizaciones en tiempo real de la gráfica de ROS 2 del robot.

## ¿Por qué importa?

Scry importa porque proporciona una forma más eficiente y efectiva de depurar robots ROS 2 en campo, lo que puede ayudar a reducir el tiempo de respuesta y mejorar la experiencia del usuario. La herramienta también permite a los usuarios acceder a la gráfica de ROS 2 del robot desde su teléfono móvil, lo que puede ser especialmente útil en situaciones en las que no se tenga acceso a un ordenador.

## Consejo técnico

Si deseas utilizar Scry con tu robot ROS 2, asegúrate de instalar scry-connect en tu robot utilizando pip: pip install scry-connect. Luego, descarga la aplicación Scry para Android y sigue las instrucciones para configurar la conexión con tu robot.

```bash
pip install scry-connect
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/scry-debug-your-ros-2-robot-from-your-phone-with-an-ai-assistant/55593](https://discourse.openrobotics.org/t/scry-debug-your-ros-2-robot-from-your-phone-with-an-ai-assistant/55593)
