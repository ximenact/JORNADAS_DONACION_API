
from fastapi import HTTPException
from pwdlib import PasswordHash

from app.repositories import usuario_repository as repo

password_hash = PasswordHash.recommended()


def listar(db):
    return repo.obtener_todos(db)


def obtener(db, usuario_id: int):
    usuario = repo.obtener_por_id(db, usuario_id)

    if not usuario:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    return usuario


def crear(db, datos):

    correo = str(datos.correo).lower()

    existente = repo.obtener_por_correo(db, correo)

    if existente:
        raise HTTPException(
            status_code=409,
            detail="Este correo ya está registrado"
        )

    usuario = {
        "nombre": datos.nombre.strip(),
        "correo": correo,
        "contrasena_hash": password_hash.hash(datos.contrasena)
    }

    return repo.crear(db, usuario)


def actualizar(db, usuario_id: int, datos):

    usuario = obtener(db, usuario_id)

    cambios = datos.model_dump(exclude_unset=True,exclude_none=True)

    if "correo" in cambios and cambios["correo"] is not None:

        correo = str(cambios["correo"]).lower()

        existente = repo.obtener_por_correo(db, correo)

        if existente and existente.id != usuario_id:
            raise HTTPException(
                status_code=409,
                detail="Este correo ya pertenece a otro usuario"
            )

        cambios["correo"] = correo

    if "nombre" in cambios and cambios["nombre"] is not None:
        cambios["nombre"] = cambios["nombre"].strip()

    if "contrasena" in cambios:
        cambios["contrasena_hash"] = password_hash.hash(
            cambios.pop("contrasena")
        )

    return repo.actualizar(db, usuario, cambios)


def eliminar(db, usuario_id: int):

    usuario = obtener(db, usuario_id)

    repo.eliminar(db, usuario)

    return {"mensaje": "Usuario eliminado correctamente"}
