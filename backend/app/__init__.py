import os
from flask import Flask
from flask_cors import CORS
from sqlalchemy import text
from .db import init_engine, get_session
from .models import Base
from .routes import api as api_blueprint

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Config de DB
    db_url = os.getenv("DATABASE_URL", "sqlite:///../db/app.db")
    engine = init_engine(db_url)

    # Crear tablas si no existen
    Base.metadata.create_all(engine)

    # Registrar blueprints
    app.register_blueprint(api_blueprint, url_prefix="/")

    # Health simple
    @app.get("/health")
    def health():
        try:
            with get_session() as session:
                session.execute(text("SELECT 1"))
            return {"status": "ok"}, 200
        except Exception as e:
            return {"status": "error", "detail": str(e)}, 500

    return app
