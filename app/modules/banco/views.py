from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from ...ext.db import db
from ...models import Banco, Sala
from ...schemas import SalaSchema
from . import banco


@banco.route("/criar_sala", methods=["POST"])
@jwt_required()
def criar_sala():
    identity = get_jwt_identity()
    banco: Banco = Banco.query.filter_by(id=identity).first()
    
    try:
        code = request.json.get("code")
        
        sala = Sala(code=code, banco=banco)

        db.session.add(sala)
        db.session.commit()

        return jsonify({"msg": "sala criada!"}), 201
    except:
        return jsonify({"msg": "essa sala já foi criada!"}), 401


@banco.route("/deletar_sala/<code>", methods=["DELETE"])
@jwt_required()
def deletar_sala(code):
    sala: Sala = Sala.query.filter_by(code=code).first()

    if(sala is not None):
        db.session.delete(sala)
        return jsonify({"msg": "sala deletada"}), 200

    return jsonify({"msg": "code invalido"})


@banco.route("/listar_salas", methods=["GET"])
@jwt_required()
def listar_salas():
    sala_schema = SalaSchema()
    salas = Sala.query.all()
    
    json_list = [sala_schema.dump(sala) for sala in salas]

    return jsonify(json_list), 200

@banco.route("/player_data/<int:id>", methods=["GET"])
@jwt_required()
def player_data(id):
    pass

