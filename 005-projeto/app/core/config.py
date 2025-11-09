from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Valores padrão para satisfazer o Pydantic
    # Mesmo que estejamos usando uma string de conexão direta no session.py
    APP_NAME: str = "API Lanchonete"
    PG_HOST: str = "127.0.0.1"
    PG_PORT: int = 5432
    PG_DB: str = "postgres"  # Usando o banco padrão
    PG_USER: str = "postgres" # Usando o usuário padrão
    PG_PASSWORD: str = "1234"  # Coloque sua senha aqui

    class Config:
        # Isso ainda tentará ler o .env, mas se falhar (o que queremos), 
        # ele usará os valores padrão que definimos acima.
        env_file = ".env"

# objeto settings da classe Settings
settings = Settings()