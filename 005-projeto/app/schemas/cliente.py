from pydantic import BaseModel, ConfigDict

class ClienteCreate(BaseModel):
    nome: str

class ClienteOut(BaseModel):
    id: int
    nome: str
    model_config = ConfigDict(from_attributes=True)