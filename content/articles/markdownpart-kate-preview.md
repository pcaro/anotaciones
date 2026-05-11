Title: Markdown preview en Kate Editor con markdownpart
Date: 2026-05-11
Tags: kate, markdown, linux, kde, editor
Slug: markdownpart-kate-preview
Lang: es
Featured_image: /images/markdownpart-kate-preview.png
Summary: Cómo activar la vista previa de Markdown en Kate usando markdownpart.
Category: Linux

Resulta que KDE tiene un componente llamado `markdownpart` que permite hacer preview de Markdown en tiempo real dentro de Kate.

```bash
sudo apt install markdownpart
```

Una vez instalado, en Kate:

1. **Preferencias → Configurar Kate → Complementos**
2. Activar **Vista previa del documento** (o similar según la versión)

Aparecerá un botón en la barra lateral con un icono de un documento con una lupa. Al hacer clic, se abre un panel con el Markdown renderizado. Y lo mejor: tiene opciones de actualizar en vivo mientras escribes.

![Markdown preview en Kate](/images/markdownpart-kate-preview.png)
