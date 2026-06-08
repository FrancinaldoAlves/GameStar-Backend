from pydantic import BaseModel
from typing import Optional
from datetime import date

class UsuarioSchema(BaseModel):
    nome: str
    email: str
    senha: str
    admin: Optional[bool]

    class Config:
        from_attributes = True

class LoginSchema(BaseModel):
    email: str
    senha: str

    class Config:
        from_attributes = True

class JogoSchema(BaseModel):
    titulo: str
    descricao: str
    data_lancamento: date
    nota: float
    url_jogo: str

    class Config:
        from_attributes = True

class NoticiaSchema(BaseModel):
    url_noticia: str
    descricao_noticia: str

    class Config:
        from_attributes = True