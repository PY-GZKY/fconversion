import pdfkit

from src.constants import *
from src.template_.html_template import html_

try:
    from markdown import markdown
except ModuleNotFoundError as e:
    os.system("pip install markdown")
    os.system("pip install python-markdown-math")
    os.system("pip install markdown_checklist")
    from markdown import markdown


class MARKDOWN:
    def __init__(self,
                 wkhtmltopdf_path: str = WKHTMLTOPDF_PATH,
                 encoding:str = ENCODING_
                 ):
        self.encoding = encoding
        self.html = html_
        self.wkhtmltopdf_path = wkhtmltopdf_path
        self.extensions = MD_EXTENSIONS
        self.extension_configs = MD_EXTENSIONS_CONFIGS

    def markdown2image(self, input_file: str, output_file: str = None):
        """
        转换为不可编辑
        """

    def markdown2pdf(self, input_file: str, output_file: str):
        """
        转换为不可编辑
        """
        conf = pdfkit.configuration(wkhtmltopdf=self.wkhtmltopdf_path)
        output_file_ = self.markdown2html(input_file,"./tf_/hello_.html")
        pdfkit.from_file(output_file_, output_file, options={'encoding': self.encoding}, configuration=conf)  # HTML转PDF

    def markdown2html(self, input_file: str, output_file: str):
        """
        转换为不可编辑
        """
        try:
            with open(input_file, "r", encoding=self.encoding) as file_md:
                md_text = file_md.read()
        except Exception as e:
            print("<Error>", e)
            return False

        title = '.'.join(os.path.basename(input_file).split('.')[:-1])
        html_text = markdown(md_text,
                             output_format='html',
                             extensions=self.extensions,
                             extension_configs=self.extension_configs)  # MarkDown转HTML
        self.html = self.html.format(title_=title, div_=html_text)

        try:
            with open(output_file, 'w', encoding=self.encoding) as file_html:
                file_html.write(self.html)
        except Exception:
            return False

        return output_file


