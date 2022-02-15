# -*- coding:utf-8 -*-
import os

import pandas
import pymysql
from colorama import init as colorama_init_
from dotenv import load_dotenv

load_dotenv(verbose=True)
colorama_init_(autoreset=True)


class FileEngine():
    """
    FileEngine Class
    """

    def __init__(self):
        ...

    def csv_to_sql(self, file_path, db_setting):
        df_csv_ = pandas.read_csv(file_path)
        conn_ = pymysql.connect(**db_setting)
        df_csv_.to_sql(name='test_', con=conn_)


if __name__ == '__main__':
    M = FileEngine()
