# Sabotaje en OpenMandriva: repositorios dañados por contribuyente descontento

**Fecha:** 2026-07-09
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** OpenMandriva: Statement regarding attempted distribution sabotage

---

## Introducción

La distribución de Linux OpenMandriva ha sufrido un sabotaje en sus repositorios, causado por un contribuyente con credenciales administrativas. El incidente podría haber dañado los sistemas de usuarios que utilizan gnome o cosmic.

## ¿Qué es?

OpenMandriva es una distribución de Linux que ofrece una alternativa a otras distribuciones populares como Ubuntu o Fedora. Se enfoca en ofrecer una experiencia de usuario intuitiva y fácil de usar, con un conjunto de herramientas y aplicaciones completas.

## ¿Cómo funciona?

La distribución de Linux OpenMandriva se basa en el núcleo Linux y utiliza el sistema de gestión de paquetes RPM. Los contribuyentes pueden crear y compartir paquetes para la distribución, lo que permite a los usuarios instalar y actualizar aplicaciones de manera sencilla.

## ¿Por qué importa?

El sabotaje en OpenMandriva es importante porque podría haber afectado a los usuarios que dependen de la distribución para sus necesidades de computación. Además, el incidente destaca la importancia de la seguridad y la gestión de credenciales en proyectos de código abierto.

## Consejo técnico

Si eres un contribuyente de OpenMandriva, asegúrate de revisar tus credenciales y configuraciones de seguridad para evitar incidentes similares en el futuro. Puedes hacer esto revisando tus permisos y configuraciones en el sistema de gestión de paquetes RPM.

```bash
rpm -qa --queryformat '%{NAME} %{VERSION} %{RELEASE}
'
```

---

**Fuente original:** [https://lwn.net/Articles/1081884/](https://lwn.net/Articles/1081884/)
