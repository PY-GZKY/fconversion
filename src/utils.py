# -*- coding: utf-8 -*-
import getpass
import re
import uuid
from typing import List

import alive_progress
from PIL import Image
from colorama import init as colorama_init_, Fore
from pymdownx import superfences

colorama_init_(autoreset=True)


def get_user_name() -> str:
    return getpass.getuser()


def gen_uuid() -> str:
    return str(uuid.uuid4())


def sort_key(s) -> int:
    try:
        c = re.findall('\d+', s)[0]
    except:
        c = -1
    return int(c)


def md_extensions_():
    # return [
    #     'toc',  # 目录，[toc]
    #     'extra',  # 缩写词、属性列表、释义列表、围栏式代码块、脚注、在HTML的Markdown、表格
    #     'mdx_math',  # KaTeX数学公式，$E=mc^2$和$$E=mc^2$$
    #     'markdown_checklist.extension',  # checklist，- [ ]和- [x]
    #     'pymdownx.magiclink',  # 自动转超链接，
    #     'pymdownx.caret',  # 上标下标，
    #     'pymdownx.superfences',  # 多种块功能允许嵌套，各种图表
    #     'pymdownx.betterem',  # 改善强调的处理(粗体和斜体)
    #     'pymdownx.mark',  # 亮色突出文本
    #     'pymdownx.highlight',  # 高亮显示代码
    #     'pymdownx.tasklist',  # 任务列表
    #     'pymdownx.tilde'  # 删除线
    # ]
    return [
        'markdown.extensions.extra',
        'markdown.extensions.abbr',
        'markdown.extensions.attr_list',
        'markdown.extensions.def_list',
        'markdown.extensions.fenced_code',
        'markdown.extensions.footnotes',
        'markdown.extensions.md_in_html',
        'markdown.extensions.tables',
        'markdown.extensions.admonition',
        'markdown.extensions.codehilite',
        'markdown.extensions.legacy_attrs',
        'markdown.extensions.legacy_em',
        'markdown.extensions.meta',
        'markdown.extensions.nl2br',
        'markdown.extensions.sane_lists',
        'markdown.extensions.smarty',
        'markdown.extensions.toc',
        'markdown.extensions.wikilinks',

        'toc',
        'extra',
        'mdx_math',
        'markdown_checklist.extension',
        'pymdownx.magiclink',
        'pymdownx.caret',
        'pymdownx.superfences',
        'pymdownx.betterem',
        'pymdownx.mark',
        'pymdownx.highlight',
        'pymdownx.tasklist',
        'pymdownx.tilde'
    ]


def md_extensions_configs_():
    return {
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


def write_image_(page, pg: int, trans, target_file: str):
    pix = page.get_pixmap(matrix=trans, alpha=False)  # alpha=False 白色背景  不透明
    pix.save(f'{target_file}/image_{pg}.jpg')


def merge_img_(img_list: List, target_file: str = None):
    if target_file is None:
        target_file = "merge_.png"

    """拼接图片"""
    color_mod = 'RGB'  # jpeg格式不支持RGBA 'RGBA' if img_list_[0].endswith('.jpg') else
    first_img = Image.open(img_list[0])
    height_size = first_img.size[1]
    total_width = first_img.size[0]
    # print(f"获取图像大小为: {height_size},{total_width}", )
    total_height = height_size * len(img_list)  # 合并图总高度
    left = 0
    right = height_size
    target = Image.new(color_mod, (total_width, total_height))  # 最终拼接的图像的大小
    merge_time_ = int((len(img_list) / 3))
    merge_time_ = merge_time_ if merge_time_ != 0 else 1
    total_ = len(img_list) + merge_time_
    title_ = f'{Fore.GREEN}正在合并 → {target_file}'
    with alive_progress.alive_bar(total_, title=title_, bar="blocks") as bar:
        for img in img_list:
            target.paste(Image.open(img), (0, left, total_width, right))
            left += height_size
            right += height_size
            bar()
        target.save(target_file, quality=90)
        bar(merge_time_)
    return target_file


if __name__ == '__main__':
    merge_img_(img_list=[], target_file="合并后.png")
