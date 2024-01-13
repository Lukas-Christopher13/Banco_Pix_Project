from flask import jsonify, request
from flask_jwt_extended import create_access_token

from ...ext.db import db
from ...models import Player, Sala
from . import auth


@auth.route("/sala-code", methods=["POST"])
def enter_sala():
    sala_code = request.json.get("code")

    sala: Sala = Sala.query.filter_by(code=sala_code).first()

    if sala is None:
        return jsonify({"msg": "sala inexistente"}), 401
    
    return jsonify({"code": f"{sala.code}"})

@auth.route("/create-player/<code>", methods=["POST"])
def create_player(code):
    sala: Sala = Sala.query.filter_by(code=code).first()

    if sala is None:
        return jsonify({"msg": "sala inexistente"}), 401
    
    username = request.json.get("username")
    
    player = Player(username=username, sala=sala)

    db.session.add(player)
    db.session.commit()

    accesse_token = create_access_token(username)

    return jsonify(accesse_token=accesse_token)



    
    

