from fastapi import APIRouter, Depends, HTTPException
from schemas import JogoSchema
from sqlalchemy.orm import Session
from models import Usuario, Jogo
from dependencies import pegar_sessao, verificar_token


jogo_router = APIRouter(prefix="/jogo", tags=["jogo"])

@jogo_router.post("/criar_jogo")
async def criar_jogo(jogo_schema: JogoSchema, session: Session = Depends(pegar_sessao), usuario: Usuario= Depends(verificar_token)):
    if not usuario.admin:
        raise HTTPException(status_code=400, detail="Você não é administrador")
    else:
        novo_jogo = Jogo(jogo_schema.titulo, jogo_schema.descricao, jogo_schema.data_lancamento, jogo_schema.nota, jogo_schema.url_jogo)
        session.add(novo_jogo)
        session.commit()
        return{"mensagem": f"jogo adicionado com sucesso {jogo_schema.titulo}"}

@jogo_router.delete("/deletar_jogo")
async def deletar_jogo(id: int, session: Session = Depends(pegar_sessao), usuario: Usuario= Depends(verificar_token)):
    if not usuario.admin:
        raise HTTPException(status_code=400, detail="Você não é administrador") 
    else:
        jogo = session.query(Jogo).filter(Jogo.id == id).first()
        if not jogo:
            raise HTTPException(status_code=400, detail="não existe este jogo")
        else:
            session.delete(jogo)
            session.commit()
            return{"mensagem": f"jogo removido com sucesso {jogo.titulo}"}

@jogo_router.get("/listar_jogo")
async def listar_jogo(session: Session = Depends(pegar_sessao), usuario: Usuario= Depends(verificar_token)):
    jogo = session.query(Jogo).all()
    return jogo