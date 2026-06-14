Title: Unsloth docs: la documentación más clara sobre requisitos hardware para LLMs locales
Date: 2026-06-14
Tags: llm, unsloth, hardware, local-llm, documentacion, vram
Slug: unsloth-docs
Lang: es
Featured_image: /images/unsloth-docs.png
Summary: La documentación de Unsloth es una referencia imprescindible para saber qué hardware necesitas para ejecutar y hacer fine-tuning de modelos locales. Tablas de VRAM, requisitos por GPU, y guías paso a paso para cada modelo.
Category: Herramientas

![Unsloth docs](/images/unsloth-docs.png)

Cuando te empiezas a interesar por ejecutar LLMs en local, la primera pregunta es siempre la misma: ¿qué hardware necesito? Y no es fácil encontrar una respuesta clara. Cada modelo publica sus requisitos en su Hugging Face, en blogs, en papers... La documentación de [Unsloth](https://unsloth.ai/docs) hace un trabajo excelente centralizando y organizando esta información.

## Tablas de VRAM para fine-tuning

Una de las páginas más útiles es la de [requisitos del sistema](https://unsloth.ai/docs/get-started/fine-tuning-for-beginners/unsloth-requirements), que incluye una tabla directa con VRAM necesaria para fine-tuning según el tamaño del modelo:

| Parámetros | QLoRA (4-bit) | LoRA (16-bit) |
|------------|--------------|---------------|
| 3B | 3.5 GB | 8 GB |
| 7B | 5 GB | 19 GB |
| 8B | 6 GB | 22 GB |
| 14B | 8.5 GB | 33 GB |
| 27B | 22 GB | 64 GB |
| 32B | 26 GB | 76 GB |
| 70B | 41 GB | 164 GB |
| 405B | 237 GB | 950 GB |

Esto te permite hacer cálculos rápidos: con una RTX 3090/4090 de 24 GB puedes hacer QLoRA de modelos de hasta ~27B parámetros.

Recomiendan mantener el batch size en 1, 2 o 3 para no OOMear. Y [aquí](https://unsloth.ai/docs/basics/unsloth-benchmarks#context-length-benchmarks) tienen benchmarks de context length.

## Guías por modelo con requisitos específicos

Cada modelo que soportan tiene su propia guía con requisitos detallados. Algunos ejemplos:

- **Gemma 4**: la 12B corre en 8 GB RAM (4-bit), la 26B-A4B necesita 18 GB y la 31B necesita 20 GB.
- **Qwen3.5**: la serie Small (hasta 9B) funciona con **12 GB de RAM/VRAM**. La 35B-A3B cabe en 22 GB.
- **Qwen3.6**: la 27B corre en 18 GB, la 35B-A3B en 22 GB.
- **Kimi K2.5**: necesitas ~240 GB+ para 10+ tokens/s con cuantización 4-bit. El modelo completo en FP16 ocupa 630 GB.
- **Kimi K2.6**: la cuantización 2-bit dinámica necesita 350 GB+.
- **MiniMax M3**: mínimo 133 GB RAM para la cuantización más ligera, recomendado 159 GB.
- **GLM-4.6 (355B)**: recomiendan 205 GB+ para 5 tokens/s.

## Lo que hace buena esta documentación

Varias cosas que la hacen especialmente útil:

- **Tablas directas**: sin rodeos. Necesitas saber VRAM para un modelo de X parámetros con Y método de fine-tuning? La tabla está ahí.
- **Guías por modelo**: cada modelo tiene su página con tabla de requisitos, instrucciones de instalación con llama.cpp y ejemplos de uso.
- **Cubre inferencia y fine-tuning**: no solo para entrenar, también para ejecutar modelos.
- **Multiplataforma**: requisitos específicos para Windows (con y sin WSL), macOS (Intel y Apple Silicon), Linux, y CPU-only.
- **Cuantizaciones**: explican qué tamaño ocupa cada cuantización (GGUF) y qué hardware necesitas para cada una. Consejo recurrente: *tu RAM + VRAM combinada debe superar el tamaño del archivo cuantizado que descargues*.
- **MTP (Multi-Token Prediction)**: incluyen requisitos específicos para esta técnica que predice varios tokens futuros en paralelo (~1 GB extra sobre la GGUF normal).

Todo está en [unsloth.ai/docs](https://unsloth.ai/docs). Si estás mirando hardware para montar un equipo de inferencia local, es la primera página que deberías visitar.

*Fuente original*: [Unsloth Documentation](https://unsloth.ai/docs)
