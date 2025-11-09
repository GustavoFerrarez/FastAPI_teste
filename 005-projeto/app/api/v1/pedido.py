from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.schemas.pedido import PedidoCreate, PedidoOut
from app.repositories import pedido as repo

rotas = APIRouter(prefix="/v1/pedido", tags=["pedido"])

@rotas.post("/", response_model=PedidoOut, status_code=status.HTTP_201_CREATED)
def create(payload: PedidoCreate, db: Session = Depends(get_db)):
    """
    Cria um novo pedido (com cliente e lista de itens).
    O valor total é calculado automaticamente pela API.
    """
    # A exceção (HTTPException) já é tratada dentro do 'repo.create'
    return repo.create(db, payload)

@rotas.get("/", response_model=list[PedidoOut])
def list_all(db: Session = Depends(get_db)):
    """Lista todos os pedidos cadastrados."""
    return repo.get_all(db)

@rotas.get("/{pedido_id}", response_model=PedidoOut)
def get_id(pedido_id: int, db: Session = Depends(get_db)):
    """Obtém um pedido por ID."""
    objeto = repo.get(db, pedido_id)
    if not objeto:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Pedido nao encontrado")
    return objeto