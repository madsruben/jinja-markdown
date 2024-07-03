# jinja-markdown

Script to convert jinja including markdown pages into html.

1. Traverses pages/ directory and looks for files
2. If file is a .md markdown file, convert it to a jinja .j2 file
3. Template the .j2 file into a .html file, output into generated/
4. If subdirectories are found in pages/, recurse through them and process any .j2 and .md files inside

# Usage

    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ python generate.py

# Expected directory structure

- /
  - generate.py - main script
  - markdown_ext.py - markdown converter
  - html/
    - templates/ - templates from which the jinja pages are derived from
    - pages/ - jinja2 (.j2) and markdown (.md) pages
      - (custom folder structure, will be replicated in generated/)
    - generated/ - generated files


