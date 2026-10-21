Title: aa-opencode: OpenCode models with benchmarks and price in one table
Date: 2026-10-21
Category: Tools
Tags: opencode, ai, benchmarks, pricing, cli, python
Slug: aa-opencode
Lang: en
Summary: aa-opencode crosses the OpenCode model catalog with Artificial Analysis benchmarks and prints one table with intelligence, speed, and price per model. A Python CLI I just published.
Featured_image: /images/aa-opencode.png

![aa-opencode output with the Go catalog](/images/aa-opencode.png)

I use [OpenCode](https://opencode.ai/) as one of the model providers in [pi](https://pablocaro.es/en/que-es-pi-coding-agent), and there's the problem: the list of available models is long and says nothing. You get names, sure. What you don't get is how well each one reasons, how fast it answers, or what a million tokens costs you. Picking by eye is a coin toss.

[Artificial Analysis](https://artificialanalysis.ai/) publishes exactly that: independent intelligence, coding, and math indices, plus output speed, time to first token, and price. But it has its own catalog and its own names, so crossing it by hand against OpenCode's models is a chunk of work every time you want to check.

So I wrote [aa-opencode](https://github.com/pcaro/aa-opencode): it grabs the OpenCode model list, crosses it with the Artificial Analysis API, and prints a table. Nothing else. It's about 430 lines of Python with `httpx` and `rich`.

## Installation

```bash
uv tool install git+https://github.com/pcaro/aa-opencode
```

It needs an Artificial Analysis API key, which is free: create an account, generate the key, and put it in the environment.

```bash
export ARTIFICIAL_ANALYSIS_API_KEY="your-key"
```

It also reads `AA_API_KEY`, and if you want to pass it ad hoc there's `--api-key`.

## Usage

```bash
# Default table, sorted by intelligence
aa-opencode

# Other sort keys
aa-opencode --sort price
aa-opencode --sort speed
aa-opencode --sort coding

# JSON to chain into something else
aa-opencode --format json
```

By default it pulls the **Go** catalog. For the **Zen** catalog:

```bash
aa-opencode --catalog zen
```

## What comes out

The Go catalog has 33 models with data in Artificial Analysis. The first thing that jumps out is that the smartest model in the catalog isn't the one I'd use for coding every day. `gemini-4-argon-contributor` leads with a 52.6 index and costs $8.0 per million. `mimo-v2.6-pro` scores 46.3 and costs $0.5. Sixteen times less for 11% less index.

On coding it flips. `mimo-v2.5` scores 60.2 on the coding index at $0.2 per million, and `muse-spark-1.2-contributor` scores 58.6 at $0.1. Those are models I would never have considered opening without seeing those numbers side by side.

Speed: `claude-haiku-5-5` runs at 238.9 tok/s and `deepseek-v4.1-flash` at 216.1. But look at the first one's TTFT: 285.8 seconds. That's not time to first token, it's an artifact of the test (queues, rate limits, whatever happened that day). TTFT from the API has to be read with tongs.

And price. OpenCode's price doesn't come from Artificial Analysis: it comes from [models.dev](https://models.dev/), which is the source OpenCode uses for its catalog. Comparing the two, there are models where OpenCode charges you noticeably less than the public reference: `mimo-v2.5` 68% less, `longcat-2.0` 60% less, `deepseek-v4.1-flash` 50% less.

Zen is a different picture. There the top models run $20 per million (`claude-fable-5-1`, `gpt-6-astra`), and the quality/price ranking fills up with models that don't even show in Go.

Four Go models have no Artificial Analysis data: `omen-alpha`, `hy4-preview`, `longcat-2.5-preview-free`, and `beam-free`. They're previews and free models, so that's expected. In JSON they show up with `matched: false`, and in the human table you list them with `--show-unmatched`.

## How it matches models

OpenCode IDs and Artificial Analysis slugs almost never match, so the matcher tries three things in order:

**Exact slug.** `gpt-5.4` against `gpt-5.4`. Normalizing first: lowercase, dots to dashes, and everything non-alphanumeric stripped.

**Substring.** If one contains the other, it keeps the shortest slug, which is the most specific one. That's where things like `gemini-4-argon-contributor` → `gemini-4-argon` land.

**Token set.** For reordered names, like `haiku-4-5` against `4-5-haiku`.

It's pure heuristics, there's no hand-written equivalence table. It works well enough, but a badly matched model gives you believable, wrong numbers, which is the worst kind of error. When OpenCode adds new models, it's worth eyeballing the row before trusting it.

## What it doesn't do

- It doesn't tell you which model suits you. It just puts the numbers together and sorts them.
- It doesn't check availability: if a model is down, it won't notice.
- It keeps no history. Every run is a snapshot.
- There's no manual equivalence table, so odd matches are possible.

Using the free Artificial Analysis API requires attribution, so: benchmarks come from [Artificial Analysis](https://artificialanalysis.ai/) and OpenCode pricing from [models.dev](https://models.dev/).

*Original source*: [github.com/pcaro/aa-opencode](https://github.com/pcaro/aa-opencode)
