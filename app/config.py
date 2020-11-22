import os
from dotenv import load_dotenv
load_dotenv(verbose=True)

class Config(object):
    # LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
    # DEBUG = True
    # DEVELOPMENT = True
    # ENV = 'development'
    # TESTING = True
    MONGO_CONN_STR = os.getenv('MONGO_CONN_STR', None)
    MONGO_DB= os.environ.get("MONGO_DB")
    MONGO_COLLECTION = os.environ.get("MONGO_COLLECTION")
