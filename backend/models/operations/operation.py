from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Numeric, Enum as SAEnum, String

from decimal import Decimal

from core.db import Base
from .enums import OperationType


# Classe abstrata Operação
class Operation(Base):
    __tablename__ = "operations"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    operation_type: Mapped[OperationType] = mapped_column(
        SAEnum(OperationType),
        nullable=False
    )

    amount: Mapped[Decimal] = mapped_column(
        Numeric(precision=15, scale=2),
        default=Decimal("0.00"),
        nullable=False
    )

    __mapper_args__ = {
        "polymorphic_on": operation_type,
        "polymorphic_identity": "operation"
    }