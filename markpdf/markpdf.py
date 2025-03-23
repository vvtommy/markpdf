import os
from pathlib import Path
import time
from typing import Union

from playwright.sync_api import sync_playwright
from mdit_py_plugins.anchors import anchors_plugin

from markdown_it import MarkdownIt
from weasyprint import HTML

from markpdf.template import render_html


class MarkPDF:
    def __init__(self, output_html: bool = False):
        self._output_html = output_html
        self._md = MarkdownIt("commonmark").enable("table").enable(
            "strikethrough").use(anchors_plugin)
        self._playwright = sync_playwright().start()
        self._browser = self._playwright.chromium.launch(
            headless=True, channel="chrome")

    def _open_markdown(self, markdown: Union[str, Path]) -> str:
        if isinstance(markdown, Path):
            with open(markdown, "r") as f:
                return f.read()
        return markdown

    def render(self, markdown: Union[str, Path], output: Union[str, Path]) -> str:
        with self._browser as browser:
            page = browser.new_page()
            page.set_content(render_html(self._open_markdown(markdown)))
            page.wait_for_timeout(1)

            rendered_html = page.content()
            HTML(string=rendered_html).write_pdf(output)
            if self._output_html:
                with open(output.with_suffix(".html"), "w") as f:
                    f.write(rendered_html)
