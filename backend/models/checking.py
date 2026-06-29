from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Numeric

from decimal import Decimal

from .account import Account
from .enums import AccountType


# Classe Conta Corrente
class CheckingAccount(Account):
    __tablename__ = "checking_accounts"

    overdraft_limit: Mapped[Decimal] = mapped_column(
        Numeric(precision = 15, scale = 2),
        default=Decimal("500.00")
    )

    tax: Mapped[Decimal] = mapped_column(
        Numeric(precision = 15, scale = 2),
        default = Decimal("1.00")
    )

    @property
    def account_type(self) -> AccountType:
        return AccountType.CHECKING
