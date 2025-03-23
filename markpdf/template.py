from mdit_py_plugins.anchors import anchors_plugin

from markdown_it import MarkdownIt

script_content = '''
<style>
    table {
        border-collapse: collapse;
        border: 1px solid #000;
    }
    table th, table td {
        border: 1px solid #000;
        padding: 5px;
    }

    p {
        margin: 0; 
        padding: 0;
        line-height: 1.5;
    }

    pre, code {
        font-family: "JetBrains Mono", Courier, monospace;
        white-space: pre-wrap;
        word-wrap: break-word;
    }
</style>
<script>
    document.addEventListener("DOMContentLoaded", function() {
        renderMathInElement(document.body, {
          delimiters: [
              {left: '$$', right: '$$', display: true},
              {left: '$', right: '$', display: false},
              {left: '\$', right: '\$', display: false},
              {left: '\$$', right: '\$$', display: true}
          ],
          throwOnError : false
        });
    });
    document.addEventListener("DOMContentLoaded", function() {
        mermaid.initialize({ startOnLoad: false });
        mermaid.run({
            querySelector: '.language-mermaid',
        });
    });
</script>
'''

html_template = """
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.21/dist/katex.min.css" integrity="sha384-zh0CIslj+VczCZtlzBcjt5ppRcsAmDnRem7ESsYwWwg3m/OaJ2l4x7YBZl9Kxxib" crossorigin="anonymous">
        <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.21/dist/katex.min.js" integrity="sha384-Rma6DA2IPUwhNxmrB/7S3Tno0YY7sFu9WSYMCuulLhIqYSGZ2gKCJWIqhBWqMQfh" crossorigin="anonymous"></script>
        <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.21/dist/contrib/auto-render.min.js" integrity="sha384-hCXGrW6PitJEwbkoStFjeJxv+fSOOQKOPbJxSfM6G5sWZjAyWhXiTIIAmQqnlLlh" crossorigin="anonymous"
            onload="renderMathInElement(document.body);"></script>
        <script src="https://cdn.jsdelivr.net/npm/mermaid@11.5.0/dist/mermaid.min.js"></script>
        {script_content}
    </head>
    <body>
        {inner_body}
    </body>
</html>
"""

def render_html(markdown: str) -> str:
    md = MarkdownIt("commonmark").enable("table").enable(
        "strikethrough").use(anchors_plugin)
    inner_body = md.render(markdown)
    return html_template.format(inner_body=inner_body, script_content=script_content)
