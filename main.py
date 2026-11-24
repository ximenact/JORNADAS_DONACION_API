
from fastapi import FastAPI

from app.database.conexion import Base, engine

from app.models.usuario import Usuario
from app.models.jornada import Jornada

from app.routes.usuarios import router as usuarios_router
from app.routes.jornadas import router as jornadas_router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="API de Jornadas de Donación de Sangre",
    description="API para administrar jornadas de donación y usuarios",
    version="1.0.0"
)


app.include_router(usuarios_router)
app.include_router(jornadas_router)


@app.get("/")
def inicio():
    return {
        "mensaje": "API de jornadas de donación de sangre funcionando"
    }
