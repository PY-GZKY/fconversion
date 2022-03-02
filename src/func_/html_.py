import pdfkit

"""
html2pdf(wkhtmltopdf_path=r'D:\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
html2image(wkhtmltoimage_path=r'D:\\wkhtmltopdf\\bin\\wkhtmltoimage.exe')
"""


def html2pdf(wkhtmltopdf_path: str, html_file: str = None,
             url: str = 'https://mp.weixin.qq.com'):
    """
    pip install pdfkit
    并且依赖于 wkhtmltopdf 环境
    :return:
    """
    if wkhtmltopdf_path is None:
        raise ValueError("wkhtmltopdf path cannot be empty")
    confg = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

    if url is not None:
        pdfkit.from_url(url, './下载文件.pdf', configuration=confg)
    else:
        pdfkit.from_file(html_file, '下载文件2.pdf', configuration=confg)


def html2image(self, wkhtmltoimage_path: str,
               url: str = 'https://docs.python.org/zh-cn/3/library/asyncio-queue.html'):
    """
    pip install pdfkit
    并且依赖于 wkhtmltopdf 环境
    :return:
    """
    if wkhtmltoimage_path is None:
        raise ValueError("wkhtmltoimage path cannot be empty")
    import imgkit
    options = {
        "encoding": "UTF-8"  # 这个具体要看你那个html页面到底是以什么编码格式保存的
    }

    cfg = imgkit.config(wkhtmltoimage=wkhtmltoimage_path)
    # imgkit.from_file(r'./helloworld.html', 'helloworld.jpg', config=cfg)
    imgkit.from_url(url, 'ip.jpg', options=options, config=cfg)
