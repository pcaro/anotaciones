#!/usr/bin/env python3

import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

from invoke import task


@task
def build(c):
    """Build the site using pelican"""
    c.run("pelican -s pelicanconf.py -o output_dev")
    # Generate search index
    generate_search_index()


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
                generate_search_index()

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
{'#' * len(title)}

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


def generate_search_index():
    """Generate search index JSON for the blog"""

    def extract_metadata_and_content(rst_file):
        """Extract metadata and content from RST file"""
        with open(rst_file, "r", encoding="utf-8") as f:
            content = f.read()

        lines = content.split("\n")
        title = lines[0] if lines else "Untitled"
        slug = rst_file.stem  # Default fallback

        # Extract metadata and content separately
        content_lines = []
        tags = []
        category = ""
        summary = ""
        in_metadata = False
        header_done = False

        for i, line in enumerate(lines):
            # Skip title and title underline
            if i <= 1:
                continue

            # Check if we're in metadata section
            if line.strip().startswith(":") and ":" in line.strip()[1:]:
                in_metadata = True
                # Extract useful metadata
                if ":tags:" in line:
                    tag_content = line.split(":tags:")[1].strip()
                    tags = [
                        tag.strip() for tag in tag_content.split(",") if tag.strip()
                    ]
                elif ":category:" in line:
                    category = line.split(":category:")[1].strip()
                elif ":summary:" in line:
                    summary = line.split(":summary:")[1].strip()
                elif ":slug:" in line:
                    slug = line.split(":slug:")[1].strip()
                continue
            elif in_metadata and line.strip() == "":
                in_metadata = False
                header_done = True
                continue
            elif in_metadata:
                continue

            # Skip RST directives
            if line.strip().startswith(".. "):
                continue

            # Skip RST header underlines
            if re.match(r'^[=\-~`#\*\+\^"]+$', line.strip()):
                continue

            # Add content lines
            if header_done or not in_metadata:
                content_lines.append(line)

        # Build searchable content
        main_text = " ".join(content_lines)
        main_text = " ".join(main_text.split())  # Normalize whitespace

        # Include summary if exists and is different from main text
        if summary and summary not in main_text:
            main_text = f"{summary} {main_text}"

        # Create searchable text (include tags and category for better search)
        searchable_content = main_text
        if tags:
            searchable_content += " " + " ".join(tags)
        if category:
            searchable_content += f" {category}"

        return {
            "title": title,
            "url": slug,  # Remove .html extension for URLs
            "text": main_text[:400],  # Main content for display
            "searchable": searchable_content[:800],  # Extended content for search
            "tags": tags,
            "category": category,
            "slug": slug,
        }

    content_dir = Path("content/articles")
    search_index = []

    if content_dir.exists():
        for rst_file in content_dir.glob("*.rst"):
            try:
                article_data = extract_metadata_and_content(rst_file)
                search_index.append(article_data)
            except Exception as e:
                print(f"Error processing {rst_file}: {e}")

    # Save to output directory
    output_file = Path("output_dev/search_index.json")
    output_file.parent.mkdir(exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(search_index, f, indent=2, ensure_ascii=False)

    print(f"Generated search index with {len(search_index)} articles")
