from ..ext.db import db
from ..models import Banco

class BancoRepository:
    def select(self):
        data = db.session.query(Banco).all()
        return data
    
    def insert(self, username, password):
        banco = Banco(username=username)
        banco.set_password(password)

        db.session.add(banco)
        db.session.commit()
    
    def delete(self, id):
        db.session.query(Banco).filter(Banco.id == id).delete()
        db.session.commit()
    
    def update(self, id, username):
        db.session.query(Banco).filter(Banco.id == id).update({"username": username})