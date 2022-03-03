# SETTING
import os

try:
    from pymdownx import superfences
except ModuleNotFoundError as e:
    os.system("pip install pymdown-extensions")
    from pymdownx import superfences

WKHTMLTOPDF_PATH = r'./wkhtmltopdf./bin./wkhtmltopdf.exe'  # 安装位置
PANDAS_ENCODING = 'utf_8_sig'
TIME_ZONE = 'Asia/Shanghai'

# 扩展配置
MD_EXTENSIONS = [
    'toc',  # 目录，[toc]
    'extra',  # 缩写词、属性列表、释义列表、围栏式代码块、脚注、在HTML的Markdown、表格

    'mdx_math',  # KaTeX数学公式，$E=mc^2$和$$E=mc^2$$
    'markdown_checklist.extension',  # checklist，- [ ]和- [x]
    'markdown.extensions.extra',
    'markdown.extensions.codehilite',
    'markdown.extensions.tables',
    'markdown.extensions.toc'
]


MD_EXTENSIONS_CONFIGS = {
    'mdx_math': {
        'enable_dollar_delimiter': True  # 允许单个$
    },
    'pymdownx.superfences': {
        "custom_fences": [
            {
                'name': 'mermaid',  # 开启流程图等图
                'class': 'mermaid',
                'format': superfences.fence_div_format
            }
        ]
    },
    'pymdownx.highlight': {
        'linenums': True,  # 显示行号
        'linenums_style': 'pymdownx-inline'  # 代码和行号分开
    },
    'pymdownx.tasklist': {
        'clickable_checkbox': True,  # 任务列表可点击
    }
}
