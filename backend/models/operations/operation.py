from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Numeric, Enum

from decimal import Decimal

from core.db import Base
from .enums import OperationType


# Classe abstrata Operação
class Operation(Base):
    __tablename__ = "operations"

    __mapper_args__ = {
        "polymorphic_on": type
    }

    id: Mapped[int] = mapped_column(primary_key = True, index = True)

    opType: Mapped[OperationType] = mapped_column(
        Enum(OperationType),
        nullabe=False
    )

    ammount: Mapped[Decimal] = mapped_column(
        Numeric(precision = 15, scale = 2),
        default=Decimal("0.00"),
        nullable=False
    )
