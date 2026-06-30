from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from .operation import Operation


# Classe de depósito
class Deposit(Operation):
    __tablename__ = "deposits"

    id: Mapped[int] = mapped_column(
        ForeignKey("operations.id"),
        primary_key=True
    )

    account_id: Mapped[int] = mapped_column(
        ForeignKey("accounts.id"),
        nullable=False
    )

    __mapper_args__ = {
        "polymorphic_identity": "deposit"
    }