from sqlalchemy import Column, Integer, String, Date, ForeignKey, TIMESTAMP, SmallInteger
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta
from config import Base
import logging
logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)

class Usuario(Base):
    __tablename__ = 'Usuarios'
    Numero_Usuario = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    apellido = Column(String(50))
    dni = Column(String(20))
    telefono = Column(String(20))
    email = Column(String(100))
    creado_el = Column(TIMESTAMP, default=datetime.now)
    actualizado_el = Column(TIMESTAMP, default=datetime.now, onupdate=datetime.now)
    estado = Column(SmallInteger, default=1)

class Genero(Base):
    __tablename__ = 'Generos'
    Numero_Genero = Column(Integer, primary_key=True)
    genero = Column(String(50))

class Libro(Base):
    __tablename__ = 'Libros'
    Numero_Libro = Column(Integer, primary_key=True)
    nombre_libro = Column(String(100))
    autor = Column(String(100))
    fecha_lanzamiento = Column(Date)
    id_genero = Column(Integer, ForeignKey('Generos.Numero_Genero'))
    creado_el = Column(TIMESTAMP, default=datetime.now)
    actualizado_el = Column(TIMESTAMP, default=datetime.now, onupdate=datetime.now)
    estado = Column(SmallInteger, default=1)
    genero = relationship("Genero")

class Prestamo(Base):
    __tablename__ = 'Prestamos'
    Numero_Prestamo = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('Usuarios.Numero_Usuario'))
    libro_id = Column(Integer, ForeignKey('Libros.Numero_Libro'))
    fecha_prestamo = Column(Date, default=datetime.now)
    fecha_devolucion_estimada = Column(Date, default=(datetime.now() + timedelta(days=7)))
    fecha_devolucion_real = Column(Date, nullable=True)
    usuario = relationship("Usuario")
    libro = relationship("Libro")

from config import engine
Base.metadata.create_all(engine)
