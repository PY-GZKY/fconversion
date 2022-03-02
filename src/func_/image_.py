from PIL import Image


def png2jpg(source_file: str, target_file: str):
    """
    :param source_file: .png
    :param target_file: .jpg
    :return:
    """
    im = Image.open(source_file)
    im = im.convert('RGB')
    im.save(target_file, quality=95)


def jpg2png():
    ...
