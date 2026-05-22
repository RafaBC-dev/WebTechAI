# Resolver rutas de paquetes en controladores de ROS

**Fecha:** 2026-05-22
**Categoría:** linux
**Tags:** robotica, linux, codigo
**Título original:** Resolving package paths in controller `params_file`?

---

## Introducción

Un desarrollador de ROS ha descubierto una forma de cargar parámetros de configuración para controladores de forma dinámica, lo que podría simplificar la gestión de archivos de configuración.

## ¿Qué es?

Un controlador de ROS (Robot Operating System) es un programa que gestiona y controla un dispositivo o sistema robótico. Los parámetros de configuración son información importante que se necesita para que el controlador funcione correctamente.

## ¿Cómo funciona?

El controlador manager de ROS puede cargar parámetros de configuración desde un archivo YAML utilizando la opción `params_file`. Sin embargo, solo funciona con rutas absolutas o relativas a la carpeta de trabajo actual, lo que no es muy portable. Esto se debe a que el comando `ros2 pkg prefix` no se puede utilizar para expandir las rutas.

## ¿Por qué importa?

Esta funcionalidad puede ser útil para simplificar la gestión de archivos de configuración en proyectos de robótica que utilizan ROS. También puede ayudar a reducir el tamaño de los archivos de configuración y mejorar la legibilidad del código.

## Consejo técnico

Si deseas utilizar la opción `params_file` para cargar parámetros de configuración, asegúrate de utilizar rutas absolutas o relativas a la carpeta de trabajo actual. Si necesitas expandir las rutas, considera utilizar la función `ament_index_cpp::get_package_share_directory` para obtener la ruta de la carpeta de share del paquete.

```bash
ros2 pkg prefix
```

---

**Fuente original:** [https://discourse.openrobotics.org/t/resolving-package-paths-in-controller-params-file/55009](https://discourse.openrobotics.org/t/resolving-package-paths-in-controller-params-file/55009)
