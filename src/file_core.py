# -*- coding:utf-8 -*-
import os

import fitz
import pdfkit
from PIL import Image
from alive_progress import alive_bar
from colorama import init as colorama_init_
from dotenv import load_dotenv
from moviepy.editor import VideoFileClip

from src.utils import _merge_img

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

    def mp4_to_mp3(self):
        ...

    def flv_to_mp3(self, source_file: str, target_file: str):
        """
        :param source_file: .fly
        :param target_file: .mp3
        :return:
        """
        video = VideoFileClip(source_file)
        audio = video.audio
        audio.write_audiofile(target_file)

    def mp4_to_wav(self):
        ...

    def mp3_to_text(self):
        ...

    def pdf_to_image(self, source_file: str, target_file: str=None, zoom_x: int = 4, zoom_y: int = 4,
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

        pdf_doc_ = fitz.open(source_file)
        # todo 1、此处应当加入多线程 2、图片命名(后面合并用)
        with alive_bar(pdf_doc_.pageCount, title=f'{source_file} → {target_file} loading ...', bar="blocks",
                       spinner="elements") as bar:
            for pg in range(pdf_doc_.pageCount):
                page = pdf_doc_[pg]
                rotate = int(0)
                # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
                # 此处若是不做设置，默认图片大小为：792X612, dpi=96
                trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
                pix = page.getPixmap(matrix=trans, alpha=False)  # alpha=False 白色背景  不透明
                pix.writePNG(f'{target_file}/image_{pg}.png')  # 将图片写入指定的文件夹内
                bar()  # 更新控制台进度条

        if is_merge:
            _merge_img(img_list=[])

        # end_time_ = datetime.datetime.now()  # 结束时间
        # print('操作时间: ', (end_time_ - start_time_).seconds)

    def html_to_pdf(self, wkhtmltopdf_path: str):
        """
        pip install pdfkit
        并且依赖于 wkhtmltopdf 环境
        :return:
        """
        if wkhtmltopdf_path is None:
            raise ValueError("wkhtmltopdf path cannot be empty")

        url = 'https://zhuanlan.zhihu.com/p/94608155'  # 一篇博客的url
        confg = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)
        pdfkit.from_url(url, './下载文件.pdf', configuration=confg)

        # pdfkit.from_file('my.html', '下载文件2.pdf',configuration=confg)
        # pdfkit.from_string('wocao, '下载文件3.pdf', configuration=config)


if __name__ == '__main__':
    M = FileEngine()
    M.pdf_to_image(source_file="joyfulpandas.pdf", target_file="joyfulpandas")
