import imgkit
import pdfkit

from src.constants import WKHTMLTOPDF_PATH, WKHTMLTOIMAGE_PATH


class HTML:
    def __init__(self,
                 wkhtmltopdf_path: str = WKHTMLTOPDF_PATH,
                 wkhtmltoimage_path: str = WKHTMLTOIMAGE_PATH,
                 encoding='utf-8'
                 ):
        self.encoding = encoding
        self.wkhtmltopdf_path = wkhtmltopdf_path
        self.wkhtmltoimage_path = wkhtmltoimage_path

    def html2pdf(self, input_file: str, output_file: str, url: str = None):
        """
        pip install pdfkit
        并且依赖于 wkhtmltopdf 环境
        :return:
        """
        if self.wkhtmltopdf_path is None:
            raise ValueError("wkhtmltopdf path cannot be empty")
        confg = pdfkit.configuration(wkhtmltopdf=self.wkhtmltopdf_path)

        if url is not None:
            pdfkit.from_url(url, output_file, configuration=confg)
        else:
            pdfkit.from_file(input_file, output_file, configuration=confg)

    def html2image(self, input_file: str, output_file: str,
                   url: str = 'https://docs.python.org/zh-cn/3/library/asyncio-queue.html'):
        """
        pip install pdfkit
        并且依赖于 wkhtmltopdf 环境
        :return:
        """
        if self.wkhtmltoimage_path is None:
            raise ValueError("wkhtmltoimage path cannot be empty")
        options = {
            "encoding": self.encoding
        }
        cfg = imgkit.config(wkhtmltoimage=self.wkhtmltoimage_path)
        # imgkit.from_file(input_file, output_file, config=cfg)
        imgkit.from_url(url, 'ip.jpg', options=options, config=cfg)
