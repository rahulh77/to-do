import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = True
    DEVELOPMENT = True
    ENV = 'development'
    TESTING = True
    MONGO_CONN_STR = os.getenv('MONGO_CONN_STR', None)
    MONGO_DB= 'tododb'
    MONGO_COLLECTION = 'todo'
