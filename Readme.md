**Note**

This repository currently hosts a self-contained tool I use personally. It is ​not yet optimized for public use, lacks detailed documentation, and has not been adapted for broader developer scenarios.

# MarkPDF

MarkPDF 是一款将 markdown 渲染为 PDF 的工具。

## 特性

- 使用 [markdown-it-py](https://github.com/executablebooks/markdown-it-py) 渲染 markdown. 它 100% 兼容 CommonMark 规范.
- 使用 [WeasyPrint](https://github.com/Kozea/WeasyPrint) 将 markdown 渲染为 PDF.
- 通过 [Playwright](https://github.com/microsoft/playwright) 渲染以支持浏览器 javascript 的其他组件:
  - mermaid.js
  - 嵌入的图片
  - 嵌入的网页

## Usage

```bash
pip install markpdf
```
