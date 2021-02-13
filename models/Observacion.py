import database.db as db
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

class Observacion(db.Base):
    __tablename__ = 'observaciones'
    
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    idMedicion = Column('idMedicion', Integer, ForeignKey('mediciones.id',onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    documentoUsuario = Column('documentoUsuario', Integer, ForeignKey('usuarios.documento',onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    observacion = Column('observacion', String(2000), back_populates='usuarios')

    def __init__(self, idMedicion, documentoUsuario, observacion):
        self.idMedicion = idMedicion
        self.documentoUsuario = documentoUsuario
        self.observacion = observacion

    def __repr__(self):
        return f"<Usuario {self.id}>"