import database.db as db
from datetime import datetime
from sqlalchemy import *
from models.Usuario import Usuario
from models.Medicion import Medicion
from models.Observacion import Observacion

def get_signos (user_id, fecha_inicial, fecha_final):
    fecha_final = fecha_final + " 23:59:59.999999"
    signos = db.session.query(Medicion).filter(Medicion.id_user_tel == user_id).filter(and_(Medicion.fecha_toma >= fecha_inicial, Medicion.fecha_toma <= fecha_final)).all()
    db.session.commit()
    if not signos:
        return None
    return signos

# Lógica bienvenida e inicio al bot
def validar_medico (id_usuario_chat):
    usuario = db.session.query(Usuario).filter(Usuario.id_user_tel == id_usuario_chat).filter(Usuario.tipoUsuario == 2).first()
    db.session.commit()   

    if not usuario:
        return None
        
    return usuario

def get_pacientes ():
    pacientes = db.session.query(Usuario).filter(Usuario.tipoUsuario == 1).all()
    db.session.commit()
    if not pacientes:
        return None
    return pacientes    


# consultar signos”  PARA CONSULTAR  -SK
def consulta_signos(user_id, index):
    #se guarda la consulta en la variable signo
    signo = db.session.query(Medicion).filter(
    Medicion.id_user_tel == user_id
    ).filter(
    Medicion.id == index
    ).first()
    #si no hay nada en signos
    if not signo:
        db.session.rollback()
        return None
    #Si hay un registro en signos
    return signo

def consulta_medicion(index):
    #se guarda la consulta en la variable signo
    signo = db.session.query(Medicion).filter(
    Medicion.id == index).first()
    #si no hay nada en signos
    if not signo:
        db.session.rollback()
        return None
    #Si hay un registro en signos
    return signo
'''
# consultar los observaciones”  PARA CONSULTAR  -SK
def consulta_observaciones(index):
    #se guarda la consulta en la variable obsercion
    observacion = db.session.query(Observacion).filter( Observacion.id == index).first()
    #si no hay nada en Observacion
    if not observacion:
        db.session.rollback()
        return None
    #Si hay un registro en Observacion
    return observacion
    '''