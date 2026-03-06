Title: De net-tools a iproute2: equivalents de comandos
Date: 2026-03-06 11:30
Tags: linux, networking, iproute2, net-tools, terminal
Category: Linux
Slug: net-tools-to-iproute
Summary: Guía de equivalencias entre los comandos clásicos de net-tools (ifconfig, route, arp) y los modernos de iproute2 (ip).
Lang: es

Más de 30 años con Linux, y es difícil cambiar a lo que ya estás acostumbrado. En mi caso, siempre he usado **ifconfig**, **arp**, **route** y **netstat** para configurar y diagnosticar la red. Pero estos comandos pertenecen al paquete **net-tools**, que lleva años siendo reemplazado por **iproute2**.

## net-tools vs iproute2

Tradicionalmente ha habido dos formas de configurar la red en Linux:

- **La forma antigua**: con comandos como `ifconfig`, `arp`, `route` y `netstat`, que pertenecen al paquete *net-tools*
- **La forma nueva**: mayormente (¡pero no enteramente!) encapsulada en un único comando `ip`, que pertenece al paquete *iproute2*

Parece que iproute2 fue marcado como "important" en Debian en 2008, lo que significa que cada lanzamiento desde Debian 5 "lenny" (!) ha incluido el comando `ip`.

He estado entrenando lentamente a mi cerebro para usar los nuevos comandos, pero a veces olvido algunos. Aquí tienes una tabla de equivalencias:

| net-tools | iproute2 | Forma corta | Función |
|-----------|----------|-------------|---------|
| `ifconfig` | `ip address` | `ip a` | Mostrar/configurar direcciones IP |
| `ifconfig -s` | `ip link` | `ip l` | Mostrar estado de enlaces (up/down, contadores) |
| `route` | `ip route` | `ip r` | Mostrar o modificar la tabla de rutas |
| `arp` | `ip neigh` | `ip n` | Mostrar tabla ARP/vecinos |
| `netstat` | `ss` | `ss` | Mostrar estadísticas de sockets |

## Comparación visual

Aquí puedes ver la diferencia entre usar `ip a` y `ip -br -c a`:

### `ip a` (salida completa)

![ip a output](/images/net-tools-ip-a.png)

### `ip -br -c a` (salida resumida y coloreada)

![ip -br -c a output](/images/net-tools-ip-br.png)

## Mi alias favorito

También suelo crear un alias para que la salida sea más legible:

```bash
alias ip='ip -br -c'
```

Esto proporciona una salida mucho más bonita y legible, como puedes ver en la segunda imagen.

¿Tú sigues usando los comandos antiguos o ya te has pasado a iproute2?
