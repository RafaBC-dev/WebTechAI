# Linux 7.1 habilitará AVX-512 BMM en máquinas virtuales KVM

**Fecha:** 2026-04-05
**Categoría:** linux
**Tags:** ia-local, linux, kvm
**Título original:** Linux 7.1 To Expose AMD Zen 6's AVX-512 BMM For Guest VMs

---

## Introducción

La próxima versión del kernel Linux, Linux 7.1, incluirá una característica importante para las máquinas virtuales KVM. Esta característica permitirá a las máquinas virtuales aprovechar al máximo las instrucciones AVX-512 BMM de los procesadores AMD Zen 6.

## ¿Qué es?

AVX-512 BMM es una instrucción de procesador que permite realizar operaciones de multiplicación de matrices y reversión de bits de manera eficiente. Se trata de una característica importante para aplicaciones que requieren procesamiento de grandes cantidades de datos, como la inteligencia artificial y la ciencia de datos.

## ¿Cómo funciona?

La característica se implementará en el código de KVM x86, que es el componente responsable de la virtualización de procesadores en Linux. El código permitirá a las máquinas virtuales detectar la presencia de AVX-512 BMM en el procesador anfitrión y aprovecharla para mejorar el rendimiento de las operaciones de procesamiento de datos.

## ¿Por qué importa?

La habilitación de AVX-512 BMM en las máquinas virtuales KVM permitirá a los usuarios aprovechar al máximo el rendimiento de sus sistemas y mejorar la eficiencia de sus aplicaciones. Esto es especialmente importante para aplicaciones que requieren procesamiento de grandes cantidades de datos, como la inteligencia artificial y la ciencia de datos.

## Consejo técnico

Si estás utilizando Linux 7.1 y KVM, puedes probar la característica de AVX-512 BMM creando una máquina virtual y ejecutando una aplicación que requiera procesamiento de grandes cantidades de datos. Puedes utilizar herramientas como QEMU o VirtualBox para crear y configurar la máquina virtual.

```bash
qemu-system-x86_64 -cpu Znver6 -m 4096 -vnc :0 -enable-kvm
```

---

**Fuente original:** [https://www.phoronix.com/news/Linux-7.1-KVM-AVX-512-BMM](https://www.phoronix.com/news/Linux-7.1-KVM-AVX-512-BMM)
