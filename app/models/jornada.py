from sqlalchemy import Column, Integer, String, Date, Time, CheckConstraint
from app.database.conexion import Base

class Jornada(Base):
    __tablename__ = "jornadas"

    __table_args__ = (
        CheckConstraint(
            "capacidad_maxima > 0",
            name="check_capacidad_positiva"
        ),
    )

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
    lugar = Column(String(200), nullable=False)
    fecha = Column(Date, nullable=False)
    hora = Column(Time, nullable=False)
    capacidad_maxima = Column(Integer, nullable=False)
    entidad_organizadora = Column(String(180), nullable=False)