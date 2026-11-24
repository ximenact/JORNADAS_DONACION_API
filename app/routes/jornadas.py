
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database.conexion import get_db
from app.schemas.jornada_schema import (
    JornadaCreate,
    JornadaUpdate,
    JornadaResponse
)
from app.services import jornada_service as service


router = APIRouter(
    prefix="/jornadas",
    tags=["Jornadas de donación"]
)


@router.post("/", response_model=JornadaResponse, status_code=201)
def crear_jornada(
    datos: JornadaCreate,
    db: Session = Depends(get_db)
):
    return service.crear(db, datos)


@router.get("/", response_model=list[JornadaResponse])
def listar_jornadas(
    lugar: str | None = Query(default=None),
    db: Session = Depends(get_db)
):
    return service.listar(db, lugar)


@router.get("/{jornada_id}", response_model=JornadaResponse)
def obtener_jornada(
    jornada_id: int,
    db: Session = Depends(get_db)
):
    return service.obtener(db, jornada_id)


@router.put("/{jornada_id}", response_model=JornadaResponse)
def actualizar_jornada(
    jornada_id: int,
    datos: JornadaUpdate,
    db: Session = Depends(get_db)
):
    return service.actualizar(db, jornada_id, datos)


@router.delete("/{jornada_id}")
def eliminar_jornada(
    jornada_id: int,
    db: Session = Depends(get_db)
):
    return service.eliminar(db, jornada_id)
