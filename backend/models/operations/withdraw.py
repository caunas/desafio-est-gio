from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from .operation import Operation


# Classe de saque
class Withdraw(Operation):
    __mapper_args__ = {
        "polymorphic_identity": "withdraw"
    }

    AccountFrom: Mapped[int] = mapped_column(
        ForeignKey("accounts.id"),
        nullabe=False)

    AccountTo: Mapped[int] = mapped_column(
        ForeignKey("accounts.id")
    )