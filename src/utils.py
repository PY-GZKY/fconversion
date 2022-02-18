# -*- coding: utf-8 -*-
import datetime
import decimal
import getpass
import json
import time
import uuid

from PIL import Image as PIL_Image
from bson import ObjectId
from dateutil import tz

from src.constants import TIME_ZONE


def get_user_name():
    return getpass.getuser()


def gen_uuid():
    return str(uuid.uuid4())


def as_int(f: float) -> int:
    return int(round(f))


def timestamp_ms() -> int:
    return as_int(time.time() * 1000)


def ms_to_datetime(unix_ms: int) -> datetime:
    tz_ = tz.gettz(TIME_ZONE)
    return datetime.datetime.fromtimestamp(unix_ms / 1000, tz=tz_)


def to_str_datetime():
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



def _merge_img(img_list, target_file: str = "images.png"):
    """拼接图片"""
    # todo 1、图片列表排序问题 2、
    if img_list:
        img_name = img_list[0]
        color_mod = 'RGBA' if img_name.endswith('.png') else 'RGB'  # jpeg格式不支持RGBA
        first_img = PIL_Image.open(img_list[0])
        height_size = first_img.size[1]
        total_width = first_img.size[0]
        print(f"获取图像大小为: {height_size},{total_width}", )
        total_height = height_size * len(img_list)  # 合并图总高度
        left = 0
        right = height_size
        target = PIL_Image.new(color_mod, (total_width, total_height))  # 最终拼接的图像的大小
        for img in img_list:
            target.paste(PIL_Image.open(img), (0, left, total_width, right))
            left += height_size
            right += height_size
        target.save(target_file, quality=100)
        return img_name
    else:
        return


