from decimal import Decimal
from pydantic import BaseModel


# schema de conta corrente
class CheckingAccountBase(BaseModel):
    holder_name: str


class CheckingAccountCreate(CheckingAccountBase):
    holder_name: str
    initial_balance: Decimal = Decimal("0.00")


# schema de conta poupança
class SavingsAccountBase(BaseModel):
    holder_name: str


class SavingsAccountCreate(SavingsAccountBase):
    holder_name: str
    initial_balance: Decimal = Decimal("0.00")


# Resposta universal de conta
class AccountResponse(BaseModel):
    account_type: str
    id: int
    holder_name: str
    balance: Decimal


    model_config = {
        "from_attributes": True
    }
