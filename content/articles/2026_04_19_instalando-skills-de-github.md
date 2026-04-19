Title: Instalando skills de GitHub
Date: 2026-04-19 12:00
Category: Programación
Tags: GitHub, CLI, Agentes IA, Skills
Slug: instalando-skills-de-github
Lang: es
featured_image: /images/gh-skill-vs-npx-skills.jpg
Summary: Comparando `gh skill` vs `npx skills` para instalar y gestionar skills de agentes de IA.
Status: published

Dos formas principales de instalar skills para agentes de IA (Claude Code, Codex, Cursor, etc.): el nuevo subcomando `gh skill` de GitHub CLI y la herramienta `npx skills` de Vercel Labs.

## `gh skill` — el enfoque oficial de GitHub

GitHub CLI ahora tiene un subcomando nativo para gestionar skills:

```bash
# Buscar skills
gh skill search terraform

# Instalar un skill específico
gh skill install github/awesome-copilot documentation-writer

# Previsualizar antes de instalar
gh skill preview github/awesome-copilot documentation-writer

# Actualizar todos los skills instalados
gh skill update --all

# Validar skills antes de publicar
gh skill publish --dry-run
```

**Cómo instala**: `gh skill` **copia** los archivos (no usa symlinks) e inyecta metadata de tracking directamente en el frontmatter del `SKILL.md` (repositorio, ref, tree SHA). Esta metadata permite que `gh skill update` detecte cambios reales de contenido comparando el tree SHA local vs el remoto.

**Dónde instala**: Por defecto en **scope de proyecto** (dentro del repositorio git actual), pero puedes usar `--scope user` para instalar en tu home directory y que esté disponible globalmente. Los directorios por agente son:

| Agente | Proyecto | Usuario |
|--------|----------|---------|
| GitHub Copilot | `.agents/skills` | `~/.copilot/skills` |
| Claude Code | `.claude/skills` | `~/.claude/skills` |
| Cursor | `.agents/skills` | `~/.cursor/skills` |
| Codex | `.agents/skills` | `~/.codex/skills` |
| Gemini CLI | `.agents/skills` | `~/.gemini/skills` |
| Antigravity | `.agents/skills` | `~/.gemini/antigravity/skills` |

Nota: GitHub Copilot, Cursor, Codex, Gemini CLI, Antigravity y Pi comparten `.agents/skills` a nivel de proyecto.

Lo interesante es que está integrado directamente en `gh`, así que si ya usas GitHub CLI para todo, no necesitas otra dependencia más. Pero la búsqueda es bastante básica y limitada al ecosistema de GitHub.

## `npx skills` — la herramienta de Vercel Labs

Llevo tiempo usando [`npx skills`](https://github.com/vercel-labs/skills) de Vercel Labs y me parece más completa para el día a día:

```bash
# Listar skills disponibles en un repo
npx skills add github/awesome-copilot --list

# Instalar un skill específico
npx skills add github/awesome-copilot --skill publish-to-pages

# Instalar todos los skills de un repo
npx skills add vercel-labs/agent-skills --all

# Actualizar skills
npx skills update

# Buscar skills de forma interactiva
npx skills find
```

Ventajas que le veo:

- **Soporte multi-agente**: Funciona con Pi, Claude Code, Codex, Cursor, OpenCode, Gemini CLI, y más de 40 agentes. Cada uno tiene su directorio de skills y `npx skills` los gestiona todos.
- **Instalación flexible**: Puedes instalar skills de forma global (`-g`) o por proyecto, y elegir entre symlink (recomendado para actualizar fácil) o copiar archivos.
- **Búsqueda interactiva**: El comando `npx skills find` te da una interfaz tipo `fzf` para explorar skills disponibles.
- **Actualizaciones más granulares**: Puedes actualizar skills individuales o todos, y elegir si son los globales o los del proyecto.

El punto débil es que la búsqueda no funciona del todo bien cuando un repo tiene múltiples skills — a veces no los encuentra todos o no los lista como esperas.

Pero donde `npx skills` realmente brilla es con `npx skills find` — una interfaz interactiva tipo `fzf` para explorar y buscar skills disponibles. Es muchísimo mejor que la búsqueda básica de `gh skill`:

![npx skills find](/images/npx-skills-find.png)

Puedes buscar por palabra clave, navegar interactivamente por los resultados, ver el número de instalaciones y lanzar el comando de instalación directamente. Para descubrir nuevas skills, esta es la mejor opción sin duda.

## Comparativa técnica

| Característica | `gh skill` | `npx skills` |
|----------------|------------|--------------|
| Método de instalación | Copia archivos | Symlink (recomendado) o copia |
| Scope por defecto | Proyecto | Proyecto |
| Scope global | `--scope user` | `-g` / `--global` |
| Tracking de versión | Tree SHA en frontmatter | Metadata similar |
| Update | Compara tree SHA local vs remoto | Git pull en el repo |
| Agentes soportados | 6 (Copilot, Claude, Cursor, Codex, Gemini, Antigravity) | 40+ |
| Búsqueda interactiva | No (`gh skill search` es básico) | Sí (`npx skills find` con fzf) |
| Integración | Nativo en gh CLI | Herramienta independiente |

## `skills-lock.json` — el archivo de lock de `npx skills`

`npx skills` mantiene un archivo de lock global en `~/.agents/.skill-lock.json` (formato v3) que registra:

- Todos los skills instalados globalmente
- Su origen (repo, URL, tipo de fuente)
- Hash de la carpeta para detectar cambios
- Fechas de instalación y última actualización
- Preferencias del usuario (agentes seleccionados)

Actualmente funciona como **registro** para que `npx skills update` sepa qué verificar, pero **no como manifiesto declarativo** — no hay un comando `npx skills install` que restaure skills desde cero leyendo el lock (como haría `npm ci`). Es decir, si borras tus skills instalados, el lock file solo sirve como referencia, no para restaurar automáticamente.

## Mi flujo actual

Para instalar skills nuevos:

```bash
# Ver qué skills tiene un repo
npx skills add github/awesome-copilot --list

# Instalar solo los que me interesan
npx skills add github/awesome-copilot --skill publish-to-pages --skill documentation-writer
```

Y para mantenerlos actualizados:

```bash
npx skills update
```

En resumen: me quedo con `npx skills` de Vercel sin duda. GitHub CLI está bien si solo usas Copilot y quieres todo integrado en `gh`, pero si trabajas con múltiples agentes (como yo, que uso Pi como principal), `npx skills` es muy superior por su soporte multi-agente, flexibilidad y sobre todo por `npx skills find` para descubrir nuevas skills.

## Enlaces

- [`gh skill` documentation](https://cli.github.com/manual/gh_skill)
- [`npx skills` repo](https://github.com/vercel-labs/skills)
- [Skills directory](https://skills.sh)
