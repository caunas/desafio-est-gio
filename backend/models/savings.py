from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Numeric

from decimal import Decimal

from .account import Account
from .enums import AccountType


# Classe ContaPoupança
class SavingsAccount(Account):
    __tablename__ = "savings_accounts"

    @property
    def account_type(self) -> AccountType:
        return AccountType.SAVINGS
