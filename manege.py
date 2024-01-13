from app import create_app
from app.ext.db import db
from app.models import *

app = create_app("development")

with app.app_context():
    db.create_all()

# @app.make_shell_context()
# def shell():
#     return {
#         "Banco": Banco, 
#         "Sala": Sala,
#         "Player": Player,
#         "db": db
#     }

if __name__ == "__main__":
    app.run(debug=True)