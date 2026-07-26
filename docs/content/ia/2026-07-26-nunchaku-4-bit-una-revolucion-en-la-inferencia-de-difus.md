# Nunchaku 4-bit: una revolución en la inferencia de difusores

**Fecha:** 2026-07-26
**Categoría:** ia
**Tags:** llms, ia-local, benchmarks
**Título original:** Bringing Nunchaku 4-bit Diffusion Inference to Diffusers

---

## Introducción

Los modelos de difusores pueden crear imágenes impresionantes, pero requieren mucha memoria y no son accesibles para la mayoría de los ordenadores de consumo. La cuantización es una solución poderosa que reduce la memoria necesaria, pero hasta ahora no había una forma sencilla de implementarla en los difusores. La tecnología Nunchaku 4-bit cambia esto todo.

## ¿Qué es?

Nunchaku 4-bit es una tecnología de cuantización que reduce la memoria necesaria para la inferencia de difusores. Funciona almacenando los pesos y activaciones en 4 bits, lo que reduce significativamente la memoria necesaria. Esto no solo reduce la memoria, sino que también acelera la denoising loop.

## ¿Cómo funciona?

Nunchaku 4-bit utiliza la técnica de SVDQuant para cuantizar los pesos y activaciones de los modelos de difusores. Esto se logra almacenando los pesos en 4 bits y realizando la desquantización en tiempo de ejecución. Esto reduce la memoria necesaria y acelera la denoising loop.

## ¿Por qué importa?

La tecnología Nunchaku 4-bit es importante porque permite a los modelos de difusores ser utilizados en ordenadores de consumo, que no tienen suficiente memoria para cargar los modelos en alta precisión. Esto abre nuevas posibilidades para la creación de imágenes y videos de alta calidad.

## Consejo técnico

Para aprovechar la tecnología Nunchaku 4-bit, puedes utilizar la herramienta Diffusers y cargar un modelo pre-cuantizado como cualquier otro modelo de difusores. Por ejemplo, puedes utilizar el comando `pip install -U diffusers transformers accelerate kernels bitsandbytes` para instalar las dependencias necesarias y luego cargar un modelo con `ErnieImagePipeline.from_pretrained('lite-infer/ERNIE-Image-Turbo-nunchaku-lite-nvfp4_r32-bnb4-text-encoder')`.

```bash
pip install -U diffusers transformers accelerate kernels bitsandbytes
```

---

**Fuente original:** [https://huggingface.co/blog/nunchaku-diffusers](https://huggingface.co/blog/nunchaku-diffusers)
