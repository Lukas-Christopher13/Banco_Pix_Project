from flask import Blueprint

banco = Blueprint("banco", __name__)

from . import views