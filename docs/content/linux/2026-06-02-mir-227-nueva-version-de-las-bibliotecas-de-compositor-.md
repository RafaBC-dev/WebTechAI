# Mir 2.27: Nueva versión de las bibliotecas de compositor Wayland

**Fecha:** 2026-06-02
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Mir 2.27 Released With More Wayland Rust Code

---

## Introducción

Canonical ha lanzado Mir 2.27, una actualización importante de las bibliotecas de compositor Wayland. Esta versión incluye mejoras significativas en la integración con Rust y la implementación de características importantes como el soporte a decoraciones de servidor y cliente.

## ¿Qué es?

Mir es un conjunto de bibliotecas de compositor para Linux que permiten a los desarrolladores crear shells basados en Wayland de manera sencilla. Estas bibliotecas están diseñadas para funcionar en el paradigma de Ubuntu Linux y proporcionan una forma fácil de crear interfaces gráficas de usuario para aplicaciones de escritorio.

## ¿Cómo funciona?

Mir 2.27 implementa la interfaz de programa `org_kde_kwin_server_decoration`, que permite a los clientes solicitar decoraciones de servidor o cliente. También soporta la función `EGL_TEXTURE_EXTERNAL_WL`, necesaria para dispositivos que ejecutan sistemas operativos basados en `libhybris` con su propio stack de drivers EGL. Además, incluye cambios importantes en el código de Rust `wayland-rs`, que permite generar implementaciones para eventos de Wayland y enviarlos desde C++ a Rust y luego a los clientes Wayland.

## ¿Por qué importa?

Esta versión de Mir es importante porque proporciona una forma más fácil de crear interfaces gráficas de usuario para aplicaciones de escritorio en Linux. La integración con Rust es una mejora significativa, ya que permite a los desarrolladores crear aplicaciones más rápidas y eficientes. Además, el soporte a decoraciones de servidor y cliente es una característica importante para mejorar la experiencia del usuario.

## Consejo técnico

Si deseas aprovechar al máximo las características de Mir 2.27, te recomendamos investigar sobre el uso de `wayland-rs` para crear aplicaciones de escritorio en Rust. Puedes comenzar con el tutorial de `wayland-rs` en GitHub y aprender a crear implementaciones para eventos de Wayland y enviarlos a los clientes Wayland.

```bash
git clone https://github.com/wayland-rs/wayland-rs.git
```

---

**Fuente original:** [https://www.phoronix.com/news/Mir-2.27-Released](https://www.phoronix.com/news/Mir-2.27-Released)
