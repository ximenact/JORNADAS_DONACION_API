
from fastapi import HTTPException

from app.repositories import jornada_repository as repo


def listar(db, lugar=None):

    if lugar and lugar.strip():
        return repo.obtener_por_lugar(db, lugar.strip())

    return repo.obtener_todas(db)


def obtener(db, jornada_id: int):

    jornada = repo.obtener_por_id(db, jornada_id)

    if not jornada:
        raise HTTPException(
            status_code=404,
            detail="Jornada no encontrada"
        )

    return jornada


def crear(db, datos):

    return repo.crear(
        db,
        datos.model_dump()
    )


def actualizar(db, jornada_id: int, datos):

    jornada = obtener(db, jornada_id)

    cambios = datos.model_dump(exclude_unset=True)

    return repo.actualizar(db, jornada, cambios)


def eliminar(db, jornada_id: int):

    jornada = obtener(db, jornada_id)

    repo.eliminar(db, jornada)

    return {"mensaje": "Jornada eliminada correctamente"}
