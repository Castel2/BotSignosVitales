import database.db as db
from sqlalchemy import Column, Integer, String, Float, Date, Time, DateTime, ForeignKey, func

class Usuario(db.Base):

    __tablename__ = 'usuarios'

    id_user_tel = Column('id_user_tel', Integer,primary_key=True)
    documento = Column('documento',Integer,  nullable=False)
    tipoUsuario = Column('tipoUsuario', Integer, server_default='1')
    nombreCompleto = Column('nombreCompleto', String(500), nullable=False)

    def __init__(self, id_user_tel, documento, nombreCompleto,tipoUsuario):
        self.id_user_tel = id_user_tel
        self.documento = documento
        self.nombreCompleto = nombreCompleto
        self.tipoUsuario = tipoUsuario

    def __repr__(self):
        return f"<Usuario {self.id_user_tel}>"