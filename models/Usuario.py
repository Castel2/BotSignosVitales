import database.db as db
from sqlalchemy import Column, Integer, String, Float

class Usuario(db.Base):

    __tablename__ = 'usuarios'

    documento = Column('documento', Integer, primary_key=True, nullable=False)
    tipoDocumento = Column('tipoDocumento', Integer, server_default='1')
    tipoUsuario = Column('tipoUsuario', Integer, server_default='1')
    nombreCompleto = Column('nombreCompleto', String(500), nullable=False)

    def __init__(self, documento, nombreCompleto):
        self.documento = documento
        self.nombreCompleto = nombreCompleto

    def __repr__(self):
        return f"<Usuario {self.id}>"