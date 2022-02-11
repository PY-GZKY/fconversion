from typing import List, Tuple, Union, Optional
from .constants import *
from pymongo import MongoClient


class MongoEngine(object):
    """
    MongoEngine Class
    """
    host: Union[str, List[Tuple[str, int]]] = MONGO_HOST
    port: int = MONGO_PORT
    username: Optional[str] = MONGO_USERNAME
    password: Optional[str] = MONGO_PASSWORD
    database: str = MONGO_DATABASE
    collection: str = MONGO_COLLECTION
    conn_timeout: int = 1
    conn_retries: int = 5

    def __init__(self):
        self.mongo_core_ = MongoClient(host=self.host, port=self.port, username=self.username, password=self.password)
        self.db_ = self.mongo_core_[self.database]
        self.collection_ = self.db_[self.collection]

    def to_csv(self):
        ...

    def to_xlsx(self):
        ...

    def to_json(self):
        ...
