Title: OpenCode en el móvil: sesiones remotas con Tailscale y la web como PWA
Date: 2026-10-26 12:00
Category: Herramientas
Tags: opencode, tailscale, pwa, agentes-ia, linux, seguridad
Slug: opencode-sesiones-remotas-tailscale-pwa
Lang: es
featured_image: /images/opencode-sesiones-remotas-tailscale-pwa.png
Summary: OpenCode no tiene app para el móvil, pero no la necesita: el servidor que ya corre en el escritorio sirve su propia web, y esa web se instala como PWA. Así la dejo accesible desde el teléfono con Tailscale, con HTTPS y sin abrir nada a Internet.

Cuando dejo una sesión larga trabajando en el escritorio, lo que quiero es poder mirarla desde el sofá. Y resulta que para eso no hace falta instalar ninguna aplicación: [OpenCode](https://opencode.ai/) ya sirve su propia interfaz web desde el mismo servidor que usa la TUI y la app de escritorio. Solo hay que hacer que el teléfono llegue hasta ese servidor.

Lo he montado con **Tailscale** y la web instalada como **PWA**: sin túneles públicos y sin abrir un solo puerto en el router.

![Móvil con la PWA de OpenCode conectando por Tailscale al servidor local del escritorio](/images/opencode-sesiones-remotas-tailscale-pwa.png)

## Cliente y servidor, eso es todo

Desde la versión 2, OpenCode es cliente/servidor. Hay un servicio en segundo plano que guarda las sesiones, los ficheros, los proveedores y las credenciales, y luego hay clientes que hablan con él: la TUI, la app de escritorio y la web. La app de escritorio, de hecho, [arranca ese mismo servicio cuando la abres](https://pablocaro.es/opencode-desktop-linux).

Eso significa que "sesión remota" no es una función aparte: es conectar otro cliente al servidor que ya tienes corriendo. Puedes verlo con:

```bash
opencode service status
# http://127.0.0.1:49374
```

El puerto por defecto depende de la plataforma: **49374** en macOS, Linux y WSL, y **28894** en Windows (Windows reserva los puertos altos y WSL con red reflejada también toca ese rango). Por defecto escucha **solo en localhost** y pide contraseña, que se genera sola la primera vez.

## Cómo se empareja por defecto

El mecanismo nativo es `opencode pair`. Imprime un enlace de un solo uso y un QR:

```bash
opencode pair

# Open a link to connect. Links work once and expire in 5 minutes.
# http://127.0.0.1:49374/auth/connect/...
```

Abrir ese enlace en un navegador inicia sesión con una cookie y carga la interfaz web. La sesión dura **30 días**, y cambiar la contraseña del servidor las revoca todas. En la app de escritorio lo mismo está en **Settings → Pairing → Pair device**, que muestra el QR para escanear desde otro dispositivo.

Para salir de localhost hay dos caminos, y aquí está la decisión importante:

**El camino oficial: OpenTunnel.** `opencode pair --remote` levanta un túnel cifrado de extremo a extremo hasta un relay público y te da un enlace HTTPS alcanzable desde cualquier sitio. La primera vez avisa de que va a exponer el servidor a Internet y pide confirmación. Sigue haciendo falta la contraseña, pero el servidor pasa a tener una puerta en Internet. Es exactamente lo que hace el botón *Pair device* del escritorio: activa `opencode service set remote true` y construye el QR con la URL pública del túnel (para apagarlo, `opencode service set remote false`).

**El camino propio: tu red privada.** Si ya tienes Tailscale en los dispositivos, el móvil y el escritorio se ven por una IP privada sin exponer nada. Es el que uso.

## Tailscale en lugar de OpenTunnel

La pieza que lo hace cómodo es `tailscale serve`. Mantiene OpenCode escuchando en localhost y deja que Tailscale termine el TLS y publique ese puerto dentro de la tailnet. Antes hay que activar **MagicDNS** y **HTTPS Certificates** en la consola de Tailscale; sin certificados, Serve no puede darte HTTPS.

```bash
tailscale serve --bg 49374
tailscale serve status
# https://maquina.tailxxxx.ts.net
```

Y ahora sí, generas el enlace de emparejamiento con la URL externa, no con localhost:

```bash
opencode pair --url https://maquina.tailxxxx.ts.net
```

Ese enlace ya lleva el host correcto, así que sirve tanto para pegarlo en el móvil como para escanear el QR. El servidor sigue escuchando **solo en `127.0.0.1`**: no hay que tocar `hostname 0.0.0.0` ni abrir puertos en el router. Si quieres quitarlo, `tailscale serve reset`.

Un detalle práctico: como **Pair device** ya está cableado a OpenTunnel, para usar Tailscale hay que pasar por la CLI. Deja *Remote access* apagado en los ajustes y usa `opencode pair --url`, que habla con el mismo servicio en segundo plano.

## Instalarla como PWA

Abres el enlace en el navegador del móvil y lo tienes funcionando. Para que deje de parecer una pestaña, el menú de Chrome ofrece **Instalar app** (o *Añadir a pantalla de inicio*). No es un atajo: la interfaz web trae su `manifest` con `display: standalone`, iconos de 192 y 512, `apple-touch-icon` y un service worker con Workbox que precarga el shell de la aplicación. Al abrirla desde el icono no hay barra de direcciones ni pestañas.

Aquí está el motivo de que HTTPS importe. Instalar una PWA y usar la cámara para escanear el QR son cosas de *secure context*: en `https://maquina.tailxxxx.ts.net` funcionan, y en `http://100.x.y.z:49374` el navegador solo te deja navegar. Hecho así, el móvil tiene icono propio, pantalla completa y cámara para el QR.

El service worker cachea el shell: si te quedas sin cobertura, la app abre aunque no haya servidor. Lo que no hay es magia, las sesiones siguen viviendo en el escritorio, así que sin red verás la interfaz vacía y sin datos.

## Qué se puede hacer desde el móvil

La web es la misma aplicación que el escritorio, no una versión recortada. Desde el teléfono puedo:

- Ver la conversación en tiempo real, con razonamiento, herramientas y diffs por turno.
- **Aprobar o denegar permisos**, que es el 90% de lo que necesito cuando estoy fuera.
- Abrir la terminal integrada, con teclado táctil y las teclas de control a mano.
- Revisar ficheros del proyecto, incluidos PDF y documentos de Office.
- Cambiar de modelo, de agente y de nivel de razonamiento.

Lo que no esperaría de ella:

- **Notificaciones push no hay.** La notificación del navegador solo salta con la página abierta u oculta; si el sistema congela la pestaña, el SSE se corta y no llega nada.
- Escribir prompts largos en el móvil sigue siendo un castigo, por muy bien que funcione el dictado.
- El escritorio tiene que estar encendido y con el servicio vivo. Si lo apagas, no hay sesión que mirar.

## Seguridad en cuatro líneas

- La contraseña del servidor sigue siendo obligatoria; Tailscale protege la red, no la aplicación.
- Limita el acceso en la tailnet con ACL o Grants a `maquina:443` para tus dispositivos.
- **No actives Funnel.** Serve es para tu tailnet; Funnel publica el servicio en Internet y ahí ya estamos como con OpenTunnel, pero sin su cifrado extremo a extremo.
- Si algún día sospechas, cambia la contraseña con `opencode service set password "..."`: todas las sesiones de 30 días caen de golpe.

## Alternativas

Si no quieres montar Serve, `ssh -L` hace lo mismo para un cliente local:

```bash
ssh -L 49374:127.0.0.1:49374 mi-servidor
```

Y dentro de la tailnet, sin certificados, también funciona `opencode service set hostname 0.0.0.0` y entrar por `http://100.x.y.z:49374`. El tráfico va cifrado por WireGuard igualmente, pero al no ser contexto seguro pierdes la instalación como PWA y la cámara. Para un rato vale; para el día a día, Serve es mucho mejor.

## Conclusión

Las sesiones remotas de OpenCode no son un producto aparte, son la consecuencia de que todo sea cliente/servidor: el servidor ya está en el escritorio y lo único que hace falta es un cliente que llegue hasta él. La web que sirve es la app completa, y con Tailscale Serve tienes HTTPS de verdad sin exponer nada. Es la forma más limpia que he encontrado de seguir una sesión desde el móvil sin instalar nada raro.

*Fuente original*: [OpenCode — Web](https://opencode.ai/v2/docs/cli/web), [OpenCode — Commands](https://opencode.ai/v2/docs/cli/commands) y [Tailscale Serve](https://tailscale.com/kb/1242/tailscale-serve).
