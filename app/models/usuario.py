from sqlalchemy import Column, Integer, String
from app.database.conexion import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
    correo = Column(String(150), unique=True, nullable=False)
    contrasena_hash = Column(String(255), nullable=False)