
from sqlalchemy.orm import Session
from app.models.usuario import Usuario


def obtener_todos(db: Session):
    return db.query(Usuario).all()

def obtener_por_id(db: Session, usuario_id: int):
    return db.query(Usuario).filter(
        Usuario.id == usuario_id
    ).first()

def obtener_por_correo(db: Session, correo: str):
    return db.query(Usuario).filter(
        Usuario.correo == correo
    ).first()

def crear(db: Session, datos: dict):
    usuario = Usuario(**datos)

    db.add(usuario)
    db.commit()
    db.refresh(usuario)

    return usuario

def actualizar(db: Session, usuario: Usuario, datos: dict):
    for campo, valor in datos.items():
        setattr(usuario, campo, valor)

    db.commit()
    db.refresh(usuario)

    return usuario

def eliminar(db: Session, usuario: Usuario):
    db.delete(usuario)
    db.commit()
