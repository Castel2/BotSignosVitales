import database.db as db
from datetime import datetime
from sqlalchemy import extract
from models.Usuario import Usuario
from models.Medicion import Medicion

def get_signos (user_id):
    print(user_id)
    signos = db.session.query(Medicion).filter(Medicion.id_user_tel == user_id).all()
    db.session.commit()
    print(signos)
    if not signos:
        print("ENTROOOOOOOOOOOOOO")
        return None
    return signos