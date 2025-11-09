from pydantic import BaseModel, ConfigDict

# Schema para criar um item (o que o front-end envia)
class ItemPedidoCreate(BaseModel):
    produto_id: int
    quantidade: int

# Schema para exibir um item (o que a API retorna)
class ItemPedidoOut(BaseModel):
    id: int
    produto_id: int
    quantidade: int
    preco_unitario: float
    
    model_config = ConfigDict(from_attributes=True)