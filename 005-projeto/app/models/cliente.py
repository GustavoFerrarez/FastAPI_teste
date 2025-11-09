# em app/models/cliente.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship # <-- Importe
from app.db.base import Base

class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)

    # <-- VERIFIQUE SE ESTA RELAÇÃO EXISTE -->
    pedidos = relationship(
        "Pedido", 
        back_populates="cliente",
        cascade="all, delete-orphan"
    )