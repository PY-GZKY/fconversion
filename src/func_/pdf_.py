import os
from concurrent.futures import ThreadPoolExecutor

import fitz
from alive_progress import alive_bar

from src import write_image_, sort_key, merge_img_
from src.constants import pool_max_workers
from src.utils.time_ import to_str_datetime


def pdf2epub():  # noqa F401
    """
    """


def pdf2word(input_path: str, output_path: str = None, pdf_password: str = None, multi_processing: bool = True,
             cpu_count: int = 2, start: int = 0):  # noqa F401
    try:
        from pdf2docx import Converter
    except ModuleNotFoundError:
        os.system("pip install pdf2docx")
        from pdf2docx import Converter

    if output_path is None:
        output_path = f'{input_path}_{to_str_datetime()}.docx'

    # convert pdf to docx
    cv = Converter(input_path, pdf_password)
    cv.convert(docx_filename=output_path, start=start, multi_processing=multi_processing, cpu_count=cpu_count)
    cv.close()


def pdf2image(input_path: str, output_path: str = None, zoom_x: int = 4, zoom_y: int = 4,
              is_merge: bool = False, merge_path: str = None): # noqa F401
    """
    pip install fitz, PyMuPDF
    """
    if not input_path.upper().endswith(".PDF"):
        raise TypeError("source file must be of pdf type")
    if output_path is None:
        output_path = "."
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    pdf_doc_ = fitz.open(input_path)
    page_count_ = pdf_doc_.page_count

    trans = fitz.Matrix(zoom_x, zoom_y).prerotate(int(0))
    title_ = f'正在导出 {input_path} → {output_path}'
    with alive_bar(page_count_, title=title_, bar="blocks") as bar:
        with ThreadPoolExecutor(max_workers=pool_max_workers) as executor:
            for pg in range(page_count_):
                executor.submit(write_image_, pdf_doc_[pg], pg, trans, output_path).add_done_callback(
                    lambda func: bar())
            executor.shutdown()
    pdf_doc_.close()

    if is_merge:
        if merge_path is None:
            merge_path = "merge_.png"
        imgs = []
        for root, dirs, files in os.walk(output_path): imgs = files
        imgs.sort(key=sort_key)
        img_list = [f'{output_path}/{img}' for img in imgs]
        merge_img_(img_list=img_list, target_file=merge_path)


if __name__ == '__main__':
    pdf2word(input_path="../../src/test_files/joyfulpandas.pdf",
             output_path="../../src/test_files/joyfulpandas.docx")
