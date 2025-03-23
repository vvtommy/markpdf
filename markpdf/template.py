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
        line-height: 1.5;
    }

    pre {
        background-color: #f4f4f4;
        padding: 10px;
        border-radius: 5px;
    }

    pre, code {
        font-family: "JetBrains Mono", Courier, monospace;
        white-space: pre-wrap;
        word-wrap: break-word;
    }
</style>
<script>
    function renderKatex() {
        renderMathInElement(document.body, {
          delimiters: [
              {left: '$$', right: '$$', display: true},
              {left: '$', right: '$', display: false},
              {left: '\$', right: '\$', display: false},
              {left: '\$$', right: '\$$', display: true}
          ],
          throwOnError : false
        });
    }
    function renderMermaid() {
        mermaid.initialize({ startOnLoad: false });
        mermaid.run({
            querySelector: '.language-mermaid',
        });
    };
    
    document.addEventListener("DOMContentLoaded", function() {
        const md = new markdownit({
            html: true,
            linkify: true,
            typographer: true,
            quotes: '“”‘’',
        }).use(markdownItAttrs).use(markdownItAnchor);
        const templateTag = document.getElementById('markdown-content');
        const markdownContent = templateTag.textContent;
        document.body.innerHTML = md.render(markdownContent);
        templateTag.remove();
        
        setTimeout(renderKatex, 1);
        setTimeout(renderMermaid, 1);
    })
</script>
'''

html_template = """
<!DOCTYPE html>
<html>
    <head>
        <script type="text/x-markdown" id="markdown-content">
{markdown_content}
        </script>
        <script src="https://cdn.jsdelivr.net/npm/markdown-it@14.1.0/dist/markdown-it.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/markdown-it-attrs@4.3.1/markdown-it-attrs.browser.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/markdown-it-anchor@9.2.0/dist/markdownItAnchor.umd.min.js"></script>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.21/dist/katex.min.css" integrity="sha384-zh0CIslj+VczCZtlzBcjt5ppRcsAmDnRem7ESsYwWwg3m/OaJ2l4x7YBZl9Kxxib" crossorigin="anonymous">
        <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.21/dist/katex.min.js" integrity="sha384-Rma6DA2IPUwhNxmrB/7S3Tno0YY7sFu9WSYMCuulLhIqYSGZ2gKCJWIqhBWqMQfh" crossorigin="anonymous"></script>
        <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.21/dist/contrib/auto-render.min.js" integrity="sha384-hCXGrW6PitJEwbkoStFjeJxv+fSOOQKOPbJxSfM6G5sWZjAyWhXiTIIAmQqnlLlh" crossorigin="anonymous"
            onload="renderMathInElement(document.body);"></script>
        <script src="https://cdn.jsdelivr.net/npm/mermaid@11.5.0/dist/mermaid.min.js"></script>
        {script_content}
    </head>
    <body>
    </body>
</html>
"""


def render_html(markdown: str) -> str:
    # md = MarkdownIt("commonmark").enable("table").enable(
    #     "strikethrough").use(anchors_plugin)
    # inner_body = md.render(markdown)
    return html_template.format(
        markdown_content=markdown,
        script_content=script_content)
