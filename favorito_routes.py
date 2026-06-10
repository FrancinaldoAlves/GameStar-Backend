from fastapi import APIRouter, Depends, HTTPException
from schemas import FavoritoSchema
from sqlalchemy.orm import Session
from models import Usuario, Jogo, Favorito
from dependencies import pegar_sessao, verificar_token

favorito_router = APIRouter(prefix="/favorito", tags=["favorito"])

@favorito_router.post("/favoritar")
async def favoritar_jogo(favorito_schema: FavoritoSchema, session: Session = Depends(pegar_sessao), usuario: Usuario = Depends(verificar_token)):
    jogo = session.query(Jogo).filter(Jogo.id == favorito_schema.jogo_id).first()
    if not jogo:
        raise HTTPException(status_code=404, detail="Jogo não encontrado")
    
    ja_favoritado = session.query(Favorito).filter(
        Favorito.usuario_id == usuario.id,
        Favorito.jogo_id == favorito_schema.jogo_id
    ).first()
    if ja_favoritado:
        raise HTTPException(status_code=400, detail="Jogo já está nos favoritos")
    
    novo_favorito = Favorito(usuario.id, favorito_schema.jogo_id)
    session.add(novo_favorito)
    session.commit()
    return {"mensagem": f"Jogo '{jogo.titulo}' adicionado aos favoritos"}

@favorito_router.delete("/desfavoritar")
async def desfavoritar_jogo(jogo_id: int, session: Session = Depends(pegar_sessao), usuario: Usuario = Depends(verificar_token)):
    favorito = session.query(Favorito).filter(
        Favorito.usuario_id == usuario.id,
        Favorito.jogo_id == jogo_id
    ).first()
    if not favorito:
        raise HTTPException(status_code=404, detail="Favorito não encontrado")
    
    session.delete(favorito)
    session.commit()
    return {"mensagem": "Jogo removido dos favoritos"}

@favorito_router.get("/listar_favoritos")
async def listar_favoritos(session: Session = Depends(pegar_sessao), usuario: Usuario = Depends(verificar_token)):
    favoritos = session.query(Favorito).filter(Favorito.usuario_id == usuario.id).all()
    if not favoritos:
        return {"mensagem": "Nenhum jogo favoritado"}
    
    ids_jogos = [f.jogo_id for f in favoritos]
    jogos = session.query(Jogo).filter(Jogo.id.in_(ids_jogos)).all()
    return jogos

@favorito_router.get("/contagem")
async def contagem_favoritos(jogo_id: int, session: Session = Depends(pegar_sessao), usuario: Usuario = Depends(verificar_token)):
    jogo = session.query(Jogo).filter(Jogo.id == jogo_id).first()
    if not jogo:
        raise HTTPException(status_code=404, detail="Jogo não encontrado")

    contagem = session.query(Favorito).filter(Favorito.jogo_id == jogo_id).count()

    ja_favoritado = session.query(Favorito).filter(
        Favorito.usuario_id == usuario.id,
        Favorito.jogo_id == jogo_id
    ).first()

    return {
        "jogo_id": jogo_id,
        "titulo": jogo.titulo,
        "total_favoritos": contagem,
        "favoritado_por_mim": bool(ja_favoritado)
    }