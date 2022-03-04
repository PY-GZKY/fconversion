# SETTING
import os

try:
    from pymdownx import superfences
except ModuleNotFoundError as e:
    os.system("pip install pymdown-extensions")
    from pymdownx import superfences

# WKHTMLTOPDF_PATH = r'E:\\Py_Word_Code\\fconversion\\src\\bin\\wkhtmltopdf.exe'  # 安装位置
# WKHTMLTOIMAGE_PATH = r'E:\\Py_Word_Code\\fconversion\\src\\bin\\wkhtmltoimage.exe'  # 安装位置
WKHTMLTOPDF_PATH = r'D:/wkhtmltopdf/bin/wkhtmltopdf.exe'  # 安装位置
WKHTMLTOIMAGE_PATH = r'D:/wkhtmltopdf/bin/wkhtmltoimage.exe'  # 安装位置
ENCODING_ = 'utf_8_sig'
TIME_ZONE = 'Asia/Shanghai'
POOL_MAX_WORKERS = 8
# 扩展配置
MD_EXTENSIONS = [
    'toc',  # 目录，[toc]
    'extra',  # 缩写词、属性列表、释义列表、围栏式代码块、脚注、在HTML的Markdown、表格
    'mdx_math',  # KaTeX数学公式，$E=mc^2$和$$E=mc^2$$
    'markdown_checklist.extension',  # checklist，- [ ]和- [x]
    'pymdownx.magiclink',  # 自动转超链接，
    'pymdownx.caret',  # 上标下标，
    'pymdownx.superfences',  # 多种块功能允许嵌套，各种图表
    'pymdownx.betterem',  # 改善强调的处理(粗体和斜体)
    'pymdownx.mark',  # 亮色突出文本
    'pymdownx.highlight',  # 高亮显示代码
    'pymdownx.tasklist',  # 任务列表
    'pymdownx.tilde',  # 删除线
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

options_ = {
    # 'page-size': 'Letter',
    # 'margin-top': '0.75in',
    # 'margin-right': '0.75in',
    # 'margin-bottom': '0.75in',
    # 'margin-left': '0.75in',
    # 'encoding': "UTF-8",
    # 'custom-header': [
    #     ('Accept-Encoding', 'gzip')
    # ],
    # 'no-outline': None
}
