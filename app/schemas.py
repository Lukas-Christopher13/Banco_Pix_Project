from .ext.marshmallow import ma

from .models import Sala, Player

class SalaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Sala()

    code = ma.auto_field()

class PlayerSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Player()
    
    username = ma.auto_field()
    sala_code = ma.auto_field()

