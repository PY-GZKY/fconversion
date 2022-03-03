import dotenv
import pytest

from src.func_.markdown_ import Markdown

dotenv.load_dotenv(verbose=True)


def setup_function():
    global M
    M = Markdown()


# def test_markdown2pdf():
#     markdown2pdf(input_file='../README.md', output_file='./README.pdf')



def test_markdown2html():
    M.markdown2html(input_file='./tf_/春回大地.md', output_file='./tf_/春回大地.html')



def teardown_function():
    ...


if __name__ == "__main__":
    pytest.main(["-s", "test_.py"])
