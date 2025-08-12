from contextlib import contextmanager
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

_engine = None
_SessionLocal = None

def init_engine(database_url: str):
    global _engine, _SessionLocal
    if _engine is None:
        # sqlite: check_same_thread False para usar con threads en Flask
        connect_args = {"check_same_thread": False} if database_url.startswith("sqlite") else {}
        _engine = create_engine(database_url, echo=False, future=True, connect_args=connect_args)
        _SessionLocal = sessionmaker(bind=_engine, autoflush=False, autocommit=False, future=True)
    return _engine

@contextmanager
def get_session():
    session = _SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
