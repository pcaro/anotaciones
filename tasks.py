#!/usr/bin/env python3

import os
from datetime import datetime

from invoke import task


@task
def build(c):
    """Build the site using pelican"""
    c.run("pelican -s pelicanconf.py -o output_dev")


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
    with socketserver.TCPServer(("", port), HTMLHandler) as httpd:
        print(f"Serving on http://localhost:{port}")
        httpd.serve_forever()


@task
def develop(c, port=7000):
    """Build and serve the site for development"""
    build(c)
    print(f"Serving on http://localhost:{port}")
    serve(c, port)


@task
def develop_live(c, port=7000):
    """Develop with live reload and HTML rewriting"""
    from livereload import Server
    import http.server
    import socketserver
    import os
    from urllib.parse import urlparse, unquote

    class HTMLRewriteHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            # Parse the URL
            parsed_path = urlparse(self.path)
            path = unquote(parsed_path.path)

            # If path doesn't end with .html and file doesn't exist, try adding .html
            if not path.endswith(".html") and path != "/":
                file_path = path.lstrip("/")
                if file_path and not os.path.exists(file_path):
                    html_file = file_path + ".html"
                    if os.path.exists(html_file):
                        self.path = "/" + html_file

            return super().do_GET()

    build(c)

    # Create a custom server with HTML rewriting
    class CustomServer(Server):
        def serve(
            self,
            port=5000,
            liveport=35729,
            host="127.0.0.1",
            root=None,
            debug=None,
            open_url=False,
            restart_delay=2,
        ):
            if root:
                os.chdir(root)

            # Set up file watching
            def rebuild():
                c.run("pelican -s pelicanconf.py -o output_dev")

            self.watch("../content/", rebuild)
            self.watch("../pelicanconf.py", rebuild)

            # Flex theme is installed via pip, no need to watch theme files

            # Start the custom HTTP server
            with socketserver.TCPServer(("", port), HTMLRewriteHandler) as httpd:
                print(f"Serving on http://localhost:{port} with live reload")
                httpd.serve_forever()

    server = CustomServer()
    server.serve(port=port, liveport=35729, root="output_dev")


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
