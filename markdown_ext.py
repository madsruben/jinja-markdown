#!/usr/bin/python
import markdown
from markdown.extensions import Extension
from markdown.postprocessors import Postprocessor
import re


class JinjaHtmlPostprocessor(Postprocessor):
    """ Post Processor to remove <p> wrapping around jinja template sections.
    Markdown processing use etree to structure the contents. Each etree is an XML element, and for
    jinja template parameters, <p> is used to wrap {% %} blocks intended for jinja processing.
    This post processor removes the <p> element at the end of Markdown processing.
    """

    def run(self, text: str) -> str:
        """ Search for wrapped jinja and restore original. """

        pattern = r'<p>{%(.*?)%}</p>'
        repl = r'{%\1%}'
        processed_text = re.sub(pattern, repl, text)

        return processed_text


class NoJinjaExtension(Extension):
    def extendMarkdown(self, md):
        md.postprocessors.register(JinjaHtmlPostprocessor(md), 'nojinja', 175)


def gen_markdown(file_path):
    out_path = file_path
    if out_path[-3:] == '.md':
        out_path = out_path[:-3] + '.j2'

        # default output format is xhtml, use html5 instead.
        markdown.markdownFromFile(input=file_path, output=out_path, extensions=[NoJinjaExtension()], output_format='html')

