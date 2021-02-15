import database.db as db
from datetime import datetime
from sqlalchemy import extract
from models.Usuario import Usuario


#########################################################
# Lógica bienvenida e inicio al bot
def get_paciente (documento):
    usuario = db.session.query(Usuario).get(documento)
    db.session.commit()
    
    if not usuario:
        return None
        
    return usuario

def set_paciente(documento, nombreCompleto): 
    usuario = Usuario(documento, nombreCompleto)
    
    db.session.add(usuario)    
    db.session.commit()

    return True
