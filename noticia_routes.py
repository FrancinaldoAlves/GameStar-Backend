from fastapi import APIRouter, Depends, HTTPException
from schemas import NoticiaSchema
from sqlalchemy.orm import Session
from models import Usuario, Noticia
from dependencies import pegar_sessao, verificar_token

noticia_router = APIRouter(prefix="/noticia", tags=["noticia"])

@noticia_router.post("/criar_noticia")
async def cria_noticia(noticia_schema: NoticiaSchema, session: Session = Depends(pegar_sessao), usuario: Usuario = Depends(verificar_token)):
    if not usuario.admin:
        raise HTTPException(status_code=400, detail="Você não é administrador")
    else:
        nova_noticia = Noticia(noticia_schema.url_noticia, noticia_schema.descricao_noticia)
        session.add(nova_noticia)
        session.commit()
        return {"mensagem": f"noticia cadastrada com sucesso com id: {nova_noticia.id}"}
    
@noticia_router.delete("/deletar_noticia")
async def deleta_noticia(id: int, session: Session = Depends(pegar_sessao), usuario: Usuario = Depends(verificar_token)):
    if not usuario.admin:
        raise HTTPException(status_code=400, detail="Você não é administrador")
    else:
        noticia = session.query(Noticia).filter(Noticia.id==id).first()
        if not noticia:
            raise HTTPException(status_code=400, detail="Não existe esta noticia")
        else:
            session.delete(noticia)
            session.commit()
            return {"mensagem": f"noticia deletada com sucesso com id: {noticia.id}"}
        
@noticia_router.get("/listar_noticia")
async def lista_noticia(session: Session = Depends(pegar_sessao), usuario: Usuario = Depends(verificar_token)):
    noticia = session.query(Noticia).all()
    return noticia