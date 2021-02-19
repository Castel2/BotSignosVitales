import database.db as db
from datetime import datetime
from sqlalchemy import *
from models.Usuario import Usuario
from models.Medicion import Medicion

def get_signos (user_id, fecha_inicial, fecha_final):
    fecha_final = fecha_final + " 23:59:59.999999"
    signos = db.session.query(Medicion).filter(Medicion.id_user_tel == user_id).filter(and_(Medicion.fecha_toma >= fecha_inicial, Medicion.fecha_toma <= fecha_final)).all()
    db.session.commit()
    if not signos:
        return None
    return signos