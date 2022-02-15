# -*- coding:utf-8 -*-
from colorama import init as colorama_init_
from dotenv import load_dotenv

load_dotenv(verbose=True)
colorama_init_(autoreset=True)


class FileEngine():

    def __init__(self):
        ...

    def png_to_jpg(self):
        ...

    def jpg_to_png(self):
        ...

    def mp4_to_mp3(self):
        ...

    def mp4_to_wav(self):
        ...

    def mp4_to_wa(self):
        ...

    def mp3_to_text(self):
        ...

    def doc_to_pdf(self):
        ...

    def html_to_pdf(self):
        ...


if __name__ == '__main__':
    M = FileEngine()
