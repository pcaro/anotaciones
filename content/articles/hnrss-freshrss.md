Title: hnrss: feeds RSS a medida para Hacker News
Date: 2026-09-28
Tags: rss, hackernews, freshrss, nas, self-hosted, feeds
Slug: hnrss-freshrss
Lang: es
Featured_image: /images/hnrss-freshrss.png
Summary: hnrss.org genera feeds RSS, Atom y JSON personalizados de Hacker News. Lo uso para seguir solo lo que me interesa desde mi FreshRSS autoalojado en el NAS.
Category: Herramientas

![hnrss y FreshRSS en el NAS](/images/hnrss-freshrss.png)

[Hacker News](https://news.ycombinator.com/) no tiene RSS. O mejor dicho, no tiene los RSS que a mí me gustaría: un feed único de portada, sin filtros ni búsquedas. Por suerte existe [hnrss.org](https://hnrss.github.io/), que genera feeds RSS personalizados en tiempo real a partir de la web y de la API de búsqueda de Algolia.

## Qué es hnrss.org

Es un servicio (con [código abierto](https://github.com/hnrss/hnrss)) que expone decenas de endpoints. Tú construyes la URL según lo que quieras seguir y obtienes un RSS válido por HTTPS. Los tipos de feed principales:

**Firehose**: todo lo nuevo, posts y comentarios.

```text
https://hnrss.org/newest
https://hnrss.org/newcomments
https://hnrss.org/frontpage
```

**Búsquedas**: posts o comentarios que contengan una palabra clave.

```text
https://hnrss.org/newest?q=rust
https://hnrss.org/newcomments?q=kubernetes
```

Puedes combinar términos con `OR` y percent-encodear caracteres reservados (por ejemplo `C%2B%2B`).

**Respuestas**: comentarios que responden a un usuario o a un comentario concreto.

```text
https://hnrss.org/replies?id=USERNAME
https://hnrss.org/replies?id=17752464
```

**Puntos y actividad**: solo lo que supera un umbral.

```text
https://hnrss.org/newest?points=300
https://hnrss.org/newest?comments=250
```

**Self-posts**: Ask HN, Show HN y encuestas.

```text
https://hnrss.org/ask
https://hnrss.org/show
https://hnrss.org/polls
```

**Jobs**: ofertas de startups de YC y los hilos mensuales de "Who is hiring?".

**Usuarios**: lo que publica o comenta alguien concreto.

Además de RSS, cualquier endpoint acepta `.atom` o `.jsonfeed` al final:

```text
https://hnrss.org/frontpage.atom
https://hnrss.org/ask.jsonfeed?comments=10
```

## Parámetros que uso

Los que más rentabilizo:

- `points=N` y `comments=N` para filtrar el ruido del firehose. Es la forma más rápida de bajarle el volumen a `newest`.
- `q=...` para vigilancia de temas concretos sin abrir el navegador.
- `count=N` para traer más de los 20 items por defecto (tope de 100).
- `link=comments` para que el enlace del item apunte al hilo de HN en vez de al artículo original.
- `description=0` si solo quieres los enlaces, sin descripción.

```text
https://hnrss.org/newest?q=linux&points=100&count=50
```

## Cómo lo uso en mi FreshRSS del NAS

Tengo [FreshRSS](https://freshrss.org/) corriendo en Docker en el NAS, que es mi lector de feeds central. Añadir un feed de hnrss es como cualquier otro: en la interfaz web, **Suscripción → Añadir un feed**, pegas la URL y listo.

Lo que tengo montado:

- La portada (`/frontpage`) para el pulso diario.
- Un par de búsquedas por tema (`?q=python`, `?q=postgres`) con `points` mínimo, que es donde de verdad merece la pena ahorrar tiempo.
- Los hilos de "Who is hiring?" filtrados con `q=` cuando me interesa mirar el mercado.

Como FreshRSS hace fetch de forma programada, conviene ajustar la frecuencia. La documentación de hnrss pide ser especialmente conservador con los endpoints que raspan HN (por ejemplo `/favorites`), así que ahí mejor un intervalo largo. Para el resto, con actualizaciones cada 30-60 minutos sobra: HN tampoco va a irse a ningún lado en ese rato.

La ventaja de tenerlo todo en FreshRSS es obvia: un único sitio donde leo, marco y busco, con mis reglas de filtrado, y sin depender de la portada de HN ni de su ranking.

*Fuente original*: [Hacker News RSS](https://hnrss.github.io/)
