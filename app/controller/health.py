from flask import Blueprint
from flask.wrappers import Response
from flask import current_app

health = Blueprint('health', __name__)


# index route, shows index.html view
@health.route('/health')
def index():
    current_app.logger.debug("From /health endpoint")
    return Response(status=200)
