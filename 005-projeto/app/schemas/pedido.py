from pydantic import BaseModel, ConfigDict
from typing import List
from app.schemas.item_pedido import ItemPedidoCreate, ItemPedidoOut

# Schema para criar um pedido (o que o front-end envia)
class PedidoCreate(BaseModel):
    cliente_id: int
    # O usuário enviará uma lista de produtos que ele quer
    itens: List[ItemPedidoCreate] = []

# Schema para exibir um pedido (o que a API retorna)
class PedidoOut(BaseModel):
    id: int
    cliente_id: int
    status: str
    valor_total: float
    # O pedido retornado mostrará a lista de itens formatada
    itens: List[ItemPedidoOut] = []

    model_config = ConfigDict(from_attributes=True)