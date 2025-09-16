#!/usr/bin/env python3
import os
from pathlib import Path

def generate_readme():
    current_dir = Path('.')
    files = []

    for item in current_dir.iterdir():
        if item.is_file() and item.name not in ['README.md', 'generate_readme.py']:
            files.append(item.name)

    files.sort()

    readme_content = "# AI Summaries\n\n"
    readme_content += "This directory contains AI-generated summaries and related files.\n\n"
    readme_content += "## Files\n\n"

    for file in files:
        readme_content += f"- [{file}](./{file})\n"

    with open('README.md', 'w') as f:
        f.write(readme_content)

    print(f"Generated README.md with {len(files)} file links")

if __name__ == "__main__":
    generate_readme()