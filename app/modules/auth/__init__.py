from flask import Blueprint

auth = Blueprint("auth", __name__)

from . import banco_login, player_login