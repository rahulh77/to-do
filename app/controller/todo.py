from datetime import datetime
from flask import Blueprint, request, jsonify, Response
from bson import json_util
from ..repository.tododb import TodoDB
import json

todo = Blueprint('todo', __name__)


# index route, shows index.html view
@todo.route('/')
def index():
    return "baz"

@todo.route('/todo', methods=['GET'])
def getall():
    tododb = TodoDB()
    result = tododb.getAll()
    data = []
    for doc in result:
        doc['_id'] = str(doc['_id']) 
        data.append(doc)
    return jsonify(data)
    # return Response(json.dumps(result,default=str),mimetype="application/json")
    # return json.loads(json_util.dumps(result))

@todo.route('/todo', methods=['POST'])
def post_todo():
    item = request.json
    item['created_on'] = datetime.now()
    tododb = TodoDB()
    result = tododb.insert(item)
    print(result.inserted_id)
    return jsonify({'id': str(result.inserted_id)})