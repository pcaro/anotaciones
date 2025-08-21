#!/usr/bin/env python3
"""
Generate a simple search index for the blog
"""
import json
import os
import re
from pathlib import Path


def extract_metadata_and_content(rst_file):
    """Extract metadata and content from RST file"""
    with open(rst_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract title (first line usually)
    lines = content.split("\n")
    title = lines[0] if lines else "Untitled"

    # Extract slug from filename
    slug = rst_file.stem

    # Extract text content (remove RST markup)
    text_content = content
    # Remove RST directives
    text_content = re.sub(r"^\.\. .*$", "", text_content, flags=re.MULTILINE)
    # Remove RST headers markup
    text_content = re.sub(r'^[=\-~`#\*\+\^"]+$', "", text_content, flags=re.MULTILINE)
    # Clean up multiple spaces and newlines
    text_content = " ".join(text_content.split())

    return {
        "title": title,
        "url": f"{slug}.html",
        "text": text_content[:500],  # First 500 chars
        "slug": slug,
    }


def main():
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
    output_file = Path("output/search_index.json")
    output_file.parent.mkdir(exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(search_index, f, indent=2, ensure_ascii=False)

    print(f"Generated search index with {len(search_index)} articles")


if __name__ == "__main__":
    main()
