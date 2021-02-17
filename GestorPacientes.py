import database.db as db
from datetime import datetime
from sqlalchemy import extract
from models.Usuario import Usuario

#########################################################
# Lógica bienvenida e inicio al bot
def get_paciente (documento):
    usuario = db.session.query(Usuario).filter(Usuario.documento==documento)
    db.session.commit()
    
    if not usuario:
        return None
        
    return usuario

def set_paciente(id_user_tel, documento, nombreCompleto): 
    usuario = Usuario(id_user_tel, documento, nombreCompleto)
    
    db.session.add(usuario)    
    db.session.commit()

    return True
