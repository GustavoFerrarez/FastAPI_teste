from typing import Generator
from sqlalchemy.engine import Connection
from app.db.session import engine
from app.db.session import SessionLocal # <-- IMPORTAÇÃO ADICIONADA
from sqlalchemy.orm import Session       # <-- IMPORTAÇÃO ADICIONADA

def get_connection() -> Generator[Connection, None, None]:
    """Dependência para V2 (SQL puro)"""
    with engine.begin() as conn:
        yield conn

# --- FUNÇÃO CRÍTICA ADICIONADA ---
def get_db() -> Generator[Session, None, None]:
    """Dependência para V1 (ORM / Repositories)"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# ---------------------------------