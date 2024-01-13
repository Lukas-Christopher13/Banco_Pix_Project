from flask import jsonify, request
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                get_jwt_identity, jwt_required)

from ...models import Banco
from . import auth


@auth.route("/banco-login", methods=["POST"])
def banco_login():
    username = request.json.get("username")
    password = request.json.get("password")

    banco: Banco = Banco.query.filter_by(username=username).first()

    if banco is None:
        return jsonify({"msg": "invalid username"}), 401
    
    if not banco.check_password(password):
        return jsonify({"msg": "invalid password"}), 401
    
    access_token = create_access_token(identity=banco.id)
    refresh_token = create_refresh_token(identity=banco.id)

    return jsonify(access_token=access_token, refresh_token=refresh_token)

@auth.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    identify = get_jwt_identity()
    access_token = create_access_token(identity=identify)
    return jsonify(access_token=access_token)


#test, remover mais tarde 
@auth.route("/test", methods=["GET"])
@jwt_required()
def test():
    return jsonify("ok")