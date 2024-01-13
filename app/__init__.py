from flask import Flask

from config import config

from .ext.db import db
from .ext.marshmallow import ma
from .ext.jwt_extendend import jwt


def create_app(config_name="development"):
    app = Flask(__name__)

    app.config.from_object(config[config_name])

    db.init_app(app)
    jwt.init_app(app)
    ma.init_app(app)

    from .modules.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix="/auth")

    from .modules.banco import banco as banco_blueprint
    app.register_blueprint(banco_blueprint, url_prefix="/banco")

    return app