from flask import Flask
from .controller.foo import foo
from .controller.todo import todo

app = Flask("todo_flask")

print(app.name)
app.debug = True
app.register_blueprint(foo)
app.register_blueprint(todo)

app.run()
