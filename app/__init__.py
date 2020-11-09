from flask import Flask
from .controller.foo import foo
from .controller.todo import todo

app = Flask("todo_flask")


app.config.from_object("app.config.Config")
app.debug = True
# print(app.config)
app.register_blueprint(foo)
app.register_blueprint(todo)

if __name__ == '__main__':
    app.run()
