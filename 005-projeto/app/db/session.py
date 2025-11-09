## conexao com postgresql (MODO DIRETO, SEM .ENV)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# Removido: from app.core.config import settings

# --- 1. CONEXÃO DIRETA ---
# Coloque aqui sua senha de administrador do PostgreSQL (a que você usa no DBeaver)
SUA_SENHA_DE_ADMIN = "1234" # <-- TROQUE AQUI PELA SUA SENHA

# Estamos conectando como usuário 'postgres' ao banco 'postgres'
# (Esse banco e usuário quase sempre existem por padrão)
DATABASE_URL = (
    f"postgresql+psycopg2://postgres:{SUA_SENHA_DE_ADMIN}"
    f"@127.0.0.1:5432/postgres"
)
# ------------------------

engine = create_engine(
    DATABASE_URL,
    pool_size = 10,
    max_overflow = 0,
    pool_timeout= 5,
    pool_pre_ping= True,
    # Isso ajuda a corrigir o UnicodeDecodeError se a senha estiver correta
    connect_args={"client_encoding": "utf8"}
)

# (O resto do arquivo que já corrigimos)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_connection():
    with engine.connect() as conn:
        yield conn