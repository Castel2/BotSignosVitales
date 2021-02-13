import database.db as db
from datetime import datetime
from sqlalchemy import extract
from models.Usuario import Usuario

def get_help_message ():
    response = (
        "Registro de pacientes, para realizar el registro ingrese documento y nombre en el siguiente formato \n"
        )

    return response


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