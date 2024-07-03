#!/usr/bin/python
from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
from markdown_ext import gen_markdown

# structure:
#
# generate.py
# markdown_ext
# html/
#   pages/ -> jinja / markdown files to be generated as html
#   templates/ -> jinja templates that pages are deriving from
#   generated/ -> auto-generated folder, based on structure in pages/
#
# usage: venv/bin/python generate.py

templates_dir = 'html'
pages_dir = 'pages'
output_dir = 'generated'


env = Environment(
    loader=FileSystemLoader(templates_dir),
    autoescape=select_autoescape()
)

# here we can also generate a global dict variable, ie list of posts, to be converted to html and/or shown in a nav bar.


def gen_templates(dir):
    print(f'generating templates in dir: {templates_dir}/{pages_dir}/{dir}')
    template = None
    template_path = None
    output_path = None

    for f in os.scandir(os.path.join(templates_dir, pages_dir, dir)):
        if dir == '.': # special handling of the first directory during recursive processing.
            template_path = os.path.join(pages_dir, f.name)
            output_path = os.path.join(templates_dir, output_dir, f.name.replace(".j2", ".html"))

        else:
            template_path = os.path.join(pages_dir, dir, f.name)
            output_path = os.path.join(templates_dir, output_dir, dir, f.name.replace(".j2", ".html"))

        print(f'template_path: {template_path}, output_path: {output_path}')

        if f.is_file():
            # first generate .j2 file from markdown, if required
            if template_path[-3:] == '.md':
                print(f'generating jinja from markdown {template_path}')
                gen_markdown(os.path.join(templates_dir, template_path))
                template_path = template_path[:-3] + '.j2'
                output_path = output_path[:-3] + '.html'

            # if file is a jinja template, generate it.
            if template_path[-3:] == '.j2':
                template = env.get_template(template_path)
                template.stream().dump(output_path)

            else:
                # non-jinja files are skipped. if you want to still copy other files,
                # like static/ files for css, images, etc, do it here.
                print(f'skipping non-jinja file {template_path}')

        elif f.is_dir():
            # create directory structure if it doesn't exist
            dir_path = os.path.join(templates_dir, output_dir, dir, f.name)
            if not os.path.isdir(dir_path):
                os.mkdir(dir_path)

            # recursive; generate templates from this subfolder.
            next_level = f.name if dir == '.' else os.path.join(dir, f.name)
            gen_templates(next_level)


if __name__ == '__main__':
    # generate html from .j2 files. create subdirectories if they don't exist.
    gen_templates('.')

