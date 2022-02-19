# -*- coding:utf-8 -*-
import os
# from pydub import AudioSegment
from concurrent.futures import ThreadPoolExecutor

import fitz
import pdfkit
from PIL import Image
from alive_progress import alive_bar
from colorama import init as colorama_init_,Fore
from dotenv import load_dotenv
# from moviepy.editor import VideoFileClip
from win32com.client import constants, gencache

from src.constants import POOL_MAX_WORKERS
from src.utils import write_image_, merge_img_, sort_key

load_dotenv(verbose=True)
colorama_init_(autoreset=True)


class FileEngine():

    def __init__(self):
        ...

    def png_to_jpg(self, source_file: str, target_file: str):
        """
        :param source_file: .png
        :param target_file: .jpg
        :return:
        """
        im = Image.open(source_file)
        im = im.convert('RGB')
        im.save(target_file, quality=95)

    def jpg_to_png(self):
        ...

    def video_to_audio(self, source_file: str, target_file: str):
        """
        video = VideoFileClip(source_file)
        audio = video.audio
        audio.write_audiofile(target_file)
        """

    def audio_to_audio(self, source_file: str, target_file: str):
        """
        pip install pydub
        :param source_file: .fly .mp3 .wav .ogg .flac
        :param target_file: .fly .mp3 .wav .ogg .flac
        :return:
        """
        # song = AudioSegment.from_wav("Python.wav")
        # song.export("Python.mp3", format="mp3")

    def audio_to_text(self):
        ...

    def word_to_pdf(self, source_file: str, target_file: str = None):
        """
        word转pdf 只作用于 windows 平台
        :param wordPath: word文件路径
        :param pdfPath:  生成pdf文件路径
        """
        word = gencache.EnsureDispatch('Word.Application')
        doc = word.Documents.Open(source_file, ReadOnly=1)
        doc.ExportAsFixedFormat(target_file, constants.wdExportFormatPDF,
                                Item=constants.wdExportDocumentWithMarkup,
                                CreateBookmarks=constants.wdExportCreateHeadingBookmarks)
        word.Quit(constants.wdDoNotSaveChanges)

    def pdf_to_word(self, source_file: str, target_file: str = None, ):
        """
        from pdf2docx import Converter
        """
        # pdf_file = '/path/to/sample.pdf'
        # docx_file = 'path/to/sample.docx'
        #
        # # convert pdf to docx
        # cv = Converter(pdf_file)
        # cv.convert(docx_file, start=0, end=None)
        # cv.close()

    def pdf_to_image(self, source_file: str, target_file: str = None, zoom_x: int = 4, zoom_y: int = 4,
                     is_merge: bool = False):
        """
        pip install fitz PyMuPDF
        """
        if not source_file.upper().endswith(".PDF"):
            raise TypeError("source file must be of pdf type")
        if target_file is None:
            target_file = "."
        if not os.path.exists(target_file):  # 判断存放图片的文件夹是否存在
            os.makedirs(target_file)  # 若图片文件夹不存在就创建
        # start_time_ = datetime.datetime.now()  # 时间
        pdf_doc_ = fitz.open(source_file)
        page_count_ = 30  # pdf_doc_.page_count
        rotate = int(0)
        trans = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)

        with alive_bar(page_count_, title=f'{Fore.GREEN}正在导出 {source_file} → {target_file}', bar="blocks",
                       spinner="elements") as bar:
            with ThreadPoolExecutor(max_workers=POOL_MAX_WORKERS) as executor:
                for pg in range(page_count_):
                    executor.submit(write_image_, pdf_doc_[pg], pg, trans, target_file).add_done_callback(
                        lambda func: bar())
                executor.shutdown()

        pdf_doc_.close()

        if is_merge:
            imgs = []
            for root, dirs, files in os.walk(target_file): imgs = files
            imgs.sort(key=sort_key)
            img_list = [f'{target_file}/{img}' for img in imgs]
            merge_img_(img_list=img_list, target_file="h_.png")

        # end_time_ = datetime.datetime.now()  # 结束时间
        # print('操作时间: ', (end_time_ - start_time_).seconds)

    def html_to_pdf(self, wkhtmltopdf_path: str, html_file: str = None,
                    url: str = 'https://zhuanlan.zhihu.com/p/94608155'):
        """
        pip install pdfkit
        并且依赖于 wkhtmltopdf 环境
        :return:
        """
        if wkhtmltopdf_path is None:
            raise ValueError("wkhtmltopdf path cannot be empty")
        confg = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

        if url is not None:
            pdfkit.from_url(url, './下载文件.pdf', configuration=confg)
        else:
            pdfkit.from_file(html_file, '下载文件2.pdf', configuration=confg)


if __name__ == '__main__':
    M = FileEngine()
    # M.png_to_jpg(source_file="images.png",target_file="./joyfulpandas.jpg")
    M.pdf_to_image(source_file="./joyfulpandas.pdf", target_file="./joyfulpandas", is_merge=True)
    # M.word_to_pdf(source_file="E:/Py_Word_Code/fconversion/src/resume.docx",
    #               target_file="E:/Py_Word_Code/fconversion/src/resume.pdf")
