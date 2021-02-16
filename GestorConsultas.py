import database.db as db
from datetime import datetime
from sqlalchemy import extract
from models.Usuario import Usuario
from models.Medicion import Medicion

def get_balance (user_id):
    medicion = db.session.query(Medicion).get(user_id)
    db.session.commit()
    if not medicion:
        return None
    return medicion