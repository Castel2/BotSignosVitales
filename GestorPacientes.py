import database.db as db
from datetime import datetime
from sqlalchemy import extract
from models.Usuario import Usuario

#########################################################
# Lógica bienvenida e inicio al bot
def get_paciente (documento):

    print(documento)

    usuario = db.session.query(Usuario).filter(Usuario.documento == documento).all()
    db.session.commit()    

    if not usuario:
        return None
        
    return usuario

def set_paciente(id_user_tel, documento, nombreCompleto): 
    usuario = Usuario(id_user_tel, documento, nombreCompleto)
    
    db.session.add(usuario)    
    db.session.commit()

    return True

#funcion exclusiva para validar la exitencia de un paciente... retorna True o False
def existencia_paciente (user_id):

    print(user_id)
    tipo_Usuario = 1

    usuario = db.session.query(Usuario).filter(
    Usuario.id_user_tel == user_id
    ).filter(
    Usuario.tipoUsuario == tipo_Usuario
    ).first()   

    if not usuario:
        return False
        
    return True