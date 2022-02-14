from typing import Optional

from pandas import DataFrame
from pymongo import MongoClient

from src.constants import *


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
            password=self.password
        )
        self.db_ = self.mongo_core_[self.database]
        # todo 如果不指定 collection 则导出此库中所有文档
        self.collection_ = self.db_[self.collection]

    def to_csv(self, query: dict, filename: str, _id: bool=False, limit: int = 20):
        if not isinstance(query, dict):
            raise TypeError('query must be of Dict type.')

        doc_list_ = list(self.collection_.find(query).limit(limit))
        data = DataFrame(doc_list_)
        # print(data)
        data.to_csv(path_or_buf=f'{filename}.csv')

    def to_excel(self, query: dict, filename: str, _id: bool=False, limit: int=20):
        if not isinstance(query, dict):
            raise TypeError('query must be of Dict type.')
        if filename is None:
            filename = "nihao_"
        doc_list_ = list(self.collection_.find(query).limit(limit))
        data = DataFrame(doc_list_)

        data.to_excel(excel_writer=f'{filename}.xlsx', sheet_name=filename)

    def to_json(self):
        ...

    def to_mysql(self):
        ...

    def __del__(self):
        ...

if __name__ == '__main__':
    M = MongoEngine(host="192.168.0.141",
                    port=27017,
                    username="admin",
                    password="...",
                    database="tyc_mini",
                    collection="公司基本信息")
    M.to_excel(query={}, filename="ok",limit=5000)
    M.to_csv(query={}, filename="ok",limit=5000)
    M.to_json()
