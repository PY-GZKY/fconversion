import dotenv
import pytest

from src.func_.markdown_ import MARKDOWN

dotenv.load_dotenv(verbose=True)


def setup_function():
    global M
    M = MARKDOWN()


def test_markdown2pdf():
    M.markdown2pdf(input_file='./tf_/春回大地.md', output_file='./tf_/春回大地.pdf')


# def test_markdown2html():
#     M.markdown2html(input_file='./tf_/春回大地.md', output_file='./tf_/春回大地.html')


def teardown_function():
    ...


if __name__ == "__main__":
    pytest.main(["-s", "test_.py"])
