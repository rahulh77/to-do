from flask import Flask
import flask_monitoringdashboard as dashboard
import logging
from .controller.foo import foo
from .controller.todo import todo
from .controller.health import health
from .config import Config
from .metrics import metrics
from .helper import CustomJSONEncoder


app = Flask("todo_flask")
from .globalhandlers import bp as gh_bp
# dashboard.bind(app)
# dashboard.config.init_from()
metrics.init_metrics(app)


app.config.from_object(Config())
app.json_encoder = CustomJSONEncoder

# app.config['DEBUG'] = True

app.logger.info("from app logger")

print(app.config)


app.register_blueprint(gh_bp)
app.register_blueprint(foo)
app.register_blueprint(todo)
app.register_blueprint(health)


if __name__ == '__main__':
    # print("in __init__")
    app.run()

if __name__ != '__main__':
    # print("in not __main__")
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)