from datetime import datetime
from flask import Blueprint, request, jsonify, Response
from bson import json_util
from ..repository.tododb import TodoDB
from flask import current_app as app
todo = Blueprint('todo', __name__)


# index route, shows index.html view
@todo.route('/')
def index():
    app.logger.info("From root endpoint")
    return "baz"

@todo.route('/todo', methods=['GET'])
def getall():
    tododb = TodoDB()
    result = list(tododb.getAll())
    # data = []
    # for doc in result:
    #     doc['_id'] = str(doc['_id']) 
    #     data.append(doc)
    app.logger.debug("From /todo endpoint")
    return jsonify(result)
    # data = json_util.loads(json_util.dumps(result))
    # return data

@todo.route('/todo/<name>', methods=['GET'])
def get_todo(name):
    tododb = TodoDB()
    result = tododb.get(name)
    if not result:
        return Response(f'Item "{name}" not found', 404)
    app.logger.info(f'todo item found {name}')
    # data = result
    # data['_id'] = str(result['_id']) 
    app.logger.debug(f"From /todo/{name} endpoint")
    return jsonify(result)

@todo.route('/todo', methods=['POST'])
def post_todo():
    item = request.json
    item['created_on'] = datetime.now()
    tododb = TodoDB()
    result = tododb.insert(item)
    app.logger.info(result.inserted_id)
    return jsonify({'id': str(result.inserted_id)})

@todo.route('/todo/<name>', methods=['DELETE'])
def remove_todo(name):
    tododb = TodoDB()
    result = tododb.remove(name)
    if result.deleted_count == 0:
        return Response(f'Item "{name}" not found', 404)
    app.logger.info(f'todo item deleted {name}')
    app.logger.info(f'ack: {result.acknowledged} , no of items deleted: {result.deleted_count}')
    return jsonify(result.raw_result)