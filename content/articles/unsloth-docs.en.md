Title: Unsloth docs: the clearest documentation on hardware requirements for local LLMs
Date: 2026-06-14
Tags: llm, unsloth, hardware, local-llm, documentation, vram
Slug: unsloth-docs
Lang: en
Featured_image: /images/unsloth-docs.png
Summary: Unsloth's documentation is an essential reference for knowing what hardware you need to run and fine-tune local models. VRAM tables, GPU requirements, and step-by-step guides for each model.
Category: Herramientas

![Unsloth docs](/images/unsloth-docs.png)

When you start getting interested in running LLMs locally, the first question is always the same: what hardware do I need? And it's not easy to find a clear answer. Each model publishes its requirements on Hugging Face, blogs, papers... [Unsloth](https://unsloth.ai/docs)'s documentation does an excellent job centralizing and organizing this information.

## VRAM tables for fine-tuning

One of the most useful pages is the [system requirements](https://unsloth.ai/docs/get-started/fine-tuning-for-beginners/unsloth-requirements), which includes a straightforward VRAM table for fine-tuning by model size:

| Parameters | QLoRA (4-bit) | LoRA (16-bit) |
|-----------|--------------|---------------|
| 3B | 3.5 GB | 8 GB |
| 7B | 5 GB | 19 GB |
| 8B | 6 GB | 22 GB |
| 14B | 8.5 GB | 33 GB |
| 27B | 22 GB | 64 GB |
| 32B | 26 GB | 76 GB |
| 70B | 41 GB | 164 GB |
| 405B | 237 GB | 950 GB |

This lets you make quick calculations: with an RTX 3090/4090 (24 GB) you can QLoRA fine-tune models up to ~27B parameters.

They recommend keeping batch size at 1, 2, or 3 to avoid OOM errors. And [here](https://unsloth.ai/docs/basics/unsloth-benchmarks#context-length-benchmarks) they have context length benchmarks.

## Per-model guides with specific requirements

Each supported model has its own guide with detailed requirements. A few examples:

- **Gemma 4**: the 12B runs on 8 GB RAM (4-bit), the 26B-A4B needs 18 GB, and the 31B needs 20 GB.
- **Qwen3.5**: the Small series (up to 9B) runs on **12 GB RAM/VRAM**. The 35B-A3B fits in 22 GB.
- **Qwen3.6**: the 27B runs on 18 GB, the 35B-A3B on 22 GB.
- **Kimi K2.5**: you need ~240 GB+ for 10+ tokens/s with 4-bit quantization. The full FP16 model is 630 GB.
- **Kimi K2.6**: dynamic 2-bit quantization needs 350 GB+.
- **MiniMax M3**: minimum 133 GB RAM for the lightest quantization, 159 GB recommended.
- **GLM-4.6 (355B)**: they recommend 205 GB+ for 5 tokens/s.

## What makes this documentation great

Several things make it especially useful:

- **Straightforward tables**: no fluff. Need to know VRAM for an X-parameter model with Y fine-tuning method? The table is right there.
- **Per-model guides**: each model has its own page with requirement tables, llama.cpp installation instructions, and usage examples.
- **Covers inference and fine-tuning**: not just for training, but also for running models.
- **Cross-platform**: specific requirements for Windows (with and without WSL), macOS (Intel and Apple Silicon), Linux, and CPU-only.
- **Quantizations**: they explain the size of each quantization (GGUF) and what hardware you need for each. Recurring tip: *your combined RAM + VRAM must exceed the size of the quantized file you download*.
- **MTP (Multi-Token Prediction)**: they include specific requirements for this technique that predicts several future tokens in parallel (~1 GB extra over regular GGUF).

Everything is at [unsloth.ai/docs](https://unsloth.ai/docs). If you're looking at hardware for a local inference setup, it's the first page you should visit.

*Original source*: [Unsloth Documentation](https://unsloth.ai/docs)
