import dotenv
import pytest

from src.func_.html_ import HTML
from src.func_.markdown_ import MARKDOWN

dotenv.load_dotenv(verbose=True)


def setup_function():
    global M, H
    M = MARKDOWN()
    H = HTML()


# def test_html2pdf():
#     H.html2pdf(input_path='./tf_/hello_.html',output_path='./tf_/hello_.pdf')

def test_html2image():
    H.html2image(input_path='hello_.html', output_path='hello_.png')

# def test_markdown2pdf():
#     M.markdown2pdf(input_path='./tf_/hello_.md', output_path='./tf_/hello_.pdf')

# def test_markdown2image():
#     M.markdown2image(input_path='./tf_/hello_.md', output_path='./tf_/hello_.jpg')

# def test_markdown2html():
#     M.markdown2html(input_path='./tf_/hello_.md', output_path='./tf_/hello_.html')


def teardown_function():
    ...


if __name__ == "__main__":
    pytest.main(["-s", "test_.py"])
