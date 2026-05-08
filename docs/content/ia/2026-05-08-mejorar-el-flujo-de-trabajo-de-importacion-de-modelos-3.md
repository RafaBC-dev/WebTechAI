# Mejorar el flujo de trabajo de importación de modelos 3D con texturas

**Fecha:** 2026-05-08
**Categoría:** ia
**Tags:** robotica, linux, codigo
**Título original:** Improving Asset Import Workflow for External Models with Textures (FBX, glTF, GLB, USDZ, etc.)

---

## Introducción

Los usuarios de Gazebo Sim / Fuel se enfrentan a dificultades al importar modelos 3D externos con texturas. Los formatos comunes como FBX, glTF y USDZ no son fáciles de convertir a formatos compatibles con SDF. Esto puede llevar a errores en la conversión de texturas.

## ¿Qué es?

Gazebo Sim / Fuel es un entorno de simulación de realidad virtual que permite la creación de escenarios y la simulación de robots y objetos. Los modelos 3D con texturas son fundamentales para crear escenarios realistas. Sin embargo, la importación de estos modelos puede ser complicada debido a la falta de soporte nativo para formatos modernos como FBX, glTF y USDZ.

## ¿Cómo funciona?

Actualmente, los usuarios deben utilizar herramientas como gz-usd para convertir los modelos 3D con texturas a formatos compatibles con SDF. Sin embargo, esta herramienta puede fallar en la conversión de texturas, lo que lleva a errores en la simulación.

## ¿Por qué importa?

Mejorar el flujo de trabajo de importación de modelos 3D con texturas es crucial para permitir a los usuarios crear escenarios realistas y complejos en Gazebo Sim / Fuel. Esto puede tener aplicaciones en la robótica, la automatización y la simulación de realidad virtual.

## Consejo técnico

Para mejorar el flujo de trabajo de importación de modelos 3D con texturas, los usuarios pueden utilizar herramientas como gz-usd y ajustar las opciones de conversión para asegurarse de que las texturas se importen correctamente.

```bash
gz-usd
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/improving-asset-import-workflow-for-external-models-with-textures-fbx-gltf-glb-usdz-etc/54622](https://discourse.openrobotics.org/t/improving-asset-import-workflow-for-external-models-with-textures-fbx-gltf-glb-usdz-etc/54622)
