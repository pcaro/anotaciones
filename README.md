# Anotaciones. Blog de Pablo Caro

These are my blog ([anotaciones](http://pablocaro.es)) contents for [Pelican](http://getpelican.com).

## Getting up and running

The steps below will get you up and running with a local development environment. We assume you have the following installed:

* **uv** ([https://docs.astral.sh/uv/](https://docs.astral.sh/uv/))

First install dependencies using `uv`:

```bash
uv sync
```

Then download theme and plugins:

```bash
git submodule update --init --recursive
git clone https://github.com/getpelican/pelican-plugins.git plugins
```

### Development Commands

Build the site:

```bash
uv run invoke build
```

Develop with local server:

```bash
uv run invoke develop
```

Build for production:

```bash
uv run invoke production
```

### Publishing

The site is automatically deployed to GitHub Pages when you push to the `master` branch using GitHub Actions.

For manual publishing:

```bash
uv run invoke publish
```

### New entries

Create a new post:

```bash
uv run invoke write "título del post"
```

A new file is created with the current date and content like:

```markdown
Title: título del post
Date: 2026-02-26 14:20
Category: Programación
Tags:
Slug: titulo-del-post
Lang: es
Summary:
Status: draft

(Content goes here)
```

*(Note: Although the task script defaults to `.rst`, the project now primarily uses `.md` for new entries.)*

It's time to write entries!!!
