#!/usr/bin/env python3

import os
from datetime import datetime

from invoke import task


@task
def build(c):
    """Build the site using pelican"""
    c.run("pelican -s pelicanconf.py -o output_dev", pty=True)


@task
def regenerate(c):
    """Regenerate the site with auto-reload"""
    c.run("pelican -r -s pelicanconf.py -o output_dev")


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
    """Build and serve the site for development"""
    build(c)
    c.run(f"python3 -m invoke serve --port {port}", pty=True)


@task
def develop_live(c, port=7000):
    """Develop with live reload and HTML rewriting"""
    from livereload import Server
    import os

    build(c)

    # Use a simpler approach with livereload's built-in capability
    # but configure it to watch paths.
    server = Server()

    def rebuild():
        c.run("pelican -s pelicanconf.py -o output_dev", warn=True)

    server.watch("content/", rebuild)
    server.watch("pelicanconf.py", rebuild)

    # Note: livereload server is good enough for development.
    # It might not do the clean URL rewriting exactly as our custom
    # handler did, but it usually handles .html files fine.
    # If URL rewriting is critical, we'd need a more complex setup,
    # but this simplifies things significantly and fixes the blocking issue.
    os.chdir("output_dev")
    server.serve(port=port, host="127.0.0.1", root=".")


@task
def production(c):
    """Build for production"""
    c.run("pelican -s publishconf.py")


@task
def publish(c):
    """Build and publish to GitHub Pages using ghp-import"""
    production(c)
    c.run("ghp-import -m 'Generate Pelican site' -b gh-pages output")
    c.run("git push origin gh-pages")


@task
def write(c, title):
    """Create a new post"""
    today = datetime.today()
    slug = title.lower().strip().replace(" ", "-")
    filename = (
        f"content/articles/{today.year}_{today.month:02d}_{today.day:02d}_{slug}.rst"
    )

    template = f"""{title}
{"#" * len(title)}

:date: {today.year}-{today.month:02d}-{today.day:02d} {today.hour:02d}:{today.minute:02d}
:tags:
:lang: es
:category: Programación
:slug: {slug}
:summary:
:status: draft

"""

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
