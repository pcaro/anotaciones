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
    uv run invoke build
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
    # Find and kill process using port (e.g., 7000)
    lsof -ti:7000 | xargs kill

    # Or manually
    lsof -ti:7000  # Get PID
    kill <PID>     # Kill the process

    # Force kill if needed
    kill -9 <PID>
    ```

*   **Build for production**:
    ```bash
    uv run invoke production
    ```

*   **Create a new post**:
    ```bash
    uv run invoke write "Title of your new post"
    ```
    *(This will create a new reStructuredText file in `content/articles/` with a pre-filled template.)*

## Deployment

The site is automatically deployed to [GitHub Pages](https://pages.github.com/) via GitHub Actions whenever changes are pushed to the `master` branch.

*   **Workflow File**: `.github/workflows/deploy.yml`
*   **Deployment Method**: The workflow builds the site and pushes the output to a `gh-pages` branch. GitHub Pages is configured to serve content from this `gh-pages` branch.

### CI/CD Pipeline Steps

1. **Checkout**: Clone repository with submodules
2. **Setup**: Install `uv` and Python dependencies
3. **Install Pelican plugins**: Clone pelican-plugins if not present
4. **Install Stork**: Download Stork v1.6.0 binary for search indexing
5. **Build**: Run Pelican with production config
6. **Deploy**: Push output to `gh-pages` branch

**Important**: Stork CLI must be installed in CI environment for the search plugin to work. The workflow downloads the binary from `https://files.stork-search.net/releases/v1.6.0/stork-ubuntu-20-04`.

## Development Conventions

*   **Content Format**: Blog posts are written in reStructuredText (`.rst`) or Markdown (`.md`).
*   **Configuration**:
    *   `pelicanconf.py`: Main Pelican configuration (for both development and production).
    *   `publishconf.py`: (Optional) Overrides `pelicanconf.py` settings specifically for production builds (currently empty as all settings are consolidated in `pelicanconf.py`).
*   **Local Development**: `uv run invoke develop` is recommended for immediate feedback.
*   **Build Verification**: Always run a local build and verify it works correctly before committing to avoid breaking the automated deployment.
*   **Asset Paths**: Ensure `SITEURL` in `pelicanconf.py` is set correctly to the root domain (`https://pablocaro.es`) and `RELATIVE_URLS = False` for production builds to avoid path issues. Static assets are managed under the `themes/Flex/static/` and `content/images/` directories.

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

### Requirements

- **Stork CLI**: Must be installed and available on `$PATH`
  - Check installation: `which stork`
  - Current location: `/usr/local/bin/stork`
  - Install: https://stork-search.net/docs/install
  - **Note for Ubuntu 22.04+**: Stork v1.6.0 depends on `libssl1.1`. If missing, download it from [ubuntu security](http://security.ubuntu.com/ubuntu/pool/main/o/openssl/) and place `libssl.so.1.1` and `libcrypto.so.1.1` in `~/.local/lib`, then wrap the stork binary to set `LD_LIBRARY_PATH`.

### Theme Template

The Flex theme required a custom `search.html` template to support Stork. The template is located at:
- `themes/Flex/templates/search.html`

The template detects which search plugin is active (`pelican-search` or `tipue_search`) and renders the appropriate interface. For Stork, it includes:
- Stork CSS from CDN (`basic.css`)
- Search input field with `data-stork="sitesearch"` attribute
- Output container with `data-stork="sitesearch-output"` attribute
- Stork JavaScript library from CDN
- Registration of the search index: `stork.register("sitesearch", "/search-index.st")`

### Migration Note

The blog previously used custom `generate_search_index()` code that:
- Manually parsed RST files with regex
- Generated simple JSON index (`search_index.json`)
- Required manual calls in `build()` task

**This code has been removed** in favor of `pelican-search` because:
- ✅ Automatic integration with Pelican
- ✅ More robust (extracts from HTML, not source files)
- ✅ Better performance (Stork's binary index and WASM search)
- ✅ Community maintained

### Testing Search Functionality

#### 1. Launch Development Server
```bash
# Build the site first
uv run invoke build

# Launch the development server
uv run invoke serve --port 7000
# Server runs on http://localhost:7000
```

#### 2. Test in Browser
- Navigate to: `http://localhost:7000/search.html`
- Enter a search query (e.g., "python")
- Results should appear instantly with highlighted excerpts

#### 3. Test via CLI (for debugging)
```bash
# Search the index directly with Stork CLI
stork search --index output_dev/search-index.st --query "python"

# Count results
stork search --index output_dev/search-index.st --query "python" | jq '.results | length'

# Show result titles
stork search --index output_dev/search-index.st --query "python" | \
  jq -r '.results[] | "- \(.entry.title) (\(.entry.url))"'
```

#### 4. Verify Files
```bash
# Check search index exists and size
ls -lh output_dev/search-index.st

# Verify search index is accessible via HTTP
curl -I http://localhost:7000/search-index.st

# Check search page content
curl -s http://localhost:7000/search.html | grep "stork"
```

**Example Results**: A search for "python" returns 10 articles including:
- "HTTPX: Cliente HTTP moderno para Python"
- "Reduce el Ruido en tus Logs de Python"
- "Pandas Styler: Mejora la presentación de tus DataFrames"

## Troubleshooting

*   **Outdated DNS IP Addresses**: If GitHub Pages reports issues with outdated IP addresses, update your domain's A records to point to GitHub's current IP addresses (e.g., `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`).
*   **Domain Conflicts**: A custom domain can only be assigned to one GitHub Pages repository at a time. If you encounter conflicts, ensure the domain is removed from any other repositories.
*   **HTTPS Enforcement**: After configuring your custom domain and DNS, enable "Enforce HTTPS" in your GitHub Pages settings.
*   **Caching Issues**: Browsers and CDNs can aggressively cache content. If changes are not visible after deployment, clear your browser cache and perform a hard refresh.
*   **Search Not Working**: If search fails to build, verify that Stork is installed (`which stork`). The search plugin will raise an exception if Stork is not found on `$PATH`.
