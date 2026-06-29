from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Numeric

from decimal import Decimal

from core.db import Base


# Classe abstrata Conta
class Account(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key = True, index = True)

    holder_name: Mapped[str] = mapped_column(nullable = False)

    balance: Mapped[Decimal] = mapped_column(
        Numeric(precision = 15, scale = 2),
        default=Decimal("0.00")
    )
