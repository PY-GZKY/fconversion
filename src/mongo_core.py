# -*- coding:utf-8 -*-
import os
import warnings
from concurrent.futures import ThreadPoolExecutor, wait, as_completed, ALL_COMPLETED
from typing import Optional
from colorama import init as colorama_init_, Fore
from dotenv import load_dotenv
from pandas import DataFrame
import pandas as pd
from pymongo import MongoClient

from src.constants import *
from src.utils import to_str_datetime, serialize_obj

load_dotenv(verbose=True)
colorama_init_(autoreset=True)


class MongoEngine:

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
            doc_list_ = list(self.collection_.find(query,{"_id": int(_id)}).limit(limit))
            data = DataFrame(doc_list_)
            data.to_csv(path_or_buf=f'{filename}.csv', index=False, encoding=PANDAS_ENCODING)
            print(f'[+] {Fore.GREEN}{self.collection} → exported successfully ... done')
        else:
            warnings.warn('No collection specified, All collections will be exported.', DeprecationWarning)
            self.to_csv_s_()

    def to_excel(self, query: dict, filename: str = None, _id: bool = False, limit: int = 20):
        if not isinstance(query, dict):
            raise TypeError('query must be of Dict type.')
        if self.collection_:
            if filename is None:
                filename = f'{self.collection}_{to_str_datetime()}'
            doc_list_ = list(self.collection_.find(query).limit(limit))
            data = DataFrame(doc_list_)
            data.to_excel(excel_writer=f'{filename}.xlsx', sheet_name=filename, index=False, encoding=PANDAS_ENCODING)
            print(f'[+] {Fore.GREEN}{self.collection} → exported successfully ... done')
        else:
            warnings.warn('No collection specified, All collections will be exported.', DeprecationWarning)
            self.to_excel_s_()

    def to_json(self, query: dict, filename: str = None, _id: bool = False, limit: int = 20):
        if not isinstance(query, dict):
            raise TypeError('query must be of Dict type.')
        if self.collection_:
            if filename is None:
                filename = f'{self.collection}_{to_str_datetime()}'
            doc_list_ = list(self.collection_.find(query).limit(limit))
            data = {'RECORDS': doc_list_}
            with open(f'{filename}.json', 'w', encoding="utf-8") as f:
                f.write(serialize_obj(data))
            print(f'[+] {Fore.GREEN}{self.collection} → exported successfully ... done')
        else:
            warnings.warn('No collection specified, All collections will be exported.', DeprecationWarning)
            self.to_json_s_()

    def to_pickle(self, query: dict, filename: str = None, _id: bool = False, limit: int = 20):
        if not isinstance(query, dict):
            raise TypeError('query must be of Dict type.')
        if self.collection_:
            if filename is None:
                filename = f'{self.collection}_{to_str_datetime()}'
            doc_list_ = list(self.collection_.find(query).limit(limit))
            data = DataFrame(doc_list_)
            data.to_pickle(path=f'{filename}.pkl')
            print(f'[+] {Fore.GREEN}{self.collection} → exported successfully ... done')
        else:
            warnings.warn('No collection specified, All collections will be exported.', DeprecationWarning)

    def to_feather(self, query: dict, filename: str = None, _id: bool = False, limit: int = 20):
        if not isinstance(query, dict):
            raise TypeError('query must be of Dict type.')
        if self.collection_:
            if filename is None:
                filename = f'{self.collection}_{to_str_datetime()}'
            doc_list_ = list(self.collection_.find(query).limit(limit))
            data = DataFrame(doc_list_)
            data.to_feather(path=f'{filename}.feather')
            print(f'[+] {Fore.GREEN}{self.collection} → exported successfully ... done')
        else:
            warnings.warn('No collection specified, All collections will be exported.', DeprecationWarning)

    def to_parquet(self, query: dict, filename: str = None, _id: bool = False, limit: int = 20):
        if not isinstance(query, dict):
            raise TypeError('query must be of Dict type.')
        if self.collection_:
            if filename is None:
                filename = f'{self.collection}_{to_str_datetime()}'
            doc_list_ = list(self.collection_.find(query).limit(limit))
            data = DataFrame(doc_list_)
            data.to_parquet(path=f'{filename}.parquet')
            print(f'[+] {Fore.GREEN}{self.collection} → exported successfully ... done')
        else:
            warnings.warn('No collection specified, All collections will be exported.', DeprecationWarning)

    def to_hdf5(self, query: dict, filename: str = None, _id: bool = False, limit: int = 20):
        if not isinstance(query, dict):
            raise TypeError('query must be of Dict type.')
        if self.collection_:
            if filename is None:
                filename = f'{self.collection}_{to_str_datetime()}'
            doc_list_ = list(self.collection_.find(query).limit(limit))
            data = DataFrame(doc_list_)
            h5 = pd.HDFStore(f'.{filename}.h5', 'w', complevel=4, complib='blosc')
            h5['df_'] = data
            h5.close()
            print(f'[+] {Fore.GREEN}{self.collection} → exported successfully ... done')
        else:
            warnings.warn('No collection specified, All collections will be exported.', DeprecationWarning)

    def no_collection_to_csv_(self, collection_: str, filename: str, _id: bool = False):
        if collection_:
            doc_list_ = list(self.db_[collection_].find({}, {"_id": int(_id)}))
            data = DataFrame(doc_list_)
            data.to_csv(path_or_buf=f'{filename}.csv', index=False, encoding=PANDAS_ENCODING)
            return f'[+] {Fore.GREEN}{collection_} → exported successfully ... done'

    def no_collection_to_excel_(self, collection_: str, filename: str, _id: bool = False):
        if collection_:
            doc_list_ = list(self.db_[collection_].find({}))
            data = DataFrame(doc_list_)
            data.to_excel(excel_writer=f'{filename}.xlsx', index=False, encoding=PANDAS_ENCODING)
            return f'[+] {Fore.GREEN}{collection_} → exported successfully ... done'

    def no_collection_to_json_(self, collection_: str, filename: str, _id: bool = False):
        if collection_:
            doc_list_ = list(self.db_[collection_].find({}))
            data = {'RECORDS': doc_list_}
            with open(f'{filename}.json', 'w', encoding="utf-8") as f:
                f.write(serialize_obj(data))
            return f'[+] {Fore.GREEN}{collection_} → exported successfully ... done'

    def to_csv_s_(self):
        # todo 如果不指定 collection 则导出此库中所有集合
        self.concurrent_(self.no_collection_to_csv_, self.collection_names)

    def to_excel_s_(self):
        self.concurrent_(self.no_collection_to_excel_, self.collection_names)

    def to_json_s_(self):
        self.concurrent_(self.no_collection_to_json_, self.collection_names)

    def concurrent_(self, func, collection_names):
        with ThreadPoolExecutor(max_workers=THREAD_POOL_MAX_WORKERS) as executor:
            futures_ = [executor.submit(func, collection_name, collection_name) for
                        collection_name in
                        collection_names]
            wait(futures_, return_when=ALL_COMPLETED)
            for future_ in as_completed(futures_):
                if future_.done():
                    print(future_.result())
                    ...

    def insert_(self, item):
        if item:
            self.collection_.insert_one(item)


    def many_insert_(self, items):
        if items:
            self.collection_.insert_many(items)


    def update_(self, key, item):
        if item:
            if self.collection_.update_one({key: item[key]}, {'$set': item}, True):
                ...
            else:
                ...

    def many_update_(self, key, item):
        if item:
            if self.collection_.update_many({key: item[key]}, {'$set': item}, True):
                ...
            else:
                ...



if __name__ == '__main__':
    M = MongoEngine(
        host= os.getenv('MONGO_HOST'),
        port= int(os.getenv('MONGO_PORT')),
        username=os.getenv('MONGO_USERNAME'),
        password=os.getenv('MONGO_PASSWORD'),
        database=os.getenv('MONGO_DATABASE'),
        collection=os.getenv('MONGO_COLLECTION')
    )
    # M.to_csv(query={}, _id=False, filename="_")
    # M.to_excel(query={})
    # M.to_json(query={})
    # M.to_pickle(query={})
    M.to_hdf5(query={})
