#!/usr/bin/env python3

import os
from datetime import datetime

from invoke import task


@task
def serve(c, port=7000):
    """Serve the site locally with URL rewriting for .html files"""
    import http.server
    import socketserver
    import os
    import sys
    from urllib.parse import urlparse, unquote

    class HTMLHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            # Parse the URL
            parsed_path = urlparse(self.path)
            path = unquote(parsed_path.path)

            # If path doesn't end with .html and file doesn't exist, try adding .html
            if not path.endswith(".html") and path != "/":
                # Remove leading slash and check if file exists
                file_path = path.lstrip("/")
                if file_path and not os.path.exists(file_path):
                    html_file = file_path + ".html"
                    if os.path.exists(html_file):
                        # Rewrite the path internally
                        self.path = "/" + html_file

            return super().do_GET()

    os.chdir("output_dev")
    # Allow address reuse to avoid "Address already in use" errors after restart
    socketserver.TCPServer.allow_reuse_address = True

    try:
        with socketserver.TCPServer(("", port), HTMLHandler) as httpd:
            sys.stdout.write(f"Serving on http://localhost:{port}\n")
            sys.stdout.flush()
            httpd.serve_forever()
    except KeyboardInterrupt:
        sys.stdout.write("\nStopping server...\n")


@task
def drafts(c):
    """List all draft annotations (Status: draft)"""
    import glob
    import re

    # Get all markdown files in the articles directory
    files = glob.glob("content/articles/*.md")
    if not files:
        print("No articles found.")
        return

    draft_files = []

    for filepath in files:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Check if file has Status: draft in its metadata
        if re.search(r"^Status:\s*draft\s*$", content, re.MULTILINE):
            # Extract title from metadata
            title_match = re.search(r"^Title:\s*(.+)$", content, re.MULTILINE)
            title = title_match.group(1).strip() if title_match else "Unknown"

            # Extract date from metadata
            date_match = re.search(r"^Date:\s*(.+)$", content, re.MULTILINE)
            date = date_match.group(1).strip() if date_match else "Unknown"

            # Extract language (check if it's English version)
            lang_match = re.search(r"^Lang:\s*(.+)$", content, re.MULTILINE)
            lang = lang_match.group(1).strip() if lang_match else "es"

            draft_files.append({
                "filepath": filepath,
                "title": title,
                "date": date,
                "lang": lang
            })

    if not draft_files:
        print("No draft articles found.")
        return

    # Sort by filepath (which includes date in filename)
    draft_files.sort(key=lambda x: x["filepath"], reverse=True)

    # Group by base article (ES and EN versions together)
    grouped = {}
    for draft in draft_files:
        # Extract base name (without .en.md or .md suffix)
        base = draft["filepath"].replace(".en.md", "").replace(".md", "")
        if base not in grouped:
            grouped[base] = {}
        grouped[base][draft["lang"]] = draft

    print(f"\nFound {len(draft_files)} draft article(s) ({len(grouped)} unique):\n")

    for base in sorted(grouped.keys(), reverse=True):
        langs = grouped[base]
        # Use Spanish version for display if available, otherwise English
        article = langs.get("es", langs.get("en"))

        print(f"📝 {article['title']}")
        print(f"   Date: {article['date']}")

        # Show file paths for available languages
        lang_str = " + ".join(sorted(langs.keys()))
        print(f"   Files: {lang_str}")
        for lang, info in sorted(langs.items()):
            print(f"          {info['filepath']}")
        print()


@task
def develop(c, port=7000):
    """Build, serve and auto-reload the site upon file changes"""
    import subprocess
    import sys

    # 1. Initial build
    print("Building site...")
    c.run("uv run pelican -s pelicanconf.py -o output_dev", pty=True)

    # 2. Start pelican auto-reload in background
    print("Starting auto-reloader...")
    pelican_proc = subprocess.Popen(
        ["uv", "run", "pelican", "-r", "-s", "pelicanconf.py", "-o", "output_dev"],
        stdout=sys.stdout,
        stderr=sys.stderr
    )

    # 3. Start local server
    try:
        serve(c, port=port)
    finally:
        print("\nStopping auto-reloader...")
        pelican_proc.terminate()
        pelican_proc.wait()


@task
def write(c, title):
    """Create a new article template in Spanish and English (Markdown)"""
    today = datetime.today()
    slug = title.lower().strip().replace(" ", "-")

    # Spanish version
    filename_es = f"content/articles/{today.year}_{today.month:02d}_{today.day:02d}_{slug}.md"
    template_es = f"""Title: {title}
Date: {today.year}-{today.month:02d}-{today.day:02d} {today.hour:02d}:{today.minute:02d}
Category: Programación
Tags: 
Slug: {slug}
Lang: es
featured_image: /images/
Summary: 
Status: draft

(Escribe aquí directamente el contenido en tono personal, sin empezar con "Nota mental: "...)
"""

    # English version
    filename_en = f"content/articles/{today.year}_{today.month:02d}_{today.day:02d}_{slug}.en.md"
    template_en = f"""Title: {title}
Date: {today.year}-{today.month:02d}-{today.day:02d} {today.hour:02d}:{today.minute:02d}
Category: Programación
Tags: 
Slug: {slug}
Lang: en
featured_image: /images/
Summary: 
Status: draft

(Write the content directly here in a personal tone, without starting with "Mental note: "...)
"""

    for filename, template in [(filename_es, template_es), (filename_en, template_en)]:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(template)
        print(f"File created -> {filename}")


@task
def format_code(c):
    """Format Python code with black"""
    c.run("black .")


@task
def lint(c):
    """Lint code with ruff"""
    c.run("ruff check .")


@task
def edit_latest(c):
    """Open the most recently modified article (both ES and EN versions) in $EDITOR"""
    import glob
    
    # Get all markdown files in the articles directory
    files = glob.glob("content/articles/*.md")
    if not files:
        print("No articles found.")
        return
        
    # Sort files by modification time, newest first
    files.sort(key=os.path.getmtime, reverse=True)
    
    # Get the latest file
    latest_file = files[0]
    
    # Determine the base name without language suffix
    if latest_file.endswith(".en.md"):
        base_name = latest_file[:-6]
    else:
        base_name = latest_file[:-3]
        
    # Construct paths for both versions
    file_es = f"{base_name}.md"
    file_en = f"{base_name}.en.md"
    
    # Check which ones actually exist to pass to the editor
    files_to_edit = []
    if os.path.exists(file_es):
        files_to_edit.append(file_es)
    if os.path.exists(file_en):
        files_to_edit.append(file_en)
        
    if not files_to_edit:
        print("Could not find the article files.")
        return
        
    # Get the preferred editor (default to 'vim' if not set)
    editor = os.environ.get("EDITOR", "vim")
    
    # Run the editor with the files
    print(f"Opening with {editor}: {' and '.join(files_to_edit)}")
    # Use pty=True so interactive editors like vim/nano work properly
    c.run(f"{editor} {' '.join(files_to_edit)}", pty=True)

