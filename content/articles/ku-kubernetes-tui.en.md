Title: ku: navigate Kubernetes from the terminal like a pro
Date: 2026-08-03
Tags: kubernetes, tools, terminal, tui, k8s
Slug: ku-kubernetes-tui
Lang: en
Featured_image: /images/ku-kubernetes-tui.jpg
Summary: ku is a fast, keyboard-driven Kubernetes TUI inspired by k9s and lazygit. Read-only by default, with a cluster cockpit, logs, pod shells, port-forwarding, and object editing.
Category: Tools

![ku TUI](/images/ku-kubernetes-tui.jpg)

I'm back working with Kubernetes. I have a locally deployed microsite architecture — several namespaces, deployments, services, ingresses — and needed a fast way to navigate everything without constantly running `kubectl get` and `kubectl describe` by hand. `kubectl` muscle memory is fine, but to move through a cluster fluently you need to see the whole picture.

I went to GitHub and found [ku](https://github.com/bjarneo/ku), a Kubernetes TUI by a Norwegian developer. It's fast, keyboard-only, and clearly inspired by k9s, Lens, and lazygit. I liked it from the first `ku`.

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/bjarneo/ku/main/install.sh | sh
```

Or with Go:

```bash
go install github.com/bjarneo/ku@latest
```

## What sold me

- **Read-only by default**. You start up and can't break anything. To edit, delete, or scale you have to enable edit mode with `Shift+E`. The header shows a green `● READ-ONLY` or red `● EDIT` chip so you always know what mode you're in. For those of us with butterfingers, this is peace of mind.

- **Cockpit on launch**. A cluster overview: server version, node status, live CPU and memory gauges, pods by phase, ready deployments, and recent warnings (deduplicated, with recurrence count). Auto-refreshes every few seconds.

- **Tables with the right columns**. Uses the same `Table` API representation as `kubectl get`, so columns are exactly what you expect for every resource. CRDs work too. Cells have semantic coloring: green for healthy, yellow for transient, red for broken. The sorted column shows its direction.

- **lazygit-style layout**: left panel with resource navigation, `Tab` to switch panes, bottom status bar showing only the keys relevant to your current selection.

- **Curated summaries**. `Enter` on an object opens a type-specific summary: pods show live usage, health, requests/limits; services, ingresses, configmaps, and secrets get purpose-built views. `d` or `y` opens the full YAML with syntax highlighting.

- **Logs with follow**. `l` on a pod streams logs. Filter with regex, copy lines, switch between current and previous instance, and toggle auto-scroll. All inside the TUI.

- **Shell into pods and nodes**. `s` on a pod opens an interactive shell (`bash` or `sh`) in an overlay with a virtual terminal. On a node, it spins up a privileged debug pod with `chroot /host`. `Ctrl+\` detaches.

- **Service port-forwarding**. `p` on a Service and pick the port. Map `8080:http` or `18080:80`. Active forwards show in the header and you manage them from the command palette.

- **Equivalent `kubectl` command**. `C` shows the `kubectl` command that replicates the current view. Great for learning or copying to a script.

- **Built-in Kubernetes docs**. `O` opens the upstream docs for the selected resource in your browser.

- **Customizable sidebar**. `ku config init` generates `~/.config/ku/config.yaml` where you can add CRDs to the sidebar. Supports group-qualified resources (`scaledobjects.keda.sh`, `certificates.cert-manager.io`).

- **Developer mode**. `ku --dev` hides cluster admin resources (nodes, PVs, namespaces, events) and disables node operations. For when you only manage your own apps.

- **Remembers context and namespace**. Persists them in `~/.config/ku/state.json` between sessions.

## What's missing (for now)

- No dependency graph or topology view.
- Port-forward is Services only, not individual pods.
- No Helm integration.

It's a young project (~500 stars, ~100 commits) but very well thought out. Using it feels like a tool that understands how you work with Kubernetes and removes friction at every step. For my current setup — a microsite architecture with multiple namespaces — it lets me jump between resources, follow logs, and check cluster health without leaving the terminal.

*Original source*: [github.com/bjarneo/ku](https://github.com/bjarneo/ku)
