from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Numeric, ForeignKey
from decimal import Decimal

from .account import Account


# Classe Conta Corrente
class CheckingAccount(Account):
    __tablename__ = "checking_accounts"

    id: Mapped[int] = mapped_column(
        ForeignKey("accounts.id"),
        primary_key=True
    )

    overdraft_limit: Mapped[Decimal] = mapped_column(
        Numeric(precision=15, scale=2),
        default=Decimal("500.00")
    )

    tax: Mapped[Decimal] = mapped_column(
        Numeric(precision=15, scale=2),
        default=Decimal("1.00")
    )

    __mapper_args__ = {
        "polymorphic_identity": "checking",
    }