from sqlalchemy import Column, ForeignKey, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash

from .ext.db import db


class Banco(db.Model):
    __tablename__ = "banco"

    id = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True, nullable=False)
    password_hash = Column(String(512))

    salas = db.relationship("Sala", backref="banco")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Sala(db.Model):
    __tablename__ = "sala"

    code = Column(String(4), primary_key=True)
    banco_id = Column(Integer, ForeignKey("banco.id"))

    players = db.relationship("Player", backref="sala")

class Player(db.Model):
    __tablename__ = "player"

    username = Column(String(64), primary_key=True)
    sala_code = Column(String(4), ForeignKey("sala.code"))