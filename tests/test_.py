import dotenv
import pytest

from src.file_core import FileEngine
from src.utils import _merge_img

dotenv.load_dotenv(verbose=True)


def setup_function():
    global M
    M = FileEngine()


# def test_pdf_to_img():
#     M.pdf_to_image(source_file="joyfulpandas.pdf", target_file="joyfulpandas")
    # assert "successfully" in result_

# def test_merge_img():
#     _merge_img(img_list=["joyfulpandas/images_0.png",
#                      "joyfulpandas/images_1.png",
#                      "joyfulpandas/images_2.png"])

def test_html_to_pdf():
    M.html_to_pdf(wkhtmltopdf_path=r'D:\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')

def teardown_function():
    ...


if __name__ == "__main__":
    pytest.main(["-s", "test_.py"])
