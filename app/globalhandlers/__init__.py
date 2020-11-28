from flask import Blueprint

bp = Blueprint('globalhandlers', __name__)

from app.globalhandlers import error_handlers
from app.globalhandlers import handlers
