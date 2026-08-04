# Linux 7.3: ¿Qué es FailFS y por qué es importante?

**Fecha:** 2026-08-04
**Categoría:** linux
**Tags:** linux, codigo, herramientas
**Título original:** Linux 7.3 Looks Like It Will Upstream FailFS

---

## Introducción

El kernel de Linux 7.3 ha incorporado un nuevo filesystem llamado FailFS, que se suma a NULLFS. FailFS es un filesystem que siempre devuelve un error cuando se intenta realizar una operación sobre él, lo que lo hace ideal para ciertas aplicaciones que necesitan un filesystem inmutable.

## ¿Qué es?

FailFS es un filesystem que siempre devuelve un error cuando se intenta realizar una operación sobre él, lo que lo hace ideal para ciertas aplicaciones que necesitan un filesystem inmutable. Es un filesystem que no se puede montar, no se puede clonar y no se puede acceder desde el espacio de usuario.

## ¿Cómo funciona?

FailFS se monta durante la inicialización del sistema y se crea un solo instante de FailFS. No se puede acceder a él desde el espacio de usuario y no se puede montar nada sobre él. Las operaciones sobre él siempre devuelven un error, lo que lo hace ideal para aplicaciones que necesitan un filesystem inmutable.

## ¿Por qué importa?

FailFS es importante porque proporciona un filesystem inmutable que se puede utilizar en aplicaciones que necesitan un filesystem que no cambie. Esto puede ser útil en entornos de desarrollo, pruebas y producción, donde se necesita un filesystem que no se modifique accidentalmente.

## Consejo técnico

Si estás desarrollando aplicaciones que necesitan un filesystem inmutable, puedes utilizar FailFS como una opción. Para hacerlo, debes agregar el driver de FailFS al kernel de Linux 7.3 y montar el filesystem durante la inicialización del sistema.

```bash
git checkout -b vfs-7.3.failfs
```

---

**Fuente original:** [https://www.phoronix.com/news/Linux-7.3-Expects-FailFS](https://www.phoronix.com/news/Linux-7.3-Expects-FailFS)
