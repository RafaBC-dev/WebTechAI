# Microsoft lanza VibeVoice, un modelo de audio para reconocimiento de voz

**Fecha:** 2026-04-28
**Categoría:** ia
**Tags:** ia-local, llms, linux
**Título original:** microsoft/VibeVoice

---

## Introducción

Microsoft ha lanzado VibeVoice, un modelo de audio para reconocimiento de voz que puede transcribir audio en tiempo real y realizar diarización de hablantes. Este modelo se basa en la tecnología de Whisper y está disponible bajo licencia MIT.

## ¿Qué es?

VibeVoice es un modelo de audio para reconocimiento de voz que utiliza la tecnología de Whisper para transcribir audio en tiempo real. Se trata de un modelo de lenguaje que puede reconocer y transcribir el habla en diferentes idiomas y dialectos. Además, VibeVoice incluye la función de diarización de hablantes, que permite identificar a los diferentes hablantes en un audio.

## ¿Cómo funciona?

VibeVoice funciona mediante la utilización de un modelo de lenguaje entrenado con grandes cantidades de datos de audio. Cuando se le proporciona un archivo de audio, el modelo puede reconocer y transcribir el habla en tiempo real. El modelo utiliza una arquitectura de red neuronal para procesar el audio y generar una transcripción del mismo.

## ¿Por qué importa?

VibeVoice es importante porque puede ser utilizado en una variedad de aplicaciones, como el reconocimiento de voz en dispositivos móviles, el transcripción de audio en conferencias y reuniones, y la identificación de hablantes en audio de seguridad. Además, VibeVoice puede ser utilizado para mejorar la experiencia del usuario en aplicaciones de voz, como asistentes virtuales y aplicaciones de mensajería.

## Consejo técnico

Si deseas probar VibeVoice, puedes utilizar el comando `uv run --with mlx-audio mlx_audio.stt.generate --model mlx-community/VibeVoice-ASR-4bit --audio archivo_audio.mp3 --output-path salida --format json --verbose --max-tokens 32768` para transcribir un archivo de audio.

```bash
uv run --with mlx-audio mlx_audio.stt.generate --model mlx-community/VibeVoice-ASR-4bit --audio archivo_audio.mp3 --output-path salida --format json --verbose --max-tokens 32768
```

---

**Fuente original:** [https://simonwillison.net/2026/Apr/27/vibevoice/#atom-everything](https://simonwillison.net/2026/Apr/27/vibevoice/#atom-everything)
