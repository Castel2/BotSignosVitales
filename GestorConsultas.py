import database.db as db
from datetime import datetime
from sqlalchemy import extract
from models.Usuario import Usuario
from models.Medicion import Medicion

def get_signos (user_id):
    signos = db.session.query(Medicion).filter(Medicion.id_user_tel == user_id).all()
    db.session.commit()
    if not signos:
        return None
    return signos