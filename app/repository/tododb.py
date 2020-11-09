from pymongo import MongoClient
from ..config import MONGO_COLLECTION, MONGO_CONN_STR, MONGO_DB




class TodoDB(object):
    def __init__(self):
        self._myclient = MongoClient(MONGO_CONN_STR)
        self._mydb = self._myclient[MONGO_DB] # database
        self._mycoll = self._mydb[MONGO_COLLECTION] # table

    # Create operation
    def insert(self, item):
        result = self._mycoll.insert_one(item)
        return result

    # Get operation
    def getAll(self):
        return self._mycoll.find()