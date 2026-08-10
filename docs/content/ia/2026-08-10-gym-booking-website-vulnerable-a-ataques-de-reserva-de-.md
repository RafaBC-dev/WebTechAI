# Gym-booking website vulnerable a ataques de reserva de espacios

**Fecha:** 2026-08-10
**Categoría:** ia
**Tags:** ia-ethics, generative-ai, openclaw, ai, ai-security-research, llms
**Título original:** Quoting OpenClaw

---

## Introducción

Un hacker ha descubierto una vulnerabilidad en un sitio web de reservas de gimnasios que le permite cancelar reservas de otros usuarios sin autorización. Esta vulnerabilidad pone en riesgo la privacidad y la seguridad de los usuarios.

## ¿Qué es?

OpenClaw es un proyecto de hacking ético que busca identificar vulnerabilidades en sistemas y aplicaciones. En este caso, han encontrado una vulnerabilidad en un sitio web de reservas de gimnasios australiano que permite cancelar reservas de otros usuarios sin autorización.

## ¿Cómo funciona?

La vulnerabilidad se encuentra en la API del sitio web, que no realiza comprobaciones de autorización cuando se cancela una reserva. Esto significa que cualquier usuario puede cancelar una reserva de otro usuario simplemente llamando a la API con la información de la reserva.

## ¿Por qué importa?

Esta vulnerabilidad es importante porque pone en riesgo la privacidad y la seguridad de los usuarios. Si un atacante puede cancelar reservas de otros usuarios, puede también acceder a información sensible como la información de pago o la información de contacto.

## Consejo técnico

Si eres desarrollador, asegúrate de realizar comprobaciones de autorización en tus APIs para evitar vulnerabilidades como esta. Puedes utilizar herramientas como OWASP ZAP para probar tus APIs y detectar vulnerabilidades.

```bash
curl -X DELETE 'https://sitio-web.com/reservas/123' -H 'Authorization: Bearer token-de-autenticacion'
```

---

**Fuente original:** [https://simonwillison.net/2026/Aug/10/openclaw/#atom-everything](https://simonwillison.net/2026/Aug/10/openclaw/#atom-everything)
