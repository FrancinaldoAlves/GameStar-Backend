from fastapi import APIRouter, Depends, HTTPException
from schemas import ReviewSchema
from sqlalchemy.orm import Session
from models import Usuario, Review, Jogo
from dependencies import pegar_sessao, verificar_token

review_router = APIRouter(prefix="/review", tags=["review"])

@review_router.post("/criar_review")
async def criar_review(review_schema: ReviewSchema, session: Session = Depends(pegar_sessao), usuario: Usuario= Depends(verificar_token)):
    review_repetida = session.query(Review).filter(Review.usuario_id == usuario.id, Review.jogo_id == review_schema.jogo_id).first()
    if review_repetida:
        raise HTTPException(status_code=400, detail="Você já avaliou este jogo")
    nova_review= Review(review_schema.usuario_id, review_schema.jogo_id, review_schema.nota, review_schema.data_finalizacao, review_schema.descricao, review_schema.finalizado, review_schema.dropado)
    session.add(nova_review)
    session.commit()
    jogo = session.query(Jogo).filter(
        Jogo.id == review_schema.jogo_id
    ).first()

    reviews = session.query(Review).filter(
        Review.jogo_id == review_schema.jogo_id
    ).all()

    if reviews:
        jogo_media = sum(notas.nota for notas in reviews) / len(reviews)
        jogo.nota_media = jogo_media
        session.add(jogo)
        session.commit()

    return {"mensagem": f"Review criada com sucesso"}


@review_router.delete("/deletar_review")
async def deletar_review(id: int, session: Session = Depends(pegar_sessao), usuario: Usuario= Depends(verificar_token)):
    review = session.query(Review).filter(Review.id == id).first()
    if not review:
        raise HTTPException(status_code=400, detail="não existe essa review")
    else:
        session.delete(review)
        session.commit()
        id_jogo = review.jogo_id
        jogo = session.query(Jogo).filter(
            Jogo.id == id_jogo
        ).first()

        reviews = session.query(Review).filter(
            Review.jogo_id == id_jogo
        ).all()
        
        if reviews:
            jogo_media = sum(notas.nota for notas in reviews) / len(reviews)
            jogo.nota_media = jogo_media
            session.add(jogo)
            session.commit()

        return{"mensagem": f"review removida com sucesso"}

@review_router.get("/listar_review")
async def listar_review(session: Session = Depends(pegar_sessao), usuario: Usuario= Depends(verificar_token)):
    review = session.query( Review).all()
    return review