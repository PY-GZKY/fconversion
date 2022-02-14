from concurrent.futures import ThreadPoolExecutor, wait, as_completed, ALL_COMPLETED
from typing import Optional

from pandas import DataFrame
from pymongo import MongoClient

from src.constants import *
from src.utils import to_str_datetime


class MongoEngine:
    """
    MongoEngine Class
    """

    def __init__(
            self,
            host: Optional[str] = None,
            port: Optional[int] = None,
            username: Optional[str] = None,
            password: Optional[str] = None,
            database: Optional[str] = None,
            collection: Optional[str] = None,
            conn_timeout: Optional[int] = 30,
            conn_retries: Optional[int] = 5
    ):
        self.host = MONGO_HOST if host is None else host
        self.port = MONGO_PORT if port is None else port
        self.username = username
        self.password = password
        self.database = MONGO_DATABASE if database is None else database
        self.collection = MONGO_COLLECTION if collection is None else collection
        self.conn_timeout = MONGO_CONN_TIMEOUT if conn_timeout is None else conn_timeout
        self.conn_retries = MONGO_CONN_RETRIES if conn_retries is None else conn_retries
        self.mongo_core_ = MongoClient(
            host=self.host,
            port=self.port,
            username=self.username,
            password=self.password,
            maxPoolSize=None
        )
        self.db_ = self.mongo_core_[self.database]
        self.collection_names = self.db_.list_collection_names()
        if self.collection:
            self.collection_ = self.db_[self.collection]
        else:
            self.collection_ = None

    def to_csv(self, query: dict, filename: str, _id: bool = False, limit: int = 200):
        if not isinstance(query, dict):
            raise TypeError('query must be of Dict type.')
        if self.collection_:
            if filename is None:
                filename = f'{self.collection}_{to_str_datetime()}'
            doc_list_ = list(self.collection_.find(query).limit(limit))
            data = DataFrame(doc_list_)
            data.to_csv(path_or_buf=f'{filename}.csv', encoding=PANDAS_ENCODING)
        else:
            raise TypeError('to export a single csv file, you must specify a collection name.')

    def to_excel(self, query: dict, filename: str = None, _id: bool = False, limit: int = 20):
        if not isinstance(query, dict):
            raise TypeError('query must be of Dict type.')
        if self.collection_:
            if filename is None:
                filename = f'{self.collection}_{to_str_datetime()}'
            doc_list_ = list(self.collection_.find(query).limit(limit))
            data = DataFrame(doc_list_)
            data.to_excel(excel_writer=f'{filename}.xlsx', sheet_name=filename)
        else:
            raise TypeError('to export a single excel file, you must specify a collection name.')

    def no_collection_to_csv_(self, collection_: str, filename: str, _id: bool = False):
        if collection_:
            doc_list_ = list(self.db_[collection_].find({}))
            data = DataFrame(doc_list_)
            data.to_csv(path_or_buf=f'{filename}.csv', encoding=PANDAS_ENCODING)

    def no_collection_to_excel_(self, collection_: str, filename: str, _id: bool = False):
        if collection_:
            doc_list_ = list(self.db_[collection_].find({}))
            data = DataFrame(doc_list_)
            data.to_excel(excel_writer=f'{filename}.csv', encoding=PANDAS_ENCODING)

    def to_csvs(self):
        # todo 如果不指定 collection 则导出此库中所有文档
        self.concurrent_(self.no_collection_to_csv_, self.collection_names)

    def to_excels(self):
        # todo 如果不指定 collection 则导出此库中所有文档
        self.concurrent_(self.no_collection_to_excel_, self.collection_names)

    def concurrent_(self, func, collection_names):
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures_ = [executor.submit(func, collection_name, collection_name) for
                        collection_name in
                        collection_names]
            wait(futures_, return_when=ALL_COMPLETED)
            for future_ in as_completed(futures_):
                if future_.done():
                    # print(future_.result())
                    ...

    def to_json(self):
        ...

    def to_mysql(self):
        ...


if __name__ == '__main__':
    M = MongoEngine(
        host="192.168.0.141",
        port=27017,
        username="admin",
        password="",
        database="sm_admin_test",
        collection="xhs_chengdu"
    )
    # M.to_csvs()
    # M.to_csv(query={}, filename="小红书")
    M.to_excel(query={})
    # M.to_json()
