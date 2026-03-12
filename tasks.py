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
def develop(c, port=7000):
    """Build, serve and auto-reload the site upon file changes"""
    import subprocess
    import sys
    
    # 1. Initial build to ensure index.html and output_dev exist
    print("Performing initial build...")
    c.run("pelican -s pelicanconf.py -o output_dev", pty=True)
    
    # 2. Start pelican auto-reload in the background
    print("Starting auto-reloader...")
    pelican_proc = subprocess.Popen(
        ["pelican", "-r", "-s", "pelicanconf.py", "-o", "output_dev"],
        stdout=sys.stdout,
        stderr=sys.stderr
    )
    
    # 3. Start the custom local server in the foreground
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

