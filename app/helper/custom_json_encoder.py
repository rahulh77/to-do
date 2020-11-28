from flask.json import JSONEncoder
from bson import json_util, ObjectId
import datetime

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj): 
        if isinstance(obj, datetime.datetime) or isinstance(obj,datetime.date):
            return obj.isoformat()
        if isinstance(obj, ObjectId):
            return str(obj)
        return json_util.default(obj)