from flask import Blueprint
from flask.wrappers import Response

health = Blueprint('health', __name__)


# index route, shows index.html view
@health.route('/health')
def index():
    return Response(status=200)
