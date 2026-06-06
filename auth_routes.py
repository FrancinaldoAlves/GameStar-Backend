from fastapi import APIRouter, Depends, HTTPException
from models import Usuario
from dependencies import pegar_Sessao
from main import bcrypt_context
from schemas import UsuarioSchema
from sqlalchemy.orm import Session

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/") 
async def autenticar():
    return {
        "mensagem": "Você acessou a rota padrão de autenticação", 
        "autenticação": False
    }

@auth_router.post("/criar_conta")
async def cria_conta(usuario_schema: UsuarioSchema, session: Session = Depends(pegar_Sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==usuario_schema.email).first()
    if usuario:
        raise HTTPException(status_code=400, detail="Email do usuário já cadastardo")
    else:
        senha_criptografada = bcrypt_context.hash(usuario_schema.senha)
        novo_usuario = Usuario(usuario_schema.nome, usuario_schema.email, senha_criptografada, usuario_schema.admin)
        session.add(novo_usuario)
        session.commit()
        return {"mensagem": f"usuário cadastrado com sucesso {usuario_schema.email}"}
