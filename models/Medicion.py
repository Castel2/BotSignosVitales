import database.db as db
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

class Medicion(db.Base):
    __tablename__ = 'mediciones'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    documentoUsuario = Column('documentoUsuario', Integer, ForeignKey('usuarios.documento',onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    pas = Column('pas', Integer, back_populates='mediciones')
    pad = Column('pad', Integer, back_populates='mediciones')
    fc = Column('fc', Integer, back_populates='mediciones')
    peso = Column('peso', Float, back_populates='mediciones')
    fecha = Column('fecha', Date, back_populates='mediciones')
    hora = Column('hora', Time, back_populates='mediciones')

    def __init__(self, documentoUsuario, pas, pad, fc, peso, fecha, hora):
        self.documentoUsuario = documentoUsuario
        self.pas = pas
        self.pad = pad
        self.fc = fc
        self.peso = peso
        self.fecha = fecha
        self.hora = hora

    def __repr__(self):
        return f"<Medicion {self.id}>"