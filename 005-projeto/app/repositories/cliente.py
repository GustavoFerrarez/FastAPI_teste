from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.deps import get_db  # Importando o get_db (padrão v1/v4)
from app.schemas.cliente import ClienteCreate, ClienteOut
from app.repositories import cliente as repo

rotas = APIRouter(prefix="/v1/cliente", tags=["cliente"])

@rotas.post("/", response_model=ClienteOut, status_code=status.HTTP_201_CREATED)
def create(payload: ClienteCreate, db: Session = Depends(get_db)):
    """Cria um novo cliente."""
    return repo.create(db, payload)

@rotas.get("/", response_model=list[ClienteOut])
def list_all(db: Session = Depends(get_db)):
    """Lista todos os clientes."""
    return repo.get_all(db)

@rotas.get("/{cliente_id}", response_model=ClienteOut)
def get_id(cliente_id: int, db: Session = Depends(get_db)):
    """Obtém um cliente por ID."""
    objeto = repo.get(db, cliente_id)
    if not objeto:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Cliente nao encontrado")
    return objeto

# NOTA: O CRUD completo (PUT/DELETE) também seguiria esse padrão.