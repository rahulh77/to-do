from flask import Blueprint

foo = Blueprint('foo', __name__)


# index route, shows index.html view
@foo.route('/foo')
def index():
    return "bar"
