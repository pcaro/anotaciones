---
title: Bloqueo DNS de enlaces de AliExpress con NextDNS
date: 2026-05-03 10:01
tags: dns, nextdns, aliexpress, bloqueo, linux
lang: es
category: Infraestructura
slug: bloqueo-dns-aliexpress-nextdns
summary: Al usar una blocklist DNS demasiado agresiva en NextDNS, los enlaces de afiliado de AliExpress dejaban de funcionar. Diagnóstico con dig y solución con HaGeZi Multi PRO.
featured_image: /images/dns-blocking-nextdns.jpg
---

![DNS blocking illustration](/images/dns-blocking-nextdns.jpg)

Llevaba unos días con un problema raro: los enlaces de AliExpress que aparecen en descripciones de vídeos de productos no cargaban. Firefox mostraba "Servidor no encontrado". Sabía que tenía pinta de ser un bloqueo DNS, porque al activar la VPN de PIA (Private Internet Access) el problema desaparecía.

## El diagnóstico

El comando `dig` lo confirmó enseguida:

```bash
# Consultando al router (que usa NextDNS)
$ dig s.click.aliexpress.com @192.168.1.1

;; ANSWER SECTION:
s.click.aliexpress.com. 300	IN	A	0.0.0.0
```

```bash
# Consultando a Google DNS
$ dig s.click.aliexpress.com @8.8.8.8

;; ANSWER SECTION:
s.click.aliexpress.com. 300	IN	A	23.40.114.185
```

El router devolvía `0.0.0.0` para `s.click.aliexpress.com`. Eso no es un NXDOMAIN —dominio inexistente—, es un bloqueo deliberado: el dominio resuelve a una IP nula y el navegador no puede conectar.

Con la VPN activa, las consultas DNS pasaban por los servidores de PIA, que no aplican blocklists, y los enlaces funcionaban sin problema.

## La causa

El router tenía configurado **NextDNS** con la lista de bloqueo por defecto. Bloqueaba bien el malware y el phishing, pero también estaba tocando dominios legítimos como los de redirección de afiliados. Demasiado agresiva para mi día a día.

## La solución

La solución más simple habría sido añadir `s.click.aliexpress.com` a la lista blanca de NextDNS y ya está. Pero aproveché para revisar qué lista estaba usando y cambiarla por **HaGeZi - Multi PRO**, que de paso resolvía el problema.

Según la [guía oficial de HaGeZi](https://github.com/hagezi/dns-blocklists/wiki/FAQ#whatshouldiuse):

| Lista    | Nivel de bloqueo     | Falsos positivos            |
| -------- | -------------------- | --------------------------- |
| Light    | Relajado             | Ninguno                     |
| Normal   | Relajado/Equilibrado | Casi ninguno                |
| **Pro**  | **Equilibrado**      | **Muy raros** ← recomendada |
| Pro++    | Equilibrado/Agresivo | Algunos                     |
| Ultimate | Agresivo             | Frecuentes                  |

Multi PRO (~420k dominios, ~200k comprimidos) es la **recomendación personal del autor** de HaGeZi para un bloqueo efectivo sin problemas. Bloquea anuncios, trackers, telemetría, phishing, malware, scam, cryptojacking y "crap", con muy pocos falsos positivos.

## El detalle clave: dominios de referral

La FAQ de HaGeZi dedica una sección entera a explicar que los **dominios de referral** —enlaces de afiliado/tracking como `s.click.aliexpress.com`— están **permitidos en todas las listas**, salvo unos pocos que también funcionan como trackers puros y solo se bloquean en Pro++ y Ultimate.

Estos dominios solo se activan tras un click manual del usuario y no se usan para mostrar publicidad. Bloquearlos rompe enlaces de resultados de búsqueda, ofertas, emails de confirmación, etc.

## Resumen

Una blocklist DNS demasiado agresiva bloquea dominios que no son publicidad ni malware, sino mecanismos de redirección del comercio electrónico. El equilibrio está en **Multi PRO**: buena protección de privacidad sin romper funcionalidad cotidiana.

Si en algún momento necesito más agresividad, el precio será tener que desbloquear falsos positivos manualmente. Por ahora, Multi PRO va perfecto.

_Más información_: [HaGeZi DNS Blocklists](https://github.com/hagezi/dns-blocklists)
