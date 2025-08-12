from flask import jsonify
from . import api
from ..db import get_session
from ..models import Cliente

@api.get("/clientes")
def listar_clientes():
    with get_session() as session:
        data = [c.to_dict() for c in session.query(Cliente).order_by(Cliente.id.asc()).all()]
    return jsonify(data)
