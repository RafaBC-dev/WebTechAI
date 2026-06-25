# Fedora impone 2FA para proteger su cadena de suministro

**Fecha:** 2026-06-25
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** [$] Fedora: 2FA, or not 2FA, that is the question

---

## Introducción

Fedora, una distribución de Linux popular, ha sufrido un ataque de malware gracias a una cuenta comprometida. Para evitar que esto vuelva a ocurrir, el proyecto está implementando la autenticación en dos factores (2FA) para sus paqueteros.

## ¿Qué es?

Fedora es una distribución de Linux gratuita y de código abierto que se utiliza en servidores, supercomputadoras y sistemas embebidos. La autenticación en dos factores (2FA) es un método de autenticación que requiere la presentación de un segundo factor de autenticación además del nombre de usuario y contraseña, como un código generado por una aplicación de autenticación móvil.

## ¿Cómo funciona?

Fedora está implementando la 2FA para sus paqueteros, que son responsables de crear y mantener los paquetes de software para la distribución. Los paqueteros deben habilitar la 2FA dentro de los próximos tres meses. Esto significa que deben configurar una aplicación de autenticación móvil y utilizarla para generar un código de autenticación cada vez que inician sesión en el sistema.

## ¿Por qué importa?

La implementación de la 2FA en Fedora es importante porque reduce el riesgo de que los atacantes accedan a las cuentas de los paqueteros y utilicen su acceso para introducir malware en la cadena de suministro de la distribución. Esto puede tener consecuencias graves, como la propagación de malware a los usuarios de Fedora.

## Consejo técnico

Si eres un paqueteo de Fedora, asegúrate de habilitar la 2FA en tu cuenta dentro de los próximos tres meses. Puedes hacerlo configurando una aplicación de autenticación móvil como Google Authenticator o Authy y siguiendo las instrucciones de Fedora para habilitar la 2FA.

---

**Fuente original:** [https://lwn.net/Articles/1078964/](https://lwn.net/Articles/1078964/)
