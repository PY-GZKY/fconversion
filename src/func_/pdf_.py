import os
from concurrent.futures import ThreadPoolExecutor

# from .constants import POOL_MAX_WORKERS
import fitz
from alive_progress import alive_bar


def pdf2epub():
    """
    """


def pdf2word(self, source_file: str, target_file: str = None, ):
    """
    转换为可编辑
    from pdf2docx import Converter
    """
    # pdf_file = '/path/to/sample.pdf'
    # docx_file = 'path/to/sample.docx'
    #
    # # convert pdf to docx
    # cv = Converter(pdf_file)
    # cv.convert(docx_file, start=0, end=None)
    # cv.close()


def pdf2image(source_file: str, target_file: str = None, zoom_x: int = 4, zoom_y: int = 4,
              is_merge: bool = False, merge_path: str = None):
    """
    pip install fitz, PyMuPDF
    """
    if not source_file.upper().endswith(".PDF"):
        raise TypeError("source file must be of pdf type")
    if target_file is None:
        target_file = "."
    if not os.path.exists(target_file):
        os.makedirs(target_file)

    pdf_doc_ = fitz.open(source_file)
    page_count_ = pdf_doc_.page_count
    rotate = int(0)
    trans = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)
    title_ = f'{Fore.GREEN}正在导出 {source_file} → {target_file}'
    with alive_bar(page_count_, title=title_, bar="blocks") as bar:
        with ThreadPoolExecutor(max_workers=POOL_MAX_WORKERS) as executor:
            for pg in range(page_count_):
                executor.submit(write_image_, pdf_doc_[pg], pg, trans, target_file).add_done_callback(
                    lambda func: bar())
            executor.shutdown()
    pdf_doc_.close()

    if is_merge:
        if merge_path is None:
            merge_path = "merge_.png"
        imgs = []
        for root, dirs, files in os.walk(target_file): imgs = files
        imgs.sort(key=sort_key)
        img_list = [f'{target_file}/{img}' for img in imgs]
        merge_img_(img_list=img_list, target_file=merge_path)
