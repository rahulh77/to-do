from flask import Flask
from .controller.foo import foo
import os

app = Flask(__name__)
app.debug = True
app.register_blueprint(foo)
app.run()
