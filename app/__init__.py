from flask import Flask
import flask_monitoringdashboard as dashboard
import logging
from .controller.foo import foo
from .controller.todo import todo
from .controller.health import health
from .config import Config
from .metrics import metrics

app = Flask("todo_flask")
# dashboard.bind(app)
# dashboard.config.init_from()
metrics.init_metrics(app)


app.config.from_object(Config())
# app.config['DEBUG'] = True

app.logger.info("from app logger")

print(app.config)

from .errors import bp as errors_bp
app.register_blueprint(errors_bp)
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