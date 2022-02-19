# -*- coding: utf-8 -*-
import datetime
import decimal
import getpass
import json
import re
import time
import typing
import uuid

import alive_progress
from PIL import Image
from bson import ObjectId
from colorama import init as colorama_init_, Fore
from dateutil import tz

from constants import TIME_ZONE

colorama_init_(autoreset=True)


def get_user_name() -> str:
    return getpass.getuser()


def gen_uuid() -> str:
    return str(uuid.uuid4())


def as_int(f: float) -> int:
    return int(round(f))


def timestamp_ms() -> int:
    return as_int(time.time() * 1000)


def ms_to_datetime(unix_ms: int) -> datetime:
    tz_ = tz.gettz(TIME_ZONE)
    return datetime.datetime.fromtimestamp(unix_ms / 1000, tz=tz_)


def to_str_datetime() -> str:
    return datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S%f')


def _alchemy_encoder(obj):
    if isinstance(obj, datetime.date):
        return obj.strftime("%Y-%m-%d %H:%M:%S")
    elif isinstance(obj, decimal.Decimal):
        return float(obj)
    elif isinstance(obj, ObjectId):
        return str(obj)


def serialize_obj(obj):
    if isinstance(obj, list):
        return json.dumps([dict(r) for r in obj], ensure_ascii=False, default=_alchemy_encoder)
    else:
        return json.dumps(dict(obj), ensure_ascii=False, default=_alchemy_encoder)


def write_image_(page, pg: int, trans, target_file: str):
    pix = page.get_pixmap(matrix=trans, alpha=False)  # alpha=False 白色背景  不透明
    pix.save(f'{target_file}/image_{pg}.jpg')


def sort_key(s) -> int:
    try:
        c = re.findall('\d+', s)[0]
    except:
        c = -1
    return int(c)


def merge_img_(img_list: typing.List, target_file: str = None):
    if target_file is None:
        target_file = "merge_.png"

    """拼接图片"""
    color_mod = 'RGB'  # jpeg格式不支持RGBA 'RGBA' if img_list_[0].endswith('.jpg') else
    first_img = Image.open(img_list[0])
    height_size = first_img.size[1]
    total_width = first_img.size[0]
    # print(f"获取图像大小为: {height_size},{total_width}", )
    total_height = height_size * len(img_list)  # 合并图总高度
    left = 0
    right = height_size
    target = Image.new(color_mod, (total_width, total_height))  # 最终拼接的图像的大小
    merge_time_ = int((len(img_list) / 3))
    merge_time_ = merge_time_ if merge_time_ != 0 else 1
    total_ = len(img_list) + merge_time_
    title_ = f'{Fore.GREEN}正在合并 → {target_file}'
    with alive_progress.alive_bar(total_, title=title_, bar="blocks") as bar:
        for img in img_list:
            target.paste(Image.open(img), (0, left, total_width, right))
            left += height_size
            right += height_size
            bar()
        target.save(target_file, quality=90)
        bar(merge_time_)
    return target_file


if __name__ == '__main__':
    merge_img_(img_list=[], target_file="合并后.png")
