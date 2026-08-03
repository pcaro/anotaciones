Title: ku: Kubernetes desde la terminal como un ninja
Date: 2026-08-03
Tags: kubernetes, herramientas, terminal, tui, k8s
Slug: ku-kubernetes-tui
Lang: es
Featured_image: /images/ku-kubernetes-tui.jpg
Summary: ku es una TUI para Kubernetes rápida, navegable solo con teclado e inspirada en k9s y lazygit. Read-only por defecto, con cockpit de cluster, logs, shell en pods, port-forward y edición de objetos.
Category: Herramientas

![ku TUI](/images/ku-kubernetes-tui.jpg)

He vuelto a trabajar con Kubernetes. Tengo desplegada en local una arquitectura de micrositios — varios namespaces, deployments, servicios, ingresses — y necesitaba una forma rápida de moverme por todo sin estar constantemente tirando de `kubectl get` y `kubectl describe` a mano. La memoria muscular del `kubectl` está bien, pero para navegar un cluster con soltura necesitas ver el panorama completo.

Entré a GitHub y encontré [ku](https://github.com/bjarneo/ku), una TUI para Kubernetes de un desarrollador noruego. Es rápida, va solo con teclado y está claramente inspirada en k9s, Lens y lazygit. Me gustó desde el primer `ku`.

## Instalación

```bash
curl -fsSL https://raw.githubusercontent.com/bjarneo/ku/main/install.sh | sh
```

O con Go:

```bash
go install github.com/bjarneo/ku@latest
```

## Lo que me ha convencido

- **Read-only por defecto**. Arrancas y no puedes romper nada. Para editar, borrar o escalar tienes que activar el modo edición con `Shift+E`. El header muestra un chip verde `● READ-ONLY` o rojo `● EDIT` para que siempre sepas en qué modo estás. Para los que tenemos dedos de mantequilla, esto es paz mental.

- **Cockpit al arrancar**. Una vista general del cluster: versión del server, estado de los nodos, gauges de CPU y memoria en vivo, pods por fase, deployments listos y warnings recientes (deduplicados, con contador de recurrencia). Se refresca solo cada pocos segundos.

- **Tablas con las columnas correctas**. Usa la misma representación `Table` de la API que `kubectl get`, así que las columnas son exactamente las que esperas para cada recurso. Los CRDs también funcionan. Las celdas tienen color semántico: verde sano, amarillo transitorio, rojo roto. La columna ordenada muestra la dirección.

- **Layout lazygit**: panel izquierdo con la navegación de recursos, `Tab` para cambiar entre paneles, barra de estado inferior que muestra solo las teclas relevantes para lo que tienes seleccionado.

- **Resúmenes curados**. `Enter` sobre un objeto abre un resumen específico para ese tipo: los pods muestran uso live, health, requests/limits; los servicios, ingress, configmaps y secrets tienen vistas adaptadas. `d` o `y` abre el YAML completo con syntax highlighting.

- **Logs con follow**. `l` sobre un pod streamea los logs. Puedes filtrar con regex, copiar líneas, cambiar entre instancia actual y anterior, y hacer toggle de auto-scroll. Todo dentro de la TUI.

- **Shell en pods y nodos**. `s` sobre un pod abre una shell interactiva (`bash` o `sh`) en un overlay con terminal virtual. Sobre un nodo, levanta un pod de debug privilegiado con `chroot /host`. `Ctrl+\` detacha.

- **Port-forward de servicios**. `p` sobre un Service y eliges el puerto. Puedes mapear `8080:http` o `18080:80`. Los forwards activos se ven en el header y los gestionas desde la paleta de comandos.

- **Comando `kubectl` equivalente**. `C` te muestra el comando `kubectl` que replica la vista actual. Ideal para aprender o para copiarlo a un script.

- **Documentación de Kubernetes integrada**. `O` abre la doc upstream del recurso seleccionado en el navegador.

- **Sidebar configurable**. Con `ku config init` generas un `~/.config/ku/config.yaml` donde puedes añadir CRDs al menú lateral. Soporta recursos con grupo (`scaledobjects.keda.sh`, `certificates.cert-manager.io`).

- **Modo desarrollador**. `ku --dev` oculta recursos de administración del cluster (nodos, PVs, namespaces, eventos) y desactiva operaciones de nodo. Para cuando solo gestionas tus propias apps.

- **Recuerda contexto y namespace**. Los persiste en `~/.config/ku/state.json` entre sesiones.

## Lo que no tiene (aún)

- No hay vista de gráficos de dependencias ni topología.
- El port-forward es solo para Services, no para pods individuales.
- No tiene integración con Helm.

Es un proyecto joven (~500 estrellas, ~100 commits) pero muy bien pensado. La sensación al usarlo es la de una herramienta que entiende cómo trabajas con Kubernetes y te quita fricción en cada paso. Para mi caso actual — una arquitectura de micrositios con varios namespaces — me permite saltar entre recursos, seguir logs y ver el estado general del cluster sin salir de la terminal.

*Fuente original*: [github.com/bjarneo/ku](https://github.com/bjarneo/ku)
