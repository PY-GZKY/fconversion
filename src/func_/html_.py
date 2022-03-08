import os
from src.constants import *
from src.source import imgkit
from src.source import pdfkit


class HTML:
    def __init__(self,
                 wkhtmltopdf_path: str = None,
                 wkhtmltoimage_path: str = None,
                 encoding='utf-8'
                 ):
        self.encoding = encoding
        self.wkhtmltopdf_path = default_wkhtmltopdf_path if wkhtmltopdf_path is None else wkhtmltopdf_path
        self.wkhtmltoimage_path = default_wkhtmltoimage_path if wkhtmltoimage_path is None else wkhtmltoimage_path

    def html2pdf(self, input_path: str, output_path: str, url: str = None, enable_local_file: bool = True):
        """
        pip install pdfkit
        """
        # if self.wkhtmltopdf_path is None:
        #     raise ValueError("wkhtmltopdf path cannot be empty")

        conf = pdfkit.configuration(wkhtmltopdf=self.wkhtmltopdf_path)
        options = {
            "enable-local-file-access": None
        } if enable_local_file else default_options_

        if url is not None:
            pdfkit.from_url(url, output_path, configuration=conf, options=options)
        else:
            pdfkit.from_file(input_path, output_path, configuration=conf, options=options)

    def html2image(self, input_path: str, output_path: str, url: str = None):
        """
        pip install imgkit
        """
        options = {
            'encoding': "utf_8_sig",
            'enable-local-file-access': None
        }
        conf = imgkit.config(wkhtmltoimage=self.wkhtmltoimage_path)

        if url is not None:
            imgkit.from_url(url, output_path, options=options, config=conf)
        else:
            imgkit.from_file(input_path, output_path, options=options, config=conf)


if __name__ == '__main__':
    H = HTML()
    H.html2pdf(input_path=f'../../src/test_files/_.html', output_path=f'../../src/test_files/_.pdf')
    H.html2image(input_path=f'../../src/test_files/_.html', output_path=f'../../src/test_files/_.jpg')
