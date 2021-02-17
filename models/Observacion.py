import database.db as db
from sqlalchemy import Column, Integer, String, Float, Date, Time, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship

class Observacion(db.Base):
    __tablename__ = 'observaciones'
    
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    idMedicion = Column('idMedicion', Integer, ForeignKey('mediciones.id',onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    id_user_tel = Column('id_user_tel', Integer, ForeignKey('usuarios.id_user_tel',onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    observacion = Column('observacion', String(2000), back_populates='observaciones')

    def __init__(self, idMedicion, id_user_tel, observacion):
        self.idMedicion = idMedicion
        self.id_user_tel = id_user_tel
        self.observacion = observacion

    def __repr__(self):
        return f"<Usuario {self.id}>"