from sqlalchemy import Column, Integer, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from app.db.base import Base

class ItemPedido(Base):
    __tablename__ = "itens_pedido"
    
    id = Column(Integer, primary_key=True, index=True)
    
    pedido_id = Column(Integer, ForeignKey("pedidos.id", ondelete="CASCADE"), nullable=False)
    produto_id = Column(Integer, ForeignKey("produtos.id", ondelete="RESTRICT"), nullable=False)
    
    quantidade = Column(Integer, nullable=False, default=1)
    
    # O preço do produto no momento da compra
    preco_unitario = Column(Numeric(10, 2), nullable=False)

    # Relações SQLAlchemy
    pedido = relationship("Pedido", back_populates="itens")
    produto = relationship("Produto")