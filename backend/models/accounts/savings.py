from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Numeric, ForeignKey
from decimal import Decimal

from .account import Account


# Classe Conta Poupança
class SavingsAccount(Account):
    __tablename__ = "savings_accounts"

    id: Mapped[int] = mapped_column(
        ForeignKey("accounts.id"),
        primary_key=True
    )

    __mapper_args__ = {
        "polymorphic_identity": "savings",
    }