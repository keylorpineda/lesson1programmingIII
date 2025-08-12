from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, DateTime, Numeric
from datetime import datetime
from typing import List, Optional

class Base(DeclarativeBase):
    pass

class Cliente(Base):
    __tablename__ = "clientes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(120), nullable=False)
    email: Mapped[Optional[str]] = mapped_column(String(160), nullable=True)

    compras: Mapped[List["Compra"]] = relationship(back_populates="cliente", cascade="all, delete-orphan")

    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre, "email": self.email}

class Compra(Base):
    __tablename__ = "compras"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    cliente_id: Mapped[int] = mapped_column(ForeignKey("clientes.id"), nullable=False, index=True)
    fecha: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    total: Mapped[float] = mapped_column(Numeric(10,2), nullable=False)

    cliente: Mapped[Cliente] = relationship(back_populates="compras")

    def to_dict(self):
        return {
            "id": self.id,
            "cliente_id": self.cliente_id,
            "fecha": self.fecha.isoformat(),
            "total": float(self.total),
        }
