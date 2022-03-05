html_ = '''
<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, minimal-ui">
    <title>{title_}</title>
    <link rel="stylesheet" href="../../src/static/linenum.css">
    <link rel="stylesheet" href="../../src/static/markdown.css">
    <link rel="stylesheet" href="../../src/static/tasklist.css">
    <link rel="stylesheet" href="../../src/static/codehilite.css">
    <link rel="stylesheet" href="../../src/static/progress.css">
    <script src="https://unpkg.com/mermaid@8.7.0/dist/mermaid.min.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex/dist/katex.min.css" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/katex/dist/katex.min.js" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/katex/dist/contrib/mathtex-script-type.min.js" defer></script>

    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/mathjax@2/MathJax.js"></script>
</head>
<body{class_}>
<div class="mume markdown-preview">            
<article class="markdown-body">
{div_}
</article>
</div>
</body>
</html>
'''
