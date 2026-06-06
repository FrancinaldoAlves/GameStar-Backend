from fastapi import APIRouter

order_router = APIRouter(prefix="/home", tags=["home"])

@order_router.get("/")
async def home():
    return {"mensagem": "Você acessoyu a rota home"}