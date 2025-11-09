from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Pedido(Base):
    __tablename__ = "pedidos"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # Chave estrangeira para Cliente
    cliente_id = Column(Integer, ForeignKey("clientes.id", ondelete="SET NULL"), nullable=True)
    
    status = Column(String, nullable=False, default="Aberto")
    valor_total = Column(Numeric(10, 2), nullable=True, default=0.0) # Será calculado pela regra de negócio

    # Relações SQLAlchemy
    cliente = relationship("Cliente", back_populates="pedidos")
    
    # Um pedido tem vários "itens"
    itens = relationship(
        "ItemPedido", 
        back_populates="pedido",
        cascade="all, delete-orphan"
    )