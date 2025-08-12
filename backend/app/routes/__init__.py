from flask import Blueprint

api = Blueprint("api", __name__)

# Importar módulos que registran rutas
from . import clientes, compras  # noqa: E402,F401
