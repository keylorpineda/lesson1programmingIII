from flask import jsonify
from . import api
from ..db import get_session
from ..models import Compra

@api.get("/clientes/<int:cliente_id>/compras")
def compras_por_cliente(cliente_id: int):
    with get_session() as session:
        data = [c.to_dict() for c in session.query(Compra).filter(Compra.cliente_id == cliente_id).all()]
    return jsonify(data)
