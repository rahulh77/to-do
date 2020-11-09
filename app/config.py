import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    MONGO_CONN_STR = os.getenv('MONGO_CONN_STR', None)
    MONGO_DB= 'tododb'
    MONGO_COLLECTION = 'todo'