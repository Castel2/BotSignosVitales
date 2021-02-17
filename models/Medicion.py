import database.db as db
import datetime
from sqlalchemy import Column, Integer, String, Float, Date, Time, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship

class Medicion(db.Base):
    __tablename__ = 'mediciones'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    id_user_tel = Column('id_user_tel', Integer, ForeignKey('usuarios.id_user_tel',onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    pas = Column('pas', Integer, back_populates='mediciones')
    pad = Column('pad', Integer, back_populates='mediciones')
    fc = Column('fc', Integer, back_populates='mediciones')
    peso = Column('peso', Float, back_populates='mediciones')
    fecha_toma = Column('fecha_toma', DateTime, back_populates='mediciones')    
    fecha_registro = Column('fecha_registro', DateTime, default=datetime.datetime.utcnow, back_populates='mediciones')   

    def __init__(self, id_user_tel, pas, pad, fc, peso, fecha_toma):
        self.id_user_tel = id_user_tel
        self.pas = pas
        self.pad = pad
        self.fc = fc
        self.peso = peso
        self.fecha_toma = fecha_toma

    def __repr__(self):
        return f"<Medicion {self.id}>"