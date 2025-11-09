from sqlalchemy.orm import Session, joinedload
from fastapi import HTTPException, status
from decimal import Decimal

# Importamos todos os modelos e schemas necessários
from app.models.pedido import Pedido
from app.models.item_pedido import ItemPedido
from app.models.produto import Produto
from app.models.cliente import Cliente
from app.schemas.pedido import PedidoCreate

def create(db: Session, payload: PedidoCreate) -> Pedido:
    """
    Cria um novo pedido no banco de dados, implementando a regra de negócio
    de cálculo de valor total.
    """
    
    # --- 1. Validação de Entidades
    
    # Verifica se o cliente existe
    cliente = db.get(Cliente, payload.cliente_id)
    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Cliente com ID {payload.cliente_id} nao encontrado"
        )
        
    # Verifica se há itens no pedido
    if not payload.itens:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Um pedido nao pode ser criado sem itens"
        )

    # --- 2. Regra de Negócio: Cálculo do Valor Total ---
    
    valor_total_calculado = Decimal("0.0")
    itens_para_db = []

    for item_payload in payload.itens:
        
        # Busca o produto no banco de dados para pegar o PREÇO REAL
        produto = db.get(Produto, item_payload.produto_id)
        if not produto:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f"Produto com ID {item_payload.produto_id} nao encontrado"
            )
            
        # Calcula o subtotal do item
        subtotal_item = Decimal(produto.preco) * Decimal(item_payload.quantidade)
        valor_total_calculado += subtotal_item
        
        # Cria a instância do ItemPedido para o banco
        db_item = ItemPedido(
            produto_id=produto.id,
            quantidade=item_payload.quantidade,
            preco_unitario=produto.preco # Salva o preço do produto no momento da compra
        )
        itens_para_db.append(db_item)

    # --- 3. Criação do Pedido no Banco ---

    # Cria a instância principal do Pedido
    db_pedido = Pedido(
        cliente_id=payload.cliente_id,
        valor_total=valor_total_calculado,
        status="Aberto" # Status padrão
    )
    
    # Associa os itens ao pedido (mágica do relationship do SQLAlchemy)
    db_pedido.itens = itens_para_db

    db.add(db_pedido)
    db.commit()
    db.refresh(db_pedido)
    
    return db_pedido

def get_all(db: Session) -> list[Pedido]:
    """Retorna todos os pedidos."""
    # Usamos joinedload() para otimizar a consulta e já trazer os itens
    # Isso evita o "problema N+1"
    return db.query(Pedido).options(joinedload(Pedido.itens)).order_by(Pedido.id).all()

def get(db: Session, pedido_id: int) -> Pedido | None:
    """Busca um pedido pelo ID."""
    # Também usamos joinedload para trazer o cliente e os itens
    return (
        db.query(Pedido)
        .options(joinedload(Pedido.cliente), joinedload(Pedido.itens))
        .filter(Pedido.id == pedido_id)
        .first()
    )