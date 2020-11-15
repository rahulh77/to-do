from flask import Flask
import flask_monitoringdashboard as dashboard
from .controller.foo import foo
from .controller.todo import todo
from .controller.health import health
from .config import Config

app = Flask("todo_flask")
# dashboard.bind(app)
# dashboard.config.init_from()


app.config.from_object(Config())
# app.config['DEBUG'] = True

# print(app.config)
app.register_blueprint(foo)
app.register_blueprint(todo)
app.register_blueprint(health)

if __name__ == '__main__':
    app.run()
