
from sqlalchemy.orm import Session
from app.models.jornada import Jornada


def obtener_todas(db: Session):
    return db.query(Jornada).all()


def obtener_por_id(db: Session, jornada_id: int):
    return db.query(Jornada).filter(
        Jornada.id == jornada_id
    ).first()


def obtener_por_lugar(db: Session, lugar: str):
    return db.query(Jornada).filter(
        Jornada.lugar.ilike(f"%{lugar}%")
    ).all()


def crear(db: Session, datos: dict):
    jornada = Jornada(**datos)

    db.add(jornada)
    db.commit()
    db.refresh(jornada)

    return jornada


def actualizar(db: Session, jornada: Jornada, datos: dict):
    for campo, valor in datos.items():
        setattr(jornada, campo, valor)

    db.commit()
    db.refresh(jornada)

    return jornada

def eliminar(db: Session, jornada: Jornada):
    db.delete(jornada)
    db.commit()
