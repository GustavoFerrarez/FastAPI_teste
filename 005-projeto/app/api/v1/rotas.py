from fastapi import APIRouter
from . import produto, categoria
# from . import cliente, pedido  # <-- Comente estas por enquanto

api_rotas = APIRouter()
api_rotas.include_router(produto.rotas)
api_rotas.include_router(categoria.rotas)
api_rotas.include_router(cliente.rotas)  # <-- Comente estas por enquanto
api_rotas.include_router(pedido.rotas)   # <-- Comente estas por enquanto