Title: Markdown Preview in Kate Editor with markdownpart
Date: 2026-05-11
Tags: kate, markdown, linux, kde, editor
Slug: markdownpart-kate-preview
Lang: en
Featured_image: /images/markdownpart-kate-preview.png
Summary: How to enable live Markdown preview in Kate using markdownpart.
Category: Linux

Turns out KDE has a component called `markdownpart` that provides live Markdown preview inside Kate.

```bash
sudo apt install markdownpart
```

Once installed, in Kate:

1. **Preferences → Configure Kate → Plugins**
2. Enable **Document Preview** (or similar, depending on version)

A button will appear in the sidebar with a document-with-magnifying-glass icon. Click it to open a rendered Markdown panel. Best part: it has options to update live as you type.

![Markdown preview in Kate](/images/markdownpart-kate-preview.png)
