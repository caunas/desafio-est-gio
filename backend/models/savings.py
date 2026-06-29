from sqlalchemy import Mapped, mapped_column
from sqlalchemy import Numeric

from decimal import Decimal

from .account import Account


# Classe ContaPoupança
class SavingsAccount(Account):
    __tablename__ = "savings_accounts"
