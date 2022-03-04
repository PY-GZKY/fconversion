import os

import markdown

try:
    from markdown import markdown
except ModuleNotFoundError as e:
    os.system("pip install markdown")
    os.system("pip install python-markdown-math")
    os.system("pip install markdown_checklist")
    from markdown import markdown

from src.constants import *
from src.source import imgkit
from src.source import pdfkit
from src.templates.html_template import html_
from src.utils import md_extensions_, md_extensions_configs_


class MARKDOWN:
    def __init__(self,
                 wkhtmltopdf_path: str = None,
                 wkhtmltoimage_path: str = None,
                 encoding: str = encoding_
                 ):
        self.encoding = encoding
        self.html_ = html_
        self.wkhtmltopdf_path = default_wkhtmltopdf_path if wkhtmltopdf_path is None else wkhtmltopdf_path
        self.wkhtmltoimage_path = default_wkhtmltoimage_path if wkhtmltoimage_path is None else wkhtmltoimage_path
        self.extensions = md_extensions_()
        self.extension_configs = md_extensions_configs_()

    def markdown2image(self, input_path: str, output_path: str):
        """
        pip install imgkit
        """
        conf = imgkit.config(wkhtmltoimage=self.wkhtmltoimage_path)
        options = {
            'format': 'jpg',
            'encoding': "UTF-8"
        }
        css = [
            "../../src/static/linenum.css",
            "../../src/static/markdown.css",
            "../../src/static/tasklist.css",
            "../../src/static/codehilite.css",
        ]
        output_path_ = self.markdown2html(input_path, "../../tests/hello_.html", is_save=True)
        imgkit.from_file(output_path_, output_path, options=options, config=conf, css=css)
        # imgkit.from_string(output_path_, output_path, options=options, config=conf, css=css)


    def markdown2pdf(self, input_path: str, output_path: str,enable_local_file:bool=True):
        """
        """
        conf = pdfkit.configuration(wkhtmltopdf=self.wkhtmltopdf_path)
        options = {
            "enable-local-file-access": None
        } if enable_local_file else default_options_

        """
        html_text_ = self.markdown2html(input_path, "./tf_/hello_.html",is_center=False,is_save=False)
        pdfkit.from_string(html_text_, output_path, options=options, configuration=conf)
        """

        output_path_ = self.markdown2html(input_path, "./tf_/hello_.html",is_center=False,is_save=True)
        pdfkit.from_file(output_path_, output_path, options=options, configuration=conf)

    def markdown2html(self, input_path: str, output_path: str, is_center:bool=True, is_save:bool=True):
        """
        """
        try:
            with open(input_path, "r",  encoding="utf-8") as md_:
                md_text_ = md_.read()
        except Exception as e:
            print("<Error>", e)

        title = '.'.join(os.path.basename(input_path).split('.')[:-1])
        html_text_ = markdown(md_text_,
                              output_format='html',
                              extensions=self.extensions,
                              extension_configs=self.extension_configs
                              )

        class_ = ' for="html-export"' if is_center else ""
        html_text_ = self.html_.format(title_=title, div_=html_text_,class_=class_)
        if is_save:
            try:
                with open(output_path, 'w', encoding=self.encoding) as file_html_:
                    file_html_.write(html_text_)
                return output_path
            except Exception:
                return False
        else:
            return html_text_





if __name__ == '__main__':
    M = MARKDOWN()
    # M.markdown2html(input_path='../../tests/tf_/hello_.md', output_path='../../tests/tf_/hello_.html')
    M.markdown2image(input_path='../../tests/hello_.md', output_path='../../tests/tf_/_.jpg')