Title: Probando Aurora: mi primer vistazo al futuro del escritorio Linux
Date: 2026-04-24 09:51
Category: Linux
Tags: aurora, linux, kde, escritorio, devcontainers, homebrew
Slug: probando-aurora-mi-primer-vistazo-al-futuro-del-escritorio-linux
Lang: es
featured_image: /images/aurora-desktop-2026-04-24.png
Summary: Aurora: Image-based, actualizaciones atómicas, devcontainers, homebrew y toda la experiencia DX que estoy probando en una VM.

Siempre he sido de KDE. Con distros Suse o Debian. Desde hace unos años mi escritorio principal es KDE Neon.

Pero últimamente he estado siguiendo el proyecto [Aurora](https://getaurora.dev/en/) y decidí darle una oportunidad en una máquina virtual. 
Y tengo que decirlo: tiene muy buena pinta.

## ¿Qué es Aurora?

Aurora es una distribución Linux basada en Fedora que está replanteando cómo debería funcionar un escritorio moderno. No es solo "otra distro con KDE" — es un cambio de paradigma completo.

Lo primero que llama la atención es que usa un **modelo image-based**. En lugar de actualizar paquetes individuales con `dnf` o `apt`, el sistema operativo completo se actualiza como una imagen atómica. Esto significa:

- **Actualizaciones en segundo plano** que se aplican al reiniciar
- **Rollback instantáneo** si algo sale mal (puedes arrancar en la versión anterior desde el grub)
- **Sistema inmutable** que es mucho más difícil de romper

Para alguien que viene de un sistema tradicional, con muchos años a sus espaldas, esto es un gran gran cambio.

## KDE, pero diferente

Aurora usa KDE Plasma, pero no es el KDE simple original que se solía encontrar en Fedora (nunca fue la mejor distro para este gui).
Está cuidadosamente personalizado para ofrecer una experiencia "out of the box" que simplemente funciona. No hay que configurar nada, no hay que instalar tweaks ni ajustes raros.

Y aun así, mantiene la esencia de KDE: es flexible, es potente, y se siente familiar desde el primer momento.

## Aurora DX: el verdadero atractivo

Pero donde Aurora realmente brilla es en la **Developer Experience (DX)**. Llevo días trasteando con esto y cada vez que descubro algo nuevo, parace una buena decisión.
Eso sí, he de tener en cuenta que tengo mucho linux a mis espaldas y es difícil cambiar viejas costumbres.

### Devcontainers por defecto

El IDE preinstalado es Visual Studio Code con la extensión de **DevContainers** ya configurada. Todo el desarrollo ocurre dentro de contenedores, no en el host. Esto significa:

- Tu sistema operativo no se ensucia con dependencias de proyectos
- Cada proyecto puede tener su propio entorno aislado
- Puedes descartar y recrear entornos en segundos

### Homebrew integrado

Aurora incluye **Homebrew** preinstalado y configurado para no tocar el sistema base. Quieres una herramienta CLI nueva? `brew install`. Listo. Sin conflictos con los paquetes del sistema, sin necesidad de sudo, sin romper nada. Ya sabéis que me gusta mantener algunas tools pequeñas muy actualizadas y usar gah para instalar.

Tienen incluso un `ujust bbrew` que te da un menú interactivo para instalar categorías enteras de herramientas: fonts, k8s-tools, ai, cncf...

### ujust: comandos que simplifican la vida

`ujust` es como un alias con superpoderes. Comandos como:

```bash
ujust devmode        # Activa el modo desarrollador
ujust dx-group       # Te añade a los grupos necesarios
ujust jetbrains-toolbox  # Instala JetBrains Toolbox
ujust cncf           # Navega e instala herramientas CNCF
```

Cada comando te guía paso a paso. Es como tener un asistente que sabe exactamente qué necesitas.

### Tailscale y herramientas cloud-native

Tailscale viene preconfigurado para VPN. Cockpit para gestión del sistema. Herramientas de profiling como `sysprof`, `bcc`, `bpftrace`. Todo lo que necesitarías para desarrollo cloud-native está ahí, listo para usar.

### Terminal con soporte de contenedores

El terminal por defecto es **Ptyxis**, que tiene integración nativa con Distrobox. Puedes tener contenedores "pet" interactivos y cambiar entre ellos y el host con un atajo. Es muy cómodo.

## Las grandes diferencias

En Aurora, el sistema se cuida solo:

1. **No puedes romperlo fácilmente** — el sistema base es inmutable
2. **Las actualizaciones son atómicas** — o funcionan completas, o no se aplican
3. **Todo está en contenedores** — tus herramientas, tus entornos, tus dependencias
4. **Si algo falla, hay rollback** — arrancas la versión anterior y listo

Es como la diferencia entre cuidar un jardín y vivir en un hotel. En un hotel, todo simplemente funciona.

## ¿Dejaré KDE Neon?

No lo sé aún. Llevo años en KDE Neon y tengo mi flujo de trabajo montado. Pero Aurora me está haciendo replantear cosas.

Lo que más me tira:

- **El DX** es simplemente superior para desarrollo moderno
- **Las actualizaciones automáticas** sin tener que estar pendiente
- **La filosofía** de "todo en contenedores" tiene mucho sentido

Lo que me da miedo:

- **La inmutabilidad** — al principio se siente restrictivo
- **El cambio de mentalidad** — dejar de tener control total
- **¿Y si necesito algo específico? (que me a ocurrir seguro)** — aunque con homebrew y contenedores, probablemente no sea mucho


---

**Enlaces:**

- [Aurora Website](https://getaurora.dev/en/)
- [Aurora DX Documentation](https://docs.getaurora.dev/dx/aurora-dx-intro/)
- [Universal Blue (el proyecto detrás)](https://universal-blue.org)
