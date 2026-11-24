
from pydantic import BaseModel, EmailStr, Field, ConfigDict

class UsuarioCreate(BaseModel):
    nombre: str = Field(min_length=2, max_length=150)
    correo: EmailStr
    contrasena: str = Field(min_length=8, max_length=128)

class UsuarioUpdate(BaseModel):
    nombre: str | None = Field(default=None, min_length=2, max_length=150)
    correo: EmailStr | None = None
    contrasena: str | None = Field(default=None, min_length=8, max_length=128)

class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    correo: EmailStr

    model_config = ConfigDict(from_attributes=True)
