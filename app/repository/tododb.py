from pymongo import MongoClient
# from ..config import Config as CONFIG
from flask import current_app


class TodoDB(object):
    def __init__(self):
        self._myclient = MongoClient(current_app.config['MONGO_CONN_STR'])
        self._mydb = self._myclient[current_app.config['MONGO_DB']] # database
        self._mycoll = self._mydb[current_app.config['MONGO_COLLECTION']] # table

    # Create operation
    def insert(self, item):
        result = self._mycoll.insert_one(item)
        return result

    # Get operation
    def getAll(self):
        return self._mycoll.find()