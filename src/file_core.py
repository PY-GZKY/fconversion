# -*- coding:utf-8 -*-
from colorama import init as colorama_init_
from dotenv import load_dotenv
from moviepy.editor import VideoFileClip

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

    def flv_to_mp3(self, source_file: str, target_file: str):
        """
        :param source_file: .fly
        :param target_file: .mp3
        :return:
        MoviePy - Writing audio in 点弦泛音高能！《江南》美爆的「指弹吉他」！林俊杰听了都想点赞！.mp3
        MoviePy - Done.
        """
        video = VideoFileClip(source_file)
        audio = video.audio
        audio.write_audiofile(target_file)

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
