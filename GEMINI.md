# Project: Anotaciones (Pablo Caro's Blog)

## Project Overview

This is a personal blog project using the [Pelican](https://getpelican.com/) static site generator.

*   **Purpose**: To publish blog posts, primarily on Python and Linux topics, written by Pablo Caro.
*   **Main Technologies**:
    *   **Pelican**: Static site generator (Python-based).
    *   **uv**: Modern Python package manager used for dependency management.
    *   **Invoke**: Python task runner used to automate common development and deployment tasks.
    *   **Flex Theme**: A responsive and feature-rich theme for Pelican.
    *   **GitHub Actions**: CI/CD pipeline for automated building and deployment to GitHub Pages.
*   **Architecture**: Content (reStructuredText/Markdown) is processed by Pelican to generate a static website, which is then deployed to GitHub Pages.

## Building and Running

This project uses `uv` for dependency management and `invoke` for task automation.

### Initial Setup

1.  **Install uv**: If you don't have `uv` installed, follow the instructions on their official website: [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)

2.  **Install Python Dependencies**:
    ```bash
    uv sync
    ```

3.  **Setup Theme and Plugins**:
    The `Flex` theme is configured as a git submodule.
    ```bash
    git submodule update --init --recursive
    ```
    Plugins are managed by cloning the `pelican-plugins` repository into the `plugins` directory.
    ```bash
    git clone https://github.com/getpelican/pelican-plugins.git plugins
    ```
    *(Note: The `pelican-elegant` theme mentioned in the original README.rst is no longer in use; this project uses the `Flex` theme.)*

### Development Commands

All common tasks are automated using `invoke` (defined in `tasks.py`). Note that if you are not in an active virtual environment, you should prepend `uv run` to these commands.

*   **Build the site**:
    ```bash
    uv run pelican content -o output -s pelicanconf.py
    ```

*   **Run a local development server**:
    ```bash
    uv run invoke develop
    ```

*   **Run server on specific port**:
    ```bash
    uv run invoke serve --port 7000
    ```

*   **Stop a running development server**:
    ```bash
    # Using process tool (recommended)
    process --action kill --id my-server

    # Or using lsof/kill manually
    lsof -ti:7000 | xargs kill
    kill $(lsof -ti:7000)
    kill -9 <PID>
    ```

*   **Build for production**:
    ```bash
    uv run pelican content -o output -s pelicanconf.py
    ```
    *(Production uses the same config; `SITEURL` and other settings are already set correctly in `pelicanconf.py`.)*

*   **Create a new post**:
    ```bash
    uv run invoke write "Title of your new post"
    ```
    *(This will create a new Markdown file in `content/articles/` with a pre-filled template.)*

### Background Processes

For long-running processes like development servers, use the `process` tool:

| Action | Description |
|--------|-------------|
| `start` | Start a background process (`--command`, `--name`) |
| `list` | List all managed processes |
| `kill` | Stop a process (`--id`) |
| `output` | View stdout/stderr |

Example:
```bash
# Start a server in background
process --action start --command "uv run invoke serve --port 7000" --name "dev-server"

# Later, stop it
process --action kill --id "dev-server"
```

## Deployment

The site is automatically deployed to [GitHub Pages](https://pages.github.com/) via GitHub Actions whenever changes are pushed to the `master` branch.

**CRITICAL RULE:** NEVER execute `git push` (especially to the `master` branch) without explicit, direct instruction from the user. Pushing to `master` instantly publishes the content to the public blog. The user MUST review all changes locally first. You may `git commit` work to save progress, but DO NOT push.



## Writing Style

**See `estilo_escritura.md` for the complete style guide.**

*   **Content Format**: Blog posts are ALWAYS written in Markdown (`.md`). Older articles may still use reStructuredText (`.rst`), but all new content must be Markdown.
*   **Bilingual Content**: Every new annotation MUST include both a Spanish and an English version (`.md` and `.en.md` respectively). Ensure internal links point to the corresponding language file (e.g., `.en.md` files should link to other `.en.md` files).
*   **Writing Style**: Articles are written in a personal, informal tone, acting as thoughts, notes, or future reminders for the author ("writing for myself"). **CRITICAL:** Do NOT start articles with explicit phrases like "Nota mental:", "Nota para recordar:", or "Otra nota recordatoria:". Just dive straight into the content and keep the tone naturally personal.
*   **Visual Content**: When a link is provided for an article, a screenshot of the website should be taken and saved in `content/images/`. This image MUST be added both inside the article AND as `featured_image: /images/filename.png` in the Markdown metadata so it appears on the homepage.


## Development Conventions

*   **Configuration**:
    *   `pelicanconf.py`: Main Pelican configuration (for both development and production).
    *   `publishconf.py`: (Optional) Overrides `pelicanconf.py` settings specifically for production builds (currently empty as all settings are consolidated in `pelicanconf.py`).
*   **Local Development**: `uv run invoke develop` is recommended for immediate feedback with auto-reload.
*   **Build Verification**: Always run `uv run pelican content -o output -s pelicanconf.py` and verify it works correctly before committing to avoid breaking the automated deployment.
*   **Asset Paths**: Ensure `SITEURL` in `pelicanconf.py` is set correctly to the root domain (`https://pablocaro.es`) and `RELATIVE_URLS = False` for production builds to avoid path issues. Static assets are managed under the `themes/Flex/static/` and `content/images/` directories.
*   **Internal Linking**: Annotations should include links to other related annotations, always linking to the appropriate language version.

## Multi-language Support

The blog supports multi-language content (Spanish and English) using `pelican-i18n-subsites`.

*   **Default Language**: Spanish (`es`).
*   **Secondary Language**: English (`en`).
*   **English Subsite**: Generated at `/en/`.
*   **Translation Workflow**:
    1.  Write the original article in Spanish (default).
    2.  Create a translated version with the same slug but different filename (e.g., `slug.en.rst`).
    3.  Add `:lang: en` metadata to the translated file.
    4.  The plugin will automatically link them and generate the subsite.
*   **Configuration**: managed in `pelicanconf.py` under `I18N_SUBSITES`.

### How It Works

1. **Plugin Integration**: The `pelican-search` plugin is configured in `pelicanconf.py`:
   ```python
   PLUGINS = ['sitemap', 'neighbors', 'related_posts', 'search']
   STORK_VERSION = "1.6.0"
   DIRECT_TEMPLATES = ["index", "tags", "categories", "archives", "search"]
   ```

2. **Automatic Index Generation**: During build, the plugin:
   - Generates `search.toml` with configuration and article list
   - Extracts content from HTML using CSS selector (`html_selector = "main"`)
   - Executes `stork build` to create `search-index.st` (binary search index)
   - Creates `search.html` page for the search interface

3. **Files Generated**:
   - `search.html` - Search page (accessible at `/search.html`)
   - `search-index.st` - Binary search index (~1.3MB for 133 articles)
   - `search.toml` - Stork configuration file
