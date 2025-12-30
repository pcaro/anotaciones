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
    The `Flex` theme is located in the `themes/Flex` directory.
    Plugins are managed by cloning the `pelican-plugins` repository into the `plugins` directory.
    ```bash
    git clone https://github.com/getpelican/pelican-plugins.git plugins
    ```
    *(Note: The `pelican-elegant` theme mentioned in the original README.rst is no longer in use; this project uses the `Flex` theme.)*

### Development Commands

All common tasks are automated using `invoke` (defined in `tasks.py`).

*   **Build the site**:
    ```bash
    uv run invoke build
    ```

*   **Run a local development server**:
    ```bash
    uv run invoke develop
    ```

*   **Run a local development server with live reloading (recommended)**:
    ```bash
    uv run invoke develop-live
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

## Development Conventions

*   **Content Format**: Blog posts are written in reStructuredText (`.rst`) or Markdown (`.md`).
*   **Configuration**:
    *   `pelicanconf.py`: Main Pelican configuration (for both development and production).
    *   `publishconf.py`: (Optional) Overrides `pelicanconf.py` settings specifically for production builds (currently empty as all settings are consolidated in `pelicanconf.py`).
*   **Local Development**: `uv run invoke develop-live` is recommended for immediate feedback.
*   **Asset Paths**: Ensure `SITEURL` in `pelicanconf.py` is set correctly to the root domain (`https://pablocaro.es`) and `RELATIVE_URLS = False` for production builds to avoid path issues. Static assets are managed under the `themes/Flex/static/` and `content/images/` directories.

## Troubleshooting

*   **Outdated DNS IP Addresses**: If GitHub Pages reports issues with outdated IP addresses, update your domain's A records to point to GitHub's current IP addresses (e.g., `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`).
*   **Domain Conflicts**: A custom domain can only be assigned to one GitHub Pages repository at a time. If you encounter conflicts, ensure the domain is removed from any other repositories.
*   **HTTPS Enforcement**: After configuring your custom domain and DNS, enable "Enforce HTTPS" in your GitHub Pages settings.
*   **Caching Issues**: Browsers and CDNs can aggressively cache content. If changes are not visible after deployment, clear your browser cache and perform a hard refresh.
