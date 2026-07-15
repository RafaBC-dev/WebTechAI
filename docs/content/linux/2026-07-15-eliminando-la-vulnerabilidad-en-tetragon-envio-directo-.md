# Eliminando la vulnerabilidad en Tetragon: envío directo de paquetes desde BPF

**Fecha:** 2026-07-15
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** [$] Sending packets directly from BPF

---

## Introducción

Tetragon, una herramienta de monitoreo de seguridad basada en BPF, ha sido vulnerable a ataques que eliminan su agente de usuario. Ahora, un equipo de investigadores ha encontrado una forma de eliminar esta vulnerabilidad, permitiendo que Tetragon envíe paquetes directamente desde el kernel.

## ¿Qué es?

Tetragon es una herramienta de monitoreo de seguridad que utiliza BPF (berkeley packet filter) para monitorear diferentes aspectos del kernel de Linux. Su objetivo es detectar y prevenir ataques de seguridad, enviando información a un servicio de monitoreo centralizado. Sin embargo, esta información se envía a través de un agente de usuario, lo que crea una vulnerabilidad si el agente es eliminado.

## ¿Cómo funciona?

El equipo de investigadores ha encontrado una forma de eliminar la necesidad de un agente de usuario, permitiendo que Tetragon envíe paquetes directamente desde el kernel. Esto se logra utilizando la función de BPF para enviar paquetes a un servicio de monitoreo centralizado sin la necesidad de un agente de usuario intermedio.

## ¿Por qué importa?

Esta vulnerabilidad ha sido un problema para los usuarios de Tetragon, ya que un atacante podía eliminar el agente de usuario y evitar que la herramienta detectara y preveniera ataques de seguridad. La eliminación de esta vulnerabilidad mejora la seguridad de Tetragon y sus usuarios.

## Consejo técnico

Si deseas aprovechar esta mejora en la seguridad de Tetragon, debes asegurarte de que tu sistema de monitoreo centralizado esté configurado para recibir paquetes directamente desde el kernel. Puedes hacer esto configurando el servicio de monitoreo para utilizar la función de BPF y enviar paquetes directamente desde el kernel.

```bash
bpftrace -e 'tracepoint:kernel:net:sk:sk_data_ready { @[skb->sk->sk_mark] = count() }'
```

---

**Fuente original:** [https://lwn.net/Articles/1081696/](https://lwn.net/Articles/1081696/)
