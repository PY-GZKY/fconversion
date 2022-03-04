import sys

from .configuration import Configuration


def get_configuration_(configuration):
    configuration_ = None
    if configuration is None:
        if sys.platform == 'win32':
            wkhtmltopdf_path = "E:/Py_Word_Code/fconversion/src/bin/wkhtmltopdf.exe"
            configuration_ = Configuration(wkhtmltopdf=wkhtmltopdf_path)
            print("wkhtmltopdf_path：", configuration_.wkhtmltopdf)
    else:
        configuration_ = configuration
    return configuration_


def wkhtmltoimage_error():
     return "Wkhtmltoimage not found,\nIf this file exists please check that this process can read it."
