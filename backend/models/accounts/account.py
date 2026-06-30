from sqlalchemy.orm import Mapped, mapped_column, declared_attr
from sqlalchemy import Numeric, String
from decimal import Decimal

from core.db import Base


# Classe abstrata Conta
class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    holder_name: Mapped[str] = mapped_column(nullable=False)

    balance: Mapped[Decimal] = mapped_column(
        Numeric(precision=15, scale=2),
        default=Decimal("0.00"),
        nullable=False
    )

    kind: Mapped[str] = mapped_column(String, nullable=False)

    @property
    def account_type(self) -> str:
        return self.kind

    __mapper_args__ = {
        "polymorphic_on": kind,
        "polymorphic_identity": "account",
    }