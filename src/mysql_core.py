from typing import Optional

import pandas
import pymysql

from src.constants import *


class MysqlEngine:
    """
    MysqlEngine Class
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
        self.host = MYSQL_HOST if host is None else host
        self.port = MYSQL_PORT if port is None else port
        self.user = username
        self.password = password
        self.database = MYSQL_DATABASE if database is None else database
        self.collection = MYSQL_COLLECTION if collection is None else collection
        self.conn_timeout = MYSQL_CONN_TIMEOUT if conn_timeout is None else conn_timeout
        self.conn_retries = MYSQL_CONN_RETRIES if conn_retries is None else conn_retries
        self.mysql_core_ = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.database,
            charset='utf8'
        )
        self.cursor = self.mysql_core_.cursor(pymysql.cursors.DictCursor)  # 游标对象

    def to_csv(self, query: dict, filename: str, limit: int = 20):
        if not isinstance(query, dict):
            raise TypeError('query must be of Dict type.')

        sql = f"select * from {self.collection};"
        self.cursor.execute(sql)
        doc_list_ = self.cursor.fetchall()
        data = pandas.DataFrame(doc_list_)
        data.to_csv(path_or_buf=f'{filename}.csv')

    def to_excel(self, query: dict, filename: str, limit: int = 20):
        if not isinstance(query, dict):
            raise TypeError('query must be of Dict type.')

        sql = f"select * from {self.collection};"
        self.cursor.execute(sql)
        doc_list_ = self.cursor.fetchall()
        data = pandas.DataFrame(doc_list_)
        data.to_excel(path_or_buf=f'{filename}.csv')

    def to_json(self):
        ...

    def to_mongo(self):
        ...

    def __del__(self):
        self.cursor.close()
        self.mysql_core_.close()


if __name__ == '__main__':
    M = MysqlEngine(host="192.168.0.141",
                    port=3306,
                    username="root",
                    password="",
                    database="sm_admin",
                    collection="hosts"
                    )
    M.to_csv(query={}, filename="hosts", limit=5000)
    # M.to_json()
