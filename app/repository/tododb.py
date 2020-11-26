from pymongo import MongoClient
# from ..config import Config as CONFIG
from flask import current_app
from bson import ObjectId # For ObjectId to work   
import pprint 


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

    # @app.route('/star/', methods=['GET'])
    def get(self, name):
        item = self._mycoll.find_one({'name': name})
        result = None
        if item:
            result = item
        return result

    def remove(self, name):
        #Deleting a Task with various references     
        # item = self._mycoll.find_one({'name': name})
        # pprint.pprint(item)
        # print(item)
        result = self._mycoll.delete_many({'name': name})
        return result