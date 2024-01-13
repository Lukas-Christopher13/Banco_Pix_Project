from test import TestClassBase

from app.ext.db import db
from app.models import Banco, Sala


class TestAuthClass(TestClassBase):
    banco: Banco = None
    sala: Sala = None 

    def create_sala(self):
        self.create_banco()
        if self.sala is None:
            self.sala = Sala(code="1234", banco=self.banco)

            db.session.add(self.sala)
            db.session.commit()

        return self.sala
    
    def create_banco(self):
        if self.banco is None:
            self.banco = Banco(username="test")
            self.banco.set_password("123")

            db.session.add(self.banco)
            db.session.commit()

        return self.banco

