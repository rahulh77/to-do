import os

MONGO_CONN_STR = os.getenv('MONGO_CONN_STR', None)
MONGO_DB= 'tododb'
MONGO_COLLECTION = 'todo'