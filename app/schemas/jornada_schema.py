
from datetime import date, time
from pydantic import BaseModel, Field, ConfigDict


# Datos necesarios para registrar una jornada
class JornadaCreate(BaseModel):
    nombre: str = Field(min_length=3, max_length=150)
    lugar: str = Field(min_length=2, max_length=200)
    fecha: date
    hora: time
    capacidad_maxima: int = Field(gt=0)
    entidad_organizadora: str = Field(min_length=2, max_length=180)


# Datos permitidos para actualizar una jornada
class JornadaUpdate(BaseModel):
    nombre: str | None = Field(default=None, min_length=3, max_length=150)
    lugar: str | None = Field(default=None, min_length=2, max_length=200)
    fecha: date | None = None
    hora: time | None = None
    capacidad_maxima: int | None = Field(default=None, gt=0)
    entidad_organizadora: str | None = Field(default=None, min_length=2, max_length=180)


# Datos que devolverá la API
class JornadaResponse(BaseModel):
    id: int
    nombre: str
    lugar: str
    fecha: date
    hora: time
    capacidad_maxima: int
    entidad_organizadora: str

    model_config = ConfigDict(from_attributes=True)
